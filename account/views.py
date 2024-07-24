from django.shortcuts import redirect, render

def user_login (request,):
    return render (request, "account/login.html", )

def user_register (request,):
    return render (request, "account/register.html", )

def user_logout (request,):  #cookies sil, anasayfaya yönlendir. 
    return redirect ("index" )

