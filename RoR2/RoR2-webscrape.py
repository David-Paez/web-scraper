from bs4 import BeautifulSoup
import requests

source = requests.get('https://riskofrain2.gamepedia.com/Items').text

items_page = BeautifulSoup(source, 'lxml')

# tbody is the whole chart
items_chart = items_page.tbody.findAll("tr")

items_rows = []

for row in items_chart:
    items_rows.append(row.findAll("td"))

for row in items_rows:
    for item in row:
        print(item.a['title'])
        print("https://riskofrain2.gamepedia.com" + item.a['href'])
        print("")

# print(items_page.tbody.tr.td.a['title'])

# for item in item_chart.tr.findAll('td'):
#     print(item.a['title'])

#     print("")
