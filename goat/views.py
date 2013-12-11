from django.shortcuts import render

def index(request):
  context = {'somthin':1}
  return render(request, 'goat/index.html', context)