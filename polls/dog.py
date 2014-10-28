from bs4 import BeautifulSoup
import urllib2
import re

class Pet:
    def __init__( self, path, img ):
        self.path = path
        self.img =img

    def __str__(self):
        return 'path: %s img: %s' % (self.path, self.img)

class Doghome:
    def __init__(self, url):
        self.url = url
        self.pets = []

    def getPets(self):
        response = urllib2.urlopen( self.url)
        html = response.read()
        soup = BeautifulSoup(html)
        array = soup.findAll(href=re.compile("^http://www.doghome.org.tw/phpbb2/viewtopic.php"))

        for item in array:
            if 'img border' in str(item):
                path = item['href']
                img = item.img['src']
                pet = Pet( path.encode('utf-8'), img.encode('utf-8'))
                self.pets.append(pet)

        return self.pets

    def getHappyPets(self):
        response = urllib2.urlopen( self.url)
        html = response.read()
        soup = BeautifulSoup(html)

        soup = soup.findAll("ul", { "class" : "topiclist topics" })

#        f = open('dog.html', 'w')
#        f.write(str(array))

        array = soup[1].findAll(href=re.compile("/viewtopic.php?"))

        for item in array:
            if 'img class' in str(item):
                path = 'http://www.tsaca.org.tw/phpBB3' + item['href'][1:]
                img = 'http://www.tsaca.org.tw/phpBB3' + item.img['src'][1:]
                pet = Pet( path.encode('utf-8'), img.encode('utf-8'))
                self.pets.append(pet)

        return self.pets