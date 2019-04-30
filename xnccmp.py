import xarray as xr

import sys

ds1 = xr.open_dataset(sys.argv[1])
ds2 = xr.open_dataset(sys.argv[2])

print(ds1.equals(ds2))
