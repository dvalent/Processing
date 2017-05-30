from bs4 import BeautifulSoup
import urllib2
import json


url = "https://github.com/b-g/processing-sublime/tree/master/Snippets"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content, "html.parser")

a = soup.find_all(name= 'a')
myLinks = []

for link in a:
    if 'blob' in link.get('href'):
        newlink = str('https://raw.githubusercontent.com'+link.get('href'))
        cc = newlink.replace('blob/',"")
        myLinks.append(cc)

#print myLinks[0]
def writeSnippets(towrite):
    with open("snippets.cson",'a') as f:
        f.write(towrite)

def linker(link):
    #print 'LINK IS {}'.format(link)
    content = urllib2.urlopen(link).read()
    linkSoup = BeautifulSoup(content,"html.parser")
    print linkSoup.prettify()
    command =  linkSoup.find(name='tabtrigger').string
    autocomplete = linkSoup.find(name='content').string
    name =  linkSoup.find(name='description').string
    #name
    #prefix
    #body
    end = "  '{}':\n    'prefix': '{}'\n    'body': '{}'\n".format(name,command,autocomplete)
    writeSnippets(end)
    return end



result =  [linker(i) for i in myLinks]
