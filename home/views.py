from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from jsonFunctions import read_json,choose_language,Merge

#Imports for posting on the blog and rendering material

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm,  CategoryForm ,CommentForm
from django.urls import reverse_lazy, reverse

# Create your views here.

# parameter that reads the language chosen from the language tap 
param = read_json('js-dj-transfer.JSON').get('param')

class BlogView(ListView):
    model = Post
    template_name= 'blog.html'
    #ordering = ['-id'] #Ordering in the negative id starting from the last one
    ordering = ['-post_date']

    # his function helps to generate the parameters that will be used in the html
    # Just like the dictionary paramters that we have stored in the JSON file
    # In other words it generates the context that we usually passed to our render function <render(request)
    def get_context_data (self, **kwargs):
        postData = super(BlogView, self).get_context_data(**kwargs)
        parameters = choose_language(param)
        context = Merge(parameters,postData)
        return context


class AddArticleView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add-article.html'
    #fields = '__all__'
    #fields = ('title', 'body','author')

    def get_context_data (self, **kwargs):
        postData = super(AddArticleView, self).get_context_data(**kwargs)
        parameters = choose_language(param)
        context = Merge(parameters,postData)
        return context

def AdminPanView(request):
    context = choose_language(param)
    return render(request,'adminPan.html',context)

# class that renders the home page
class HomeView(BlogView):
    model = Post
    template_name= 'home.html'

class UpdateArticleView(UpdateView):
    model = Post
    template_name = 'update-article.html'
    form_class = PostForm

    def get_context_data (self, **kwargs):
        postData = super(UpdateArticleView, self).get_context_data(**kwargs)
        parameters = choose_language(param)
        context = Merge(parameters,postData)
        return context

class DeleteArticleView(DeleteView):
    model = Post
    template_name = 'delete-article.html'
    success_url = reverse_lazy('adminPan')

    def get_context_data (self, **kwargs):
        postData = super(DeleteArticleView, self).get_context_data(**kwargs)
        parameters = choose_language(param)
        context = Merge(parameters,postData)
        return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' ')) 
    parameters = choose_language(param)
    parameters['category_posts'] = category_posts
    print(cats)
    context = Merge(parameters,{'cats': cats.title().replace('-',' ')})
    return render(request, 'category.html', context)

class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add-category.html'

    def get_context_data (self, **kwargs):
        postData = super(AddCategoryView, self).get_context_data(**kwargs)
        parameters = choose_language(param)
        context = Merge(parameters,postData)
        return context

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add-comment.html'    
    success_url = reverse_lazy('blog') #We need to return to the 'article-detail' page 

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_context_data (self, **kwargs):
        postData = super(AddCommentView, self).get_context_data(**kwargs)
        parameters = choose_language(param)
        context = Merge(parameters,postData)
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article-detail.html'

    def get_context_data (self, **kwargs):
        postData = super(ArticleDetailView, self).get_context_data(**kwargs)
        parameters = choose_language(param)
        context = Merge(parameters,postData)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = True
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = False
            
        context['total_likes'] = total_likes
        context['liked'] = liked

        return context

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

# def CommentView(request, comts):
#     comments_posts = Comment
#     parameters = choose_language(param)
#     parameters['comments_posts'] = comments_posts
#     #print(comments_posts)
#     context = Merge(parameters,{'comts': comts.name().replace('-',' ')})
#     return render(request, 'comments.html', context)





