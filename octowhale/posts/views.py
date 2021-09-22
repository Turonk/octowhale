from django.urls import reverse_lazy
from .models import Post, Group
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class PostsList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'index.html'
    queryset = Post.objects.all()[:11]


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/new_post.html'
    success_url = reverse_lazy("posts:index")
    fields = ['post_title', 'text', 'group']

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/edit_post.html'
    fields = ['post_title', 'text', 'group']
    success_url = reverse_lazy("posts:index")


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('posts:index')
