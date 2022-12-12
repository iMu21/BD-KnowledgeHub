from django.db import models 
from django.contrib.auth.models import User
from datetime import date
from examination.models import mcqQuestion

from django.db.models.fields import BLANK_CHOICE_DASH


class pendingAccount(models.Model):
    username = models.CharField(max_length=100 )
    firstName = models.CharField(max_length=100,null=True,blank=True)
    lastName = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    authToken = models.CharField(max_length=100)
    joinAt = models.DateField(auto_now_add=True )

    def __str__(self):
        return str(self.username)



class memberBasic(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100,null=True,blank=True )
    lastName = models.CharField(max_length=100,null=True,blank=True )
    memberProfilePhoto = models.ImageField(null=True,blank=True,upload_to="images/ProfilePhoto/")
    memberCoverPhoto = models.ImageField(null=True,blank=True,upload_to="images/CoverPhoto/")
    memberDivision = models.CharField(max_length=50,null=True,blank=True )
    memberDistrict = models.CharField(max_length=50,null=True,blank=True )
    memberBirthDate = models.DateField(blank=True,null=True)
    about = models.CharField(max_length=500, blank=True,null=True)
    followedMember = models.ManyToManyField(User, related_name="Friends")
    joinAt = models.DateField(blank=True,null=True)
    ownQuestions = models.ManyToManyField(mcqQuestion,related_name='ownQuestions',blank=True)

    def totalFollowing(self):
        return self.followedMember.count()

    def memberAge(self):
        today = date.today()
        birthDate = self.memberBirthDate
        return today.year-birthDate.year

    def __str__(self):
        return str(self.username)    
    
 
class memberInstitution(models.Model):
    userName = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True )
    institutionName = models.CharField(max_length=200,blank=True,null=True)
    about = models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return str(self.userName)

class memberPhoneNumber(models.Model): 
    userName = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True )
    phoneNumber = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return str(self.userName)

class memberWorking(models.Model): 
    userName = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True )
    workingPlace = models.CharField(max_length=100,blank=True,null=True) 
    about = models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return str(self.userName)
 
class websiteType(models.Model):
    name = models.CharField(max_length=30,blank=True,null=True)
    websitelogo = models.ImageField(upload_to="logo/website/")

    def __str__(self):
        return str(self.name)

class memberWebsite(models.Model):
    userName = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True )
    address = models.CharField(max_length=100,blank=True,null=True)
    type = models.ForeignKey(websiteType , on_delete=models.CASCADE,blank=True,null=True )

    def __str__(self):
        return str(self.userName) + '|' + str(self.type)



