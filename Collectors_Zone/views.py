from django.shortcuts import render
from django.db.models import Q
from Posty.models import Post
from Dropy.models import Drop
from Forum.models import Temat
from django.contrib import messages


def home(request):
    Posts = Post.objects.all()[:8]
    Drops = Drop.objects.all().order_by('-Data')[:3]
    context = {'Posts': Posts, 'Drops': Drops}
    return render(request, 'Main_page/main.html', context)


def search(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            searched = request.POST['searched']
            posts = Post.objects.filter(Q(Tytuł__icontains=searched) | Q(Opis__icontains=searched))
            drops = Drop.objects.filter(Q(Tytuł__icontains=searched) | Q(Data__icontains=searched))
            topics = Temat.objects.filter(Tytuł__icontains=searched)

            if not posts and not drops and not topics:
                messages.success(request, 'Brak wyszukiwań dla podanej frazy.')
                return render(request, 'Main_page/search.html', {})
            else:
                return render(request, 'Main_page/search.html',
                              {'searched': searched, 'posts': posts, 'drops': drops, 'topics': topics})
        else:
            return render(request, 'Main_page/search.html', {})

    else:
        if request.method == 'POST':
            searched = request.POST['searched']
            posts = Post.objects.filter(Q(Tytuł__icontains=searched) | Q(Opis__icontains=searched))
            drops = Drop.objects.filter(Q(Tytuł__icontains=searched) | Q(Data__icontains=searched))

            if not posts and not drops:
                messages.success(request, 'Brak wyszukiwań dla podanej frazy.')
                return render(request, 'Main_page/search.html', {})
            else:
                return render(request, 'Main_page/search.html', {'searched': searched, 'posts': posts, 'drops': drops})
        else:
            return render(request, 'Main_page/search.html', {})
