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
3. Click Create a Task and choose the OCT generator v.3 (att)
4. Upload the .dat file
5. Take the parameters from the corresponding .ini file
