from django.contrib import admin

# Register your models here.

from .models import Teacher, StudentSignIn
class TeacherAdmin(admin.ModelAdmin):
	list_display = ('id', 'ClassroomId','NameList')
admin.site.register(Teacher,TeacherAdmin)

class StudentSignInAdmin(admin.ModelAdmin):
	list_display = ('id', 'UserId','name','ClassroomId')
admin.site.register(StudentSignIn, StudentSignInAdmin)

