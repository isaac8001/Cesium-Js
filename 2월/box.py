import json
import sys

filepath = './box50m.json'

# 박스 갯수, 가로, 세로, 높이, 위도, 경도, 땅에서 부터 몇 미터에서 시작할지, 박스 색상 3개
# 박스의 크기에 따라서 간격이 넓어지고 줄어야 함.
# 가로 박스 크기에 따라서 if문으로 우선 간격 조절 하기
# z = 땅에서 시작하는 위치 
# def makebox(boxNum, x, y, h, latitude, longitude, z, color1, color2, color3):
#     hight = int(h)
#     zin = int(z)
#     box200 = []
#     color = [color1, color2, color3]
#     startHight = [zin, zin + hight, zin + hight + hight]
#     for i in range(len(color)):
#         for s in range(1, int(boxNum) + 1):
#             for c in range(1, int(boxNum) + 1):
#                 box = {}
#                 box['x'] = int(x)
#                 box['y'] = int(y)
#                 box['h'] = int(h)
#                 box['latitude'] = round((float(latitude) + (0.00010 * s)),5)
#                 box['longitude'] = round((float(longitude) + (0.00090 * c)),5)
#                 box['z'] = startHight[i]
#                 box['color'] = str(color[i].upper())
#                 box200.append(box)
#     # json 파일 만들기
#     out_file = open(filepath, "w", encoding='utf-8')
#     json.dump(box200, out_file, indent = 4, ensure_ascii=False)
#     out_file.close()
    
# if __name__ == '__main__':
#     makebox('50', '10','10','100','127.39491','36.41944','200','SKYBLUE', 'PINK','YELLOW')

def makebox(boxNum, x, y, h, latitude, longitude, z, color1, color2, color3):
    hight = int(h)
    zin = int(z)
    box200 = []
    color = [color1, color2, color3]
    startHight = [zin, zin + hight, zin + hight + hight]
    boxWidth = 0.00090 # width of each box (in degrees)
    boxHeight = 0.00110 # height of each box (in degrees)
    halfBoxWidth = boxWidth / 2
    halfBoxHeight = boxHeight / 2
    for i in range(len(color)):
        for s in range(1, int(boxNum) + 1):
            for c in range(1, int(boxNum) + 1):
                box = {}
                box['x'] = int(x)
                box['y'] = int(y)
                box['h'] = int(h)
                # calculate the center latitude and longitude of the box
                centerLatitude = round((float(latitude) + (boxHeight * (s - 0.5))), 5)
                centerLongitude = round((float(longitude) + (boxWidth * (c - 0.5))), 5)
                # adjust the latitude and longitude values by subtracting half the height and width of the box
                box['latitude'] = round((centerLatitude - halfBoxHeight), 5)
                box['longitude'] = round((centerLongitude - halfBoxWidth), 5)
                box['z'] = startHight[i]
                box['color'] = str(color[i].upper())
                box200.append(box)
    # json 파일 만들기
    out_file = open(filepath, "w", encoding='utf-8')
    json.dump(box200, out_file, indent = 4, ensure_ascii=False)
    out_file.close()

if __name__ == '__main__':
    makebox('50', '10','10','60','127.39491','36.41944','200','SKYBLUE', 'PINK','YELLOW')