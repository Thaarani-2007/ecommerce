from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from G2k23.models import Item, Category as Cat
from .forms import NewItemform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# from G2k23.serializers import ProductSerializer
# from rest_framework.response import Response
# from rest_framework.views import APIView
from G2k23.models import Category,Item,UserProfile
# from .models import Product

# Create your views here.
def index(request):
    return render(request,'index.html' )

def about(request):
    return render(request,'about.html' )

# def newitem(request):
#     class LatestProductsList(APIView):
#         def get(self, request, format=None):
#             products = Product.objects.all()[0:4]
#             serializer = ProductSerializer(products, many=True)
#             return Response(serializer.data)

def login(request):
        try:
            if request.user.is_authenticated:
                return redirect("/browse/")
            if request.method=='POST':
                email = request.POST["email"].lower()
                passwd = request.POST["password"]
                print(email,passwd)
                user = authenticate(request, username=email,password=passwd)
                print(user)
                if user != None: 
                    auth_login(request, user)
                    return redirect("/browse/")

                elif not User.objects.filter(username=email).exists():
                        message="You are a new user please Sign-up to continue."
                        # messages.error(request, message)
                        return HttpResponseRedirect(f"/signin/")
            else:
                return render(request, "login.html")
            
        except :
             
            return redirect('')
        # return render(request,'login.html' )

# def signin(request):
#     return render(request,'signin.html' )

def browse(request):
    items = Item.objects.filter(is_sold=False)[0:10]
    categories = Cat.objects.all()
    return render(request,'browse1.html', {
        'categories':categories, 
        'items':items,
    } )


def signin(request):
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/login/')  # Create a success page in your templates
    # else:
    #     form = SignUpForm()

    # return render(request, 'signin.html', {'form': form})


    try:
        # if request.user.is_authenticated:
            # return redirect("/browse/")
        if request.method=='POST':
            if request.method=="POST":
                first_name = request.POST["first_name"].upper()
                last_name = request.POST["address"].upper()[:150]
                email = request.POST["email"].lower()
                passwd = request.POST["password"]
                repasswd= request.POST["repasswd"]
                if User.objects.filter(username=email).exists():
                    # message= "Oops! You are already an user! Please Sign-in to continue!"
                    # print(message)
                    # messages.error(request, message)
                    return redirect(f"/login/")
            
                elif not User.objects.filter(username=email).exists(): 
                    if passwd==repasswd:
                        user = User.objects.create_user(username=email,password=passwd)
                        user.first_name= first_name
                        user.last_name=last_name
                        user.email=email
                        user.save()
                        # messages.success(request, "Sign-up successful! Please login to continue.")     
                        # newstudent=studentdetails.objects.create(Student_name=sname, Admission_No=admno, password=passwd)
                        return redirect("/login/")  # Change the URL as needed
        else:
            return render(request, "signin.html")
    except:
        print('except box')


def newitem(request):
    try:
        if request.user.is_authenticated:
            if request.method=="POST":
                Category = request.POST["category"].upper()
                name = request.POST["name"].upper()[:150]
                description = request.POST["description"].lower()
                price = request.POST["price"]
                image = request.FILES["image"]
                newitem = Item.objects.create(Category_id=Category,name=name,description=description,price=price,image=image,created_by=request.user)
                newitem.save()
                return HttpResponseRedirect(f"/browse/")
            else: 
                categorylist=Cat.objects.all()
                data={"categorylist": categorylist}
                return render(request, 'newitem.html', data)
        else:
            return redirect(f"/login/")
    except Exception as e:
            print('except box', e , "\n\n\n") 


def dashboard(request):
    try:
        if request.user.is_authenticated: 
            item=Item.objects.filter(created_by_id=request.user.id)
            data={"items": item}
            return render(request, 'dashboard.html', data)
        else:
            return redirect(f"/login/")
    except Exception as e:
            print('except box', e , "\n\n\n") 



def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect("/")
    else:
        return redirect("/")
    


def edit(request , slug):
    try:
        if request.user.is_authenticated: 
            if request.method=='POST':
                item=Item.objects.get(slug=slug,created_by_id=request.user.id)
                item.Category_id = request.POST["category"].upper()
                item.name = request.POST["name"].upper()[:150]
                item.description = request.POST["description"].lower()
                item.price = request.POST["price"]
                item.image = request.FILES["image"] 
                item.save()
                return redirect(f"/dashboard/")
            else:
                categorylist=Cat.objects.all()
                item=Item.objects.get(slug=slug,created_by_id=request.user.id)
                data={"categorylist": categorylist,"item":item}
                return render(request, 'editpage.html', data)
        else:
            return redirect(f"/login/")
    except Exception as e:
            print('except box', e , "\n\n\n")

    
    
    
    
    
    
   