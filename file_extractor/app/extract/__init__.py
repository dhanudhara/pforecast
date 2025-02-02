import pandas as pd
import numpy as np

from netCDF4 import Dataset, num2date
from typing import Any


def get_dataframe(path: str) -> Any:
    with Dataset(path, 'r') as dataset:
        time_var = dataset.variables['time']
        lat = dataset.variables['lat'][:]
        lon = dataset.variables['lon'][:]
        mp_concentration = dataset.variables['mp_concentration'][:]
        num_mp_samples = dataset.variables['num_mp_samples'][:]
        stddev_mp_samples = dataset.variables['stddev_mp_samples'][:]

        times = num2date(time_var[:], units=time_var.units)

        lat_2d, lon_2d = np.meshgrid(lat, lon)
        lat_flat = lat_2d.flatten()
        lon_flat = lon_2d.flatten()
        num_spatial_points = len(lat_flat)

        dfs = []

        for i, time in enumerate(times):
            mp_conc_flat = mp_concentration[i].flatten()
            num_samples_flat = num_mp_samples[i].flatten()
            stddev_flat = stddev_mp_samples[i].flatten()
            df_time = pd.DataFrame({
                'time': [time] * num_spatial_points,
                'lat': lat_flat,
                'lon': lon_flat,
                'mp_conc': mp_conc_flat,
                'num_mp_samples': num_samples_flat,
                'stddev_mp_samples': stddev_flat
            })
            dfs.append(df_time)

        return pd.concat(dfs, ignore_index=True)
