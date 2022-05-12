from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    number = request.POST['number']
    number = int(number)
    res = number ** 2

    return render(request, 'about.html', {'res':res})