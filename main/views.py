from django.shortcuts import render
from rest_framework import generics
from .models import UserSignup
from .serializers import UserSignupSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import generics
class UserAccountCreate(generics.CreateAPIView):
    queryset = UserSignup.objects.all()
    serializer_class = UserSignupSerializer


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






@csrf_exempt
def api_signup(request):
    if request.method == 'POST':
        try:
            full_name = request.POST.get('full_name')
            date_of_birth = request.POST.get('date_of_birth')
            nationality = request.POST.get('nationality')
            phone_number = request.POST.get('phone_number')
            address_line_1 = request.POST.get('address_line_1')
            address_line_2 = request.POST.get('address_line_2')
            city = request.POST.get('city')
            state = request.POST.get('state')
            country = request.POST.get('country')
            pin_code = request.POST.get('pin_code')
            gender = request.POST.get('gender')  # Capture gender data

            user_signup = UserSignup(full_name=full_name, date_of_birth=date_of_birth, nationality=nationality,
                                     phone_number=phone_number, address_line_1=address_line_1,
                                     address_line_2=address_line_2, city=city, state=state,
                                     country=country, pin_code=pin_code, gender=gender)

            user_signup.save()

            return JsonResponse({'message': 'Signup successful!'}, status=201)
        except Exception as e:
            print(e, "*"*100)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


def signup(request):
    return render(request, 'signup.html')


def beneficiary(request):
    return render(request, 'beneficiary.html')


def login(request):
    return render(request, 'login.html')
