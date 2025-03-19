from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def why(request):
    return render(request, 'why.html')

def team(request):
    return render(request, 'team.html')

def api_signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        dob = request.POST.get('dob')
        nationality = request.POST.get('nationality')
        phone_number = request.POST.get('phoneNumber')
        address_line1 = request.POST.get('addressLine1')
        address_line2 = request.POST.get('addressLine2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        pin_code = request.POST.get('pinCode')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        gender = request.POST.get('gender')

        
        # Here you would typically validate the data and save it to the database
        user_signup = UserSignup(
            username=full_name, 
            email=email, 
            password=password,
            # Add additional fields as necessary
        )

        user_signup.save()
        
        # Here you would typically validate the data and save it to the database
        user_signup.save()
        
        return JsonResponse({'message': 'Signup successful!'}, status=201)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)

def signup(request):
    return render(request, 'signup.html')

def beneficiary(request):
    return render(request, 'beneficiary.html')

def login(request):
    return render(request, 'login.html')
