from django.shortcuts import render

from .models import Blog

# Create your views here.
def main(request):
	return render(request, 'main.html')
def products(request):
	return render(request, 'products.html')

def products2(request):
	return render(request, 'products2.html')

def products3(request):
	return render(request, 'products3.html')
def products4(request):
	return render(request, 'products4.html')
def products5(request):
	return render(request, 'products5.html')
def products6(request):
	return render(request, 'products6.html')
def products7(request):
	return render(request, 'products7.html')
def products8(request):
	return render(request, 'products8.html')
def products9(request):
	return render(request, 'products9.html')
def review(request):
	return render(request,'review.html')

def suggest(request):
	return render(request, 'suggest.html')