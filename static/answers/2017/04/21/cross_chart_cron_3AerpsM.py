from datetime import datetime
from django.core.management.base import BaseCommand
from django.core.mail import send_mail,EmailMessage
from MahitiPMS.settings import BASE_DIR, EMAIL_HOST_USER
from Intervals.cross_chart import *
from Intervals.views import yesterday_pendingtask_report
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import date,timedelta
    




class Command(BaseCommand):
    print "hai"
    
    help = 'Runs crone for generating the Cross Chart of Developer Achieved Credits on Projects'
    
    @staticmethod
    def handle(*args, **options):
            last_seven_days()
            #text_content = yesterday_pendingtask_report()
	    current_month()
            tasks_report()
            csvfile = BASE_DIR+file_name
            tod = datetime.today()
            sub = 'Task Report for the day : ' + tod.strftime('%d-%B-%Y')
            d = {}
	    d1 = {}
	    dd = date.today()
	    dd1 = dd-timedelta(days =1)
	    obj = User.objects.filter(is_active = True,is_staff=True)
	    for i in obj:
		try:
		    obj1 = Task.objects.filter(st_date = dd1,created__id = i.id)
		    if not obj1:
		        objn = Project.objects.filter(user__id = i.id)
		        proj_list = []
		        for k in objn:
		            kk = smart_str(k.name)
		            proj_list.append(kk)
		        st = ''
		        for ss in proj_list:
		            st = st+str(ss)+','
		        d1[i.username] = st
		except:
		    pass
	    ddm = dd.replace(day=1)
	    dd1 = dd-timedelta(days =1)
	    obj = User.objects.all()
	    for i in obj:
		kk = i.username
		total_tasks = Task.objects.filter(st_date = dd1,user__id = i.id).count()
		try:
		    inreview_tasks = Task.objects.filter(st_date = dd1,status__label= "In Review",user__id = i.id).count()
		    pending_tasks = Task.objects.filter(st_date = dd1,status__label= "Open",user__id = i.id).count()
		    d[kk] = {}
		    d[kk]['task_yesterday'] = total_tasks
		    d[kk]['In review'] = inreview_tasks
		    d[kk]['Open'] = pending_tasks
		    overdue_tasks = Task.objects.filter(st_date__range = [ddm,dd],user__id = i.id,status__label= "Open").count()
		    d[kk]['Overdue_tasks'] = overdue_tasks
		    if not total_tasks:
		       del  d[kk] 
		except:
		    pass    
	    st = ''
	    for ky in d.keys():
		st = st+str(ky)+','
            msg1 = "hi"            
            html_content = render_to_string('sendtable_template.html', {'msg1':msg1,'d11':d1,'lst_usrs':st,'dates':dd1}) 
            text_content = strip_tags(html_content)
            body = text_content
	    print body
            email = EmailMultiAlternatives(sub, body, EMAIL_HOST_USER, \
                                    user_mail_list, \
                                )
            email.attach_alternative(html_content, "text/html")
            attachment = open(csvfile, 'rb')
            email.attach(email_file_name,attachment.read(),'application/csv')
            email.send()
            
            print ('success')
  
