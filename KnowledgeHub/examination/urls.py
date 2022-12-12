from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from . import views

urlpatterns = [
     path('createQuesPaper',views.createQuesPaper,name='createQuesPaper'),
     path('createQuesPaperReq',views.createQuesPaperReq,name='createQuesPaperReq'),
     path('setQues/updateIndividualQues',views.updateIndividualQues,name='updateIndividualQues'),
     path('setQuesMidStage',views.setQuesMidStage,name='setQuesMidStage'),
     path('setQues/<int:examId>', views.setQues, name='setQues'),
     path('questionPaper/<int:examId>', views.questionPaper, name='questionPaper'),
     path('quesPaperList', views.quesPaperList, name='quesPaperList'),
     path('quesList', views.quesList, name='quesList'),
     path('createExam',views.createExam,name='createExam'),
     path('createExamReq',views.createExamReq,name='createExamReq'),
     path('createExamMidStage',views.createExamMidStage,name='createExamMidStage'),
     path('examDetails/<int:examId>',views.examDetails,name='examDetails'),
     path('registerExam/<int:pk>',views.registerExam,name='registerExam'),
     path('joinExam',views.joinExam,name='joinExam'),
     path('examRunning/<int:pk>',views.examRunning,name="examRunning"),
     path('examRunning/processAnswer',views.processAnswer,name='processAnswer'),
     path('examResultView/<int:examId>/<int:userId>',views.examResultView,name='examResultView'),
     path('exam/examResultViewRedirect',views.examResultViewRedirect,name='examResultViewRedirect'),
     path('sheduledExam',views.sheduledExam,name='sheduledExam'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)