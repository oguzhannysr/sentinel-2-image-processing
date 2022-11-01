from datetime import datetime
import rasterio as rio
import os
import numpy as np
start = datetime.now()

with rio.open(outSCLPath) as SCLBand_src:
    SCLBand = SCLBand_src.read(1)
    SCLBand_meta = SCLBand_src.profile
    
maskedSLC = np.logical_or(np.equal(SCLBand,4),np.equal(SCLBand,5))
for root, dirs, files in os.walk(safe_path):
    for i in files: 
        if "_B02_10m.jp2" in i:  B02Path=os.path.join(root,i)
        if "_B03_10m.jp2" in i:  B03Path=os.path.join(root,i)
        if "_B04_10m.jp2" in i:  B04Path=os.path.join(root,i)
        if "_B08_10m.jp2" in i:  B08Path=os.path.join(root,i)


with rio.open(B02Path) as B02_src:
    B02 = B02_src.read(1)
    bandsMeta = B02_src.profile
with rio.open(B03Path) as B03_src:
    B03 = B03_src.read(1)
    vegMeta = B03_src.profile # for vegetation indices
with rio.open(B04Path) as B04_src:
    B04 = B04_src.read(1)
with rio.open(B08Path) as B08_src:
    B08 = B08_src.read(1)

noDataValue_Bands = 65535
scale_factor = 10000
noDataValue_Indices = -9999
bandsMeta.update({'nodata': noDataValue_Bands,
                 'driver' : "GTiff"})
vegMeta.update({'nodata': noDataValue_Indices,
                       'driver' : "GTiff",
                       'dtype' : rio.int16})

ImageBandsArray = list((B02.astype('float32'),B03.astype('float32'),
                        B04.astype('float32'),B08.astype('float32')))
ImageBandsName = list(("B02","B03","B04","B08"))
finish = datetime.now()
res = finish-start
print(res.seconds)
