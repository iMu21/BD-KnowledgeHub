from django.contrib import admin
from .models import sheduledExam,quesSetDetail,subjectNames,topicNames,mcqQuestion, memberExamResult

admin.site.register(subjectNames)
admin.site.register(topicNames)
admin.site.register(mcqQuestion)
admin.site.register(quesSetDetail)
admin.site.register(sheduledExam)
admin.site.register(memberExamResult)
