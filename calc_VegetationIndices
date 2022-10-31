import numpy as np
import os
import rasterio as rio
from datetime import datetime

start = datetime.now()

ndvi = (B08-B04)/(B08+B04)*scale_factor
sr1 = (B08/B04)*scale_factor
sr2 = (B08/B03)*scale_factor
osavi = (1.0 + 0.16) * ((B08-B04)/(B08-B04+0.16))*scale_factor
mcari2 = 1.5 * (2.5 * (B08 - B04) - 1.3 * (B08 - B03)) / np.sqrt(np.power((2.0 * B08 + 1.0), 2) - (6.0 * B08 - 5.0 * np.sqrt(B04)) - 0.5)*scale_factor
mtvi1 = 1.2 * (1.2 * (B08 - B03) - 2.5 * (B04 - B03))
tvi =np.sqrt((((B04 - B03) / (B04 + B03))) + 0.5)*scale_factor
tgi = (((B03-0.39)*(B04-0.61))*B02)*scale_factor
vari = (B03 - B04) / (B03 + B04 - B02)*scale_factor
gndvi = (B08 - B03) / (B08 + B03)*scale_factor
savi = ((B08-B04)/(B08 + B04 + 0.5)) * (1+0.5)*scale_factor
evi = 2.5 * (B08 - B04) / ((B08 + 6.0 * B04 - 7.5 * B02) + 1.0)*scale_factor
msavi = (2.0 * B08 + 1.0 - np.sqrt(np.power((2.0 * B08 + 1.0), 2) - 8.0 * (B08 - B04))) / 2.0 * scale_factor
gsavi = (B08 - B03) / (B08 + B03 + 0.482) * (1.0 + 0.482)*scale_factor
ivi = (B08 - 0.809) / (0.393 * B03)*scale_factor

VegIndicesArray = list((ndvi,sr1,sr2,osavi,mcari2,mtvi1,
                           tvi,tgi,vari,gndvi,savi,evi,
                           msavi,gsavi,ivi))
VegIndicesName = list(("ndvi","sr1","sr2","osavi","mcari2","mtvi1",
                           "tvi","tgi","vari","gndvi","savi","evi",
                           "msavi","gsavi","ivi"))
for i in range(len(ImageBandsArray)):
    ImageBandsArray[i][np.logical_not(maskedSLC)] = noDataValue_Bands
    with rio.open(os.path.join(outDir,os.path.basename(inSCLPath).replace("20m.jp2", "10m.tiff").replace("SCL",ImageBandsName[i])), 'w', **bandsMeta) as output_image:
        output_image.write(ImageBandsArray[i],1)

for i in range(len(VegIndicesArray)):        
    VegIndicesArray[i][np.logical_not(maskedSLC)] = noDataValue_Indices
    with rio.open(os.path.join(outDir,os.path.basename(inSCLPath).replace("20m.jp2", "").replace("SCL_",VegIndicesName[i])) + ".tif", 'w', **vegMeta) as output_image:
        output_image.write(VegIndicesArray[i],1)               
finish = datetime.now()
res = finish-start
print(res.seconds)
