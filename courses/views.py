from datetime import date, datetime
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Course, Category
from django.core.paginator import Paginator


def index(request):
    kurslar = Course.objects.filter(isActive=1, isHome=1)
    kategoriler = Category.objects.all()
#    for kurs in db["courses"]:
#         if kurs["isActive"] == True: 
#             kurslar.append(kurs)
    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses': kurslar
    })


def add_course(request, ):
    if request.method == "POST":
        #POST'tan gelen bilgileri al
        title = request.POST["title"]
        description = request.POST["description"]
        imageUrl = request.POST["imageUrl"]
        slug = request.POST["slug"]
        isActive = request.POST.get ("isActive", False)
        isHome = request.POST.get("isHome", False)
        if isActive =="on": 
            isActive = True
        if isHome == "on":
            isHome = True
        #POST'tan gelen bilgileri db'ye kaydet
        kurs = Course (title=title, description=description, imageUrl = imageUrl, slug=slug, isActive= isActive, isHome=isHome)
        kurs.save()
        print(title, description, imageUrl, isActive, isHome)
        #POST işlemi sonrası kullanıcıyı anasayfaya geri gönder
        return redirect("/kurslar") 
    return render(request, "courses/add-course.html")



def search(request):
    if "q" in request.GET and request.GET["q"] !="":
        q = request.GET["q"]
        kurslar  = Course.objects.filter(isActive = True, title__contains=q).order_by("date")#category__slug = slug,
        kategoriler = Category.objects.all()
    else:
        return redirect("/kurslar")  

    
    return render(request, 'courses/search.html', {
        'categories': kategoriler,
        'courses': kurslar,
    })


def details(request, kurs_id):
    # try: 
    #     course=Course.objects.get(pk=kurs_id)
    # except:
    #     raise Http404()
    
    course = get_object_or_404(Course, pk=kurs_id)

    context = {
        'course': course
    }
    return render(request, 'courses/details.html', context)


def getCoursesByCategory(request, slug):
    kurslar  = Course.objects.filter( categories__slug= slug, isActive = True).order_by("date")#category__slug = slug,
    kategoriler = Category.objects.all()


    
    paginator = Paginator(kurslar, 3) #filtrelenmiş kursları her sayfada 5'er adet göster
    page = request.GET.get('page', 1) #query'den gelen page number'ı kullan
    page_obj = paginator.page(page) #page e düşen kursları pageob'e at
    
    print(page_obj.paginator.count) #toplam ürün sayısı
    print(page_obj.paginator.num_pages) # toplam sayfa sayısı


    return render(request, 'courses/list.html', {
        'categories': kategoriler,
        'courses': kurslar,
        'page_obj': page_obj,
        'seciliKategori': slug
    })