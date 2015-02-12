from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.http import Http404
from django.core.urlresolvers import reverse
import urllib2
from bs4 import BeautifulSoup
from pets.models import Choice, Question
import re
import pets

# Create your views here.
def index(request):
#    pets = Doghome('http://www.doghome.org.tw/phpbb2/i_love_animals.php?code=photostickers&tmpl=7').getPets()
    garden_pets = pets.getGardenPets()
    happy_pets = pets.getHappyPets()
#    for pet in pets:
#        print pet , '\n'

#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'garden_pets_list': garden_pets, 'happy_pets_list': happy_pets}
    return render(request, 'pets/index.html', context)

#    response = urllib2.urlopen('http://www.doghome.org.tw/phpbb2/i_love_animals.php?code=photostickers&tmpl=7')
#    html = response.read()
#
#    soup = BeautifulSoup(html)
#
#    array = soup.findAll(href=re.compile("^http://www.doghome.org.tw/phpbb2/viewtopic.php"))
#
#    print array[20]
#    print array[20].img

#    print array[20]
#
#    print 'img' in str(array[20])

#    filter_str = 'img border'
#
#    pets_array = [ pet for pet in array if filter_str in str(pet) ]
#
#    for item in pets_array:
#        print item
