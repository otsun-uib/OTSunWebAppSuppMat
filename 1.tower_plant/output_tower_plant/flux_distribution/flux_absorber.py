import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pathlib as Path
cwd = Path.Path().resolve()
path = str(cwd.parents[0])
import sys

sys.path.append(path)

file = path + './flux_absorber/Th_points_absorber_2M.txt'
def load_from_txt_or_csv(file):
    df = pd.read_table(
        file,
        sep=None,
        index_col=0,
        header=None,
        comment='#',
        engine='python'
    ).interpolate(method='index')
    df.insert(0,0,df.index)
    return df.values

DATA = load_from_txt_or_csv(file)
x_list = DATA[:, 1]/1000
y_list = (DATA[:, 3]-62000)/1000
z_list = DATA[:, 0]


bins_x = 60
bins_y = 45

area = 8/bins_x * 6/bins_y

number_of_rays = 2E6

source_area = 323670.2698543315 # this is the source area of source_wavelengths.txt

power_emitted_by_source = 1000 # W/m2

power_per_ray = power_emitted_by_source * (source_area / number_of_rays)


z_weights = DATA[:, 0] * power_per_ray / area / 1000000 # MW/m2

plt.hist2d(x_list,y_list,bins=[np.arange(-4 + 8/bins_x / 2, 4, 8/bins_x), np.arange(-3 + 6/bins_y/2, 3 , 6/bins_y)], cmap=plt.cm.jet, weights=(z_weights))

plt.colorbar(label="$MW/m^2$")
plt.clim(0, 10)
plt.title("OTSunWebApp flux distribution $MW/m^2$")
plt.xlabel("width [$m$]")
plt.ylabel("height [$m$]")
plt.xlim([-4, 4])
plt.ylim([-3, 3])
plt.savefig("flux_OTSun.png", format="png", bbox_inches="tight")
plt.show()

file = path + './flux_absorber/Tonatiuh_2M.txt'

DATA = np.loadtxt(file, usecols=(0, 1, 2),skiprows=1)
x_list = DATA[:, 0]
y_list = DATA[:, 1]
z_weights = DATA[:, 2] * 0.9 / 1000000 # absortance of the receiver = 0.9; W/m2

plt.hist2d(x_list,y_list,bins=[np.arange(-4 + 8/bins_x / 2, 4, 8/bins_x), np.arange(-3 + 6/bins_y/2, 3 , 6/bins_y)], cmap=plt.cm.jet, weights=(z_weights))

plt.colorbar(label="$MW/m^2$")
plt.clim(0, 10)
plt.title("Tonatiuh flux distribution $MW/m^2$")
plt.xlabel("width [$m$]")
plt.ylabel("height [$m$]")
plt.xlim([-4, 4])
plt.ylim([-3, 3])

plt.savefig("flux_Tonatiuh.png", format="png", bbox_inches="tight")
plt.show()

