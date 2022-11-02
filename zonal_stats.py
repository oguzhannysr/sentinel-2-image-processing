import os
import pandas as pd
import geopandas as gpd
from rasterstats import zonal_stats

def ZonalStats(rasterfiles_path,vectorfiles_path):
    
    
    rasters_path_dir = []

    for files in os.walk(rasterfiles_path):
        rasters_path_dir.append(files[0])

    dates = []
    for c in range(1,len(rasters_path_dir)):
        split = rasters_path_dir[c].split('\\')
        dates.append(split[4][:-5])
            
    for i in range(1,len(rasters_path_dir)):
        for files in os.walk(rasters_path_dir[i]):
            bands_path = []
            for a in files[2]:
                if "SCL" in a :
                    files[2].remove(a)                
            bands_path.append(files[2])
        df = pd.DataFrame()    
        print(i)

        for y in range(0,len(bands_path[0])):
            parcels = gpd.read_file(vectorfiles_path)  
            gdf = parcels.join(
                pd.DataFrame(
                    zonal_stats(
                        vectors=parcels['geometry'], 
                        raster=rasters_path_dir[i] +"/"+ bands_path[0][y], 
                        stats=['count','mean','nodata']
                    )
                ),
                how='left'
            )
            gdf = gdf.drop(gdf.columns[list((range(1,12)))],axis=1)
            df2 = pd.concat([gdf,df],keys=[bands_path[0][y]])
            df = df.append(df2)
            if y == (len(bands_path[0])-1):
                df.to_excel(rasters_path_dir[i] +"/"+ "zonal_stats.xlsx")
            #locals()[dates[0]+'_'+'%s' % bands_path[0][y][:-4]] = gdf
            #df = pd.DataFrame(index=[bands_path[0]],columns=gdf.columns)
ZonalStats("D:\Projects\BarleyWheat\Output", "D:\Projects\BarleyWheat\Parcels\Doktar_Yozgat_2021_polygon_selection_edit_EPSG32636.shp")
