def clip_raster(rasterfiles_path,clipping_area_path):
    
    import geopandas as gpd
    import rioxarray as rxr
    import os
    from rasterstats import zonal_stats
    from shapely.geometry import mapping
    import rasterio as rio
    global bands_path
    rasterfiles_path = "D:\Projects\BarleyWheat\Output"
    clipping_area_path = "D:\Downloads\study_area.geojson"
    rasters_path_dir = []
    for files in os.walk(rasterfiles_path):
        rasters_path_dir.append(files[0])
    
    for i in range(1,len(rasters_path_dir)):
        bands_path = []
        for files in os.walk(rasters_path_dir[i]):
            bands_path.append(files[2])
    
        bands_path[0].remove("Veg_Max_Min_Value.xlsx")
        for y in range(0,len(bands_path[0])):
            raster = rxr.open_rasterio(rasters_path_dir[i] +"/"+ bands_path[0][y])
            study_area = gpd.read_file(clipping_area_path)
            image_clipped = raster.rio.clip(study_area.geometry.apply(mapping),study_area.crs)
            
            split = rasters_path_dir[i].split("\\")
            image_clipped.rio.to_raster(rasterfiles_path + '/' +split[-1] + "/" + "clipped_" + bands_path[0][y])
            
#%%
clip_raster("D:\Projects\BarleyWheat\Output","D:\Downloads\study_area.geojson")
#%%
res = list(map(str.strip, bands_path[0]))
