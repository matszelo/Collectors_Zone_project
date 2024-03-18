from django.shortcuts import render, redirect
from .forms import DropForm
from .models import Drop


def all_drops(request):
    Drops = Drop.objects.all().order_by('-Data')
    return render(request, 'Drop/all_drops.html', {'Drops': Drops})


def drop_details(request, pk):
    drop = Drop.objects.get(pk=pk)
    return render(request, 'Drop/drop_details.html', {'drop': drop})


def add_drop(request):
    submitted = False
    if request.method == 'POST':
        form = DropForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Dropy:all_drops')
    else:
        form = DropForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'Drop/add_drop.html', {'form': form, 'submitted': submitted})


def update_drop(request, pk):
    drop = Drop.objects.get(pk=pk)
    form = DropForm(request.POST or None, request .FILES or None, instance=drop)
    if form.is_valid():
        form.save()
        return redirect('Dropy:drop_details', pk)
    return render(request, 'Drop/update_drop.html', {'drop': drop, 'form': form})


def delete_drop(request, pk):
    drop = Drop.objects.get(pk=pk)
    drop.delete()
    return redirect('Dropy:all_drops')
