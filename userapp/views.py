from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404

from adminapp.models import StaffModel
from . models import ConfidentialDataModel, Request_recordModel,Send_request_files
from django.core.paginator import Paginator


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)

        try:
            print('try')
            staff = StaffModel.objects.get(official_email=email,password=password)
        
            request.session['staff_id'] = staff.staff_id 
            messages.success(request, 'login successfully')
            return redirect('dashbord')

        except:
            messages.info(request, 'Your account is not valid')
            return redirect('user-login')

    return render(request, 'user/user-login.html')


def user_dashbord(request):
    return render(request, 'user/user-home.html')

def profile(request):
    profile_id = request.session['staff_id']
    staff = StaffModel.objects.get(pk=profile_id)
    edit = get_object_or_404(StaffModel,pk=profile_id )

    if request.method=='POST':
        name = request.POST.get('name')
        state = request.POST.get('state')
        address = request.POST.get('address')
        pin = request.POST.get('pin')

        if not request.FILES.get('profile',False):
            edit.name=name
            edit.state=state
            edit.address=address
            edit.pin=pin
        if request.FILES.get('profile',False):
            image = request.FILES['profile']
            edit.name=name
            edit.state=state
            edit.address=address
            edit.pin=pin
            edit.profile=image
        edit.save()
        return redirect('profile')

    return render(request,'user/profile.html',{'staff':staff})

def confidencial_data(request):

    a =  request.session['staff_id']
    data = StaffModel.objects.get(pk=a)
    print(a,'23456')
   
    if request.method == 'POST' and 'file' in request.FILES:
        name = request.POST['name']
        file = request.FILES['file']
        
        print(name)
        print(file)
        file_format = file.name
        if file_format and file_format.rsplit('.',1)[1].lower() in ['pdf','docx','csv'] :

            ConfidentialDataModel.objects.create(file_name=name,staff=data, data_file=file)
            messages.success(request,'data add successfully')

        else:
            messages.info(request,'upload file in pdf format')
            return redirect('conf-data')
           
    return render(request, 'user/confidentaldata.html')

def request_record(request):
    sta = request.session['staff_id']
    staff = StaffModel.objects.exclude(staff_id=sta).order_by('-staff_id')

    paginater = Paginator(staff, 3)
    page_number = request.GET.get('page')
    page = paginater.get_page(page_number)

    if request.method == 'POST':
        query = request.POST.get('search')
        if query :
            receiver = StaffModel.objects.filter(name__icontains=query).exclude(staff_id=sta)
            return render(request,'user/request-record.html',{'staff':receiver})
        else:
            messages.info(request,' Name is not available try again')
            print('noo record 454535545')

    return render(request,'user/request-record.html',{'staffs':page})

def send_request(request,id):
    sen = request.session['staff_id']
    sender = StaffModel.objects.get(pk=sen)
    receiver = StaffModel.objects.get(pk=id)
    # staff = StaffModel.objects.get(staff_id=id)
    if request.method =='POST':
        department = request.POST.get('dep')
        title = request.POST.get('title')
        description = request.POST.get('desce')
        print(department)
        print(title)
        print(description)
        req = Request_recordModel.objects.create(
            sender_id=sender, 
            receiver_id=receiver,  
            department=department,  
            request_title=title,
            description=description)
        print(req)
        messages.success(request, 'Request send')

    return render(request, 'user/send_request.html',{'receiver':receiver})

def approved_record(request):
    rece = request.session['staff_id']
    receiver = Request_recordModel.objects.filter(receiver_id=rece).filter(status='sent').order_by('-request_id')


    paginater = Paginator(receiver, 3)
    page_number = request.GET.get('page')
    page = paginater.get_page(page_number)

    context = {
        'receiver':page
    }
    return render(request, 'user/Approved-Record-Request.html',context)

def view_record(request,id):
    rece = request.session['staff_id']
    print(rece)
    receiver = Request_recordModel.objects.filter(receiver_id=rece)
    sender = Request_recordModel.objects.get(request_id=id)
    # print(sender.count(),'countttt')
    # send = Request_recordModel.objects.get(pk=id)

    
    print('vijay','yuiolkjnb ')
    
    if request.method == 'POST' and 'file' in request.FILES:
        sender_u = StaffModel.objects.get(pk=rece)
        name = request.POST['name']
        file = request.FILES['file']
        user_id=request.POST.get('id')
        description = request.POST.get('desc')
        print(name,file,description,user_id,'wertyuiopokjbv')
 
        Send_request_files.objects.create(
            name_of_the_file=name,
            file = file,
            description = description,
            sender_id=sender_u,
            receiver_id=sender.sender_id     
        )
        sender.delete()
        messages.success(request,'requested files send successfully')
        return redirect('approved-record')
    context ={
        'rece':receiver,
        'i':sender
    }
    return render(request,'user/view-record.html', context)

def received_records(request):
    requested_persion = request.session['staff_id']
    records = Send_request_files.objects.filter(receiver_id=requested_persion).order_by('-send_file_id')

    paginater = Paginator(records, 3)
    page_number = request.GET.get('page')
    page = paginater.get_page(page_number)

    return render(request,'user/requested_files.html', {'records':page})

def search_file(request):
    # requested_persion = request.session['staff_id']
    if request.method=='POST':
        query = request.POST.get('search')
        print(query)
        if query:
            print('yessss')
            file = Send_request_files.objects.filter(name_of_the_file=query)
            print(file.count())
            return render(request, 'user/requested_files.html',{'records':file})
    return render(request,'user/requested_files.html')


def delete_file(request,id):
    rem = Send_request_files.objects.get(send_file_id=id) 
    rem.delete()
    messages.success(request,'file deleted successfully')
    return redirect('received_files')

def user_logout(request):
    messages.success(request,'user log out successfully')
    return redirect('home')