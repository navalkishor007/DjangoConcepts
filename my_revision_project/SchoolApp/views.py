from django.shortcuts import render
# from django.http import HttpResponse
# from templates import SchoolApp

# Create your views here.
def home(request):
    vals = {'name': 'navalkishor', 'age': 23}
    return render(request, 'SchoolApp/index.html', context=vals)

def second_page(request):
    return render(request, 'school.html')
