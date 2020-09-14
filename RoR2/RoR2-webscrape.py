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
            link = "https://riskofrain2.gamepedia.com" + item.a['href']
            item_links.append(link)
            # print(item.a['title'])
            # print(link)
            # print("")

    return item_links

def scrape_info(links): 
    link = links[0]
    item_link = requests.get(link).text
    item_page = BeautifulSoup(item_link, 'lxml')

    item_name = item_page.h1.text

    item_box = item_page.find("table", class_="infoboxtable").tbody
    item_box_rows = item_box.findAll("tr")
    item_image_link = item_box.img['src']
    item_quick_desc = item_box.find("td", class_="infoboxdesc")

    print(item_image_link)
    # item_image_link = item_box_rows[1].a.img['src']
    # item_small_desc = item_box_rows[2].td.text
    # item_quick_desc = item_box_rows[3].text
    # item_rarity = item_box_rows[4].a.text
    # item_category = item_box_rows[5].text
    

    # print(item_name + "\n" + item_image_link + "\n" + item_small_desc + "\n" + item_quick_desc 
    # + "\n" + item_rarity + "\n" + item_category)

def main():
    links = get_links()
    scrape_info(links)

main()

# for link in item_links:
    # item_link = requests.get(link).text
    # item_page = BeautifulSoup(item_link, 'lxml')