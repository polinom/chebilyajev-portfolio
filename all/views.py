from django.shortcuts import render
from models import Image
from django.shortcuts import get_list_or_404
from django.utils import simplejson
from django.http import HttpResponse
from sorl.thumbnail import get_thumbnail

TITLE_DICT = {'illustration':'illustration.png',
             'storyboard': 'storyboard.png',
             'character_design': 'char_design.png'
}
PER_PAGE = 18


def gallery(request,gallery):
    page = int(request.GET.get('page',0))
    images = get_list_or_404(Image, gallery=gallery)
    pages = len(images)/float(PER_PAGE)
    pages = int(pages) if pages - int(pages) == 0 else int(pages) + 1
    title_img = TITLE_DICT[gallery]
    images = images[PER_PAGE*page:PER_PAGE+(page*PER_PAGE)]
    if not request.is_ajax():
        context = {'title':gallery, 'items': images[:PER_PAGE], 'first_item':images[0], 'title_img':title_img, 'pages':range(pages-1)}
        return render(request, 'gallery.html', context)
    else:
    	data = [{'image':image.image.url,'thumb':get_thumbnail(image.image, '58x58', crop='center', quality=99).url} for image in images]
    	return HttpResponse(simplejson.dumps(data),mimetype="application/json")