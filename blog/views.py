from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from menan.models import Category, Slider, Contact
from blog.models import Blogs
from django.db.models import Q
import django_filters
from django.core.paginator import Paginator



class BlogFilter(django_filters.FilterSet):
    class Meta:
        model = Blogs
        fields = ['author', 'created_at']

def blog(request):
    slider = Slider.objects.all()
    sliders = slider[:1]
    query = request.GET.get('q')
    category = request.GET.get('category')
    
    blogs = Blogs.objects.all()
    contacts = Contact.objects.all()
    blg = Blogs.objects.all()
    blgs = blg[:2]

    if query:
        blogs = blogs.filter(
            Q(title__icontains=query) | 
            Q(desc__icontains=query)
        )
    
    if category:
        blogs = blogs.filter(category__name=category)
    
    paginator = Paginator(blogs, 4)  # Show 4 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    res = {
        'sliders':sliders,
        'blogs': blogs,
        'page_obj': page_obj, 
        'query': query, 
        'category': category, 
        'categories': categories,
        'contacts': contacts,
        'blgs':blgs,
    }
    
    return render(request, 'blog.html', res)

def blog_detail(request, pk):
    slider = Slider.objects.all()
    sliders = slider[:1]
    contacts = Contact.objects.all()
    blg = Blogs.objects.all()
    blgs = blg[:2]
    if request.method == 'GET':
        blog = get_object_or_404(Blogs, pk=pk)
        context = {
            'blog':blog,
            'sliders':sliders,
            'contacts':contacts,
            'blgs':blgs,
            }
        return render(request, 'blog-single.html', context)

    # if request.method == 'POST':
    #     blog = get_object_or_404(Blog, pk=pk)
    #     blog.body = request.POST.get('body')
    #     blog.save()
    #     return redirect('blog')
    
