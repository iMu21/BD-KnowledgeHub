from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from . import models
from datetime import time

def createQuesPaper(request):
    if request.user.is_authenticated:
        return render(request,'createQuesPaper.html')
    else:
        messages.warning(request, 'Log in first.')
        redirect('logIn')

def createQuesPaperReq(request):
    if request.user.is_authenticated:
        name = request.POST.get('name')
        numOfQues = request.POST.get('numOfQues')
        description=""
        description = request.POST.get('description')
        privacy = request.POST.get('privacy')
        Obj = models.quesSetDetail.objects.create(privacy=privacy,name=name,description=description,numOfQues=numOfQues,host=request.user)
        Obj.save()
        params = {"exam":Obj}
        return render(request,'setQuestionMidStage.html',params)
    else:
        messages.warning(request, 'Log in first.')
        redirect('logIn')

def setQuesMidStage(request):
    if request.user.is_authenticated:
        examId = request.GET.get('examId')
        Obj = models.quesSetDetail.objects.get(pk=examId)
        topics = models.topicNames.objects.all()
        params = {"exam":Obj,"topics":topics}
        return render(request,'setQuestion.html',params)
    else:
        return redirect('logIn')

def setQues(request,examId):
    if request.user.is_authenticated:
        Obj = models.quesSetDetail.objects.get(pk=examId)
        topics = models.topicNames.objects.all()
        params = {"exam":Obj,"topics":topics}
        return render(request,'setQuestion.html',params)
    else:
        messages.warning(request, 'Log in first.')
        redirect('logIn')

def updateIndividualQues(request):
    if request.user.is_authenticated:
        examId = request.POST.get("examId")
        Obj = models.quesSetDetail.objects.get(pk=examId)
        question = request.POST.get("question")
        opt1 = request.POST.get("opt1")
        opt2 = request.POST.get("opt2")
        opt3 = request.POST.get("opt3")
        opt4 = request.POST.get("opt4")
        ans = request.POST.get("ans")
        topicId = request.POST.get("topicName")
        complexity = request.POST.get("complexity")
        topicObj = models.topicNames.objects.get(pk=topicId)
        newObj = models.mcqQuestion.objects.create(question=question,opt1=opt1,opt2=opt2,opt3=opt3,opt4=opt4,ans=ans,topic=topicObj,complexity=complexity)
        newObj.save()
        Obj.quesSets.add(newObj)
        params={"exam":Obj}
        return render(request,'setQuestionMidStage.html',params)
    else:
        return redirect('logIn')

def questionPaper(request,examId):
    if request.user.is_authenticated:
        Obj = models.quesSetDetail.objects.get(pk=examId)
        quesSet = Obj.quesSets.all()
        params = {"exam":Obj,"quesSet":quesSet}
        return render(request,'questionPaper.html',params)
    else:
        return redirect('logIn')

def quesPaperList(request):
    Obj = models.quesSetDetail.objects.all()
    for i in Obj:
        if i.numOfQues != i.quesSets.count():
            mcqObj = models.mcqQuestion.objects.all()
            for j in mcqObj:
                if i.quesSets.filter(id=j.id).exists():
                    j.delete()
            i.delete()
    params = {"exams":Obj}
    return render(request,'quesPaperList.html',params)

def quesList(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    sub = request.POST.get('subName')
    topic = request.POST.get('topicName')
    if models.topicNames.objects.filter(pk=topic).count():
        Obj = models.mcqQuestion.objects.filter(topic_id=topic)
        top = models.topicNames.objects.get(pk=topic)
        sub = top.subject
        topObj = models.topicNames.objects.all()
        topicNames = []
        for i in topObj:
            if str(i.subject_id)==str(sub.id):
                topicNames.append(i)
        print(topicNames)
        params = {"ques":Obj,"sub":sub,"top":top,"topicNames":topicNames}
        return render(request,'quesList.html',params)
    elif models.subjectNames.objects.filter(pk=sub).count():
        topObj = models.topicNames.objects.all()
        Obj=[]
        topicNames = []
        for i in topObj:
            print(i.subject_id)
            if str(i.subject_id)==str(sub):
                print(i.subject_id,sub)
                selectedObj = models.mcqQuestion.objects.filter(topic=i.id)
                Obj.append(selectedObj)
                topicNames.append(i)
        print(topicNames)
        subObj = models.subjectNames.objects.get(pk=sub)
        params = {"ques":Obj,"sub":subObj,"topicNames":topicNames}
        return render(request,'quesList.html',params)
    else:
        Obj = models.mcqQuestion.objects.all()
        subNames = models.subjectNames.objects.all()
        params = {"ques":Obj,"subNames":subNames}
        return render(request,'quesList.html',params)

def createExam(request):
    if request.user.is_authenticated:
        quesSet = models.quesSetDetail.objects.all()
        params = {'quesSet':quesSet}
        return render(request,'createExam.html',params)
    else:
        messages.warning(request, 'Log in first.')
        redirect('logIn')

def createExamReq(request):
    if request.user.is_authenticated:
        name = request.POST.get('name')
        quesSetId = request.POST.get('quesSetId')
        quesSet = models.quesSetDetail.objects.get(id=quesSetId)
        startTime = request.POST.get('startTime')
        duration = request.POST.get('duration')
        description=""
        password=""
        password = request.POST.get('password')
        passingMark = request.POST.get('passingMark')
        description = request.POST.get('description')
        privacy = request.POST.get('privacy')
        Obj = models.sheduledExam.objects.create(passingMark=passingMark,password=password,startTime=startTime,duration=duration,privacy=privacy,name=name,description=description,quesSet=quesSet,host=request.user)
        Obj.save()
        params = {"exam":Obj}
        return render(request,'createExamMidStage.html',params)
    else:
        messages.warning(request, 'Log in first.')
        redirect('logIn')

def createExamMidStage(request):
    if request.user.is_authenticated:
        examId = request.GET.get('examId')
        Obj = models.sheduledExam.objects.get(pk=examId)
        params = {"exam":Obj}
        return render(request,'setQuestion.html',params)
    else:
        messages.warning(request, 'Log in first.')
        redirect('logIn')

def examDetails(request,examId):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    if request.user.is_authenticated:
        Obj = models.sheduledExam.objects.get(pk=examId)
        registered=int(0)
        if Obj.registeredMember.filter(id=request.user.id).exists():
            registered = int(1)
        params = {"exam":Obj,"registered":registered}
        print(Obj.running())
        return render(request,'examDetails.html',params)

def joinExam(request):
    examId = request.POST.get('examId')
    exam = models.sheduledExam.objects.get(id=examId)
    if exam.registeredMember.filter(id=request.user.id).exists():
        if exam.joinedMember.filter(id=request.user.id).exists():
            params = {"exam":exam,"joined":1,"registered":1}
            return render(request,'examRunningMidStage.html',params)
        else:
            exam.joinedMember.add(request.user)
            params = {"exam":exam,"joined":1,"registered":1}
            return render(request,'examRunningMidStage.html',params)
    registered = int(0)
    params = {"exam":exam,"registered":registered}
    return render(request,'examDetails.html',params)
    
def examRunningMidStage(request):
    if request.user.is_authenticated:
        examId = request.GET.get('examId')
        Obj = models.sheduledExam.objects.get(pk=examId)
        params = {"exam":Obj}
        return render(request,'examRunning.html',params)
    else:
        messages.warning(request, 'Log in first.')
        redirect('logIn')
def examRunning(request,pk):
    if request.user.is_authenticated:
        Obj = models.sheduledExam.objects.get(pk=pk)
        quesPaper = Obj.quesSet.quesSets.all()
        params = {"exam":Obj,"quesPaper":quesPaper}
        print(Obj)
        if Obj.registeredMember.filter(id=request.user.id).exists():
            if Obj.joinedMember.filter(id=request.user.id).exists():
                return render(request,'examRunning.html',params)
        return redirect(examDetails,pk)
    else:
        messages.warning(request, 'Log in first.')
        redirect('logIn')
def registerExam(request,pk):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('logIn')
    exam = models.sheduledExam.objects.get(id=pk)
    registered=int(1)
    if exam.registeredMember.filter(id=request.user.id).exists():
        registered=int(0)
        exam.registeredMember.remove(request.user)
    else:
        exam.registeredMember.add(request.user)
    params = {"exam":exam,"registered":registered}
    return redirect('examDetails',pk)

def processAnswer(request):
    if request.user.is_authenticated:
        examId = request.POST.get('examId')
        Obj = models.sheduledExam.objects.get(pk=examId)
        quesPaper = Obj.quesSet.quesSets.all()
        solution = ""
        obtainedMark = int(0)
        for i in quesPaper:
            ans = request.POST.get(str(i.pk))
            if i.ans == ans:
                obtainedMark+=1
            solution=solution+ "(" + str(i.pk)+","+ans+") "
        solution=solution[:-1]
        if models.memberExamResult.objects.filter(user=request.user,exam=Obj).exists():
            messages.warning(request,'You have already submitted. This is your previous result.')
        else:
            Obj1 = models.memberExamResult.objects.create(solution=solution,user=request.user,exam=Obj,obtainedMark=obtainedMark)
            Obj1.save()
            Obj.submittedMember.add(request.user)

        userId=request.user.id
        params = {'userId':userId,'examId':examId}
        return render(request,'examResultViewRedirect.html',params)
    else:
        return redirect('logIn')
        
        
def examResultViewRedirect(request):
    examId= request.GET.get('examId')
    userId= request.GET.get('userId')
    params = {'userId':userId,'examId':examId}
    return render(request,'examResultViewRedirect.html',params)

def examResultView(request,examId,userId):
    if request.user.is_authenticated:
        exam = models.sheduledExam.objects.get(pk=examId)
        student = User.objects.get(pk=userId)
        result = models.memberExamResult.objects.get(user=student,exam=exam)
        params = {"exam":exam,"student":student,"result":result}
        return render(request,'examResultView.html',params)

def sheduledExam(request):
    exams = models.sheduledExam.objects.all()
    params ={"exams":exams}
    return render(request,'sheduledExam.html',params)
def deleteExam(request):
    pass

def searchExam(request):
    pass

def regExam(request):
    pass


def cancelRegExam(request):
    pass