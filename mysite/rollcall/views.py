from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class home(TemplateView):
	template_name = 'home.html'		

from .forms import TeacherForm, StudentForm
from allauth.socialaccount.models import SocialAccount # get user id from allauth
from .models import Teacher, StudentSignIn

# split the name list entered by teacher
def splitNameList(ClassroomId):
	SplitNameList = []
	if Teacher.objects.filter(ClassroomId = ClassroomId):
		SplitNameList.extend(Teacher.objects.filter(ClassroomId = ClassroomId)[0].NameList.split("\r\n"))	
	return(SplitNameList)

# where teacher enter the name list of students
def teacher(request):
	# use teacher's ID to be the classroom ID
	ClassroomId = int(SocialAccount.objects.filter(user=request.user, provider='google')[0].uid) % 10000000000
	
	# initialize student's database
	StudentSignIn.objects.filter(ClassroomId = ClassroomId).delete()
	
	form = TeacherForm(request.POST or None)	
	if form.is_valid():
		FormInput = form.save(commit=False)		
		
		#initialize teacher's database
		Teacher.objects.filter(ClassroomId = ClassroomId).delete()
		
		FormInput.ClassroomId = ClassroomId
		FormInput = form.save()
		form = TeacherForm() # clear form	
	
	context = {
	'form' : form,
	'ClassroomId' : ClassroomId,
	'SplitNameList' : splitNameList(ClassroomId),
	}
	return render(request, 'teacher.html',context)
	
# where student enter the classroom ID
from django.shortcuts import redirect
def student(request):
	form = StudentForm(request.POST or None)
	
	if form.is_valid():
		return redirect('/student/%s' %request.POST.dict()['ClassroomId'])
		
	context = {
	'form' : form,
	}
	
	return render(request, 'student.html',context,)	

# where student sign in
def studentSignIn(request,ClassroomId):
	#student's ID
	StudentId = int(SocialAccount.objects.filter(user=request.user, provider='google')[0].uid) % 10000000000 
	
	SignInName = [0]
	if request.method == "POST":
		# the student can only sign in one name
		StudentSignIn.objects.filter(UserId = StudentId).delete()
		
		SignInName[0] = request.POST.dict()['attendance']
		
		# the name can only be signed by one student
		StudentSignIn.objects.filter(ClassroomId = ClassroomId, name = SignInName[0]).delete()
		
		StudentSignIn.objects.create\
		(UserId = StudentId, ClassroomId = ClassroomId, name = SignInName[0], \
		account = SocialAccount.objects.filter(user=request.user, provider='google')[0].get_provider_account())
		
	context = {
	'ClassroomId' : ClassroomId,
	'SplitNameList' : splitNameList(ClassroomId),
	'SignInName' : SignInName[0],
	}
	return render(request, 'studentSignIn.html',context)
	
# where teacher see the attendances	
def attendanceList(request, ClassroomId):
	Attendence = []
	for element in splitNameList(ClassroomId):
		if StudentSignIn.objects.filter(ClassroomId=ClassroomId, name=element):
			Attendence.extend('O')
		else:
			Attendence.extend('X')
			
	StudentSignInAccount = []
	for element in splitNameList(ClassroomId):
		if StudentSignIn.objects.filter(ClassroomId=ClassroomId, name=element):
			StudentSignInAccount.append(StudentSignIn.objects.filter(ClassroomId=ClassroomId, name=element)[0].account)
		else:
			StudentSignInAccount.append('')
			
	RollCallList = []
	if splitNameList(ClassroomId):
		for i in range(len(splitNameList(ClassroomId))):
			RollCallList.append([splitNameList(ClassroomId)[i],Attendence[i],StudentSignInAccount[i]])
	
	context = {
	'ClassroomId' : ClassroomId,
	'RollCallList' : RollCallList,
	}
	return render(request, 'attendanceList.html',context)
