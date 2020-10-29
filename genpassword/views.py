from django.shortcuts import render
from django.http import HttpResponse
from random import choice

# Create your views here.


def main_form(request):
    return render(request, 'genpassword/mainform.html')


def form1(request):
    length = int(request.GET.get('length'))
    ascii_range = list(range(97, 123))
    if request.GET.get('uppercase'):
        ascii_range.extend(list(range(65, 91)))
    if request.GET.get('numbers'):
        ascii_range.extend(list(range(48, 58)))
    if request.GET.get('specialchar'):
        ascii_range.extend(list(range(58, 65)))
        ascii_range.extend(list(range(91, 97)))
    res = ''
    for i in range(length):
        res += str(chr(choice(ascii_range)))
    return render(request, 'genpassword/showpassword.html', {'password': res})


def about(request):
    return render(request, 'genpassword/aboutpage.html')
