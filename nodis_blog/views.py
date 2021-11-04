from django.views import generic
from .models import Post
from django.http import HttpResponse


# Create your views here. We will use class based views

# Render all posts via generic List_View
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

# Render specific post via Detail_View 
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

