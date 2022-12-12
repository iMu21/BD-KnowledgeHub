from django.contrib import admin
from .models import memberBasic,memberInstitution,memberPhoneNumber,memberWorking,pendingAccount,memberWebsite, websiteType

admin.site.register(memberBasic)
admin.site.register(memberInstitution)
admin.site.register(memberPhoneNumber)
admin.site.register(memberWorking) 
admin.site.register(pendingAccount)
admin.site.register(memberWebsite)
admin.site.register(websiteType)