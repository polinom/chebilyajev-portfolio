from django.shortcuts import render
from models import Image
from django.shortcuts import get_list_or_404

TITLE_DICT = {'illystration':'illustration.png',
             'storyboard': 'storyboard.png',
             'character_design': 'char_design.png'
}

def gallery(request,gallery):
    images = get_list_or_404(Image, gallery=gallery)
    title_img = TITLE_DICT[gallery]
    context = {'title':gallery, 'items': images, 'first_item':images[0], 'title_img':title_img}
    return render(request, 'gallery.html', context)