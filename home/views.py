from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse 
from django.views.generic import ListView,DetailView, UpdateView,DeleteView,CreateView
from  django.views.generic.edit import FormMixin
from .form import ContactForm,UpdateForm,CommentForm
from .models import Post,Category,Friendes,Comment
from django.urls import reverse_lazy,reverse
from Members.models import Profail
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
# def myblog2(requests):
#     return render(request=requests,template_name="blog.html")

class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff

class Newsapp(ListView):
    model=Post
    context_object_name="Post"
    template_name='index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Work'] = Post.objects.filter(category__name="Work").order_by("-publik_time")
        context['Blog'] = Post.objects.filter(category__name="Blog").order_by("-publik_time")
        context['Friend'] = Friendes.objects.all()
        context['Comment'] = Comment.objects.all()
        context['form'] = ContactForm()
        return context
    
    def post(self, request, *args, **kwargs):
        post = request.POST.copy()
        request.POST = post 
        context = ContactForm(request.POST)
        if context.is_valid():
            context.save()
            return render(request, template_name= 'contact.html',)
        else:
            return HttpResponse('Error ')
         
class  DetailPost(DetailView):
    model = Post
    template_name='blog-single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
       

        form = CommentForm()
        post = get_object_or_404(Post, pk=pk)
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            comment = Comment.objects.create(
                name=name, email=email, content=content, post=post
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)
class ModelUpdateView(StaffRequiredMixin,UpdateView):
    model = Post
    form_class=UpdateForm
    template_name = "update.html"
    def get_post(self, pk):
        return get_object_or_404(Post, pk=pk)
   
class DeletePost(StaffRequiredMixin,DeleteView):
    model=Post
    template_name='deletepost.html'
    success_url=reverse_lazy('index')
class CreatePost(StaffRequiredMixin,SuccessMessageMixin,CreateView):
    model=Post
    template_name='createpost.html'
    fields=('category','name','title','body','image','status')
    success_message='Your post created'
# 5228600523186114