from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?N=100007709%20600559418%20601321492%20601321493%20601321556%20601326374%20601341484%20601341621%20601341631%20601294835%20601295933%208000&cm_sp=Cat_video-Cards_2-_-Visnav-_-2k-4k-gaming_2'

# opening up connection and grabbing the page
uClient = uReq(my_url)

# places raw html into a variable
page_html = uClient.read()

# closes connection
uClient.close()

# HTML parsing
page_soup = soup(page_html, "html.parser")

# Find all objects with the div class item-container
containers = page_soup.findAll("div", {"class":"item-container"})

# opening a new filewriter called products.csv
filename = "products.csv"
f = open(filename, "w")

# headers of the file
headers = "brand, product_name, shipping\n"

# write in the headers first
f.write(headers)

for container in containers:
    brand = container.div.div.a.img['title']

    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li",{"class":"price-ship"})
    # .strip() will remove /r /n and whitespace
    shipping = shipping_container[0].text.strip()

    print("")
    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

    # writing to my file the brand, product_name, and shipping of each item
    # replace() replaces string with another string
    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()



