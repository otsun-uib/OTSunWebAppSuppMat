# Supplementary Material for manuscript "OTSunWebApp: a ray tracing web application for the analysis of concentrating solar-thermal and photovoltaic solar cells"
## By Ramón Pujol-Nadal and Gabriel Cardona

- `0.utils`: Folder with auxiliary files
	- `faces_of_a_solid.FCMacro`: Macro that adds to the active document the boundary faces of the selected solid.

- `1.tower_plant`: Folder with the files related to the experiment described in Section "3. Optical simulation of a solar power tower plant".
	- `create_scene_TowerPlant.txt`: Script used to generate the model of the Tower Plant for its analysis in OTSunWebApp.
	- `heliostats_field.txt`: Text file with the position of each heliostat (used by `create_scene_TowerPlant.py`).
	-  `Tower_Plant.FCStd`: FreeCAD file defining the geometry of the Tower Plant simulated in the paper (generated by `create_scene_TowerPlant.py`).
	- `materials_tower_plant.zip`: Zip file with the otsun materials for the Tower Plant simulated in the paper.
	- `Tower_Plant.tnh`: Tonatiuh file defining the same geometry as in `Tower_Plant.FCStd`
	- `output_tower_plant`: Folder with output files from the simulation of the Tower Plant. Contains 3 folders, corresponding to the computations for the spring equinox, summer solstice and flux distribution, respectively; each of them contains files with the corresponding outputs. The `flux_absorber.py` script is given for the calculation of the flux distribution plot using OTSunWebApp and Tonatiuh.

- `2.PV_cell`: Folder with the files related to the experiment described in Section "4. Optical simulation of a PV cell".
	- `create_PV_cell.py`: Script used to generate the model of the PV cell for its analysis in OTSunWebApp. 
	- `PV_cell.FCStd`: FreeCAD file defining the geometry of the PV cell simulated in the paper (generated by `create_PV_cell.py`).
	- `PV_cell_materials_specular.zip`: Zip file containing otsun materials for the PV cell with specular back reflector.
	- `PV_cell_materials_lambertian.zip`: Zip file containing otsun materials for the PV cell with lambertian back reflector.
	- `material_data`: Folder with the data files needed for generating the PV cell materials.
	- `output_PV_cell_OTSunWebApp`: Folder with output files for the PV cell simulated with OTSunWebApp. Contains 6 files corresponding to the different experiments made (3 different angles and 2 different back reflectors)
	- `output_PV_cell_Daidalos`: Folder with output files for the PV cell simulated with Daidalos-cloud. Contains 6 folders corresponding to the different experiments made (3 different angles and 2 different back reflectors)
