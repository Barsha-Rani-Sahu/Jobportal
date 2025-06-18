from django.shortcuts import render,redirect
from .models import Recruiter,Job,Seeker,Apply,Category,UserProfile,Saved
from django.http import HttpResponse 

from django.utils import timezone 
from datetime import date, timedelta
from django.core.mail import send_mail
from django.conf import settings




#-----------------------------------Recruiter-------------------------
def Recruiter_home(request):
    
    return render(request,'recruiter/recruiter_home.html')

def Recruiter_register(request):
    if request.method=='GET':
        return render(request,'recruiter/register.html')
    else:
        Company_Name=request.POST['Company_Name']

        Email=request.POST['Email']
        Password=request.POST['Password']
        register=Recruiter(Company_Name=Company_Name,Email=Email,Password=Password)
        register.save()
        return redirect(home)
    
def Recruiter_login(request):
    if request.method=='GET':
        return render(request,'recruiter/login.html')
    else:
        company_name=request.POST['company_name']
        pwd=request.POST['pwd']
        
        try:
            company=Recruiter.objects.get(Company_Name=company_name,Password=pwd)
        except:
            return redirect(Recruiter_login)
        else:
            request.session["company_name"]=company_name
            return redirect(Recruiter_home)
        
def Post_job(request,):
    
    if request.method=='GET':
        categories = Category.objects.all()
        return render(request,'recruiter/job.html',{'categories':categories})
    else:
        company_name=request.session.get('company_name')
        jobtitle=request.POST['Job_Title']
        responsibility=request.POST['responsibility']
        experience=request.POST['Experience']
        salary=request.POST['Salary']
        location=request.POST['Location']
        skills=request.POST['Skills']
        startdate=request.POST['Start_date']
        enddate=request.POST['End_date']
        Category_name = request.POST['category_name'] 
        image = request.FILES.get('image')
        if image:
            print(f"Uploaded image: {image.name}")
        else:
            print("No image uploaded")
        category = Category.objects.get(pk=Category_name) 
        
        jobs=Job(CompanyName=company_name,Job_Title=jobtitle,Responsibility=responsibility,Experience=experience,Salary=salary,Location=location,Skills=skills,
                 Start_date=startdate,End_date=enddate,category_name=category,image_url=image)
        jobs.save()
        return redirect(Recruiter_home)
    
def Posted_jobs(request):
    company_name=request.session.get('company_name')
    jobs=Job.objects.filter(CompanyName=company_name)
    return render(request,'recruiter/posted_jobs.html',{'jobs':jobs})

def View_Details(request,job_id):
    if 'company_name' in request.session:
        job=Job.objects.get(id=job_id)
        return render(request,'recruiter/view_details.html',{'job':job})
    else:
        return redirect('recruiter_login')
    
def Applicant(request,):
    company_name=request.session.get('company_name')
    jobs=Job.objects.filter(CompanyName=company_name)
    return render(request,'recruiter/applicant.html',{'jobs':jobs})

def applicant_list(request, job_id):
    applicants = Apply.objects.filter(job_id=job_id)
    return render(request, 'recruiter/applicant_list.html', {'applicants': applicants})
    
def Logout(request):
    request.session.clear()
    return redirect(home)
        

#----------------------------------------Seeker----------------------------

def home(request):
    catname=Category.objects.all
    jobs=Job.objects.all()
    today = date.today()
    one_week=today-timedelta(days=3)
    latest_jobs = Job.objects.filter(Start_date__range=(one_week, today))
    return render(request,'seeker/home.html',{'jobs':jobs,'catname':catname,'latest_jobs':latest_jobs})
def Seeker_register(request):
    if request.method=='GET':
        return render(request,'seeker/register.html')
    else:
        user_name=request.POST['username']
        email=request.POST['email']
        phno=request.POST['phno']
        password=request.POST['pwd']

        signup=Seeker(UserName=user_name,Email=email,PhNo=phno,Password=password)
        signup.save()
        body= """
                Hello,

                Welcome to Job Portal. We are Happy to see you here!

                We are confident that We will help you to find
                your dream job and much more.

                Have a Good Day ahead..!

                Thank You
                """
        send_mail("Welcome To Our Website",body,settings.EMAIL_HOST_USER,[email],fail_silently=False) 
        return redirect(home)
    
def Seeker_login(request):
    if request.method=='GET':
        return render(request,'seeker/login.html')
    else:
        user_name=request.POST['user_name']
        pwd=request.POST['pwd']
        
        try:
            company=Seeker.objects.get(UserName=user_name,Password=pwd)
        except:
            return redirect(Seeker_login)
        else:
            request.session["user_name"]=user_name
            return redirect(User_profile)

def Apply_job(request,job_id):
    job=Job.objects.get(id=job_id)
    if 'user_name' in request.session:
        if request.method=='GET':
            catname=Category.objects.all
            return render(request,'seeker/apply_job.html',{'job':job,'catname':catname})
        else:
            first_name=request.POST['firstname']
            last_name=request.POST['lastname']
            email=request.POST['email']
            phno=request.POST['phno']
            resume_upload = request.FILES['resume_upload']
            user_name=request.POST['user_name']
            apply_user=Apply(First_Name=first_name,Last_Name=last_name,Email=email,PhNo=phno,Resume=resume_upload,job_id=job,user=user_name)
            apply_user.save()
            return redirect(home)
        
    else:
         return redirect(Seeker_login)

    
def View_job_Details(request,job_id):
    catname=Category.objects.all( )
    if 'user_name' in request.session:
        job=Job.objects.get(id=job_id)
        return render(request,'seeker/job_view_details.html',{'job':job,'catname':catname})
    else:
        return redirect(Seeker_login)
    
def job_filter(request,cat_name):
    catname=Category.objects.all
    jobs=Job.objects.filter(category_name=cat_name)
    return render(request,'seeker/filter_job.html',{'jobs':jobs,'catname':catname})

def Application_status(request,name):
        status=Apply.objects.filter(user=name)
        return render(request,'seeker/application_status.html',{'status':status})

def Fresher_jobs(request):
    catname=Category.objects.all
    jobs=Job.objects.filter(Experience=0)
    return render(request,'seeker/filter_job.html',{'jobs':jobs,'catname':catname})

def User_profile(request):
    if request.method=='GET':
        return render(request,'seeker/user_profile.html')
    else:
        name=request.POST['full_name']
        dob=request.POST['date_of_birth']
        gender=request.POST['gender']
        nationality=request.POST['nationality']
        address=request.POST['address']
        phno=request.POST['phone_number']
        email_id=request.POST['email']
        jobstatus=request.POST['job_status']
        jobtitle =request.POST['job_title']
        companyname=request.POST['company_name']
        highestdegree= request.POST['highest_degree']
        major_field_ofstudy=request.POST['major_field_of_study']
        institutionname=request.POST['institution_name']
        graduation_year=request.POST['graduation_year']
        skills=request.POST['technical_skills']
        SoftSkills=request.POST['soft_skills']
        hobbies=request.POST['hobbies']
        interests=request.POST['interests']
        languages_spoken=request.POST['languages_spoken']
        user_name=request.POST['user_name']

        user=UserProfile(full_name = name,date_of_birth = dob ,gender = gender ,nationality = nationality ,address = address,
                        phone_number = phno ,email = email_id, job_status = jobstatus, job_title = jobtitle ,company_name = companyname,highest_degree_obtained = highestdegree,
                        major_field_of_study = major_field_ofstudy,institution_name = institutionname,graduation_year = graduation_year,technical_skills = skills,soft_skills = SoftSkills,hobbies = hobbies
                        ,interests = interests,languages_spoken=languages_spoken,user=user_name)
        user.save()
        return redirect(home)
    
def My_Profile(request):
    user_name=request.session.get('user_name')
    profile=UserProfile.objects.filter(user=user_name)
    return render(request,'seeker/myprofile.html',{'profile':profile})

def Savedjob(request,jobid):
    
    if 'user_name' in request.session:
        job=Job.objects.get(id=jobid)
        user=request.session.get('user_name')
        if not Saved.objects.filter(user=user, job_id=job).exists():
                saved_job = Saved(job_id=job, user=user, saved_on=timezone.now())
                saved_job.save()
               
        return redirect(home)
    else:
        return redirect(Seeker_login)

def Bookmark(request):
    catname=Category.objects.all
    user = request.session.get('user_name')  

    if not user:
        return redirect(Seeker_login)  
    saved_jobs = Saved.objects.filter(user=user)
    job_id = saved_jobs.values_list('job_id', flat=True)
    jobs = Job.objects.filter(id__in=job_id)
    return render(request,'seeker/saved_job.html',{'jobs':jobs,'catname':catname})


    
def Applied_job(request):
    username=request.session.get('user_name')
    user=Apply.objects.get(user=username)
    return render(request,'seeker/applied_job.html',{'user':user})

        

def user_logout(request):
    request.session.clear()
    return redirect(home)

