from cmath import log
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Profile
# Create your views here.


@login_required(login_url='signin')
def index(request):

  return render(request, 'blog/index.html')


@login_required(login_url='signin')
def settings(request):
  user_profile = Profile.objects.get()
  
  if request.method == 'POST':
    if request.FILES.get('image')== None:
      image = user_profile.profileimg
      bio = request.POST['bio']
      location = request.POST['location']

      user_profile.profileimg = image
      user_profile.bio = bio
      user_profile.location = location
      user_profile.save()
    if request.FILES.get('image') != None:
      image = request.FILES.get('image')
      bio = request.POST['bio']
      location = request.POST['location']

      user_profile.profileimg = image
      user_profile.bio = bio
      user_profile.location = location
      user_profile.save()

  return render(request, 'blog/setting.html',{'user_profile': user_profile})

def signup(request):

  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(email=email).exists():
        messages.info(request,'Email Taken')
        return redirect('signup')
      elif User.objects.filter(email=email).exists():
        messages.info(request,'Username Taken')
        return redirect('signup')
      else:
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()

        # log user in and redirect to settings page 
        user_login = auth.authenticate(username=username,  password=password)
        auth.login(request, user_login)

        #create a profile objevct for ew user
        user_model = User.objects.get(username =username)
        new_profile = Profile.objects.create(user= user_model, id_user = user_model.id)
        new_profile.save()
        return redirect('settings')

    else:
      messages.info(request, 'Password not Matching')
      return redirect('signup')
    
  else:
    return render(request, 'blog/signup.html')


def signin(request):

  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username =username, password= password)
    if user is not None:
      auth.login(request,user)
      return redirect('index')
    else:
      messages.info(request,'Credential Invalid')
      return redirect('signin')
  else:
    return render(request, 'blog/signin.html')

@login_required(login_url='signin')
def logout(request):
  auth.logout(request)
  return redirect('signin')