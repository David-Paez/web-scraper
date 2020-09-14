from bs4 import BeautifulSoup
import requests

def get_links():
    source = requests.get('https://riskofrain2.gamepedia.com/Items').text
    items_page = BeautifulSoup(source, 'lxml')

    # tbody is the whole chart
    items_chart = items_page.tbody.findAll("tr")

    items_rows = []

    for row in items_chart:
        items_rows.append(row.findAll("td"))

    item_links = []
    for row in items_rows:
        for item in row:
            print(item.a['title'])
            link = "https://riskofrain2.gamepedia.com" + item.a['href']
            print(link)
            item_links.append(link)
            print("")

    return item_links

def scrape_info(link):    
    item_link = requests.get(link).text
    item_page = BeautifulSoup(item_link, 'lxml')

    print(item_page.prettify())

def main():
    links = get_links()
    scrape_info(links[0])

main()

# for link in item_links:
    # item_link = requests.get(link).text
    # item_page = BeautifulSoup(item_link, 'lxml')