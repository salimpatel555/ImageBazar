from django.contrib import messages
from django.shortcuts import render,redirect
from myapp.models import Image,Category
from django.contrib.auth.models import User, auth
from .forms import ImageForm
# Create your views here.
def index(request):
    category = Category.objects.all()
    images = Image.objects.all()
    context = {'images':images,'category':category}
    return render(request,'index.html',context)


def category(request,id):
    category = Category.objects.all()

    category = Category.objects.get(id=id)
    print(category)

    images = Image.objects.filter(category__title=category)
    print(category)
    context = {'images':images,'category':category}
    return render(request,'index.html',context)
   

def signup(request):
    if request.method =='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.success(request,'Username is Taken')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.success(request,'Email is Taken')
                return redirect('/signup')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                return redirect('/login')    
        else:
            messages.success(request,'Password is Not Match')
            return redirect('/signup')             
    return render(request,'signup.html')    


def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.success(request,'Inbvalid Cridantial')
            return redirect('/login')

    return render(request,'login.html')   

def logout(request):
    auth.logout(request)
    return redirect('/')


def post_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,'Image Has Been Submited')
            return redirect('/')
    else:
        form = ImageForm()
    context = {'form':form}        
    return render(request,'post_image.html',context)

def delete(request,id):
    if request.user.is_authenticated:
       image = Image.objects.get(id=id)
       image.delete()
       messages.info(request,'Image Has Been Deleted')
       return redirect('/')
    else:
        messages.info(request,'User is Not Login')
        return redirect('/login')        

def profile(request):
    return render(request,'profile.html')   

    #My ImageBazar App 