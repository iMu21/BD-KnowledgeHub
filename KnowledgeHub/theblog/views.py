from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView, CreateView, UpdateView,DeleteView
from .models import Comment, Post
from examination.models import topicNames,sheduledExam
from .forms import PostForm,EditForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


def CommentView(request,pk):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    post = Post.objects.get(id=pk)
    try:
        comment = request.POST.get('comment')
        obj = Comment.objects.create(author=request.user,comment=comment)
        obj.save()
        post.comments.add(obj)
    except:
        messages.success(request, "Something wrong. Try again please.")
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

def LikeView(request,pk):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    post = Post.objects.get(id=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

def LikeHomeView(request, pk):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    post = Post.objects.get(id=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('home'))


class HomeView(ListView):
    model = Post
    ordering = ['-post_date']
    template_name = 'home.html'
    def get_context_data(self,*args,**kwargs):
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        upComingExams = sheduledExam.objects.all()[:15]
        context["upComingExams"] = upComingExams
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    def get_context_data(self,*args,**kwargs):
        stuff = Post.objects.get(id=self.kwargs['pk'])
        total_likes= stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    def get_context_data(self,*args,**kwargs):
        context = super(AddPostView,self).get_context_data(*args,**kwargs)
        return context

def AddPostView1(request):
    title = request.POST.get('title')
    catName = request.POST.get('category_name')
    catName=int(catName)
    topic = topicNames.objects.get(id=catName)
    body = request.POST.get('body')
    header_image = request.POST.get('header_image')
    Obj = Post.objects.create(author=request.user,title=title,category_name=topic,body=body,header_image=header_image)
    Obj.save()
    return redirect('article-detail',Obj.id)


class UpdatePostView(UpdateView):
    model = Post
    form_class=EditForm
    template_name = 'update_post.html'
    def get_context_data(self,*args,**kwargs):
        context = super(UpdatePostView,self).get_context_data(*args,**kwargs)
        return context

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    def get_context_data(self,*args,**kwargs):
        context = super(DeletePostView,self).get_context_data(*args,**kwargs)
        return context



def notAllowedView(request):
    return render(request, 'notAllowed.html')


