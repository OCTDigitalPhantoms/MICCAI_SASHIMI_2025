**Due to limited Repo space we provide here only first six examples (from 32)**

To generate synthetic scans using Digital phantoms:
1. Download the dat and ini for the phantom from the DigitalPhantoms folder
2. Log in to https://accounts.opticelastograph.com/ 
3. Click Create a Task and choose the OCT generator v.3 (att)
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
