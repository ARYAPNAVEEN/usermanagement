from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # Import User model (if using Django's auth system)
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile


def register(request):
    if request.method == "POST":
        username = request.POST.get('uname')  # Match form field
        contact = request.POST.get('contact')  # Ensure your model has this field
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        exist_user=User.objects.filter(username=username).exists()
        if not exist_user:
            user = User.objects.create_user(username=username, email=email, password=password)
            print(user)
            profile=Profile.objects.create(user=user)
            profile.phone=contact
            profile.save()
            
            return redirect('login')  

        else:
            messages.error(request,'already exist user')
            return redirect('register')
    return render(request, 'register.html') 

def login_user(request):
  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('profile')  
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')

@login_required
def profile(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    print(profile.image)

    return render(request,'profile.html',locals())




def admin_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user.is_superuser:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'invalid admin')

    return render(request,'admin_login.html')

@login_required
def dashboard(request):
    users=User.objects.filter(is_staff=False)
    return render(request,'dashboard.html',locals())



@login_required
def edit(request):
    print(request.user)
    user=request.user
    if request.method=="POST":
        user.email=request.POST.get('email')
        user.profile.phone=request.POST.get('phone')
        # user.password=request.POST.get('password')
        user.profile.image=request.FILES.get("profile_picture")
        print(user.profile.image)
        user.profile.save()
        user.save()
        return redirect('profile')
    return render(request,'edit.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')



@login_required
def get_user(request,id):
    user=User.objects.get(id=id)
    return redirect('update',user.id)



@login_required
def update(request,id):
    user=User.objects.get(id=id)
    profile=Profile.objects.get(user=user)
    if request.method=="POST":
        print(request.FILES)
        user.profile.phone=request.POST.get('phone')
        user.email=request.POST.get('email')
        if 'profile_picture' in request.FILES:
            user.profile.image = request.FILES['profile_picture']
        # user.profile.image=request.FILES.get("profile_picture")
            print(user.profile.image)
        user.save()
        user.profile.save()
        return redirect('dashboard')
    return render(request,'update.html',locals())


@login_required
def delete(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect('dashboard')


@login_required
def search_user(request):
    if request.method == "POST":
        text=request.POST.get("name")
        if text:
            users=User.objects.filter(username__icontains=text)
            # return redirect('dashboard')
            return render(request,'dashboard.html',{'users':users})
    return redirect('dashboard')



