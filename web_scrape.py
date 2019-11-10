from urllib.request import urlopen as uReq #importing URL open function from request module within the urllib package
from bs4 import BeautifulSoup as soup #importing module BeautifulSoup from bs4 package

newegg_laptops = 'https://www.newegg.com/Laptops-Notebooks/Category/ID-223?Tpk=laptops'

#open up a connection and download the webpage
uClient = uReq(newegg_laptops)

page_html = uClient.read() #offloads contents into variable

uClient.close() #closes connection

page_soup = soup(page_html, "html.parser") #how to parse the webpage, in variable so it's not 'lost'

#all items stored in the div container item-container. use function to find and retrieve, send class as an object
containers = page_soup.findAll("div", {"class":"item-container"})

#grab first item in the item list. Parse like an array.Use len() to find out # of results
#container = containers[0]


#in the loop below always remember that findAll() returns a list of elements, index it to get to one set of results

#get to the laptop brand stored in the item branding div within the item info div, reference title attribute like you would a dictionary in Py
for container in containers:
    div_placeholder = container.findAll("div", {"class":"item-info"}) #returns a list of lists


    branding = div_placeholder[0].div.a.img["title"] #brand name for one laptop 


    title_container = container.findAll("a", {"class":"item-title"}) 



    product_name = title_container[0].text #product name is stored as the text within the a tag/a tag list details returned


    shipping_container = container.findAll("li",{"class":"price-ship"}) #list tag contains shipping details


    shipping_details =  shipping_container[0].text.strip() #clean out any extra spaces/lines 

    print("branding:" + branding)
    print("product name:" + product_name)
    print("shipping_details:" + shipping_details)



	

	#container_title = 


