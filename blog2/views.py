from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Blog

# Create your views here.

def home2(request):
    objects = Blog.objects.all()
    return render(request, 'home2.html', {'objects':objects})

def detail2(request,id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail2.html', {'blog':blog})

# def new(request):
#     form = BlogForm()
#     return render(request, 'new.html', {'form':form})

# def create(request):
#     form = BlogForm(request.POST, request.FILES)
#     if form.is_valid():
#         n_blog = form.save(commit=False)
#         n_blog.date = timezone.now()
#         n_blog.save()
#         return redirect('detail', n_blog.id)
#     return redirect('home')

# def edit(request, id):
#     edit_blog = Blog.objects.get(id=id)
#     return render(request, 'edit.html', {'blog':edit_blog})

# def update(request, id):
#     u_blog = Blog.objects.get(id=id)
#     u_blog.subject = request.POST['subject']
#     u_blog.author = request.POST['author']
#     u_blog.content = request.POST['content']
#     u_blog.date = timezone.now()
#     u_blog.save()
#     return redirect('detail', u_blog.id)

# def delete(request,id):
#     d_blog = Blog.objects.get(id=id)
#     d_blog.delete()
#     return redirect('home')
# Create your views here.
