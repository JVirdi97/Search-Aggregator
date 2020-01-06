import bs4, requests, tkinter
from bs4 import BeautifulSoup
from tkinter import * #from tkinter import everything

def Google_Search():
    SearchTerm=SearchBar.get()
    SearchBar.delete(0,"end")
    response=requests.get("https://www.google.com/search?q="+SearchTerm) #gets the first results page of the search
    if(response.status_code == requests.codes.ok):  #check the status of the request, if its not, show what code it is
        print("Google request successful")
    else:
        print("Google request failed, the response code is: "+response.status_code)
    soup=BeautifulSoup(response.text, "html.parser") #turns the html page into a soup, to extract information from
    for link in soup.find_all("a"): #foreach link in the page html
        if("/url?q=" in str(link)): #if the html line contains url then keep and process it
            link_href=str(link.get("href")) #get link to the page
            cutoff=link_href.find("&sa=U&ved") #get rid of useless end piece
            Site_Link=link_href[7:cutoff] #get rid of useless bit at start
            text.insert(INSERT, Site_Link) #put the link in the text box
            text.insert(INSERT, """"
""") #line break
            #print(Site_Link) #show the link

#SearchTerm=input("Enter your search terms: ") #get the search terms from user
#Page_html = Google_Search(SearchTerm) #get the page html
#Google_link_Searcher(Page_html) #get the links to pages
Form=Tk()
Form.geometry("500x500")

#canvas
canvas=Canvas(Form, width=400,height=300)
canvas.pack()

#button to search with
SearchBtn=Button(Form, text="Search", command=Google_Search)
canvas.create_window(350,140,window=SearchBtn)

#SearchBar for people to enter what they want to search
SearchBar= Entry(Form, width=40)
canvas.create_window(200,140,window=SearchBar)

#text to print the links to
text=Text(Form)
text.pack()

Form.mainloop()
