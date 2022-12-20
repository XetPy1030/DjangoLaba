from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from . import models, forms


def index(request):
    films = models.Film.objects.all()
    
    return render(request, 'films/index.html', context={'films': films})

class AddView(View):
    def get(self, request):
        return render(request, 'films/add.html', context={'form': forms.FilmForm})

    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/')
        
        form = forms.FilmForm(request.POST)

        if not form.is_valid():
            return self.get(request)

        model = models.Film(
            name=form.cleaned_data['name'],
            category=models.Category.objects.get(pk=form.cleaned_data['category']),
            release_date=form.cleaned_data['release_date'],
            actors=form.cleaned_data['actors'],
            show_date=form.cleaned_data['show_date']
        )
        model.save()

        return HttpResponseRedirect('/')


class DeleteView(View):
    def get(self, request, pk):
        model = models.Film.objects.get(pk=pk)

        return render(request, 'films/delete.html', context={'film': model})

    def post(self, request, pk):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/')

        model = models.Film.objects.get(pk=pk)
        model.delete()
        
        return HttpResponseRedirect('/')


class EditView(View):
    def get(self, request, pk):
        model = models.Film.objects.get(pk=pk)
        form = forms.FilmForm(data={
            'name': model.name,
            'category': model.category.pk,
            'release_date': model.release_date, # я если что ничего не слышу, отключил звук,
            'actors': model.actors,
            'show_date': model.show_date
        })

        return render(request, 'films/edit.html', context={'form': form})

    def post(self, request, pk):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/')

        form = forms.FilmForm(request.POST)
        model = models.Film.objects.get(pk=pk)

        if not form.is_valid():
            return self.get(request)
        
        model_save = models.Film(
            pk=model.pk,
            name=form.cleaned_data['name'],
            category=models.Category.objects.get(pk=form.cleaned_data['category']),
            release_date=form.cleaned_data['release_date'],
            actors=form.cleaned_data['actors'],
            show_date=form.cleaned_data['show_date']
        )

        model.delete()
        model_save.save()

        return HttpResponseRedirect('/')
