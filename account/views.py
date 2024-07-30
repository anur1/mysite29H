from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def user_login (request,):
    #kullanıcı super admin değilse, url'deki next çıkar. Yani kullanıcı yetkisizdir. 
    if request.user.is_authenticated and "next" in request.GET: 
        return render(request, "account/login.html", {"error":"username ya da password yetkisiz alana giremez!"})
    
    if request.method =="POST":
        #Login formunu django builtin form'dan al.
        form = AuthenticationForm(request, data =request.POST)
        if form.is_valid():            #not: request.cleaned_data çalışmıyor. form.cleaned_data çalıştı. 
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            #Authentication Form kullanmadan önce bunları kullanıyorduk.
            # username = request.POST["username"]
            # password = request.POST["password"]
            # user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "giriş başarılı")
                #return redirect( "index"   )  next yoksa gitsin, varsa ilgili sayfaya gitsin
                nextUrl = request.GET.get("next", None)
                if nextUrl is None:
                    return redirect("index")
                else: 
                    return redirect(nextUrl)
                
            else: #kullanıcı None ise login formu login.html'ye gider.
                return render(request, "account/login.html", {"form": form} )
            
        else:# form valid değilse, login formu login.html'ye gider
            #messages.add_message(request, messages.ERROR, "giriş başarısız, username ya da password yanlış") bu hata mesajına artık gerek yok. form dan geliyor zaten
            return render(request, "account/login.html", {"form": form} )
        
    else:   #GET ile gelinmişse boş Login formu login.html'ye gönderilir
        form = AuthenticationForm()
        return render (request, "account/login.html", {"form": form})



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
    messages.add_message(request, messages.SUCCESS,"Çıkış başarılı")
    logout(request)
    return redirect ("index" )

