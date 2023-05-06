from django.shortcuts import render, redirect
from .gallery_form import GalleryForm, Gallery
from .category_form import CategoryForm,Category

def gallery(request):
    photos = Gallery.objects.all()
    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'gallery.html', context)


def add_category(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        context = {'form': form, 'categories': categories}
        form = CategoryForm()
    return render(request, 'add_category.html', context)

def image_upload(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        
        title=None
        categoryname=None
        description=None
        imageurl=None
        images = request.FILES.getlist('images')

        if data['title'] != 'none':
            title=data['title']
        
        if data['category'] != 'none':
            categoryname = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            categoryname=data['category_new']
            newcategory = Category.objects.create(
                name=categoryname
            )
        
        if data['description'] != 'none':
            description=data['description']

        for image in images:
            photo = Gallery.objects.create(
                title=title,
                category=categoryname,
                description=data['description'],
                image=image,
            )
        
        form = GalleryForm()
        context = {'form': form, 'categories': categories}
        form = GalleryForm(request.POST, request.FILES)
        return render(request, 'add_image.html', context)
        if form.is_valid():
            form.save()
            return redirect('image_upload')
    else:
        form = GalleryForm()
        context = {'form': form, 'categories': categories}    
    return render(request, 'add_image.html', context)