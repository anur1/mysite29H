from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def user_login (request,):
    #kullanıcı henüz giriş yapmadı ise login sayfasına gitmesine gerek yok, index e gidebilir.
    if request.user.is_authenticated: 
        return redirect( "index")
    
    if (request.method=="POST"):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect( "index"   )
        else:
            return render(request, "account/login.html", {"error":"username ya da password yanlış!"})
    else:   
        return render (request, "account/login.html", )



def user_register (request,):
    if request.method=="POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password != repassword: 
            return render (request, "account/register.html", {"error": "parlolalar eşleşmiyor", "username": username, "email": email})

        if User.objects.filter(username= username).exists():
                return render (request, "account/register.html", {"error": "aynı isimli bir kullanıcı daha var, başka bir isim seçiniz", "username": username, "email": email})
        
        if User.objects.filter(email=email).exists():
            return render (request, "account/register.html", {"error": "aynı email adresli birisi daha var, başka bir email adresi giriniz..", "username": username, "email": email})

        user = User.objects.create_user(username = username, email= email, password = password)
        user.save()
        return redirect("user_login")


    else:
        return render (request, "account/register.html", )



def user_logout (request,):  #logout yap, cookies sil, anasayfaya yönlendir. 
    logout(request)
    return redirect ("index" )

