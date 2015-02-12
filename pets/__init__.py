import dog

garden_pets = dog.Doghome('http://www.doghome.org.tw/phpbb2/i_love_animals.php?code=photostickers&tmpl=7').getPets()

happy_pets = dog.Doghome('http://www.tsaca.org.tw/phpBB3/viewforum.php?f=119').getHappyPets()
happy_pets50 = dog.Doghome('http://www.tsaca.org.tw/phpBB3/viewforum.php?f=119&start=50').getHappyPets()
happy_pets100 = dog.Doghome('http://www.tsaca.org.tw/phpBB3/viewforum.php?f=119&start=100').getHappyPets()
happy_pets150 = dog.Doghome('http://www.tsaca.org.tw/phpBB3/viewforum.php?f=119&start=150').getHappyPets()
happy_pets200 = dog.Doghome('http://www.tsaca.org.tw/phpBB3/viewforum.php?f=119&start=200').getHappyPets()
happy_pets250 = dog.Doghome('http://www.tsaca.org.tw/phpBB3/viewforum.php?f=119&start=250').getHappyPets()

happy_petsAll = happy_pets + happy_pets50 + happy_pets100 + happy_pets150 + happy_pets200 + happy_pets250

def getHappyPets():
    return happy_petsAll

def getGardenPets():
    return garden_pets