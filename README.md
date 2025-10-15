Code: Python
Purpose: Extracting temperature and precipitation from a customizable grid in ERA5-land (reanalysis data product)
Author: Isaac Reister
Initial usage: Investigating the precipitation and airtemperature records associated with the Copper River Discharge. This was done to support an NGA LTER synthesis paper on the Copper River.
Notes: 
Copper River discharge had already been obtained and processed in a matlab file, which is uploaded in 'flow_landtemp_precip_compare.ipynb'
ERA5 data is extracted in 'getCRriverprecipandtemperature.py' each day at time 00:00 for each grid point in a bounding box that is approximately the Copper River watershed, then averaged for each grid point. Data is downloaded on a yearly basis and saved as .nc files.
