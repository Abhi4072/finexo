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

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Here you would typically validate the data and save it to the database
        user_signup = UserSignup(username=username, email=email, password=password)
        user_signup.save()
        
        return JsonResponse({'message': 'Signup successful!'}, status=201)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


def beneficiary(request):
    return render(request, 'beneficiary.html')
