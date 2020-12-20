#borre todo lo que habia aqui y lo deje en web_views
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from posts.models import Post, PostView, Like, Comment, Profile
from .forms import PostForm, CommentForm

from django.views.generic.edit import FormView 
from django.http import HttpResponseRedirect


#cabildos
import json
from cabildos.forms import CrearCabildo
from cabildos.models import Cabildo, get_conceptos_Valores, get_conceptos_Derechos, get_conceptos_Deberes, get_conceptos_Instituciones 



class PostListView(ListView):
    model = Post
    form_class = CrearCabildo
    #initial = {'key': 'value'}
    #template_name = "post_list.html"

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        context['cabildo_form'] = CrearCabildo()

        conceptos_Valores = get_conceptos_Valores()
        conceptos_Derechos = get_conceptos_Derechos()
        conceptos_Deberes = get_conceptos_Deberes()
        conceptos_Instituciones = get_conceptos_Instituciones()

        json_conceptos_Valores = json.dumps(conceptos_Valores)
        json_conceptos_Derechos =json.dumps(conceptos_Derechos)
        json_conceptos_Deberes = json.dumps(conceptos_Deberes)
        json_conceptos_Instituciones = json.dumps(conceptos_Instituciones)

        context['json_conceptos_Valores'] = json_conceptos_Valores
        context['json_conceptos_Derechos'] = json_conceptos_Derechos
        context['json_conceptos_Deberes'] = json_conceptos_Deberes
        context['json_conceptos_Instituciones'] = json_conceptos_Instituciones

        return context

    #def get(self, request, *args, **kwargs):
    #    form = self.form_class(initial=self.initial)
    #    return render(request, self.template_name, {'form': form})

    # Handle POST GTTP requests
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # <process form cleaned data>
            return HttpResponseRedirect('/')

        #return render(request, self.template_name, {'form': form})
    #def post(self, request, *args, **kwargs):
    #    form = self.get_form_class()
    #    if form.is_valid(self):
    #        return self.form_valid(form)
    #    else:
    #        return self.form_invalid(form)

    #def form_valid(self, form):
    #    if form.is_valid():
    #        form.save()


class PostDetailView(DetailView):
    model = Post

    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            comment.save()
            return redirect('detail', slug=post.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm()
        })
        return context
    

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=object)

        return object

class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context

def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail', slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)
