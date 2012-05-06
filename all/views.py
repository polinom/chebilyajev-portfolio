from django.shortcuts import render
from models import Galerry
from django.shortcuts import get_list_or_404


def galerry(request,galerry):
    images = get_list_or_404(Galerry, image_type=galerry)
    context = {'title':galerry, 'items': images}
    return render(request, 'galerry.html', context)