import json

filepath = './box200m.json'

# 필드 만들기
box200 = []
for x in range(1, 51):
    for i in range(1, 51):
        box = {}
        box['x'] = int(10000)
        box['y'] = int(10000)
        box['h'] = int(1000)
        box['latitude'] = round(float(131.08863 - (0.11150*i)),5)
        box['longitude'] = round(float(38.62174 - (0.09000*x)),5)
        box['z'] = int(200)
        box['color'] = str('SKYBLUE')
        box200.append(box)
for x in range(1, 51):
    for i in range(1, 51):
        box = {}
        box['x'] = int(10000)
        box['y'] = int(10000)
        box['h'] = int(1000)
        box['latitude'] = round(float(131.08863 - (0.11150*i)),5)
        box['longitude'] = round(float(38.62174 - (0.09000*x)),5)
        box['z'] = int(1200)
        box['color'] = str('YELLOW')
        box200.append(box)
for x in range(1, 51):
    for i in range(1, 51):
        box = {}
        box['x'] = int(10000)
        box['y'] = int(10000)
        box['h'] = int(1000)
        box['latitude'] = round(float(131.08863 - (0.11150*i)),5)
        box['longitude'] = round(float(38.62174 - (0.09000*x)),5)
        box['z'] = int(2200)
        box['color'] = str('RED')
        box200.append(box)




# json 파일 만들기
out_file = open(filepath, "w", encoding='utf-8')
json.dump(box200, out_file, indent = 4, ensure_ascii=False)
out_file.close()