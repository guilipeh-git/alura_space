from django.shortcuts import render
# from django.http import HttpResponse as http_resp

# Create your views here.

# def index(request):
#     html = f'Hello world {request}'
#     return http_resp(html)

def index(request):
   return render(request, 'index.html')