from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm
from .models import Post


def all_posts(request):
    Posts = Post.objects.all()
    paginator = Paginator(Post.objects.all(), 12)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'Post/all_posts.html', {'Posts': Posts, 'posts': posts})


def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'Post/post_details.html', {'post': post})


def add_post(request):
    submitted = False
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post został poprawnie dodany!')
            return redirect('Posty:all_posts')
    else:
        form = PostForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'Post/add_post.html', {'form': form, 'submitted': submitted})


def update_post(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(request.POST or None, request .FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Zmiany zostały poprawnie zapisane.')
        return redirect('Posty:post_details', pk)
    return render(request, 'Post/update_post.html', {'post': post, 'form': form})


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    messages.success(request, 'Post został poprawnie usunięty.')
    return redirect('Posty:all_posts')