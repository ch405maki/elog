from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from .models import VisitorLog


from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        # Retrieve User fields
        username = request.POST.get("username")
        email = request.POST.get("email")  # Added Email Field
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        first_name = request.POST.get("first_name")  # First Name
        last_name = request.POST.get("last_name")    # Last Name

        # Retrieve Profile fields
        middle_name = request.POST.get("middle_name")
        dob_year = request.POST.get("dob_year")
        dob_month = request.POST.get("dob_month")
        dob_day = request.POST.get("dob_day")
        gender = request.POST.get("gender")
        student_id = request.POST.get("student_id")
        street_address1 = request.POST.get("street_address1")
        street_address2 = request.POST.get("street_address2")
        city = request.POST.get("city")
        state_prov = request.POST.get("state_prov")
        zip_code = request.POST.get("zip_code")
        mobile = request.POST.get("mobile")
        course = request.POST.get("course")
        year = request.POST.get("year")

        # Validation
        if not all([username, email, password, confirm_password, first_name, last_name]):
            messages.error(request, "All fields are required!")
            return render(request, "registration/register.html")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, "registration/register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!")
            return render(request, "registration/register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return render(request, "registration/register.html")

        # Save User and Profile
        try:
            # Create the User
            user = User.objects.create(
                username=username,
                email=email,  # Save Email
                password=make_password(password),
                first_name=first_name,  # Save First Name
                last_name=last_name,    # Save Last Name
            )
            user.save()

            # Create the Profile
            if not Profile.objects.filter(user=user).exists():
                profile = Profile.objects.create(
                    user=user,
                    middle_name=middle_name,
                    dob_year=dob_year,
                    dob_month=dob_month,
                    dob_day=dob_day,
                    gender=gender,
                    student_id=student_id,
                    street_address1=street_address1,
                    street_address2=street_address2,
                    city=city,
                    state_prov=state_prov,
                    zip_code=zip_code,
                    mobile=mobile,
                    course=course,
                    year=year,
                )
                profile.save()
            else:
                messages.success(request, "Account created successfully! You can now log in.")
                return redirect("login")

            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("login")

        except Exception as e:
            # Log the exact error
            print(f"Error: {str(e)}")
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, "registration/register.html")

    return render(request, "registration/register.html")


def landingPage(request):
    return render(request, 'landingPage.html')

def visitor(request):
    return render(request, 'visitor/index.html')

def save_visitor_log(request):
    if request.method == 'POST':
        department = request.POST.get('department')
        name = request.POST.get('name')
        address = request.POST.get('address')
        purpose = request.POST.get('purpose')
        status = request.POST.get('status')
        contact = request.POST.get('contact')
        to_whom = request.POST.get('to_whom')

        # Save to database
        VisitorLog.objects.create(
            department=department,
            name=name,
            address=address,
            purpose=purpose,
            status=status,
            contact=contact,
            to_whom=to_whom,
        )
        messages.success(request, 'Visitor log entry saved successfully!')
        return redirect('visitor_out')

    return render(request, 'visitor/visitor_out.html')

@login_required
def dashboard(request):
    pending_count = VisitorLog.objects.filter(status='Pending').count()
    approved_count = VisitorLog.objects.filter(status='Approved').count()
    declined_count = VisitorLog.objects.filter(status='Declined').count()

    context = {
        'pending_count': pending_count,
        'approved_count': approved_count,
        'declined_count': declined_count,
    }
    return render(request, 'dashboard/index.html', context)

def pending_visitors(request):
    pending_list = VisitorLog.objects.filter(status='Pending') 
    return render(request, 'visitor/pending_list.html', {'visitors': pending_list})

def approved_visitors(request):
    approved_list = VisitorLog.objects.filter(status='Approved')  
    return render(request, 'visitor/approved_list.html', {'visitors': approved_list})

def approve_visitor(request, id):
    visitor = get_object_or_404(VisitorLog, id=id)
    visitor.status = 'Approved'
    visitor.save()
    return redirect('pending_visitors')

def decline_visitor(request, id):
    visitor = get_object_or_404(VisitorLog, id=id)
    visitor.status = 'Declined'
    visitor.save()
    return redirect('pending_visitors')

def visitor_reports(request):
    visitors = VisitorLog.objects.all()  # Fetch all visitor data
    context = {
        'visitors': visitors
    }
    return render(request, 'reports/visitor_reports.html', context)

def account_index(request):
    users = User.objects.all()  
    return render(request, 'account/index.html', {'users': users})

def account_manage(request):
    users = User.objects.all()  
    return render(request, 'account/manage.html', {'users': users})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully.')
    else:
        messages.error(request, 'Invalid request method.')
    return redirect('account_manage')

def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)  
    return render(request, 'account/detail.html', {'user': user})

def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        role = request.POST['role']

        # Create the user
        user = User.objects.create(username=username, email=email, password=password)

        # Set role
        if role == 'admin':
            user.is_superuser = True
            user.is_staff = True
        elif role == 'staff':
            user.is_staff = True

        user.save()
        return redirect('account_index')

# View to display visitors with action 'In'
def visitor_out_view(request):
    visitors = VisitorLog.objects.filter(action='In')  # Filter visitors with action "In"
    context = {
        'visitors': visitors,
    }
    return render(request, 'visitor/visitor_out.html', context)

# View to handle "Out" action
def mark_visitor_out(request, visitor_id):
    visitor = get_object_or_404(VisitorLog, id=visitor_id)
    if request.method == 'POST':
        visitor.action = 'Out'
        visitor.save()
    return redirect('visitor_out')