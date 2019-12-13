"""
The purpose of this program is to aggregate content for the users search term(s)
and display it for the user
"""
def a_tag_with_href(tag):
    return tag.has_attr("href")
#^this function willreturn all a tags with the href attribute
import bs4, requests, re
#^bs4 is beautifulsoup4, re is regex
from bs4 import BeautifulSoup
SearchFor = input("Enter search terms: ")
#^user enters what they are searching for
response=requests.get("https://google.com/search?q="+SearchFor) #results page 1
SearchPage=response.text #get the html of the response as string
SearchPageHTML=BeautifulSoup(SearchPage,"html.parser")
#^the html for the search page
ListOfLinks=SearchPageHTML.find_all(a_tag_with_href)
"""PageLinks=[0,1,2,3,4,5,6,7,8,9] #array to replace entries with 10 links
for i in range (0,len(PageLinks)):
    PageLinks[i]=ListOfLinks[i]
    print(PageLinks[i])"""
for i in range(0,len(ListOfLinks)):
    #print(ListOfLinks[i].get("href"))
    print(ListOfLinks[i].prettify())
#access the page information
#skim it to get stuff to aggregate
#present it
#danny de finito \o/
"""need to get the information from the top 10 sites in PageLinks then I think
functionality will be done, then just make it look pretty"""
