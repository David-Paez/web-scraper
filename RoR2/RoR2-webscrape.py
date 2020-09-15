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


def scrape_item(links, file):
    headers = "item_name, item_image_link, item_quick_desc, item_rarity, item_category, item_cooldown, item_unlock\n"
    file.write(headers)

    for link in links:
        item_link = requests.get(link).text
        item_page = BeautifulSoup(item_link, 'lxml')

        item_name = "\"" + item_page.h1.text + "\""

        item_box = item_page.find("table", class_="infoboxtable").tbody
        item_box_rows = item_box.findAll("tr")
        item_image_link = item_box.img['src']
        item_quick_desc = "\"" + item_box.find("td", class_="infoboxdesc").text.strip() + "\""

        item_rarity = "N/A"
        item_category = "N/A"
        item_cooldown = "N/A"
        item_unlock = "N/A"

        for row in item_box_rows:
            try:
                if str.find(row.td.text, "Rarity") > -1:
                    item_rarity = row.a.text
            except:
                pass

            try:
                if str.find(row.td.text, "Category") > -1:
                    item_category = row.a.text
            except:
                pass

            try:
                if str.find(row.td.text, "Cooldown") > -1 and "%" not in row.findNext('td').findNext('td').text:
                    item_cooldown = row.findNext('td').findNext('td').text.strip()
            except:
                pass

            try:
                if str.find(row.td.text, "Unlock") > -1:
                    item_unlock = row.a.text
            except:
                pass
            
        # Finds Rarity anywhere
        # print(item_page.find(text="Rarity"))

        print("Item Name: "+ item_name + "\n" + "Image Link: " + item_image_link + "\n" + "Image Quick Desc: " + item_quick_desc
        + "\n" + "Item Rarity: " + item_rarity + "\n" + "Item Category: " + item_category + "\n" + 
        "Item Cooldown: " + item_cooldown + "\n" + "Item Unlock: " + item_unlock)

        print("")

        file.write(item_name + "," + item_image_link + "," + item_quick_desc + "," + item_rarity + "," + item_category 
        + "," + item_cooldown + "," + item_unlock + "\n")


def main():
    f = open("RoR2-items.csv", "w")
    links = get_links()
    scrape_item(links, f)
    f.close()


main()

# for link in item_links:
# item_link = requests.get(link).text
# item_page = BeautifulSoup(item_link, 'lxml')
