from datetime import timezone
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import TopicForm
from .models import Temat


def all_topics(request):
    Topics = Temat.objects.all().order_by('-Dodano')
    return render(request, 'Forum/all_topics.html', {'Topics': Topics})


def topic_details(request, pk):
    topic = Temat.objects.get(pk=pk)
    return render(request, 'Forum/topic_details.html', {'topic': topic})


def add_topic(request):
    submitted = False
    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.Autor = request.user
            new_topic.save()
            return redirect('Forum:all_topics')
    else:
        form = TopicForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'Forum/add_topic.html', {'form': form, 'submitted': submitted})
