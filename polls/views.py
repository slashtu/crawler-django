from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.http import Http404
from django.core.urlresolvers import reverse
import urllib2
from bs4 import BeautifulSoup
from polls.models import Choice, Question
import re
import polls

# Create your views here.
def index(request):
#    pets = Doghome('http://www.doghome.org.tw/phpbb2/i_love_animals.php?code=photostickers&tmpl=7').getPets()
    garden_pets = polls.getGardenPets()
    happy_pets = polls.getHappyPets()
#    for pet in pets:
#        print pet , '\n'

#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'garden_pets_list': garden_pets, 'happy_pets_list': happy_pets}
    return render(request, 'polls/index.html', context)

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

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))