from django.shortcuts import *
from django.http import *
from .models import modelsignup,modelmovie,modelrating
from .forms import formsignup,formlogin,formmovie,formselectmovie,formratinghold,formmovieholding
from datetime import date
from django.db.models import Avg, Max, Min, Sum
import math
# Create your views here.
def valid(request):
    return render(request,"valid.html")
def signupform(request):
    formsignup1=formsignup()
    return render(request,"signup.html",{'formsignup1':formsignup1})

def signup(request):
    if request.method == "POST":
        form = formsignup(request.POST,request.FILES)
        if form.is_valid():                                #check if form is valid?
            pas=form.cleaned_data['password']
            cpas=form.cleaned_data['confpassword']
            if pas!=cpas:
                return render(request,"alerthtml.html")
            else:
                temp_user_name = form.cleaned_data['user_name']
                try:
                    temp_user = modelsignup.objects.get(user_name=temp_user_name)
                    if temp_user.user_name==temp_user_name:
                        return render(request, "alert_user_dup.html")
                except:
                    sign=modelsignup()
                    sign.name=form.cleaned_data['name']
                    sign.email=form.cleaned_data['email']
                    sign.gender=form.cleaned_data['gender']
                    sign.user_name=form.cleaned_data['user_name']
                    sign.password=form.cleaned_data['password']
                    sign.save()
                    return redirect('/appmovierate/home/')
    else:
        formsignup1 = formsignup()
        return render(request, "signup.html", {'formsignup1': formsignup1})

def loginform(request):
    formlogin1 = formlogin()
    return render(request, "login.html", {'formlogin1': formlogin1})

def logcheck(request):
    if request.method == "POST":
        formlog = formlogin(request.POST, request.FILES)
        if formlog.is_valid():
            temp_login_name = formlog.cleaned_data['username']
            temp_login_pass = formlog.cleaned_data['password']
            try:
                temp_username = modelsignup.objects.get(user_name=temp_login_name)
                request.session['username1'] = formlog.cleaned_data['username']
                if temp_username.user_name=='admin' and temp_username.password=='admin':
                    return redirect('/appmovierate/admin/')
                elif temp_username.user_name==temp_login_name and temp_username.password==temp_login_pass:
                    return redirect('/appmovierate/home/')
                else:
                    return HttpResponse("NOT CORRECT")
            except:
                return HttpResponse("NOT CORRECT")

def home(request):
    return render(request,"index.html")

def profile(request):
    profname = request.session['username1']
    modelsignup1=modelsignup.objects.get(user_name=profname)
    return render(request,"profile.html",{'profname':profname,'modelsignup1':modelsignup1})

def signout(request):
    user = request.session['username1']
    print(user)
    if request.session['username1']:
        del request.session['username1']
    else:
        print("ELSE COND")
    # del request.session['username']
    # form = myform1()
    # return render(request, "login.html", {'form': form})
    return redirect('/appmovierate/login/')

def reviewed(request):
    profname = request.session['username1']
    modelrating1=modelrating.objects.filter(user_name=profname)
    return render(request,"reviews.html",{'profname':profname,'modelrating1':modelrating1})

def rated(request):
    profname = request.session['username1']
    formmovieholding1=formmovieholding()
    temp_rating=modelrating.objects.filter(movie_name="Predestination")
    # for i in temp_rating:
    #     print(i.ratings)
    return render(request,"movie_rate.html",{'profname':profname,'formmovieholding1':formmovieholding1})

def rated1(request):
    if request.method == "POST":
        form = formmovieholding(request.POST, request.FILES)
        if form.is_valid():
            temp_mname = form.cleaned_data['movie_name_get']
            request.session['movie_name1'] = temp_mname
            try:
                temp_name = modelmovie.objects.get(movie_name=temp_mname)
                temp_name2=modelrating.objects.filter(movie_name=temp_mname)
                # temp=modelrating.objects.raw("select * from appmovierate_modelrating where movie_name='Avatar' ")
                temp=modelrating.objects.filter(movie_name=temp_mname).aggregate(Avg('ratings'))
                y=temp.get("ratings__avg")
                x=round(y,1)
                print (x)
                if temp_name.movie_name==temp_mname:
                    formmovieholding1=formmovieholding()
                    return render(request, "movie_rate2.html", {'temp_name': temp_name,'formmovieholding1': formmovieholding1,'temp_name2':temp_name2,'x':x})
            except:
                return HttpResponse("2.NO MOVIE FOUND")
def rate(request):
    formselectmovie1=formselectmovie()
    return render(request, "ratemovie.html",{'formselectmovie1':formselectmovie1})

def rate1(request):
    if request.method == "POST":
        form = formselectmovie(request.POST, request.FILES)
        if form.is_valid():
            temp_mname=form.cleaned_data['movie_name_get']
            request.session['movie_name1']=temp_mname
            try:
                temp_name = modelmovie.objects.get(movie_name=temp_mname)
                if temp_name.movie_name==temp_mname:
                    ratinghold1=formratinghold()
                    formselectmovie1=formselectmovie()
                    return render(request, "ratemovie2.html", {'temp_name': temp_name,'ratinghold1': ratinghold1,'formselectmovie1':formselectmovie1})
            except:
                return HttpResponse("2.NO MOVIE FOUND")

def rate2(request):
    if request.method == "POST":
        form = formratinghold(request.POST, request.FILES)
        if form.is_valid():
            modelrating1=modelrating()
            user = request.session['username1']
            movie = request.session['movie_name1']
            try:
                temp_search = modelrating.objects.get(user_name=user,movie_name=movie)
                if temp_search.movie_name == movie:
                    return render(request, "alert_user_dup.html")
            except:
                modelrating1.user_name = request.session['username1']
                modelrating1.movie_name = request.session['movie_name1']
                modelrating1.ratings = form.cleaned_data['ratings']
                modelrating1.review = form.cleaned_data['review']
                # currentDT = datetime.datetime.now()
                today = date.today()
                currentDT=today.strftime("%B %d, %Y")
                modelrating1.date = currentDT
                modelrating1.save()
                return redirect('/appmovierate/rate/')

def release(request):
    return render(request,"upcomingrelease.html")

# --------------------------------------ADMIN-----------------------------------------------------

def admin(request):
    return render(request, "admin_main.html")

def addmovie(request):
    formmovie1=formmovie()
    return render(request,"admin_add_movie.html",{'formmovie1':formmovie1})

def adding(request):
    if request.method == "POST":
        form = formmovie(request.POST, request.FILES)
        if form.is_valid():
            model1=modelmovie()
            model1.movie_name=form.cleaned_data['movie_name']
            model1.movie_director=form.cleaned_data['movie_director']
            model1.movie_studio=form.cleaned_data['movie_studio']
            model1.movie_year=form.cleaned_data['movie_year']
            model1.movie_image=form.cleaned_data['movie_image']
            model1.save()
        formmovie1 = formmovie()
        return render(request, "admin_add_movie.html", {'formmovie1': formmovie1})
    else:
        formmovie1 = formmovie()
        return render(request,"admin_add_movie.html",{'formmovie1':formmovie1})

def userrating(request):
    return render(request, "admin_user_ratings.html")

def deluser(request):
    return render(request, "admin_user_delete.html")