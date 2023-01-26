# Supplementary Material for manuscript XXX

- `flat_mirror`: Folder with the files related to the experiment XXXX
	- `create_flat_mirror.py`: Script used to generate the flat mirror in FreeCAD for the specular deviation scattering analysis (Fig. 7 of the paper).
	- `flat_mirror.FCStd`: FreeCAD file defining the geometry of the of the falt mirror for the specular deviation scattering analysis.
	- `materials_flat_mirror_3mrad.zip`: Zip file containing otsun materials for the flat mirror, case study of sigma_s = 3 mrad for specular deviation scattering.
	- `materials_flat_mirror_1_2mrad_8mrad_0_92.zip`: zip file containing otsun materials for the flat mirror, case study of sigma_s1 = 1.2 mrad, sigma_s2 = 8 mrad and k = 0.92 for specular deviation scattering.
	- `flat_mirror.tnh`: Tonatiuh file defining the same geometry as in flat_mirror.FCStd
	- `output_flat_miror`: Folder with output files for the specular deviation scattering analysis. Case of simulation: Spectral analalysis.  

- `tower_plant`: Folder with the files related to the experiment XXXX
	- `create_scene_TowerPlant.txt`: Script used to generate the Tower Plant.
	- `heliostats_field.txt`: Text file with the position of each heliostat.
	-  `Tower_Plant.FCStd`: FreeCAD file defining the geometry of the Tower Plant simulated in the paper.
	- `materials_tower_plant.zip`: Zip file containing otsun materials for the Tower Plant simulated in the paper.
	- `Tower_Plant.tnh`: Tonatiuh file defining the same geometry as in Tower_Plant.FCStd
	- `output_tower_plant`: Folder with output files for the Tower Plant simulated.

- `PV_cell`: Folder with the files related to the experiment XXXSX
	- `create_PV_cell.py`: Scrip used to generate the PV cell simulated in the paper. 
	- `PV_cell.FCStd`: FrrCAD file defining the geometry of the PV dell simulated.
	- `PV_cell_materials_specular.zip`: Zip file containing otsun materials fort he PV cell with specular back reflcetor.
	- `PV_cell_materials_lambertian.zip`: Zip file containing otsun materials fort he PV cell with lambertian back reflcetor.
	- `material_data`: Folder with txt files for generating the PV cell materials.
	- `output_PV_cell_OTSunWebApp`: Folder with output files for the PV cell simulated with OTSunWebApp. 
	- `output_PV_cell_Daidalos`: Folder with output files for the PV cell simulated with Daidalos cloud.