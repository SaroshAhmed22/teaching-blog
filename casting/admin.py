from django.contrib import admin

from casting.models import  oberecord,projector, pro_room,sec_course, Department,Semester,teacher, student , section , Slots, Slotslab, Days, course, room, timetable, freetimetable, timetablelab, freetimetablelab
# Register your models here.

@admin.register(pro_room)
class studentadmin(admin.ModelAdmin): 
    list_display = ('id', 'proid', 'roomid' )


@admin.register(projector)
class studentadmin(admin.ModelAdmin):
 
    list_display = ('id', 'name', 'is_active', 'capacity', 't_run', 'description')

@admin.register(sec_course)
class studentadmin(admin.ModelAdmin): 
    list_display = ('id', 'secid', 'couid' )


@admin.register(student)
class studentadmin(admin.ModelAdmin):
    model = student
    list_display = ('id', 'user', 'email', 'bio')

@admin.register(teacher)
class studentadmin(admin.ModelAdmin):
    
    list_display = ('id','user', 'email', 'bio')
 

@admin.register(freetimetable)
class studentadmin(admin.ModelAdmin):
    
    list_display = ('id','day', 'slot', 'slot_room')
 

@admin.register(room)
class studentadmin(admin.ModelAdmin):
    
    list_display = ('id','name','capacity', 'pcs', 'projector', 'ac')
 
@admin.register(oberecord)
class studentadmin(admin.ModelAdmin):
 
    list_display = ('id', 'dept', 'course', 'year', 'passed', 'failed')

@admin.register(timetable)
class studentadmin(admin.ModelAdmin):
    
    list_display = ('id','day', 'slot', 'slot_room', 'slot_subject', 'slot_section')

@admin.register(timetablelab)
class studentadmin(admin.ModelAdmin):
    
    list_display = ('id','day', 'slot', 'slot_room', 'slot_subject', 'slot_section')

@admin.register(freetimetablelab)
class studentadmin(admin.ModelAdmin):
    
    list_display = ('id','day', 'slot', 'slot_room' )

admin.site.register(Department)
admin.site.register(Semester)
# admin.site.register(teacher)
# admin.site.register(student)
admin.site.register(section)
admin.site.register(Slots)

admin.site.register(Slotslab)
admin.site.register(Days)
admin.site.register(course)
# admin.site.register(room)
# admin.site.register(timetable)
# admin.site.register(freetimetable)
