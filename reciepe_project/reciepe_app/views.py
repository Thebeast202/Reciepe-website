from django.shortcuts import render,redirect
from reciepe_app.models import*
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):

    query_set = Reciepes.objects.all()
    if request.GET.get('search'):
        query_set= query_set.filter(reciepe_name__icontains=request.GET.get('search'))
    context = {"reciepes":query_set}

    return render(request,'home.html',context)





@login_required(login_url="/login-page")
def index(request):
    

    query_set = Reciepes.objects.all()
    
    if request.GET.get('search'):
        query_set= query_set.filter(reciepe_name__icontains=request.GET.get('search'))
        # print(request.GET.get('search'))

    context = {"reciepes":query_set,}
    # print(context)
 
    


    return render(request,"index.html",context)


@login_required(login_url="/login-page")
def add_reciepe(request):

    if request.method == "POST":
        data_set = request.POST
        files_set = request.FILES

        reciepe_name = data_set.get("reciepe_name")
        reciepe_description = data_set.get("reciepe_desc")
        reciepe_image = files_set.get("reciepe_img")

        reciepes = Reciepes(reciepe_name=reciepe_name,reciepe_desc=reciepe_description,reciepe_img=reciepe_image)
        reciepes.save()

        return redirect("/home")

    return render(request,'add_reciepe.html')


def delete_reciepe(request,id):

    query_set = Reciepes.objects.get(id=id)
    query_set.delete()

    return redirect("/home")

@login_required(login_url="/login-page")
def update_reciepe(request,id):


    queryset = Reciepes.objects.get(id=id)

    if request.method=="POST":

        data = request.POST
        files = request.FILES

        reciepe_name = data.get("reciepe_name")
        reciepe_description = data.get("reciepe_desc")
        reciepe_image = files.get("reciepe_img")

        queryset.reciepe_name = reciepe_name
        queryset.reciepe_desc = reciepe_description

        if reciepe_image:
            queryset.reciepe_img = reciepe_image

        queryset.save()

        return redirect("/home")

    context = {'reciepe':queryset}  


    return render(request,"update_reciepe.html",context)




def register_page(request):

    if request.method =="POST":
        data = request.POST
        
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')

        user =  User.objects.filter(username=username)

        if user.exists():

            messages.warning(request, "Username is already taken")
            return redirect('/register-page')

        user= User(first_name=first_name,last_name=last_name,username=username)
        user.set_password(password)

        
        user.save()
        messages.success(request, "Account created successfully.")
        return redirect('/register-page')
    

    return render(request,"register_page.html")


def login_page(request):

    if request.method =="POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login-page')
        
        user = authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login-page')
        else:
            login(request,user)
            return redirect("/home")
    
    return render(request,"login_page.html")

def logout_page(request):
    logout(request)
    return redirect('/login-page')


def reciepe_view(request,id):
    data = Reciepes.objects.get(id=id)
    context = {'reciepes':data}
    

    return render(request,'reciepe_view.html',context)