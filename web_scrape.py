from urllib.request import urlopen as uReq #importing URL open function from request module within the urllib package
from bs4 import BeautifulSoup as soup #importing module BeautifulSoup from bs4 package

#import schedule package to automate scraping task
#schedule found here:https://pypi.org/project/schedule/
import schedule
import time  

def laptop_price_tracker():

    newegg_laptops = 'https://www.newegg.com/Laptops-Notebooks/Category/ID-223?Tpk=laptops'
    
    uClient = uReq(newegg_laptops)#open up a connection and download the webpage
    
    page_html = uClient.read() #offloads contents into variable

    uClient.close() #closes connection

    page_soup = soup(page_html, "html.parser") #how to parse the webpage, in variable so it's not 'lost'

    containers = page_soup.findAll("div", {"class":"item-container"})#all items stored in the div container item-container. use function to find and retrieve, send class as an object


    filename = "laptop_sales.csv"

    f = open(filename, "w")  #open file with write tag to write 

    headers = "branding, product_name, previous_price, current_price, shipping_details, product_rating_out_of_five\n" #ensure a new line at end

    f.write(headers)

    #in the loop below always remember that findAll() returns a list of elements, index it to get to one set of results

    #get to the laptop brand stored in the item branding div within the item info div, reference title attribute like you would a dictionary in Py

    for container in containers:
        div_placeholder = container.findAll("div", {"class":"item-info"}) #returns a list of lists


        branding = div_placeholder[0].div.a.img["title"] #brand name for one laptop 


        title_container = container.findAll("a", {"class":"item-title"}) 


        product_name = title_container[0].text #product name is stored as the text within the a tag/a tag list details returned


        shipping_container = container.findAll("li",{"class":"price-ship"}) #list tag contains shipping details


        shipping_details =  shipping_container[0].text.strip() #clean out any extra spaces/lines 


        rating_container = container.findAll("a", {"class": "item-rating"})


        product_rating = rating_container[0]["title"] #retrieve the rating as an attribute of the a tag, stored


        out_of_five = product_rating[-1] #rating is the last thing in the string


        prev_price_container = container.findAll("li", {"class": "price-was"})


        prev_price  = prev_price_container[0].text  #price details 


        #some laptop deals don't have a previous price so check for empty strings
        if not prev_price:
            previous_price = prev_price.splitlines()[1]
        else:
            previous_price = "N/A"

        current_price_container = container.findAll("li", {"class":"price-current"})

        price_contain_two = current_price_container[0].text.strip()  #current laptop price


        #splitlines() used bto divide the string into an array for better extraction. Initial look for one product: 
        #'\n\n|\n$1,299.99\xa0(3 Offers)\n\n–\n\n' .> after splitlines: ['|\n', '$1,299.99\xa0(3 Offers)\n', '\n', '–']

        current_price = price_contain_two.splitlines()[1]

        f.write(branding + "," + product_name.replace(",", "|") + "," + previous_price + "," + current_price+ ","+shipping_details + "," + out_of_five + "\n")
        print("branding:" + branding)
        print("product name:" + product_name)
        print("previous price: " +previous_price)
        print("current price: " +current_price)
        print("shipping_details:" + shipping_details)
        print("product rating/5:" + out_of_five)

    f.close()


    

if __name__ == "__main__":

    #schedule.every().wednesday.do(laptop_price_tracker)
    schedule.every(30).minutes.do(laptop_price_tracker)

    while True:
        schedule.run_pending()
        time.sleep(1)



