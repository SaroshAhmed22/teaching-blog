from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse
from django.views.generic import (TemplateView, DetailView,
                                    ListView, CreateView,
                                    UpdateView,DeleteView,FormView,)
from casting.models import  oberecord,Department,Semester, teacher, student , section , Slots, Slotslab, Days, course, room, timetable, freetimetable,timetablelab, freetimetablelab , projector , pro_room
from django.urls import reverse_lazy
# from .forms import CommentForm,ReplyForm, LessonForm
from django.http import HttpResponseRedirect
# email
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

from django.contrib.auth.models import User
# email

# Create your views here.

# class timetable_view(DetailView):
#     context_object_name = 'courses'
#     extra_context = {
#         # 'course': course.objects.all() ,
#         'slots': Slots.objects.all()
#     }
#     model = course
#     template_name = 'casting/timetable.html'

class tableView(TemplateView):
    template_name = 'casting/timetable.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courses = course.objects.all()
        fttc = freetimetable.objects.all()
        slotsc = Slots.objects.all()
        dayc = Days.objects.all()
        timetablec = timetable.objects.all()
        context['courses'] = courses
        context['slotsc'] = slotsc
        context['dayc'] = dayc
        context['fttc'] = fttc
        context['timetablec'] = timetablec
        return context

# obe record
class oberecord_view(TemplateView):
    # template_name = 'casting/studentresult.html
    template_name = 'casting/chartjs.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        fttc = freetimetable.objects.all()
        slotsc = course.objects.all()
        dayc = Days.objects.all()
        timetablec = oberecord.objects.all() 
        context['slotsc'] = slotsc
        context['dayc'] = dayc
        context['fttc'] = fttc
        context['timetablec'] = timetablec
        return context
    
class obechart_view(TemplateView):
    # template_name = 'casting/studentresult.html
    template_name = 'casting/chartjs.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        fttc = freetimetable.objects.all()
        slotsc = course.objects.all()
        dayc = Days.objects.all()
        timetablec = oberecord.objects.all() 
        context['slotsc'] = slotsc
        context['dayc'] = dayc
        context['fttc'] = fttc
        context['timetablec'] = timetablec
        return context
def obechart_def(request):

    dict = {'a':"a"}
    if request.method == "POST":
        roomo = request.POST.get('dpt')
        sloto = request.POST.get('slotid')
        mode = request.POST.get('dayid')

        qset = oberecord.objects.filter(dept__name__istartswith=roomo, course= sloto )
        # qset= freetimetable.objects.filter(roomo.startswith(slot_room_prefix))
        c_ob = course.objects.get(pk=sloto)
        dict ={'timetablec':qset, 'd_name':roomo, 'c_name': c_ob.name}

        # for i in range(5,200):
        #     # email = 'student' + strt(i) + '@gmail.com'
            

        #     user = 'teacher' + str(i)+ '_name'
        #     pas= 'teacher' + str(i) + '_password'
        #     email =  'teacher' + str(i) + '@gmail.com'
        #     userob = User.objects.get(pk=i)
            

        #     userob = User( username= user, password=pas , email= email)
        #     userob.save()

        return render(request, 'casting/chartjs.html' , dict)
    else:
        return render(request, 'casting/chartjs.html' , dict)
    
class labView(TemplateView):
    template_name = 'casting/lab.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courses = course.objects.all()
        fttc = freetimetablelab.objects.all()
        slotsc = Slotslab.objects.all()
        dayc = Days.objects.all()
        timetablec = timetablelab.objects.all()
        context['courses'] = courses
        context['slotsc'] = slotsc
        context['dayc'] = dayc
        context['fttc'] = fttc
        context['timetablec'] = timetablec
        return context

# class freettview(DetailView):
#     context_object_name = 'freettc'
#     model = freetimetable
#     template_name = 'casting/freett.html'

def freettview(request):

    dict = {'a':"a"}
    if request.method == "POST":
        roomo = request.POST.get('dpt')
        sloto = request.POST.get('slotid')
        dayo = request.POST.get('dayid')

        qset = freetimetable.objects.filter(slot_room__name__istartswith=roomo, slot= sloto , day=dayo)
        # qset= freetimetable.objects.filter(roomo.startswith(slot_room_prefix))
        dict ={'freettc':qset}

        # for i in range(5,200):
        #     # email = 'student' + strt(i) + '@gmail.com'
            

        #     user = 'teacher' + str(i)+ '_name'
        #     pas= 'teacher' + str(i) + '_password'
        #     email =  'teacher' + str(i) + '@gmail.com'
        #     userob = User.objects.get(pk=i)
            

        #     userob = User( username= user, password=pas , email= email)
        #     userob.save()

        return render(request, 'casting/freett.html' , dict)
    else:
        return render(request, 'casting/freettshow.html' , dict)
    
def freettlabview(request):

    dict = {'a':"a"}
    if request.method == "POST":
        roomo = request.POST.get('dpt')
        sloto = request.POST.get('slotid')
        dayo = request.POST.get('dayid')

        qset = freetimetablelab.objects.filter(slot_room__name__istartswith=roomo, slot= sloto , day=dayo)
        # qset= freetimetable.objects.filter(roomo.startswith(slot_room_prefix))
        dict ={'freettc':qset}
        return render(request, 'casting/freettlab.html' , dict)
    else:
        return render(request, 'casting/freettshow.html' , dict)

# section time table 

def sec_tt_def(request, secid, slug):
    

    sec_ttob = timetable.objects.filter(slot_section__id=1)
    
    slots = Slots.objects.all()
    contex = {'sec_ttob' : sec_ttob ,
                'slots': slots
                }
    
    return render(request, 'casting/sec_tt.html' , contex)

    

#  sectioon time table df eng

class bookview(DetailView):
    context_object_name = 'day'
    print('ok print')
    extra_context = {
        'course':  course.objects.all() ,
        'teacher': teacher.objects.all(),
        'section': section.objects.all(),
    }
    model = Days
    template_name = 'casting/book.html'

    print('ok print')
     
    
def bookviewdef(request, roomname, slottime, fttid, slug): 
    teacherq= teacher.objects.all()
    
    freeob = freetimetable.objects.get(pk=fttid)
    ttob = timetable.objects.filter(slot=freeob.slot, day=freeob.day )
    secnamelist = []
    for i in ttob:
        secnamelist.append(i.slot_section.name)

    # uniq = set(secnamelist)
    # nlist = list(uniq)
    secfilter = section.objects.exclude(name__in= secnamelist)
     
    context = {
        'busy_sec_list': secnamelist,
        'secfilter' : secfilter,
        'sectionc': section.objects.all(),
        'course': course.objects.all() ,
        'teacherc': teacherq,
        'roomid': roomname,
        'slotid': slottime,
        'dayslug': slug,
        'fttid': fttid,
        
    }

    # subject = 'Your accounts need to be verified'
    # message = f'Hi paste the link to verify your account '
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = ['smsyedmuzammil7@gmail.com'] 
    # send_mail(subject, message , email_from ,recipient_list )
    # print( 'ok mail sent')  
    print(teacherq) 
    # puting user 100
    

    print(teacher)
    
    return render (request, 'casting/book.html', context)

def booklabviewdef(request, roomname, slottime, fttid, slug): 
    teacherq= teacher.objects.all()
    
    freeob = freetimetablelab.objects.get(pk=fttid)
    ttob = timetablelab.objects.filter(slot=freeob.slot, day=freeob.day )
    busy_sec_list = []
    for i in ttob:
        busy_sec_list.append(i.slot_section.name) 

    secfilter = section.objects.exclude(name__in= busy_sec_list)
     
    context = {
        'busy_sec_list': busy_sec_list,
        'secfilter' : secfilter,
        'sectionc': section.objects.all(),
        'course': course.objects.all() ,
        'teacherc': teacherq,
        'roomid': roomname,
        'slotid': slottime,
        'dayslug': slug,
        'fttid': fttid,
        
    }  
    
    return render (request, 'casting/booklab.html', context)

def bookviewdef2(request, roomname, slottime, slug): 

    # a = room.objects.all()
    slot = Slots.objects.get(id=slottime) 
    day = Days.objects.get(id=slug)
    # print(a)
    print(slot)
    dict = {
        'aroom': "new",
         'sectiona': 'segyf', 
    }

    context = {
        # 'section': section.objects.all(),
    #     'course': course.objects.all() ,
    #     'teacher': teacher.objects.all(),

        # 'aroom': "new",
        #  'sectiona': 'segyf'
        #  'roomn': a,
        #  'slot': slot,
        #  'day': day,
        # 'roomid': roomname,
        # 'slotid': slottime,
        # 'dayid': slug,

    } 
     
    return render (request, 'casting/book.html', dict)

def bookdone(request, roomname, slottime2, ok, fttid,slug): 
    if request.method=='POST':
        sec= request.POST.get('sec')
        cou= request.POST.get('cou')
        tea= request.POST.get('tea')
        secob = section.objects.get(pk=sec)
        couob = course.objects.get(pk=cou)
        teaob = teacher.objects.get(pk=tea)
        cremail= secob.cr.email
        acremail= secob.acr.email
        ademail= secob.advisor.email 
        # check 

        context = { 
            'roomid': roomname,
            'slotid': slottime2,
            'dayid': slug,
            'couname': couob,
            'secname': secob,
            'teaname': teaob,
            'cremail': cremail,
            'acremail': acremail,
            'ademail': ademail,
            # 'secid': sec,
            # 'couid': cou,
            # 'teaid':tea,
            'fttid': fttid
        } 
        # email sending
        # secc= section.objects.get(pk=sec)
        # cremail= secc.cremail



# email ending
         
        freettobj = freetimetable.objects.get(pk=fttid)

        ttobj= timetable(day=freettobj.day, slot=freettobj.slot, slot_subject=couob, slot_section=secob, slot_room=freettobj.slot_room  )
        # ttobj.save()
         


        if freettobj is not None:
            # freettobj.delete()
            print('freet obj got successed')
        else:
            print('freet obj Not got')
        
        subject = 'Your accounts need to be verified'
        message = f'Hi paste the link to verify your account '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [cremail,acremail,ademail,'smsyedmuzammil7@gmail.com'] 
        # send_mail(subject, message , email_from ,recipient_list )
        # print( 'ok mail sent')


        return render (request, 'casting/bookdone.html', context)
    else:
        return render (request, 'casting/bookdone.html', )
    

def booklabdone(request, roomname, slottime2, ok, fttid,slug): 
    if request.method=='POST':
        sec= request.POST.get('sec')
        cou= request.POST.get('cou')
        tea= request.POST.get('tea')
        secob = section.objects.get(pk=sec)
        couob = course.objects.get(pk=cou)
        teaob = teacher.objects.get(pk=tea)
        cremail= secob.cr.email
        acremail= secob.acr.email
        ademail= secob.advisor.email 
        # check 
        print (sec)

        context = { 
            'roomid': roomname,
            'slotid': slottime2,
            'dayid': slug,
            'couname': couob,
            'secname': secob,
            'teaname': teaob,
            'cremail': cremail,
            'acremail': acremail,
            'ademail': ademail, 
            'fttid': fttid
        }  
         
        freettobj = freetimetablelab.objects.get(pk=fttid)

        ttobj= timetablelab(day=freettobj.day, slot=freettobj.slot, slot_subject=couob, slot_section=secob, slot_room=freettobj.slot_room  )
        # ttobj.save()
         


        if freettobj is not None:
            # freettobj.delete()
            print('freet obj got successed')
        else:
            print('freet obj Not got') 


        return render (request, 'casting/booklabdone.html', context)
    else:
        return render (request, 'casting/bookdone.html', )

roomobaps = None

def successbookdone(request): 
    if request.method=='POST':
        b1= request.POST.get('adv')
        b2= request.POST.get('cr')
        b3= request.POST.get('acr')
        fttid= request.POST.get('fttid')
        couid= request.POST.get('couid')
        secid= request.POST.get('secid')
        teaid= request.POST.get('teaid')
        print(secid)
        print(couid)
        print(teaid)
        print(fttid)
        secob = section.objects.get(pk=secid)
        couob = course.objects.get(pk=couid)
        teaob = teacher.objects.get(pk=teaid)
        freettobj = freetimetable.objects.get(pk=fttid)
         
        ademail = None
        cremail = secob.cr.email
        print (cremail)
        acremail = None
        if b1:
            ademail= secob.advisor.email
        if b2:
            cremail= secob.advisor.email
        if b3:
            acremail= secob.advisor.email 
        if b1 or b2 or b3:
        # sending email notification
            subject = 'Class Arranged Notification Section ' + secob.name
            message = f'Dear Respected Person, \n \t You notify that an activity arranged regard Class of your section  ' +secob.name +' on ' +freettobj.day.day+ ' '+ str(freettobj.slot.start_time) +' '+ str(freettobj.slot.end_time) +  ' at Room ' +freettobj.slot_room.name+' and it will be teach or undervision by;  Teacher Sir.'+ teaob.user.username + ' for more detail you can contact/email to him  ' + teaob.email +'\n \t Thank you.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [cremail,acremail,ademail,'smsyedmuzammil7@gmail.com'] 
            print('mail sent ok')
            # send_mail(subject, message , email_from ,recipient_list )
            print( 'ok mail sent')

        if freettobj is not None: 
            ttobj= timetable(day=freettobj.day, slot=freettobj.slot, slot_subject=couob, slot_section=secob, slot_room=freettobj.slot_room  )
            # ttobj.save()
            # freettobj.delete()
            roomob = room.objects.get(pk=freettobj.slot_room.id)
            roomobaps = roomob
            roomob.twc += 1
            print(roomob.twc)
            roomob.save()
            
            
            proroomob = pro_room.objects.get(roomid=freettobj.slot_room)
            
            projob = projector.objects.get(pk=proroomob.proid.id)
            projob.twc += 1
            print(projob.twc)
            projob.save()
             

        messages.success(request, ' Allocated Class Successfully! also notified to related persons')
        return redirect('/casting/')
    else:
        pass


def successbookdonelab(request): 
    if request.method=='POST':
        b1= request.POST.get('adv')
        b2= request.POST.get('cr')
        b3= request.POST.get('acr')
        fttid= request.POST.get('fttid')
        couid= request.POST.get('couid')
        secid= request.POST.get('secid')
        teaid= request.POST.get('teaid')
        print(secid)
        print(couid)
        print(teaid)
        print(fttid)
        secob = section.objects.get(pk=secid)
        couob = course.objects.get(pk=couid)
        teaob = teacher.objects.get(pk=teaid)
        freettobj = freetimetablelab.objects.get(pk=fttid)
        if freettobj is not None: 
            ttobj= timetablelab(day=freettobj.day, slot=freettobj.slot, slot_subject=couob, slot_section=secob, slot_room=freettobj.slot_room  )
            # ttobj.save()
            # freettobj.delete()
            roomob = room.objects.get(pk=freettobj.slot_room.id)
            roomobaps = roomob
            roomob.twc += 1
            print(roomob.twc)
            roomob.save()
            
        ademail = None 
        cremail = None
        acremail = None
        if b1:
            ademail= secob.advisor.email
        if b2:
            cremail= secob.cr.email
        if b3:
            acremail= secob.acr.email 
        if b1 or b2 or b3:
        # sending email notification
            subject = 'Lab Arranged Notification Section ' + secob.name
            message = f'Dear Respected Person, \n \t You notify that an activity arranged regard Lab of your section  ' +secob.name +' on ' +freettobj.day.day+ ' '+ str(freettobj.slot.start_time) +' '+ str(freettobj.slot.end_time) +  ' at Room ' +freettobj.slot_room.name+' and it will be teach or undervision by;  Teacher Sir.'+ teaob.user.username + ' for more detail you can contact/email to him  ' + teaob.email+'\n \t Thank you.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [cremail,acremail,ademail,'smsyedmuzammil7@gmail.com']  
            send_mail(subject, message , email_from ,recipient_list )
            print( 'ok mail sent')

        messages.success(request, ' Allocated Lab Successfully! also notified to related persons ')
        return redirect('/casting/lab/')
    else:
        pass
    
    
from datetime import datetime
from pytz import utc

def FirstCronTest():
	
	print("I am 7 second executed..!")
 

def secondCronTest():
    
    # roomob = room.objects.get(pk=freettobj.slot_room.id)
    # roomobaps.twc += 1
    # print(roomobaps.twc)
    # roomobaps.save()
    projob = projector.objects.all()
    for i in projob:
        twcf = i.twc
        i.t_run = i.t_run + ((twcf/7)*2) 
        if i.t_run > (i.capacity - 5 ):
            if i.t_run < i.capacity:
                
                subject = 'Ended projector'   
                message = f'Dear Respected Person, \n \t lense time is over kindly change your  projector lense ' + str(i.id) + 'name is' + i.name
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['smsyedmuzammil7@gmail.com', 'syedqandeel7@gmail.com','hamza199jawaid@gmail.com','saroshahmed622@gmail.com']  
                send_mail(subject, message , email_from ,recipient_list )
                print( 'ok mail sent')
                print('lense time is over kindly change lense your projector')
                
            else: 
                
                subject = 'warning projector '  
                message = f'Dear Respected Person, \n \t warning alert only remaining less than 5 hour lense time only 2 or 3 classes may be conduct \n\t detail: id' + str(i.id) + 'name is' + i.name
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['smsyedmuzammil7@gmail.com', 'syedqandeel7@gmail.com','hamza199jawaid@gmail.com','saroshahmed622@gmail.com']  
                send_mail(subject, message , email_from ,recipient_list ) 
                print ("warning alert only remaining less than 5 hour lense time only 2 or 3 classes may be conduct")
        i.save()
        
    print("I am 7 second executed..!")
    


# proj start
class projView(ListView): 
    context_object_name = 'projectors'
    model = projector 
    template_name = 'casting/projector.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs) 
    #     projob = projector.objects.get(pk=1)
    #     context['tr'] = projob.t_run
    #     context['cp'] = projob.capacity - projob.t_run  
    #     return context
    