from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User  
import os

#  user info

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Semester(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)

class teacher(models.Model):

    #creating a relationship with user class (not inheriting)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #adding additional attributes
    bio = models.CharField(max_length=500)
    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Picture", blank=True)
    cell= models.IntegerField(max_length=15)
    email= models.EmailField(max_length=50)
    Engineering = 'Engineering'
    None_Engineering = 'None_Engineering' 
    teacher_types = [
        (Engineering, 'Engineering'),
        (None_Engineering, 'None_Engineering'), 
    ]
    teacher_type = models.CharField(max_length=100, choices=teacher_types, default=Engineering)

    def __str__(self):
        return self.user.username

class student(models.Model):

    #creating a relationship with user class (not inheriting)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #adding additional attributes
    bio = models.CharField(max_length=500)
    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Picture", blank=True)
    cell= models.IntegerField(max_length=15)
    email= models.EmailField(max_length=50)
    student_types = [ 
        ('student','student'),
        ('cr', 'cr'),
        ('acr', 'acr'),
    ]
    
    student_type = models.CharField(max_length=10, choices=student_types, default='student')
    def __str__(self):
        return self.user.username
   
class room(models.Model):
 
    name = models.CharField(max_length=100, unique=True )
    slug = models.SlugField(null=True, blank=True)
    capacity= models.IntegerField(max_length=200, default=45)
    twc= models.IntegerField( null=True ,max_length=200, default=45)
    pcs= models.IntegerField(max_length=200, default=2)
    # no_of_classes= models.IntegerField(max_length=200)
    projector = models.BooleanField(default=True)
    ac = models.BooleanField(default=True) 

    room_types = [ 
        ('lab','lab'),
        ('class', 'class'),
        ('meeting', 'meeting'),
    ]
    
    room_type = models.CharField(max_length=10, choices=room_types, default='class')
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
   
 
     
    
 

# forecasting 

# Create your models here.
class section(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='rn_sec_dept', default=None , null=True )
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=500,blank=True)
    cr = models.OneToOneField(student, on_delete=models.CASCADE , related_name='rncr')
    acr = models.OneToOneField(student, on_delete=models.CASCADE , related_name='rnacr')
    advisor = models.OneToOneField(teacher, on_delete=models.CASCADE , related_name='rntr')
    capacity =  models.IntegerField(max_length=15, default=40)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
def save_course_image(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.subject_id:
        filename = 'Subject_Pictures/{}.{}'.format(instance.subject_id, ext)
    return os.path.join(upload_to, filename)

class course(models.Model):
    # dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='rn_cou_dept', default=None , null=True )
    # sem = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='rn_cou_sem', default=None, null=True )
    course_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to=save_course_image, blank=True, verbose_name='Subject Image')
    description = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class sec_course(models.Model):
    secid = models.ForeignKey(section, on_delete=models.CASCADE, related_name= 'sec_cou')
    couid = models.ForeignKey(course, on_delete=models.CASCADE, related_name= 'cou_sec')
    slug = models.SlugField(null=True, blank=True)
    

     
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super().save(*args, **kwargs)



class Days(models.Model):
    # standard = models.ForeignKey(Standard, on_delete=models.CASCADE,related_name='standard_days')
    slug = models.SlugField(null=True, blank=True)
    day = models.CharField(max_length=100)
    def __str__(self):
        return self.day
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.day)
        super().save(*args, **kwargs)

class Slots(models.Model):
    # standard = models.ForeignKey(Standard, on_delete=models.CASCADE,related_name='standard_time_slots')
    slug = models.SlugField(null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.start_time) + ' - ' + str(self.end_time) 
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super().save(*args, **kwargs)

class Slotslab(models.Model):
    # standard = models.ForeignKey(Standard, on_delete=models.CASCADE,related_name='standard_time_slots')
    slug = models.SlugField(null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.start_time) + ' - ' + str(self.end_time) 
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super().save(*args, **kwargs)
    
class timetable(models.Model):
    #  stack over flow se copied for composite pk
    # class MyTable(models.Model):
    # class Meta:
    #     unique_together = (('key1', 'key2'),)

    # key1 = models.IntegerField(primary_key=True)
    # key2 = models.IntegerField()

    #  stack over flow se copied for composite pk
    # standard = models.ForeignKey(Standard, on_delete=models.CASCADE,related_name='standard_slots')
    day = models.ForeignKey(Days, on_delete=models.CASCADE,related_name='rn_tt_days')
    slot = models.ForeignKey(Slots, on_delete=models.CASCADE,related_name='rn_tt_slots')
    slot_subject = models.ForeignKey(course, on_delete=models.CASCADE,related_name='rn_tt_course')
    slot_section = models.ForeignKey(section, on_delete=models.CASCADE,related_name='rn_tt_section')
    
    slot_room = models.ForeignKey(room, on_delete=models.CASCADE,related_name='rn_tt_room')

    def __str__(self):
        return str(self.slot_room)+ ' - ' + str(self.day) + ' - ' + str(self.slot) + ' - ' + str(self.slot_subject)


class timetablelab(models.Model):
    day = models.ForeignKey(Days, on_delete=models.CASCADE,related_name='rn_ttl_days')
    slot = models.ForeignKey(Slotslab, on_delete=models.CASCADE,related_name='rn_ttl_slots')
    slot_subject = models.ForeignKey(course, on_delete=models.CASCADE,related_name='rn_ttl_course')
    slot_section = models.ForeignKey(section, on_delete=models.CASCADE,related_name='rn_ttl_section')
    
    slot_room = models.ForeignKey(room, on_delete=models.CASCADE,related_name='rn_ttl_room')

    def __str__(self):
        return str(self.slot_room)+ ' - ' + str(self.day) + ' - ' + str(self.slot) + ' - ' + str(self.slot_subject)

class oberecord(models.Model):
    slug = models.SlugField(null=True, blank=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='obe_dept')
    course = models.ForeignKey(course, on_delete=models.CASCADE, related_name='obe_cou')
    year = models.CharField(null=False, blank=False, max_length=40)
    enrolled = models.IntegerField( default=100)
    
    clo1 = models.IntegerField(default=100)
    clo2 = models.IntegerField( default=100)
    clo3 = models.IntegerField( default=100)
    clo4 = models.IntegerField( default=100)
    cloall = models.IntegerField( default=100)
    
    passed = models.IntegerField(default=100)
    failed = models.IntegerField( default=100)
    
    def __str__(self):
        return str(self.dept)+ ' - ' + str(self.course) + ' - ' + str(self.year)  
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.dept)
        super().save(*args, **kwargs)

class freetimetable(models.Model):
    # standard = models.ForeignKey(Standard, on_delete=models.CASCADE,related_name='standard_slots')
    slug = models.SlugField(null=True, blank=True)
    day = models.ForeignKey(Days, on_delete=models.CASCADE,related_name='rn_ft_days')
    slot = models.ForeignKey(Slots, on_delete=models.CASCADE,related_name='rn_ft_slots')
    slot_room = models.ForeignKey(room, on_delete=models.CASCADE,related_name='rn_ft_room')

    def __str__(self):
        return str(self.slot_room)+ ' - ' + str(self.day) + ' - ' + str(self.slot)  
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.day)
        super().save(*args, **kwargs)

class freetimetablelab(models.Model):
    # standard = models.ForeignKey(Standard, on_delete=models.CASCADE,related_name='standard_slots')
    slug = models.SlugField(null=True, blank=True)
    day = models.ForeignKey(Days, on_delete=models.CASCADE,related_name='rn_ftl_days')
    slot = models.ForeignKey(Slotslab, on_delete=models.CASCADE,related_name='rn_ftl_slots')
    slot_room = models.ForeignKey(room, on_delete=models.CASCADE,related_name='rn_ftl_room')

    def __str__(self):
        return str(self.slot_room)+ ' - ' + str(self.day) + ' - ' + str(self.slot)  
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.day)
        super().save(*args, **kwargs)

class projector(models.Model):
    # dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='rn_cou_dept', default=None , null=True )
    # sem = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='rn_cou_sem', default=None, null=True )
    pror_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    # # image = models.ImageField(upload_to=save_course_image, blank=True, verbose_name='Subject Image')
    is_active = models.BooleanField(null=True, blank=True)
    capacity = models.IntegerField(max_length=40) 
    
    twc= models.IntegerField( null=True ,max_length=200, default=1)
    t_run  = models.FloatField(max_length=40)

    description = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.t_run = round(self.t_run, 2)
        super().save(*args, **kwargs)
    
class pro_room(models.Model):
    roomid = models.ForeignKey(room, on_delete=models.CASCADE, related_name= 'room_pro')
    proid = models.ForeignKey(projector, on_delete=models.CASCADE, related_name= 'pro_room')
    slug = models.SlugField(null=True, blank=True)

        
# def save_subject_image(instance, filename):
#     upload_to = 'Images/'
#     ext = filename.split('.')[-1]
#     # get filename
#     if instance.subject_id:
#         filename = 'Subject_Pictures/{}.{}'.format(instance.subject_id, ext)
#     return os.path.join(upload_to, filename)

# class Subject(models.Model):
#     subject_id = models.CharField(max_length=100, unique=True)
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(null=True, blank=True)
#     standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='subjects')
#     image = models.ImageField(upload_to=save_subject_image, blank=True, verbose_name='Subject Image')
#     description = models.TextField(max_length=500,blank=True)

#     def __str__(self):
#         return self.name

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.subject_id)
#         super().save(*args, **kwargs)


# def save_lesson_files(instance, filename):
#     upload_to = 'Images/'
#     ext = filename.split('.')[-1]
#     # get filename
#     if instance.lesson_id:
#         filename = 'lesson_files/{}/{}.{}'.format(instance.lesson_id,instance.lesson_id, ext)
#         if os.path.exists(filename):
#             new_name = str(instance.lesson_id) + str('1')
#             filename =  'lesson_images/{}/{}.{}'.format(instance.lesson_id,new_name, ext)
#     return os.path.join(upload_to, filename)

# class Lesson(models.Model):
#     lesson_id = models.CharField(max_length=100, unique=True)
#     Standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
#     created_by = models.ForeignKey(User,on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE,related_name='lessons')
#     name = models.CharField(max_length=250)
#     position = models.PositiveSmallIntegerField(verbose_name="Chapter no.")
#     slug = models.SlugField(null=True, blank=True)
#     video = models.FileField(upload_to=save_lesson_files,verbose_name="Video", blank=True, null=True)
#     ppt = models.FileField(upload_to=save_lesson_files,verbose_name="Presentations", blank=True)
#     Notes = models.FileField(upload_to=save_lesson_files,verbose_name="Notes", blank=True)

#     class Meta:
#         ordering = ['position']

#     def __str__(self):
#         return self.name

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super().save(*args, **kwargs)

#     def get_absolute_url(self):
#         return reverse('curriculum:lesson_list', kwargs={'slug':self.subject.slug, 'standard':self.Standard.slug})

# class WorkingDays(models.Model):
#     standard = models.ForeignKey(Standard, on_delete=models.CASCADE,related_name='standard_days')
#     day = models.CharField(max_length=100)
#     def __str__(self):
#         return self.day

# class TimeSlots(models.Model):
#     standard = models.ForeignKey(Standard, on_delete=models.CASCADE,related_name='standard_time_slots')
#     start_time = models.TimeField()
#     end_time = models.TimeField()

#     def __str__(self):
#         return str(self.start_time) + ' - ' + str(self.end_time) 

# class SlotSubject(models.Model):
#     standard = models.ForeignKey(Standard, on_delete=models.CASCADE,related_name='standard_slots')
#     day = models.ForeignKey(WorkingDays, on_delete=models.CASCADE,related_name='standard_slots_days')
#     slot = models.ForeignKey(TimeSlots, on_delete=models.CASCADE,related_name='standard_slots_time')
#     slot_subject = models.ForeignKey(Subject, on_delete=models.CASCADE,related_name='standard_slots_subject')

#     def __str__(self):
#         return str(self.standard)+ ' - ' + str(self.day) + ' - ' + str(self.slot) + ' - ' + str(self.slot_subject)

# class Comment(models.Model):
#     lesson_name = models.ForeignKey(Lesson,null=True, on_delete=models.CASCADE,related_name='comments')
#     comm_name = models.CharField(max_length=100, blank=True)
#     # reply = models.ForeignKey("Comment", null=True, blank=True, on_delete=models.CASCADE,related_name='replies')
#     author = models.ForeignKey(User,on_delete=models.CASCADE)
#     body = models.TextField(max_length=500)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         self.comm_name = slugify("comment by" + "-" + str(self.author) + str(self.date_added))
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.comm_name

#     class Meta:
#         ordering = ['-date_added']

# class Reply(models.Model):
#     comment_name = models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='replies')
#     reply_body = models.TextField(max_length=500)
#     author = models.ForeignKey(User,on_delete=models.CASCADE)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return "reply to " + str(self.comment_name.comm_name)


 