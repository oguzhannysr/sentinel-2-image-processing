from datetime import datetime
from osgeo import gdal
import rasterio as rio
import os
import numpy as np

def SCLbandResampling(safe_path, output_path):
    start = datetime.now()
    for root, dirs, files in os.walk(safe_path):

        for i in files: 
            if "_SCL_20m.jp2" in i:  inSCLPath=os.path.join(root,i)

    outDirName=inSCLPath.split("/")[4].split("\\")[0]
    outDir=os.path.join(output_path, outDirName)

    if not os.path.exists(outDir): os.mkdir(outDir)

    outSCLPath=os.path.join(outDir,os.path.basename(inSCLPath).replace("20m.jp2", "10m.tiff"))
    print("outDir:",outDir)
    print("inSCLPath:", inSCLPath)
    print("outSCLPath:", os.path.basename(outSCLPath))

    inSCLRead = gdal.Open(inSCLPath)
    gdal.Warp(outSCLPath, inSCLRead, xRes = 10, yRes = 10, resampleAlg = "near") #bilinear,cubic
