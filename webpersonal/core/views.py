from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    html_text="<h1> Pagina en desarrollo </h1> "
    for i in range (5):
        html_text+="<h1> Pagina en desarrollo </h1> "
    return HttpResponse(html_text)