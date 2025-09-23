# Synthetic OCT Scans (.npy) for MedSAM Fine-Tuning

files available here: https://cloud.mail.ru/public/q9aa/TeQNG2MSX

This repository provides a synthetic Optical Coherence Tomography (OCT) dataset prepared for fine-tuning MedSAM. The data are already packaged in a ready-to-use format compatible with MedSAM’s training script:
https://github.com/bowang-lab/MedSAM

All images and ground-truth masks are synthetic; no real patient data is included.

## Directory structure

Put the data into the following structure:

```
Data/
  imgs/   # .npy image files
  gts/    # .npy ground-truth mask files
```

## Training with MedSAM

Follow MedSAM’s setup instructions, then point its training script to this dataset.
https://github.com/bowang-lab/MedSAM

## What’s inside

- Modality: synthetic OCT B-scans.
- Annotations: per-image segmentation masks aligned to each scan.
- Format: .npy files, 2D arrays with matching shapes for image and mask.
- Intended use: fine-tuning MedSAM with synthetic scans.

## License

You are free to use, modify, and distribute it for any purpose without restriction.

## How to cite (BibTeX)

If you use this dataset, please cite the accompanying proceedings paper and MedSAM:

```
@InProceedings{10.1007/978-3-032-05573-6_5,
author="Nikoshin, Denis
and Mikhailenko, Daniil
and Sovetsky, Alexander
and Matveyev, Alexander
and Zaitsev, Vladimir
and Matveev, Lev",
editor="Fernandez, Virginia
and Wiesner, David
and Zuo, Lianrui
and Casamitjana, Adri{\`a}
and Remedios, Samuel W.",
title="From Tissue-Mimicking Phantoms to Physics-Based Scans: Synthetic OCT for Few-Shot Foundation Model Training",
booktitle="Simulation and Synthesis in Medical Imaging",
year="2026",
publisher="Springer Nature Switzerland",
address="Cham",
pages="44--51",
isbn="978-3-032-05573-6"
}
```

```
@article{Ma2024MedSAM,
  title={Segment Anything in Medical Images},
  author={Ma, Jun and He, Yuting and Li, Feifei and Han, Lin and You, Chenyu and Wang, Bo},
  journal={Nature Communications},
  volume={15},
  pages={654},
  year={2024}
}
```
