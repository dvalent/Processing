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
    #print linkSoup.prettify()
    try:
        command =  linkSoup.find(name='tabtrigger').string

    except:
        command =  linkSoup.find(name='description').string[:3]

    autocomplete = linkSoup.find(name='content').string
    #print repr(autocomplete)
    name =  linkSoup.find(name='description').string
    #name
    #prefix
    #body
    end = "  '{}':\n    'prefix': '{}'\n    'body': {}\n".format(name,command,repr(autocomplete)[1::])
    writeSnippets(end)

    return end


for i,e in enumerate(myLinks):
    #print e
    print i
    linker(e)
