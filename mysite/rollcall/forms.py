from django import forms
from .models import Teacher
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('NameList',)
        widgets = {
            'NameList': forms.Textarea(attrs={'cols': 20, 'rows': 5}),
        }
        labels = {
        'NameList' : 'name list',
        }
        
#classroom ID entered by student
class StudentForm(forms.Form):
    ClassroomId = forms.CharField(max_length=200)
        
