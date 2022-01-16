import urllib.request as request
import json
import csv
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)

f = open('data.csv', 'w', encoding='utf-8')
w = csv.writer(f)

title = ['景點名稱','區域','經度','緯度','第一張圖檔網址']
w.writerow(title)
    
for test in data['result']['results']:
    total_data = []
    total_data.append(test['stitle'])
    total_data.append(test['address'][5]+test['address'][6]+test['address'][7])
    total_data.append(test['longitude'])
    total_data.append(test['latitude'])
    total_data.append('https' + test['file'].split('https')[1])
    
    w.writerow(total_data)

f.close()