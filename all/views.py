from django.shortcuts import render
from models import Image
from django.shortcuts import get_list_or_404

TITLE_DICT = {'illystration':'illustration.png',
             'storyboard': 'storyboard.png',
             'character_design': 'char_design.png'
}

def gallery(request,gallery):
    images = get_list_or_404(Image, gallery=gallery)
    pages = len(images)/float(18)
    pages = int(pages) if pages - int(pages) == 0 else int(pages) + 1
    title_img = TITLE_DICT[gallery]
    context = {'title':gallery, 'items': images[:18], 'first_item':images[0], 'title_img':title_img, 'pages':range(pages)}
    return render(request, 'gallery.html', context)