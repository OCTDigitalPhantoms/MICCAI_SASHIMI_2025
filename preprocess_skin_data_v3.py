import os
import numpy as np
import cv2
from tqdm import tqdm
import warnings

# Предполагается, что SkinDBLib_v16.py находится в той же директории
try:
    from SkinDBLib_v16 import load_skin_db, generate_gt_masks
except ImportError:
    print("ОШИБКА: Убедитесь, что файл 'SkinDBLib_v16.py' находится в той же директории.")
    exit()

# --- 1. Конфигурация ---
MAT_FILE_PATH = 'skin_db.mat'
OUTPUT_DIR = 'data/npy/SkinDB'
IMGS_DIR_NAME = 'imgs'
GTS_DIR_NAME = 'gts'
TARGET_IMG_SIZE = (1024, 1024) # (Высота, Ширина) для изображений
TARGET_MASK_SIZE = (1024, 1024)  # (Высота, Ширина) для масок
CLASS_MAPPING = {
    'Epidermis': 1,
    'Dermis': 2,
}

def preprocess_and_save_data():
    """
    Главная функция для загрузки, предобработки и сохранения данных
    из skin_db.mat в формат .npy для MedSAM.
    """
    print("--- Запуск предобработки данных для MedSAM ---")

    # --- 2. Создание структуры директорий ---
    output_imgs_path = os.path.join(OUTPUT_DIR, IMGS_DIR_NAME)
    output_gts_path = os.path.join(OUTPUT_DIR, GTS_DIR_NAME)
    os.makedirs(output_imgs_path, exist_ok=True)
    os.makedirs(output_gts_path, exist_ok=True)
    print(f"Созданы директории для вывода:\n  - Изображения: {output_imgs_path}\n  - Маски: {output_gts_path}")

    # --- 3. Загрузка данных из .mat файла ---
    print(f"\nЗагрузка данных из '{MAT_FILE_PATH}'...")
    patients_data = load_skin_db(MAT_FILE_PATH)
    if not patients_data:
        print("Не удалось загрузить данные. Проверьте путь к файлу и его содержимое. Выход.")
        return
    print(f"Найдено {len(patients_data)} пациентов.")
    total_scans_processed = 0

    # --- 4. Итерация по пациентам и сканам ---
    for patient_key, patient_obj in tqdm(patients_data.items(), desc="Обработка пациентов"):
        
        if not hasattr(patient_obj, 'oct') or patient_obj.oct is None:
            warnings.warn(f"\nПРЕДУПРЕЖДЕНИЕ: У пациента '{patient_key}' отсутствует поле 'oct'. Пропускаем.")
            continue
        
        if patient_obj.oct.ndim != 3:
            warnings.warn(f"\nПРЕДУПРЕЖДЕНИЕ: Поле 'oct' у пациента '{patient_key}' не является 3D-массивом. Пропускаем.")
            continue
            
        num_scans = patient_obj.oct.shape[2]
        
        if not hasattr(patient_obj, 'gt') or patient_obj.gt is None or len(patient_obj.gt) != num_scans:
            warnings.warn(f"\nПРЕДУПРЕЖДЕНИЕ: Данные GT для '{patient_key}' отсутствуют или не соответствуют числу сканов ({num_scans}). Пропускаем.")
            continue

        for scan_idx in range(num_scans):
            raw_image = patient_obj.oct[:, :, scan_idx]
            gt_contours = patient_obj.gt[scan_idx]

            if raw_image is None or gt_contours is None:
                warnings.warn(f"\nПРЕДУПРЕЖДЕНИЕ: Пропущен скан #{scan_idx} у пациента {patient_key} из-за пустых данных (None).")
                continue

            # --- 5. Обработка изображения ---
            original_shape = raw_image.shape[:2] # (Высота, Ширина)
            if raw_image.ndim == 2:
                # Преобразование в 3-канальное изображение (В, Ш, 3)
                image_rgb = np.stack([raw_image] * 3, axis=-1)
            elif raw_image.ndim == 3 and raw_image.shape[-1] == 1: # (В, Ш, 1)
                image_rgb = np.concatenate([raw_image] * 3, axis=-1)
            elif raw_image.ndim == 3 and raw_image.shape[-1] == 3: # Уже (В, Ш, 3)
                 image_rgb = raw_image
            else:
                warnings.warn(f"\nПРЕДУПРЕЖДЕНИЕ: Неподдерживаемый формат изображения для скана #{scan_idx} у пациента {patient_key}. Пропускаем. Форма: {raw_image.shape}")
                continue
            
            # Нормализация и изменение размера
            # Изображение должно быть (Высота, Ширина, Каналы) для cv2.resize
            image_norm = image_rgb.astype(np.float32) / 255.0
            image_resized = cv2.resize(image_norm, (TARGET_IMG_SIZE[1], TARGET_IMG_SIZE[0]), interpolation=cv2.INTER_LINEAR)
            # image_resized теперь имеет форму (TARGET_IMG_SIZE[0], TARGET_IMG_SIZE[1], 3) -> (1024, 1024, 3)

            # Закомментировано: транспонирование здесь не нужно, так как train_one_gpu.py ожидает (В, Ш, К) при загрузке,
            # а затем сам транспонирует в (К, В, Ш)
            # image_final = np.transpose(image_resized, (2, 0, 1)) 

            # --- 6. Обработка маски ---
            gt_masks_dict = generate_gt_masks(gt_contours, original_shape)
            multilabel_mask = np.zeros(original_shape, dtype=np.uint8) # (Высота_исх, Ширина_исх)
            for class_name, class_id in CLASS_MAPPING.items():
                if class_name in gt_masks_dict and gt_masks_dict[class_name].any():
                    multilabel_mask[gt_masks_dict[class_name]] = class_id
            
            # Маска должна быть (Высота, Ширина) для cv2.resize
            mask_resized = cv2.resize(multilabel_mask, (TARGET_MASK_SIZE[1], TARGET_MASK_SIZE[0]), interpolation=cv2.INTER_NEAREST)
            # mask_resized теперь имеет форму (TARGET_MASK_SIZE[0], TARGET_MASK_SIZE[1]) -> (256, 256)

            # --- 7. Сохранение файлов ---
            base_filename = f"{patient_key}_scan_{scan_idx+1:03d}.npy"
            img_save_path = os.path.join(output_imgs_path, base_filename)
            gt_save_path = os.path.join(output_gts_path, base_filename)
            
            # Сохраняем image_resized, который имеет форму (1024, 1024, 3)
            np.save(img_save_path, image_resized) 
            np.save(gt_save_path, mask_resized)
            total_scans_processed += 1

    print(f"\n--- Предобработка завершена! ---")
    if total_scans_processed > 0:
        print(f"✅ Успешно! Всего обработано и сохранено: {total_scans_processed} пар (изображение + маска).")
        print(f"Данные готовы для обучения в директории: '{OUTPUT_DIR}'")
    else:
        print(f"❌ ВНИМАНИЕ! Ни одного файла не было обработано. Проверьте структуру вашего .mat файла и предупреждения выше.")

if __name__ == '__main__':
    preprocess_and_save_data()
