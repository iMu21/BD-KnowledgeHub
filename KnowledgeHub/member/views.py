from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import memberWebsite, pendingAccount,memberBasic,memberInstitution,memberPhoneNumber,memberWorking,websiteType
from django.conf import settings
from django.core.mail import send_mail
import random
from django.contrib.auth import authenticate,login,logout


def profile(request):
    if request.user.is_authenticated:
        member = []
        if memberBasic.objects.filter(username=request.user).first():
            member = memberBasic.objects.get(username=request.user)
        else:
            Obj = memberBasic.objects.create(username=request.user)
            Obj.save()
            member = Obj
        memberPhone = [] 
        if memberPhoneNumber.objects.filter(userName=request.user).first():
            memberPhone = memberPhoneNumber.objects.all().filter(userName=request.user)
        else:
            pass  
        institution  = [] 
        if memberInstitution.objects.filter(userName=request.user).first():
            institution = memberInstitution.objects.all().filter(userName=request.user)
        else:
            pass 
        company  = [] 
        if memberWorking.objects.filter(userName=request.user).first():
            company = memberWorking.objects.all().filter(userName=request.user)
        else:
            pass 
        website = []
        if memberWebsite.objects.filter(userName = request.user).first():
            website = memberWebsite.objects.all().filter(userName=request.user)
        else:
            pass   

        params={'member':member,'memberPhone':memberPhone,'institution':institution, 'company':company, 'website':website }
        return render(request,'profile.html',params)
    else:
       return redirect('logIn')     

def profileEdit(request):
    if request.user.is_authenticated:
        member = []
        if memberBasic.objects.filter(username=request.user).first():
            member = memberBasic.objects.get(username=request.user)
        else:
            Obj = memberBasic.objects.create(username=request.user)
            Obj.save()
            member = Obj
        website = []
        if memberWebsite.objects.filter(userName = request.user).first():
            website = memberWebsite.objects.all().filter(userName=request.user)
        else:
            pass
        params = {"member":member,"website":website}
        return render(request,'profileEdit.html',params)
    else:
        return redirect('logIn')

def phoneDelete(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    phoneid = request.GET.get('phoneid')
    if memberPhoneNumber.objects.filter(id=phoneid).first():
        phone = memberPhoneNumber.objects.get(id=phoneid)
        phone.delete()
        messages.warning(request, 'Your number has been deleted.') 
    else:
        messages.warning(request, 'The number you have requested to delete is invalid.')       
    return redirect ('profile')

def phoneEdit(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    phoneid = request.GET.get('phoneid')
    if memberPhoneNumber.objects.filter(id=phoneid).first():
        phone = memberPhoneNumber.objects.get(id=phoneid)
        params = {'phone':phone}
        return render (request,'phoneEdit.html',params) 
    messages.warning(request, 'The number you have requested to edit is invalid.')
    return redirect ('profile')

def phoneAdd(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    return render (request,'phoneAdd.html' )        

def profileEdited(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    memberDistrict = request.POST.get('memberDistrict')
    memberDivision = request.POST.get('memberDivision')
    memberBirthDate = request.POST.get('memberBirthDate')
    if memberBasic.objects.filter(username=request.user).first():
        print("okk")
        Obj = memberBasic.objects.get(username=request.user)
        Obj.firstName = firstName
        Obj.lastName = lastName
        Obj.memberDistrict = memberDistrict
        Obj.memberDivision = memberDivision
        if memberBirthDate:
            Obj.memberBirthDate = memberBirthDate
        Obj.save()
        messages.warning(request, 'Your basic info has been updated.') 
    return redirect ('profile') 
def phoneEdited(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    phoneid = request.POST.get('phoneid')
    correctPhone = request.POST.get('correctPhone')
    if memberPhoneNumber.objects.filter(id=phoneid).first():
        phone = memberPhoneNumber.objects.get(id=phoneid)
        phone.phoneNumber = correctPhone
        phone.save()
        messages.warning(request, 'Your phone number has been updated.') 
    return redirect ('profile')  

def phoneAdded(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    if request.method =="POST": 
        phone = request.POST.get('phone') 
        phoneObj = memberPhoneNumber.objects.create(userName=request.user ,phoneNumber=phone ) 
        phoneObj.save()
        messages.warning(request, 'Your phone number has been saved.') 
    print("hosse na")
    return redirect ('profile')

def workDelete(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    workid = request.GET.get('workid')
    if memberWorking.objects.filter(id=workid).first():
        work = memberWorking.objects.get(id=workid)
        work.delete()
    messages.warning(request, 'The work place you have requested to delete is invalid.') 
    return redirect ('profile')


def workEdit(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    workid = request.GET.get('workid')
    if memberWorking.objects.filter(id=workid).first():
        work = memberWorking.objects.get(id=workid)
        params = {'work':work }
        return render (request,'workEdit.html',params) 
    messages.warning(request, 'The work place you have requested to edit is invalid.') 
    return redirect ('profile') 

def workEdited(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    workid = request.POST.get('workid')
    correctWork = request.POST.get('correctWork')
    correctAbout = request.POST.get('correctAbout')
    if memberWorking.objects.filter(id=workid).first():
        work = memberWorking.objects.get(id=workid)
        work.workingPlace = correctWork
        work.about = correctAbout
        work.save()
        messages.warning(request, 'Your working place has been updated.') 
    return redirect ('profile')

def workAdd(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    return render (request,'workAdd.html' )  

def workAdded(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    if request.method =="POST":
        work = request.POST.get('work')
        about = request.POST.get('about')
        workObj = memberWorking.objects.create(userName=request.user , workingPlace=work , about = about) 
        workObj.save()
        messages.warning(request, 'Your work place has been saved.') 
    return redirect ('profile')


def educationDelete(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    educationid = request.GET.get('educationid')
    if memberInstitution.objects.filter(id=educationid).first():
        education = memberInstitution.objects.get(id=educationid)
        education.delete()
    messages.warning(request, 'The institution you have requested to delete is invalid.') 
    return redirect ('profile')    



def educationEdit(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    educationid = request.GET.get('educationid')
    if memberInstitution.objects.filter(id=educationid).first():
        education = memberInstitution.objects.get(id=educationid)
        params = {'education':education }
        return render (request,'educationEdit.html',params) 
    messages.warning(request, 'The instituion you have requested to edit is invalid.') 
    return redirect ('profile') 

def educationEdited(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    educationid = request.POST.get('educationid')
    correcteducation = request.POST.get('correcteducation')
    correctAbout = request.POST.get('correctabout')
    if memberInstitution.objects.filter(id=educationid).first():
        education = memberInstitution.objects.get(id=educationid)
        education.institutionName = correcteducation
        education.about = correctAbout
        education.save()
        messages.warning(request, 'Your instituion has been updated.') 
    return redirect ('profile')

def educationAdd(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    return render (request,'educationAdd.html' )  

def educationAdded(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    if request.method =="POST":
        education = request.POST.get('education')
        about = request.POST.get('about')
        eduObj = memberInstitution.objects.create(userName=request.user , institutionName=education , about = about) 
        eduObj.save()
        messages.warning(request, 'Your instituion has been saved.') 
    return redirect ('profile')


def websiteDelete(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    websiteid = request.GET.get('websiteid')
    if memberWebsite.objects.filter(id=websiteid).first():
        website = memberWebsite.objects.get(id=websiteid)
        website.delete()
    messages.warning(request, 'The website adress you have requested to delete is invalid.') 
    return redirect ('profile')    



def websiteEdit(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    websiteid = request.GET.get('websiteid')
    if memberWebsite.objects.filter(id=websiteid).first():
        website = memberWebsite.objects.get(id=websiteid)
        params = {'website':website}
        return render (request,'websiteEdit.html',params) 
    messages.warning(request, 'The website address you have requested to edit is invalid.') 
    return redirect ('profile') 

def websiteEdited(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    websiteid = request.POST.get('websiteid')
    correctAddress = request.POST.get('correctaddress')
    correctType = request.POST.get('correcttype')
    if memberWebsite.objects.filter(id=websiteid).first():
        website = memberWebsite.objects.get(id=websiteid)
        website.address = correctAddress
        website.about = correctType
        website.save()
        messages.warning(request, 'Your '+str(website.type)+'adress has been updated.') 
    return redirect ('profile')

def websiteAdd(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    types = websiteType.objects.all()
    params={"websiteType":types}
    return render (request,'websiteAdd.html',params )  

def websiteAdded(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    if request.method =="POST":
        address = request.POST.get('address')
        typeid = request.POST.get('typeid')
        websiteObj = memberWebsite.objects.create(userName=request.user , address=address , type = websiteType.objects.get(id=typeid)) 
        websiteObj.save()
        messages.warning(request, 'Your website address has been saved.') 
    return redirect ('profile')



 

def signUp(request):
    if request.user.is_authenticated:
        return redirect('home') 
    return render(request,'signUp.html')

def logIn(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request,'logIn.html')    

def logOut(request):
    logout(request)
    return redirect('logIn')

def logInAttempt(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('logIn')
        
        
        profile_obj = pendingAccount.objects.filter(username = username ).first()

        if  profile_obj :
            messages.success(request, 'Profile is not verified, check your mail.')
            return redirect('logIn')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('logIn')
        
        login(request , user)
        return redirect('profile')

    return render(request , 'logIn.html')

def signUpConfirmation(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username = request.POST.get('username')
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        retypePassword = request.POST.get('retypePassword') 
        if User.objects.filter(username = username).first(): 
            messages.success(request, 'This username is taken before.')
            return redirect('signUp')

        if User.objects.filter(email = email).first(): 
            messages.success(request, 'This email is already in used.')
            return redirect('signUp')

        if password!=retypePassword:
            messages.success(request, "Re-entered password doesn't match.")
            return redirect('signUp')
        if len(password)<8:
            messages.success(request, "Password is too short.")
            return redirect('signUp')
        token= str(random.randrange(000000, 999999)) 
        obj = pendingAccount.objects.create(username=username,firstName=firstName,lastName=lastName,email=email,authToken=token,password=password)
        obj.save() 
        sendMail(email,token,username)
    return render(request,'signUpConfirmation.html' )  


def sendMail(email,token,username):
    subject = "Email confirmation for KnowledgeHub"  
    message = f"{username} This is your verifaction code: {token}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = {email}
    send_mail(subject,message,email_from,recipient_list)

def  verificationCheck(request):
    token = request.POST.get('token')
    email = request.POST.get('email')
    for v in pendingAccount.objects.filter(email=email):
            if str(v.authToken) != (token):
                v.delete()
    if pendingAccount.objects.filter(authToken = token,email=email ).first():
        obj = pendingAccount.objects.get(email=email ) 
        userObject = User.objects.create(username = obj.username , email = obj.email ) 
        userObject.set_password(obj.password)
        userObject.save()
        memberBasicObject = memberBasic.objects.create(username = userObject,firstName = obj.firstName, lastName = obj.lastName, joinAt = obj.joinAt)
        memberBasicObject.save()
        pendingAccount.objects.filter(email=email).delete()
        pendingAccount.objects.filter(username=userObject.username).delete()
        messages.success(request, "Signed Up successfully. Log In here")
        return redirect('logIn')
    messages.success(request, "Incorrect Email or Verification Code")
    return redirect('signUpConfirmation')    
