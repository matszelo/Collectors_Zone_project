from datetime import timezone
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TopicForm, CommentForm
from .models import Temat


def all_topics(request):
    Topics = Temat.objects.all().order_by('-id')
    paginator = Paginator(Temat.objects.all(), 6)
    page = request.GET.get('page')
    topics = paginator.get_page(page)
    return render(request, 'Forum/all_topics.html', {'Topics': Topics, 'topics': topics})


def topic_details(request, pk):
    if request.user.is_authenticated:
        form = CommentForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                comment = form.save(commit=False)
                comment.Autor = request.user
                comment.Temat = Temat.objects.get(pk=pk)
                comment.save()
                return redirect('Forum:topic_details', pk)

    topic = Temat.objects.get(pk=pk)
    form = CommentForm
    return render(request, 'Forum/topic_details.html', {'topic': topic, 'form': form})


def add_topic(request):
    submitted = False
    if request.method == 'POST':
        form = TopicForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.Autor = request.user
            new_topic.save()
            messages.success(request, 'Temat został poprawnie dodany!')
            return redirect('Forum:all_topics')
    else:
        form = TopicForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'Forum/add_topic.html', {'form': form, 'submitted': submitted})


def update_topic(request, pk):
    topic = Temat.objects.get(pk=pk)
    form = TopicForm(request.POST or None, request.FILES or None, instance=topic)
    if form.is_valid():
        form.save()
        messages.success(request, 'Zmiany zostały poprawnie zapisane.')
        return redirect('Forum:topic_details', pk)
    return render(request, 'Forum/update_topic.html', {'topic': topic, 'form': form})


def delete_topic(request, pk):
    topic = Temat.objects.get(pk=pk)
    topic.delete()
    messages.success(request, 'Twój temat został usunięty.')
    return redirect('Forum:all_topics')