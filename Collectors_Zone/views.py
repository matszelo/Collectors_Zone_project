from django.shortcuts import render
from Posty.models import Post
from Dropy.models import Drop


def home(request):
    Posts = Post.objects.all()[:8]
    Drops = Drop.objects.all().order_by('-Data')[:6]
    context = {'Posts': Posts, 'Drops': Drops}
    return render(request, 'Main_page/main.html', context)