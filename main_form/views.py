from django.shortcuts import render, redirect, reverse
from .forms import PostForm
from .models import test, jedi_bd, padawan_bd
from .models import candidate as Candidate_model
from django.core.mail import send_mail
import json


# Create your views here.
def post_list(request):
    return render(request, 'index.html', {})


def jedi_form(request):
    print('>>>>>>>>>>>>>jedi_form<<<<<<<<<<<<<<<<<<')
    if request.method == 'POST':
        print('request.POST', request.POST['name'])
        planet = jedi_bd.objects.filter(name=request.POST['name'])[0]
        print('planet=', planet)
        return redirect(reverse(
            'list_candidate') + '?planet=' + str(
            planet.planet) + '&name=' + planet.name + '&order_code=' + str(
            planet.order_code))
    list_jedi = jedi_bd.objects.all()
    print('list_jedi = ', list_jedi)
    return render(request, 'jedi_form.html', {'list_jedi': list_jedi})


def candidate_on_planet(request):
    if request.method == 'GET' and 'planet' in request.GET:
        print('request.GET', request.GET)
        p = request.GET['planet']
        name = request.GET['name']
        order_code = request.GET['order_code']
        print(p)
        print(Candidate_model.objects.filter(
            planet__name=str(request.GET['planet'])))
        count_answer = range(1, test.objects.count() + 1)
        return render(request, 'candidate_on_planet.html', {
            'candidate': Candidate_model.objects.filter(
                planet__name=str(request.GET['planet'])),
            'count_answer': count_answer, 'order_code': order_code,
            'name': name})
    elif request.method == 'POST':
        print('request.POST', request.POST)
        res = [i for i in request.POST if i != 'name_jedi' and i != 'order_code' and i != 'csrfmiddlewaretoken']
        print(res)
        candidate = Candidate_model.objects.filter(email=res[0])
        print(candidate)
        name, email, age, planet = candidate[0].name, candidate[0].email, \
                                   candidate[0].age, candidate[0].planet
        print(name, email, age, planet,request.POST['name_jedi'],request.POST['order_code'])
        padawan_bd.objects.create(name=name, email=email, age=age,
                                  planet=planet,
                                  name_jedi=jedi_bd.objects.get(name=request.POST['name_jedi']),
                                  order_code= int(request.POST['order_code']))
        send_mail(
            'Поздравляем',
            'Вы стали падаванам, ваш учитель '+request.POST['name_jedi'],
            'from@example.com',
            [email],
            fail_silently=False,
        )
        candidate.delete()
        return redirect('jedi_form')
    return render(request, '', {'candidate': []})


def candidate_form(request):
    print('>>>>>>>>>>>>>jedi_form<<<<<<<<<<<<<<<<<<', request.method)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            email = post.email
            post.save()
            return redirect(reverse('test_form') + '?candidate=' + email)
        else:
            print('FALSE')
    else:
        form = PostForm()
    return render(request, 'candidate_form.html', {'form': form})


def test_form(request):
    posts = test.objects.all()
    if request.method == "POST":
        print(request.POST)
        candidate = Candidate_model.objects.filter(email=request.POST['email'])
        print('form=', candidate)
        if len(candidate) != 0:
            answers = {}
            for i in request.POST:
                if i.isdigit():
                    answers[i] = request.POST[i]
            candidate[0].answers = json.dumps(answers)
            candidate[0].save()
            print('answers=', answers)
            return redirect('test_form')
        else:
            print('FALSE')
    elif request.method == "GET":
        if 'candidate' in request.GET:
            candidate = \
                Candidate_model.objects.filter(email=request.GET['candidate'])[
                    0]
            candidate = {'name': candidate.name, 'email': candidate.email}
            return render(request, 'test.html',
                          {'posts': posts, 'form': candidate})
        else:
            return redirect('candidate_form')
    return render(request, 'test.html', {'posts': posts})
