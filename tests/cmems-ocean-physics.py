# Packages
import numpy as np # Numpy
import matplotlib.pyplot as plt # Plotting
import getpass # API keys
import xarray as xr # Data handling
import cartopy.crs as ccrs # Coordinate reference system
import cartopy.feature as cfeature # Map features
import copernicusmarine # Copernicus Marine Services Python API
import cmocean # Oceanography colormaps

# Load current velocity dataset
current_velocity_ds = copernicusmarine.open_dataset(dataset_id="cmems_mod_glo_phy-cur_anfc_0.083deg_P1D-m")

# Set latitudinal and longitudinal bounds
lat_bounds = slice(15.0, 65.0)
lon_bounds = slice(-145.0, -112.0)
time_coord = '2025-06-06'

print("RAN SUCCESSFULLY")