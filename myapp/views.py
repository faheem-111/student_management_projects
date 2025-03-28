from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,logout


from myapp.models import CustomUser

from myapp.models import Staff

from myapp.models import Course



from myapp.models import Subject

from myapp.models import Session_year

from myapp.models import StaffNotifications

from myapp.models import Feedback


# Create your views here.
def homepage(request):
    return render(request,'index.html')
def login_page(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('email'),
            password=request.POST.get('password')
        )
        if user is not None:
            login(request,user)
            user_type= user.user_type
            if user_type == '1':
               return redirect('HODdashboard_page')
            elif user_type == '2':
                return redirect('staffboard_page')
            else:
                return redirect('login_page')
        else:
            messages.error(request, 'Invalid Email and Password')
            return redirect('login_page')

    return render(request,'login.html')
def dashboard_page(request):
    return render(request,'dashboard.html')
def HODdashboard_page(request):
    return render(request,'HODdashboard.html')
def staffboard_page(request):
    return render(request,'staffdashboard.html')
def profile_page(request):
    try:
        user = CustomUser.objects.filter(id=request.user.id).first()

        if not user:
            messages.error(request, "User profile not found. Please contact support.")
            return redirect('profile_page')  # Redirect to a safe page (like home or dashboard)
    except Exception as e:
        messages.error(request, f"An unexpected error occurred: {e}")
        return redirect('profile_page')
    context ={
        'user':user
    }


    return render(request,'profile.html',context)
def update_profile(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

    try:
        customuser = CustomUser.objects.get(id=request.user.id)
        customuser.profile_pic = profile_pic
        customuser.first_name = first_name
        customuser.last_name = last_name
        customuser.email = email
        customuser.username = username
        if password != None and password != '':
            customuser.set_password(password)
        if profile_pic != None and profile_pic != '':
            customuser.profile_pic = profile_pic
        customuser.save()
        messages.success(request, 'Your profile successfully updated')
        return redirect('profile_page')
    except:
        messages.error(request, 'failed to update your profile')

    return render(request,'profile.html')
def addstaff_page(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        # Check for duplicate email or username
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email is already taken")
            return redirect('addstaff_page')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username is already taken")
            return redirect('addstaff_page')

        try:
            # Create a new user and hash password using create_user
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                password=password,
                user_type=2  # Ensure this corresponds to staff
            )

            # Create and save the staff record
            Staff.objects.create(
                admin=user,
                address=address,
                gender=gender
            )

            messages.success(request, "Staff added successfully")
            return redirect('addstaff_page')

        except Exception as e:
            print(f"Error: {e}")  # Logs error for debugging
            messages.error(request, "An error occurred while adding staff")
            return redirect('addstaff_page')

    return render(request, 'addstaff.html')
def viewstaff_page(request):
    staff = Staff.objects.all()
    context={
        'staff':staff,
    }
    return render(request,'viewstaff.html',context)

def addcourse_page(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course = Course(
            name=course_name,
        )
        course.save()
        messages.success(request, 'Course Added Successfully')
        return redirect('addcourse_page')

    return render(request,'addcourse.html')

def viewcourse_page(request):
    course = Course.objects.all()
    context = {
        'course': course,
    }
    return render(request, 'viewcourse.html', context)

def addsubject_page(request):
    course = Course.objects.all()
    staff = Staff.objects.all()
    context = {
        'course': course,
        'staff': staff,
    }
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subjects = Subject(
            name=subject_name,
            course=course,
            staff=staff,)

        subjects.save()
        messages.success(request, "Subject Added SuccessFully")
        return redirect('addsubject_page')
    return render(request,'addsubject.html',context)

def viewsubject_page(request):
    subject = Subject.objects.all()
    context = {
        'subject': subject,
    }
    return render(request,'viewsubject.html',context)

def editstaff_page(request,id):
    staff = Staff.objects.get(id=id)
    context = {
        'staff': staff,
    }


    return render(request,'editstaff.html',context)

def updatestaff_page(request):
   if request.method == 'POST':
       staff_id = request.POST.get('staff_id')
       profile_pic = request.FILES.get('profile_pic')
       first_name = request.POST.get('first_name')
       last_name = request.POST.get('last_name')
       email = request.POST.get('email')
       username = request.POST.get('username')
       password = request.POST.get('password')
       address = request.POST.get('address')
       gender = request.POST.get('gender')

       user = CustomUser.objects.get(id=staff_id)
       user.first_name = first_name
       user.last_name = last_name
       user.email = email
       user.username = username
       if password != None and password != '':
           user.set_password(password)
       if profile_pic != None and profile_pic != '':
           user.profile_pic = profile_pic
       user.save()

       staff = Staff.objects.get(admin=staff_id)
       staff.address = address
       staff.gender = gender
       staff.save()
       messages.success(request, "Staff Updated SuccessFully")
       return redirect('viewstaff_page')

   return render(request,'editstaff.html')
def deletestaff_page(request,admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()
    messages.success(request, 'Staff Deleted Successfully')

    return redirect('viewstaff_page')

def editcourse_page(request,id):
    course = Course.objects.get(id=id)
    context = {
        'course': course,
    }

    return render(request, 'editcourse.html',context)

def updatecourse_page(request):
    if request.method == 'POST':
        name = request.POST.get('course_name')
        course_id = request.POST.get('course_id')
        course = Course.objects.get(id=course_id)
        course.name = name
        course.save()
        messages.success(request, 'Course Updated Successfully')
        return redirect('viewcourse_page')

    return render(request,'editcourse.html')

def deletecourse_page(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Course Deleted Successfully')

    return redirect('viewcourse_page')

def editsubject_page(request,id):
    subject = Subject.objects.get(id=id)
    course = Course.objects.all()
    staff = Staff.objects.all()
    context = {
        'subject': subject,
        'course': course,
        'staff': staff,
    }

    return render(request,'editsubject.html',context)

def updatesubject_page(request):
   if request.method == 'POST':
       subject_id =request.POST.get('subject_id')
       subject_name =request.POST.get('subject_name')
       course_id = request.POST.get('course_id')
       staff_id = request.POST.get('staff_id')




       subject = Subject.objects.get(id=subject_id)
       subject.name = subject_name
       subject.course =Course.objects.get(id=course_id)
       subject.staff =Staff.objects.get(id=staff_id)

       subject.save()


       messages.success(request, "Subject updated successfully!")
       return redirect('viewsubject_page')


   return render(request,'editsubject.html')

def deletesubject_page(request,id):
   subject = Subject.objects.filter(id=id)
   subject.delete()
   messages.success(request,'Subject Deleted Successfully')
   return redirect('viewsubject_page')

def addsession_page(request):
   if request.method == 'POST':
       sessionyear_start = request.POST.get('sessionyear_start')
       sessionyear_end = request.POST.get('sessionyear_end')


       session = Session_year(
           session_start = sessionyear_start,
           session_end = sessionyear_end,
       )
       session.save()
       messages.success(request,'Session Added Successfully')
       return redirect('addsession_page')
   return render(request,'addsession.html')

def viewsession_page(request):
    session = Session_year.objects.all()
    context = {
        'session': session,
    }


    return render(request,'viewsession.html',context)


def editsession_page(request,id):
    session = Session_year.objects.get(id=id)
    context = {
        'session': session,
    }

    return render(request,'editsession.html',context)

def updatesession_page(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        sessionyear_start = request.POST.get('sessionyear_start')
        sessionyear_end = request.POST.get('sessionyear_end')

        session = Session_year(
            id=session_id,
            session_start=sessionyear_start,
            session_end=sessionyear_end,
        )
        session.save()
        messages.success(request, "Session Updated SuccessFully")
        return redirect('viewsession_page')

    return render(request,'editsession.html')

def deletesession_page(request,id):
   session = Session_year.objects.get(id=id)
   session.delete()
   messages.success(request,'Session Deleted Successfully')
   return redirect('viewsession_page')

def sendstaffnotification_page(request):
    staff = Staff.objects.all()
    context = {
        'staff': staff,
    }

    return render(request,'sendstaffnotification.html',context)


def savestaffnotifications_page(request):
   if request.method == 'POST':
       staff_id = request.POST.get('staff_id')
       message = request.POST.get('message')


       staff = Staff.objects.get(id = staff_id)
       notification = StaffNotifications(
           staff_id = staff,
           message = message
       )
       notification.save()
       messages.success(request,'Notifications are successfully sent')
       return redirect('sendstaffnotification_page')
   return render(request,'sendstaffnotification.html')

def viewnotification_page(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id
        notification = StaffNotifications.objects.filter(staff_id=staff_id)

        context = {
            'notification': notification,
        }

    return render(request,'viewnotification.html',context)



def savefeedback_page(request):
    if request.method == 'POST':
        feedbacke = request.POST.get('feedback')
        staff = Staff.objects.get(admin=request.user.id)
        feedback = Feedback(
            staff_id=staff,
            feedback=feedbacke,
        )
        feedback.save()
        messages.success(request, 'Feedback Sent Successfully')
        return redirect('feedback_page')

    return render(request,'feedback.html')

def feedbackview_page(request):
    feedback = Feedback.objects.all()
    feedback_history = Feedback.objects.all()
    context = {
        'feedback': feedback,
        'feedback_history': feedback_history,
    }

    return render(request,'feedbackview.html',context)

def feedbacksave_page(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedbacks = Feedback.objects.get(id=feedback_id)
        feedbacks.feedback_reply = feedback_reply

        feedbacks.save()
        messages.success(request, 'Feedback Sent Successfully')
        return redirect('feedbacksave_page')
    return render(request, 'feedback.html')


def feedback_page(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    feedback_history = Feedback.objects.filter(staff_id=staff_id)
    context = {
        'feedback_history': feedback_history,
    }

    return render(request,'feedback.html',context)

def dologout(request):
   logout(request)
   return redirect('login_page')
