import json
import numpy as np

# 바람장을 나타내기 위한 데이터 포맷 샘플
# 위도 경도 높이 색상


def arrow(latitude, longitude, height, color, filepath):
    arrows = []
    for s in range(1, 50):
        for c in range(1, 50):
            arrow = {}
            arrow['latitude'] = round((float(latitude) + (0.00250 * s)),5)
            arrow['longitude'] = round((float(longitude) + (0.00250 * c)),5)
            arrow['height'] = int(height)
            arrow['latitudeEnd'] = round((float(latitude) + (0.00250 * s)),5)
            arrow['longitudeEnd'] = round((float(longitude) + (0.00250 * c)),5)
            arrow['heightEnd'] = int(height)
            arrow['color'] = color
            arrows.append(arrow)
    # json 파일 만들기
    out_file = open(filepath, "w", encoding='utf-8')
    json.dump(arrows, out_file, indent = 4, ensure_ascii=False)
    out_file.close()
if __name__ == '__main__':
    arrow('127.39491','36.41944','110', 'BLUE','./arrow50m.json')
    arrow('127.39491','36.41944','160', 'YELLOW','./arrow100m.json')
    arrow('127.39491','36.41944','360', 'PINK','./arrow300m.json')
    arrow('127.39491','36.41944','560', 'GREEN','./arrow500m.json')
    arrow('127.39491','36.41944','1060', 'RED','./arrow1000m.json')


# start_lat, start_lon = 36.4282169, 127.3862088
# end_lat, end_lon = 36.4283275, 127.4050294
# start_lat1, start_lon1 = 36.4156838, 127.394096
# end_lat1, end_lon1 = 36.4149729, 127.4115568

# # Define the number of points you want to interpolate
# num_points = 50

# # Create an array of evenly spaced values between the start and end coordinates
# lats = np.linspace(start_lat, end_lat, num_points)
# lons = np.linspace(start_lon, end_lon, num_points)
# lats1 = np.linspace(start_lat1, end_lat1, num_points)
# lons1 = np.linspace(start_lon1, end_lon1, num_points)

# # Calculate the longitude increment based on the difference between start and end longitudes
# lon_increment = (end_lon - start_lon) / num_points
# lon_increment1 = (end_lon1 - start_lon1) / num_points

# for lat, lon, lat1, lon1 in zip(lats, lons, lats1, lons1):
    

# # Loop through the arrays to print the corresponding latitude and longitude values
# arrows = []
# for lat, lon in zip(lats, lons):
#     arrow = {}
#     arrow['latitude'] = round(float(lat), 5)
#     arrow['longitude'] = round(float(lon), 5)
#     arrow['height'] = 160
#     arrow['latitudeEnd'] = round(float(lat), 5)
#     arrow['longitudeEnd'] = round(float(lon), 5)
#     arrow['heightEnd'] = 160
#     arrows.append(arrow)

# # Save the output as a JSON file
# filepath = "./arrow100m.json"
# with open(filepath, "w", encoding='utf-8') as out_file:
#     json.dump(arrows, out_file, indent=4, ensure_ascii=False)