from django.db import models
from django.db import models 
from django.contrib.auth.models import User
from datetime import date,datetime,timedelta
from django.db.models.deletion import CASCADE

class subjectNames(models.Model):
    subject = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return str(self.subject)

class topicNames(models.Model):
    subject = models.ForeignKey(subjectNames,on_delete=models.CASCADE)
    topic = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return str(self.topic)

class mcqQuestion(models.Model):
    question = models.CharField(max_length=400,null=True,blank=True)
    opt1 = models.CharField(max_length=100,null=True,blank=True)
    opt2 = models.CharField(max_length=100,null=True,blank=True)
    opt3 = models.CharField(max_length=100,null=True,blank=True)
    opt4 = models.CharField(max_length=100,null=True,blank=True)
    ans = models.CharField(max_length=100,null=True,blank=True)

    topic = models.ForeignKey(topicNames,max_length=100,null=True,blank=True, on_delete=models.CASCADE)

    COMPLEXITY_CHOICE_LIST = [
        ("Hard","Hard"),
        ("Medium Hard","Medium Hard"),
        ("Medium","Medium"),
        ("Easy","Easy"),
    ]

    

    complexity = models.CharField(max_length=12, choices=COMPLEXITY_CHOICE_LIST)

    
    def complexityRate(self):
        if str(self.complexity) == "Hard":
            return int(100)
        elif str(self.complexity) == "Medium Hard":
            return int(75)
        elif str(self.complexity) == "Medium":
            return int(50)
        elif str(self.complexity) == "Easy":
            return int(25)

    def __str__(self):
        return str(self.question[:15]) + "..."


class quesSetDetail (models.Model):
    name = models.CharField(max_length=150,null=True,blank=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE) 
    description = models.CharField(max_length=500,null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    PRIVACY_CHOICE_LIST = [
        ('Public' , "Public"),
        ('Protected' , "Protected"),
    ]
    TYPE_CHOICE_LIST = [
        ("Previous","Previous"),
        ("Custom","Custom"),
    ]
    numOfQues = models.IntegerField(default=10)
    previous = models.CharField(max_length=9, choices=TYPE_CHOICE_LIST,default="Custom")
    privacy = models.CharField(max_length=9, choices=PRIVACY_CHOICE_LIST,default='Public')
    quesSets = models.ManyToManyField(mcqQuestion,related_name="quesSetExamConnection",blank=True)
    
    def quesSetComplexity(self):
        result = int(0)
        for i in self.quesSets.all():
            result+=i.complexityRate()
        return result//self.numOfQues

    def numOfSetQues(self):
        return str(self.quesSets.count())

    def __str__(self):
        return str(self.name) 

class sheduledExam(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    quesSet = models.ForeignKey(quesSetDetail,on_delete=models.CASCADE)
    description = models.CharField(max_length=500,null=True,blank=True)
    startTime = models.DateTimeField()
    duration = models.IntegerField(default=0)
    passingMark = models.IntegerField(default=0)
    password = models.CharField(max_length=100,default="")
    PRIVACY_CHOICE_LIST = [
        ('Public' , "Public"),
        ('Protected' , "Protected"),
    ]
    privacy = models.CharField(max_length=9, choices=PRIVACY_CHOICE_LIST,default='Public')
    registeredMember = models.ManyToManyField(User,related_name="Registered_Members",blank=True)
    joinedMember = models.ManyToManyField(User, related_name= "Joined_Member",blank=True)
    submittedMember = models.ManyToManyField(User, related_name= "Submitted_Member",blank=True)

    def totalReg(self):
        return  self.registeredMember.count()

    def totalJoin(self):
        return  self.joinedMember.count()

    def endTime(self):
        a=str(self.startTime)
        begin = datetime.strptime(a[:-6],'%Y-%m-%d %H:%M:%S')
        end = begin+timedelta(minutes=self.duration)
        return end
    
    def ended(self):
        a=str(self.startTime)
        begin = datetime.strptime(a[:-6],'%Y-%m-%d %H:%M:%S')
        end = begin+timedelta(minutes=self.duration)
        end=str(end)
        now = str(datetime.now())
        if len(now)==26:
            now = now[:-7]
        if end < now:
            return True
        else:
            return False
    
    def running(self):
        if self.ended():
            return False
        else:
            print(self.startTime,datetime.now())
            if str(self.startTime)>str(datetime.now()):
                return False
            else:
                return True
    



    def __str__(self):
        return str(self.name)+" | "+str(self.host)

class memberExamResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    exam = models.ForeignKey(sheduledExam, on_delete=models.CASCADE)
    solution = models.CharField(max_length=10000,null=True,blank=True)
    obtainedMark = models.IntegerField( default=0)

    def status(self):
        if self.obtainedMark>= self.exam.passingMark:
            return "Passed"
        return "Failed"

    def __str__(self):
        return str(self.user) + '|' + str(self.exam) 


    