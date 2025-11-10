import xarray as xr
import matplotlib.pyplot as plt

# Coordinates
lat0 = 21.3954
lon0 = -158.0315

# Extent of bounding box
dlat = 0.05
dlon = 0.05
lat_min, lat_max = lat0 - dlat, lat0 + dlat
lon_min, lon_max = lon0 - dlon, lon0 + dlon

# NCEI THREDDS OPeNDAP for CRM Vol.10
url = "https://www.ngdc.noaa.gov/thredds/dodsC/crm/crm_vol10.nc"

# Open dataset
ds = xr.open_dataset(url)

# Slice bounding box from full dataset
cut = ds["z"].sel(
    y=slice(lat_min, lat_max),
    x=slice(lon_min, lon_max)
)
cut_flipped = cut[::-1, ::-1]

# Plot
plt.figure(figsize=(7, 6))
im = plt.imshow(
    cut.values,
    extent=[float(cut.x.min()), float(cut.x.max()), float(cut.y.min()), float(cut.y.max())],
    origin="upper",
    cmap="terrain",
    interpolation="nearest"
)
plt.colorbar(im, label="Elevation (m)")
plt.scatter([lon0], [lat0], s=40, edgecolor="k", facecolor="none", linewidths=1.5, label="Ehukai Beach Park")
plt.title("NCEI Coastal Relief Model (CRM) — Ehukai / Pūpūkea, Oʻahu")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.show()
