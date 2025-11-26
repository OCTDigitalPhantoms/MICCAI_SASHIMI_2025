To prepare real scans for MedSAM:
1. Download .zip from the supplementary materials of the paper [Del Amor, R., et al.: Automatic segmentation of epidermis and hair follicles in optical coherence tomography images of normal skin by convolutional neural networks. Front. Med. 7, 220 (2020). doi:fmed.2020.00220] 
https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2020.00220/full#supplementary-material
2. Extract skinDB.mat
3. Download preprocess_skin_data_v3.py and SkinDBLib_v16.py to the same workdir
4. Run
5. Then train MedSAM using code from the MedSAM repo

For training MedSAM on synthetic scans go to the SyntheticSkinDB subfolder and read the instructions there

To generate synthetic scans using Digital phantoms:
1. Download the dat and ini for the phantom from the DigitalPhantoms folder
2. Log in to https://accounts.opticelastograph.com/ 
3. Click Create a Task and choose the OCT generator v.3 (att) [If you have problem with access please contact drlevmatveev@gmail.com]
4. Upload the .dat file
5. Take the parameters to corresponding forms
```
   [Parameters]
scan filename = patient01_slice0_var0.dat
a-scan pixel numbers = 601
vertical pixel size mcm = 2.2
central wavelength mcm = 1.3
number of a-scans in b-scan = 975
xmax mcm = 3000.0
number of b-scans = 1
ymax mcm = 0.0
beam radius mcm = 6.0
scatterers coordinates file = patient01_slice0_var0_scatterers.dat
number of scatterers in b-scan = 255000
```

**This work was supported by the Russian Science Foundation Grant No. 25-12-20032 ( https://rscf.ru/en/project/25-12-20032/ ).**

Please cite:

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
@ARTICLE{10.3389/fmed.2020.00220,
AUTHOR={del Amor, Rocío  and Morales, Sandra  and Colomer, Adrián  and Mogensen, Mette  and Jensen, Mikkel  and Israelsen, Niels M.  and Bang, Ole  and Naranjo, Valery },
TITLE={Automatic Segmentation of Epidermis and Hair Follicles in Optical Coherence Tomography Images of Normal Skin by Convolutional Neural Networks},
JOURNAL={Frontiers in Medicine},
VOLUME={Volume 7 - 2020},
YEAR={2020},
URL={https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2020.00220},
DOI={10.3389/fmed.2020.00220},
ISSN={2296-858X},
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
