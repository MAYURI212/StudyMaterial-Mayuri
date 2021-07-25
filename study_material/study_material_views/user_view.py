from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import Group,User,auth
from study_material.study_material_forms.login import Login_user
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


def name(request):
    u=User.objects.create_user(username='MayuriRoiathod',email='mayurathod619@gmail.com',password='rathod@123',first_name='Mayuri',last_name='Rathod',is_superuser=True,is_staff=True,is_active=True)
    u=User.objects.create_user(username='ArvindRuiathod',email='rmayu702@gmail.com',password='rathod@123',first_name='Arvind',last_name='Rathod',is_superuser=True,is_staff=True,is_active=True)
    u.save()

    messages.success(request,'User Create Sucessfully')
    return HttpResponse("<h1> User Created Sucessfully </h1>")


def login_view(request):
    if request.method=='POST':
        file_obj=Login_user(request.POST)
        if file_obj.is_valid():
            try:
                print("excuted")
                user_name=file_obj.cleaned_data['user_name']
                password=file_obj.cleaned_data['password']
                ui=auth.authenticate(username=user_name,password=password)
                if ui is not None:
                    auth.login(request,ui)
                    request.session['username']=user_name
                    return redirect('dashboard')
                else:
                    messages.error(request,"Invalid Credetials")
                    return redirect('login')
            
            except:
                messages.error(request,"Check your Internet connection... Try again")
                return redirect('login')
        else:
            messages.error(request,"Form is not valid")
    else:
        file_obj=Login_user()
        
        context={'file_obj':file_obj}
    return render(request,"webpages/login.html",context)
    




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def dashboard_dash(request):
    if request.session.has_key('username'):
        lname=request.user.first_name 
        fname=request.user.last_name
        context = {
            
            'lname':lname,
        
            'fname':fname,
            
            
            }
        return render(request,"webpages/dashboard.html",context) 
    else:
        return redirect('login')

def pageExpir(request):
    return render(request,"pageviews/loginPasswd/pageexpire.html")

def logout(request):
    try:
        del request.session['username']
        auth.logout(request)
        return redirect('login')
    except KeyError:
        return redirect("pageExpire_error")    
  

    


