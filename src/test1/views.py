from django.shortcuts import render, get_object_or_404
from models import Somebody
# Create your views here.

def index(request):
    first_person = get_object_or_404(Somebody, pk=1)
    return render(request, 'test1/index.html', {'person':first_person})