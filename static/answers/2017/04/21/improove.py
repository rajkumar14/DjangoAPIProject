def latest_masterdataupdated(request):
    Masterdata = []
    MediaContent = []
    if request.method == "GET":
        deviceid = request.GET.get('deviceId')
        pdate = convert_string_to_date(request.GET.get('modified_date'))
        mdate = convert_string_to_date(request.GET.get('lastUpdateMediaContent'))
        device = ''
        try:
            device = Device.objects.get(deviceid=deviceid)
        except:
            pass
        if device:
            if device.license():
                if device.license().configuration:
                    subjects = device.license().configuration.subjects.all()
#                    cursor = connection.cursor()
#                    cles = "update curriculum_lesson set modified_on=now() where active=0;"
#                    clestopic = "update curriculum_lessontopic set modified_on=now() where active=0;"
#                    clesmedia = "update Data_media set modified_on=now() where active=0;"
#                    cursor.execute(cles)
#                    cursor.execute(clestopic)
#                    cursor.execute(clesmedia)
#                    cursor.close()
                    lessons = list(set([(j) for i in subjects for j in i.lessons()]))
                    lesson_topics = list(set([j.id for i in lessons if i.lesson_topics().filter(Q(lesson__created_on__gt=pdate)|Q(lesson__modified_on__gt=pdate)|Q(topic__created_on__gt=pdate)|Q(topic__modified_on__gt=pdate)) for j in i.lesson_topics().filter(Q(lesson__created_on__gt=pdate)|Q(lesson__modified_on__gt=pdate)|Q(topic__created_on__gt=pdate)|Q(topic__modified_on__gt=pdate))]))
                    lesson_topics = LessonTopic.objects.filter(id__in=lesson_topics).order_by('modified_on')
                    lessonss = list(set([k.id for k in lessons]))

                    if pdate:
                        Masterdata = [{'_id':lp.id, 'insertTime':lp.topic.created_on.strftime('%Y-%m-%d %H:%M:%S.%f'), 'curriculumType':lp.lesson.subject.standard.curriculum.id, 'curName':lp.lesson.subject.standard.curriculum.name, 'grade':lp.lesson.subject.standard.grade.id, 'gradeName':lp.lesson.subject.standard.grade.name, 'class':lp.lesson.subject.standard.id, 'className':lp.lesson.subject.standard.name, 'subject':lp.lesson.subject.id, 'subjectName':lp.lesson.subject.name, 'lesson':lp.lesson.id, 'lessonName':lp.lesson.name.encode('utf-8'), 'topic':lp.topic.id, 'topicName':lp.topic.name.encode('utf-8'), 'ordering':lp.order, 'languageId':lp.lesson.subject.standard.medium.id, 'languageName':lp.lesson.subject.standard.medium.name, 'active':1 if lp.active else 0, 'modified':lp.topic.modified_on.strftime('%Y-%m-%d %H:%M:%S.%f') if lp.topic.modified_on.strftime('%Y-%m-%d %H:%M:%S.%f') > lp.lesson.modified_on.strftime('%Y-%m-%d %H:%M:%S.%f') else lp.lesson.modified_on.strftime('%Y-%m-%d %H:%M:%S.%f'),'evaluationType':3} for lp in lesson_topics]
#                        lessonss = list(set([k.id for k in lessons]))
#                        lens = Lesson.objects.filter(id__in = lessonss)
#                        for les in lens.filter(Q(created_on__gt=pdate)|Q(modified_on__gt=pdate)):
#                            if len(les.topics()) == 0:
#                                les_dict = {'_id':les.id, 'insertTime':les.created_on.strftime('%Y-%m-%d %H:%M:%S.%f'), 'curriculumType':les.subject.standard.curriculum.id, 'curName':les.subject.standard.curriculum.name, 'grade':les.subject.standard.grade.id, 'gradeName':les.subject.standard.grade.name, 'class':les.subject.standard.id, 'className':les.subject.standard.name.encode('utf-8'), 'subject':les.subject.id, 'subjectName':les.subject.name.encode('utf-8'), 'lesson':les.id, 'lessonName':les.name.encode('utf-8'), 'topic':'', 'topicName':'', 'ordering':'', 'languageId':les.subject.standard.medium.id, 'languageName':les.subject.standard.medium.name.encode('utf-8'), 'active':1 if les.active else 0, 'modified':les.modified_on.strftime('%Y-%m-%d %H:%M:%S.%f'),'evaluationType':3}
#                                Masterdata.append(les_dict)
                    if mdate:
                        medias = Media.objects.filter(content_type__model='lesson')
                        topic_medias2 = TopicMedia.objects.filter(media__media_type='1', media__modified_on__gt=mdate)
                        topic_medias2 = list(set([i.id for i in topic_medias2]))
#                        lesonids = list(set([l.id for l in lessons ]))
                        medias = medias.filter(object_id__in=lessonss)
                        topic_medias1 = TopicMedia.objects.filter(Q(media__created_on__gt=mdate)|Q(media__modified_on__gt=mdate))
                        topic_medias1 = list(set([i.id for i in topic_medias1 if i.topic.lessons() for j in i.topic.lessons() if j in lessons]))
                        topic_medias = list(set([m.object_id for m in medias]))
                        if topic_medias1:
                            topic_medias.extend(topic_medias1)
                        if topic_medias2:
                            topic_medias.extend(topic_medias2)
                        topic_medias = TopicMedia.objects.filter(id__in=list(set(topic_medias)))
                        topic_medias = topic_medias.filter(Q(media__created_on__gt=mdate)|Q(media__modified_on__gt=mdate))
                        MediaContent = [{'_id':tm.topic.id, 'parentId':tm.topic.id, 'contentType':tm.media.media_type, 'mediaId':tm.media.id, 'path':tm.media.media_file.encode('utf-8'), 'parrentType':6, 'active':1 if tm.media.active else 0,'modified':tm.media.modified_on.strftime('%Y-%m-%d %H:%M:%S.%f')} for tm in topic_medias]
                    response = {'status':1,'masterTable':Masterdata,'mediaContent':MediaContent}
                else:
                    response = {"status":0, "message":"Configuration not found"}
            else:
                response = {"status":0, "message":"Not a valid licence"}
        else:
            response = {"status":0, "message":"Device Not registered"}
    else:
        response = {'status':0,'message':"please check parameters"}
    return JsonResponse(response)

OLD function:

@csrf_exempt
def latest_masterdataupdated(request):
    Masterdata = []
    MediaContent = []
    if request.method == "GET":
        deviceid = request.GET.get('deviceId')
        pdate = convert_string_to_date(request.GET.get('modified_date'))
        mdate = convert_string_to_date(request.GET.get('lastUpdateMediaContent'))
        device = ''
        try:
            device = Device.objects.get(deviceid=deviceid)
        except:
            pass
        if device:
            if device.license():
                if device.license().configuration:
                    subjects = device.license().configuration.subjects.all()
#                    cursor = connection.cursor()
#                    cles = "update curriculum_lesson set modified_on=now() where active=0;"
#                    clestopic = "update curriculum_lessontopic set modified_on=now() where active=0;"
#                    clesmedia = "update Data_media set modified_on=now() where active=0;"
#                    cursor.execute(cles)
#                    cursor.execute(clestopic)
#                    cursor.execute(clesmedia)
#                    cursor.close()
                    lessons = list(set([(j) for i in subjects for j in i.lessons()]))
                    lesson_topics = list(set([j.id for i in lessons if i.lesson_topics().filter(Q(lesson__created_on__gt=pdate)|Q(lesson__modified_on__gt=pdate)|Q(topic__created_on__gt=pdate)|Q(topic__modified_on__gt=pdate)) for j in i.lesson_topics().filter(Q(lesson__created_on__gt=pdate)|Q(lesson__modified_on__gt=pdate)|Q(topic__created_on__gt=pdate)|Q(topic__modified_on__gt=pdate))]))
                    lesson_topics = LessonTopic.objects.filter(id__in=lesson_topics).order_by('modified_on')

                    if pdate:
                        for lp in lesson_topics:
                            media_dict = {'_id':lp.id, 'insertTime':lp.topic.created_on.strftime('%Y-%m-%d %H:%M:%S.%f'), 'curriculumType':lp.lesson.subject.standard.curriculum.id, 'curName':lp.lesson.subject.standard.curriculum.name, 'grade':lp.lesson.subject.standard.grade.id, 'gradeName':lp.lesson.subject.standard.grade.name, 'class':lp.lesson.subject.standard.id, 'className':lp.lesson.subject.standard.name, 'subject':lp.lesson.subject.id, 'subjectName':lp.lesson.subject.name, 'lesson':lp.lesson.id, 'lessonName':lp.lesson.name.encode('utf-8'), 'topic':lp.topic.id, 'topicName':lp.topic.name.encode('utf-8'), 'ordering':lp.order, 'languageId':lp.lesson.subject.standard.medium.id, 'languageName':lp.lesson.subject.standard.medium.name, 'active':1 if lp.active else 0, 'modified':lp.topic.modified_on.strftime('%Y-%m-%d %H:%M:%S.%f') if lp.topic.modified_on.strftime('%Y-%m-%d %H:%M:%S.%f') > lp.lesson.modified_on.strftime('%Y-%m-%d %H:%M:%S.%f') else lp.lesson.modified_on.strftime('%Y-%m-%d %H:%M:%S.%f'),'evaluationType':3}
                            Masterdata.append(media_dict)
                        lessonss = list(set([k.id for k in lessons]))
                        lens = Lesson.objects.filter(id__in = lessonss)
                        for les in lens.filter(Q(created_on__gt=pdate)|Q(modified_on__gt=pdate)):
                            if len(les.topics()) == 0:
                                les_dict = {'_id':les.id, 'insertTime':les.created_on.strftime('%Y-%m-%d %H:%M:%S.%f'), 'curriculumType':les.subject.standard.curriculum.id, 'curName':les.subject.standard.curriculum.name, 'grade':les.subject.standard.grade.id, 'gradeName':les.subject.standard.grade.name, 'class':les.subject.standard.id, 'className':les.subject.standard.name.encode('utf-8'), 'subject':les.subject.id, 'subjectName':les.subject.name.encode('utf-8'), 'lesson':les.id, 'lessonName':les.name.encode('utf-8'), 'topic':'', 'topicName':'', 'ordering':'', 'languageId':les.subject.standard.medium.id, 'languageName':les.subject.standard.medium.name.encode('utf-8'), 'active':1 if les.active else 0, 'modified':les.modified_on.strftime('%Y-%m-%d %H:%M:%S.%f'),'evaluationType':3}
                                Masterdata.append(les_dict)
                    if mdate:
                        medias = Media.objects.filter(content_type__model='lesson')
                        topic_medias2 = TopicMedia.objects.filter(media__media_type='1', media__modified_on__gt=mdate)
                        topic_medias2 = list(set([i.id for i in topic_medias2]))
                        lesonids = list(set([l.id for l in lessons ]))
                        medias = medias.filter(object_id__in=lesonids)
                        topic_medias1 = TopicMedia.objects.filter(Q(media__created_on__gt=mdate)|Q(media__modified_on__gt=mdate))
                        topic_medias1 = list(set([i.id for i in topic_medias1 if i.topic.lessons() for j in i.topic.lessons() if j in lessons]))
                        topic_medias = list(set([m.object_id for m in medias]))
                        if topic_medias1:
                            topic_medias.extend(topic_medias1)
                        if topic_medias2:
                            topic_medias.extend(topic_medias2)
                        topic_medias = TopicMedia.objects.filter(id__in=list(set(topic_medias)))
                        topic_medias = topic_medias.filter(Q(media__created_on__gt=mdate)|Q(media__modified_on__gt=mdate))
                        for tm in topic_medias:
                            top_dict = {'_id':tm.topic.id, 'parentId':tm.topic.id, 'contentType':tm.media.media_type, 'mediaId':tm.media.id, 'path':tm.media.media_file.encode('utf-8'), 'parrentType':6, 'active':1 if tm.media.active else 0,'modified':tm.media.modified_on.strftime('%Y-%m-%d %H:%M:%S.%f')}
                            MediaContent.append(top_dict)
                    response = {'status':1,'masterTable':Masterdata,'mediaContent':MediaContent}
                else:
                    response = {"status":0, "message":"Configuration not found"}
            else:
                response = {"status":0, "message":"Not a valid licence"}
        else:
            response = {"status":0, "message":"Device Not registered"}
    else:
        response = {'status':0,'message':"please check parameters"}
    return JsonResponse(response)


