import cdsapi
import zipfile
import os
import calendar
from time import sleep

c = cdsapi.Client(wait_until_complete=True, timeout=600)

years = range(1990, 2025)

for y in years:
    print(f"⬇️ Requesting ERA5-Land data for {y}...")
    outfile = f"era5land_precip_t2m_{y}.nc"

    try:
        c.retrieve(
            "reanalysis-era5-land",
            {
                "variable": [
                    "2m_temperature",
                    "total_precipitation",
                ],
                "year": str(y),
                "month": [f"{m:02d}" for m in range(1, 13)],
                "day": [f"{d:02d}" for d in range(1, 29)],  # avoid invalid days
                "time": ["00:00"],  # pick a single time per day
                "area": [62.0, -145.5, 60.5, -143.5],  # [N, W, S, E]  ~Cordova, AK
                "format": "netcdf",
            },
            outfile,
        )
    except Exception as e:
        print(f"❌ Failed for {y}: {e}")
        sleep(5)
        continue

    # --- Auto-unzip step ---
    if zipfile.is_zipfile(outfile):
        with zipfile.ZipFile(outfile, "r") as zf:
            zf.extractall(".")
            inner = zf.namelist()[0]
            new_name = outfile.replace(".nc", "_real.nc")
            os.rename(inner, new_name)
            print(f"✅ Extracted {inner} → {new_name}")

    else:
        print(f"✅ {outfile} is already a valid NetCDF file.")
