from django.shortcuts import render
from models import Galerry
from django.shortcuts import get_list_or_404

TITLE_DICT = {'illystration':'illustration.png',
             'storyboard': 'storyboard.png',
             'character_design': 'char_design.png'
}

def galerry(request,galerry):
    images = get_list_or_404(Galerry, image_type=galerry)
    title_img = TITLE_DICT[galerry]
    context = {'title':galerry, 'items': images, 'first_item':images[0], 'title_img':title_img}
    return render(request, 'galerry.html', context)