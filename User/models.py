from django.db import models # type: ignore
from Admin.models import Category

# Create your models here.
class Recruiter(models.Model): 
    Company_Name=models.CharField(max_length=50) 
    Email=models.EmailField(max_length=50) 
    Password=models.CharField(max_length=50) 
 
    class Meta: 
        db_table="Recruiter" 
 
    def __str__(self): 
        return self.Company_Name 
    
class Seeker(models.Model):
    UserName=models.CharField(max_length=40)
    Email=models.EmailField(max_length=50)
    PhNo=models.BigIntegerField()
    Password=models.CharField(max_length=40)

    class Meta:
        db_table='Seeker'

class Job(models.Model): 
    CompanyName = models.CharField(max_length=50)  
    Job_Title=models.CharField(max_length=50) 
    Responsibility=models.CharField(max_length=100) 
    Experience=models.IntegerField(default=0) 
    Salary=models.FloatField(default=10000) 
    Location=models.CharField(max_length=50) 
    Skills=models.CharField(max_length=100) 
    Start_date=models.DateField() 
    End_date=models.DateField()
    category_name=models.ForeignKey(Category,on_delete=models.CASCADE)
    image_url=models.ImageField(upload_to="images")
    
 
    class Meta: 
        db_table="Job" 
        
    def __str__(self): 
        return (f"{self.CompanyName},{self.Job_Title}, "
                f"{self.Responsibility},{self.Experience},"
                f"{self.Salary},{self.Location},{self.Skills}, "
                f"{self.Start_date},{self.End_date},{self.category_name}")
    
class Apply(models.Model):
    First_Name=models.CharField(max_length=20)
    Last_Name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=50)
    PhNo=models.BigIntegerField()
    Resume = models.FileField(upload_to="resumes") 
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)  
    user=models.CharField(max_length=30)

    class Meta:
        db_table='Apply'

    def __str__(self):
        return (f"{self.First_Name},{self.Last_Name},{self.Email},{self.PhNo},{self.Resume},{self.job_id},{self.user}")


class UserProfile(models.Model):


    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)
    nationality = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    job_status = models.CharField(max_length=20)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    highest_degree_obtained = models.CharField(max_length=100)
    major_field_of_study = models.CharField(max_length=100)
    institution_name = models.CharField(max_length=255)
    graduation_year = models.IntegerField()
    technical_skills = models.TextField()
    soft_skills = models.TextField()
    hobbies = models.TextField()
    interests = models.TextField()
    languages_spoken = models.TextField()
    user=models.CharField(max_length=100)
    
    class Meta:
        db_table='UserProfile'


    def __str__(self):
        return self.full_name
    

class Saved(models.Model):
    job_id=models.ForeignKey(Job, on_delete=models.CASCADE)
    user=models.CharField(max_length=50)
    saved_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='Saved'

    def __str__(self):
        return self.job_id.pk