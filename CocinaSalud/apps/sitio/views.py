from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def acerca_de(request):
    return render(request, "acerca_de.html")