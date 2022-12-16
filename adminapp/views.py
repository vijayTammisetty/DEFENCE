from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from .models import StaffModel
from defenceResearch.settings import DEFAULT_FROM_EMAIL
from userapp.models import ConfidentialDataModel
from django.core.paginator import Paginator
import random

# Create your views here.

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'admin':
            messages.success(request,'admin login successfully ')
            return redirect('dashboard')
            
        else:
            messages.error(request,'Invalid user name and password')
            return redirect('admin_login')

    return render(request, 'admin/admin-login.html')

def dashboard(request):
    staff = StaffModel.objects.all().count()
    pending = ConfidentialDataModel.objects.filter(status='pending').count()
    conf_data = ConfidentialDataModel.objects.all().count()
    context = {
        'staff':staff,
        'pending':pending,
        'total_data':conf_data
    }

    return render(request, 'admin/admin-dashboard.html',context)

def add_newstaff(request):
    print('data44444')
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '0123456789'
    symbols = '!@#$%^&*'
    mix = lower+upper+number+symbols
    size = 8
    password10 = ''.join(random.sample(mix,size))
    if request.method =='POST' and 'profile' in request.FILES :
        print('new data')
        empname = request.POST.get('empname')
        print(empname)
        empId = request.POST.get('empid')
        empDep = request.POST.get('department')
        empEmail = request.POST.get('email')
        profile = request.FILES['profile']
        # dob = request.POST.get('dob')
        # password = request.POST.get('password')
        official_email = request.POST.get('email2')
        state = request.POST.get('state')
        country = request.POST.get('country')
        address = request.POST.get('address')
        pin = request.POST.get('pin')
        join_date = request.POST.get('join')
        # releave_date = request.POST.get('releave')



        try:
            StaffModel.objects.get(to=empEmail)
            messages.info(request,'Email already exists')
            return redirect('new-staff')

        except:
            
            # image = profile.name

            # if image and image.rsplit('.',1)[1].lower() in  ['jpg','jpeg','png','gif','jfif']:
                StaffModel.objects.create(
                    name=empname,
                    empId= empId,
                    empDepartment = empDep,
                    to = empEmail,
                    profile = profile,
                    # date_of_birth = dob,
                    password = password10,
                    official_email = official_email,
                    state = state,
                    country = country,
                    address = address,
                    pin = pin,
                    join_date = join_date)

              
                mail = empEmail
                html_content = f"<p>Dear Officer,</p><p> Your official email :{official_email}</p><p>  Password : {password10} :</p><span><strong>" 
                from_mail = DEFAULT_FROM_EMAIL
                to_mail = [mail]
                try:
                    msg = EmailMultiAlternatives("Authentication Credentials", html_content, from_mail, to_mail)
                    msg.attach_alternative(html_content, "text/html")
                    if msg.send():
                        print('sent')
                        messages.info(request, 'credentials has been sent successfully')
                        return redirect('manage-staff')
                except:
                    messages.warning(request, "credentials could not be sent try again later")
                    return redirect('manage-stafff')
                messages.success(request, 'Employee added  successfully')
                return redirect('new-staff')


    
    return render(request, 'admin/addnewstaff.html')

def manage_staff(request):
    staff = StaffModel.objects.all().order_by('-staff_id')
    paginater = Paginator(staff, 3)
    page_number = request.GET.get('page')
    page = paginater.get_page(page_number)
    
    return render(request, 'admin/managestaff.html', {'staff':page})

def edit_staff(request,id):
    staff = StaffModel.objects.get(pk=id)
    dep = StaffModel.objects.all()
    edit =  get_object_or_404(StaffModel,pk=id)
    print('staff')
    if request.method == 'POST':
        print('bgfvddfg')
        name = request.POST['empname']
        print(name)
        empid = request.POST['empid']
        department = request.POST['department']
        to = request.POST['email']
        # dob = request.POST['dob']
        # password = request.POST['password']
        official_email = request.POST['email2']
        state = request.POST['state']
        country = request.POST['country']
        address = request.POST['address']
        pin = request.POST['pin']
        join_date = request.POST['join']

        if not request.FILES.get('profile',False):
            edit.name = name
            edit.empId = empid 
            edit.empDepartment =department 
            edit.to = to 
            # edit.date_of_birth = dob 
            # edit.password = password 
            edit.official_email = official_email 
            edit.state = state  
            edit.country = country 
            edit.address = address 
            edit.pin = pin 
            edit.join_date = join_date 

        if request.FILES.get('profile',False):
            profile = request.FILES['profile']
            edit.name = name
            edit.empId = empid 
            edit.empDepartment =department 
            edit.to = to 
            # edit.date_of_birth = dob 
            # edit.password = password 
            edit.official_email = official_email 
            edit.state = state  
            edit.country = country 
            edit.address = address 
            edit.pin = pin 
            edit.join_date = join_date
            edit.profile = profile

            # images = profile.name
            # if images and images.rsplit('.',1)[1].lower() in ['jpg','jpeg','png','gif']:
            #    edit.profile = profile
            # else:
            #     messages.error(request,'upload valid image format')
            #     return redirect('manage-study-material')  

        edit.save()
        messages.success(request, 'staff details updated successfully ')
        return redirect('manage-staff')

    return render(request, 'admin/edit-staffdetails.html',{'staff':staff, 'depa':dep})

def delete_staff(request,id):
    staff = StaffModel.objects.get(pk=id)
    staff.delete()
    messages.success(request, 'one of the staff removed successfully')
    return redirect('manage-staff')


    
def publishedcontent(request):
    data = ConfidentialDataModel.objects.filter(status='pending')

    paginater = Paginator(data, 3)
    page_number = request.GET.get('page')
    page = paginater.get_page(page_number)

    return render(request, 'admin/publishedcontent.html', {"data":page})


def accept(request,id):
    data = ConfidentialDataModel.objects.get(pk=id)
    data.status='Accept'
    data.save(update_fields=['status'])
    data.save()
    messages.success(request,'Published content accepted successfully')
    return redirect('published')

def reject(request,id):
    print('rertertrerertretr')
    data = ConfidentialDataModel.objects.get(pk=id)
    data.delete()
    messages.success(request, 'Published content rejected successfully')
    
def allcontent(request):
    all_content = ConfidentialDataModel.objects.all().order_by('-data_id')

    paginater = Paginator(all_content, 3)
    page_number = request.GET.get('page')
    page = paginater.get_page(page_number)

    return render(request, 'admin/allcontent.html',{'all_content':page})

def delete_content(request,id):
    data = ConfidentialDataModel.objects.get(pk=id)
    data.delete()
    messages.success(request, 'content deleted successfully')
    return redirect('allcontent')


def logout(request):
    messages.success(request,'admin logout successfully')
    return redirect('home')

