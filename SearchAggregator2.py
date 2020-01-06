import bs4, requests, tkinter
from bs4 import BeautifulSoup
from tkinter import * #from tkinter import everything

def Google_Search():
    SearchTerm=SearchBar.get() #get the search term from the search bar in the form
    SearchBar.delete(0,"end") #empty the search bar (maybe keep the search query?)
    response=requests.get("https://www.google.com/search?q="+SearchTerm) #gets the first results page of the search
    if(response.status_code == requests.codes.ok):  #check the status of the request, if it failed, show what code it is
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
"""the 2 text.insert lines insert the link into the text box, and then put a
clear line between the links.
"""

#SearchTerm=input("Enter your search terms: ") #get the search terms from user
#Page_html = Google_Search(SearchTerm) #get the page html
#Google_link_Searcher(Page_html) #get the links to pages
""" ^3 lines above are not needed, just allow me to test the google_Search fn
without using the form """
Form=Tk() #registers form as the fn which will be called from the TK mainloop
Form.geometry("800x500") #make the form [x,y] in size

#canvas
canvas=Canvas(Form, width=400,height=300) # canvas with dimensions [400,300]
canvas.pack() # add the canvas to the form, Form

#button to search with
SearchBtn=Button(Form, text="Search", command=Google_Search)
#^ when the user clicks the button, it calls the google_search function to get the search results and print them
canvas.create_window(350,140,window=SearchBtn)
#^add the SearchBtn to the canvas in the form

#SearchBar for people to enter what they want to search
SearchBar= Entry(Form, width=40)
canvas.create_window(200,140,window=SearchBar)
"""^ adds the search bar to the canvas. this is used to input the search query
for the Google_Search function """

#text to print the links to
text=Text(Form)
text.pack()
#^the contents of the text are manipulated elsewhere using the text.insert(INSERT, "[insert thing here]") function

Form.mainloop() #to draw the form to process the events on the form
