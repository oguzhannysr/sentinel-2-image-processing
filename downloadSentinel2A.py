import landsatxplore
from landsatxplore.earthexplorer import EarthExplorer

path = ""
api = landsatxplore.api.API('username', 'password')
scenes = api.search(
    dataset='sentinel_2a',
    latitude=39.547811, #lat,long,start date,end date, cloud per
    longitude=35.022035,
    start_date='2020-10-01',
    end_date='2021-07-20',
    max_cloud_cover=25)

print('{} scenes found.'.format(len(scenes)))

api.logout()

image_id = []
for i in range(0,len(scenes)):
    name_id = scenes[i]['display_id']
    image_id.append(name_id)

for i in range(0,len(image_id)):
    ee = EarthExplorer('username', 'password')
    ee.download(image_id[i], output_dir=path)
    ee.logout()
