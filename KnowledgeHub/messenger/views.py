from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.models import User
from itertools import chain
from datetime import *


def conversation(request,val):
    print(val,"ooo")
    recieverId,page= val.split('+')
    reciever=User.objects.get(pk=int(recieverId))
    msgSent = models.msg.objects.filter(sender=request.user,reciever=reciever)
    msgRecieved = models.msg.objects.filter(reciever=request.user,sender=reciever)
    msg = list(chain(msgRecieved,msgSent))
    msg.sort(key=lambda s: s.date)
    msg.reverse()
    mx=int(page)*10-1+10
    mx=min(mx,len(msg)-1)
    mn = max(mx-9,0)
    selectedMsg = msg[mn:mx+1]
    selectedMsg.reverse()
    params = {'msg':selectedMsg,'recieverId':recieverId}
    return render(request,'conversation.html',params)

def msgSend(request):
    message=request.POST.get('message')
    recieverId = request.POST.get('recieverId')
    print(message,recieverId)
    sender = request.user
    reciever=User.objects.get(pk=recieverId)
    msg = models.msg.objects.create(sender=sender,reciever=reciever,message=message)
    msg.save()
    val=str(recieverId)+str('+')+str(0)
    print(val,"uff")
    return redirect(conversation,val)

