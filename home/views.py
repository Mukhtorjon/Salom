from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse 
from django.views.generic import ListView,DetailView, UpdateView,DeleteView,CreateView
from .form import ContactForm,UpdateForm,CommentForm
from .models import Post,Category,Friendes,Comment
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
# Create your views here.

# def myblog2(requests):
#     return render(request=requests,template_name="blog.html")

class Newsapp(ListView):
    model=Post
    context_object_name="Post"
    template_name='index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Category'] = Category.objects.all()
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
            return HttpResponse('send message')
        else:
            return HttpResponse(u'ОШИБОЧКА')
        
def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    post.like.add(request.user)
    return HttpResponseRedirect(reverse('index', args=[str(pk)]))

class  DetailPost(DetailView):
    model=Post
    template_name='blog-single.html'
    def get_object(self, queryset=None):
        item = super().get_object(queryset)
        item.incrementViewCount()
        return item
    def add_comment(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = CommentForm()
        return render(request, {'form': form})
class ModelUpdateView(UpdateView):
    model = Post
    form_class=UpdateForm
    template_name = "update.html"
    def get_post(self, pk):
        return get_object_or_404(Post, pk=pk)
   
class DeletePost(DeleteView):
    model=Post
    template_name='deletepost.html'
    success_url=reverse_lazy('index')
class CreatePost(CreateView):
    model=Post
    template_name='createpost.html'
    fields=('category','name','title','body','image','status')
    
