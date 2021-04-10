from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from authentication_module.models import CustomUser


@login_required
def profile_view(request):
    # profile = CustomUser.objects.get(email__in=request.email)
    current_user: CustomUser = request.user
    result = (
        current_user.id, current_user.email, current_user.is_teacher, current_user.is_student, current_user.is_employee)
    return HttpResponse(f"Logged in user is: {str(result)}")
    # context = {'profile': profile}
    # template = 'profiles/student_profile.html'
    # return render(request, template, context)
