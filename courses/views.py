from datetime import date, datetime
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Course, Category

data = {
    "programlama":  "programlama kategorisine ait kurs listesi",
    "web-gelistirme": "web geliştirme kategorisine ait kurs listesi",
    "mobil": "mobil geliştirme kategorisine ait kurs listesi",
    "programlama1":  "programlama kategorisine ait kurs listesi",
    "web-gelistirme1": "web geliştirme kategorisine ait kurs listesi",
    "mobil1": "mobil geliştirme kategorisine ait kurs listesi",
}


db = {

    "courses": [
        {
            "title": "javascript kursu",
            "description": "java script kurs açıklaması",
            "imageUrl": "1.jpg",
            "slug": "javascript-kursu",
            "date": datetime.now,
            "isActive": True

        },
        {
            "title": "python kursu",
            "description": "python kurs açıklaması",
            "imageUrl": "2.jpg",
            "slug": "python-kursu",
            "date": date(2024, 2, 2),
            "isActive": False, 
            "isUpdated": True,

        },
        {
            "title": "web geliştirme kursu",
            "description": "web geliştirme kurs açıklaması",
            "imageUrl": "3.jpg",
            "slug": "web-gelistirme-kursu",
            "date": date(2024, 3, 3),
            "isActive": False, 
            "isUpdated": False,

        },
        {
            "title": "SQL kursu",
            "description": "SQL kurs açıklaması",
            "imageUrl": "4.jpg",
            "slug": "SQL-kursu",
            "date": date(2024, 4, 4),
            "isActive": True, 
            "isUpdated": True,

        },
        {
            "title": "django kursu",
            "description": "django kurs açıklaması",
            "imageUrl": "5.jpg",
            "slug": "django-kursu",
            "date": date(2024, 5, 5),
            "isActive": True, 
            "isUpdated": True,

        },],

    "categories": [
        {"id": 1, "name": "programlama", "slug": "programlama"},
        {"id": 2, "name": "web geliştirme", "slug": "web-gelistirme"},
        {"id": 3, "name": "mobil uygulamalar", "slug": "mobil-uygulamalar"},
        {"id": 4, "name": "yapay zeka", "slug": "yapay-zeka"},
        {"id": 5, "name": "modelleme", "slug": "modelleme"},
        {"id": 5, "name": "diy", "slug": "diy"}],

}


def index(request):

    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Category.objects.all()

#    for kurs in db["courses"]:
#         if kurs["isActive"] == True: 
#             kurslar.append(kurs)



    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses': kurslar
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
    kurslar  = Course.objects.filter(category__slug = slug, isActive=True)
    kategoriler = Category.objects.all()

    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses': kurslar,
        'seciliKategori': slug
    })