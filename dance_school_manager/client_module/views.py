from django.contrib.auth.decorators import login_required
from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View, generic
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import UserChangeForm
from authentication_module.forms import EditProfileForm, ReportAbsenceForm
from operator import attrgetter



# Create your views here.


# Client can view his courses with descriptions, hyperlink to settings
class ClientView(CreateView):
    template_name = 'profiles/student/student_profile.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {'user': request.user,
                   'courses_list': request.user.courses.all(),
                   'deposit': request.user.deposit
                   }

        return render(request, self.template_name, context=context)


# Client can edit parameters given in field
class ClientSettingsView(UpdateView):
    form = UserChangeForm
    template_name = 'profiles/student/student_profile_settings.html'
    success_url = reverse_lazy('client_module:user_view')
    fields = {'email', 'username'}

    def get_object(self):
        return self.request.user


# Client can leave course
def AbandonCourse(request, pk):
    user = request.user
    to_delete = user.courses.get(id=pk)
    context = {'item': to_delete}
    if request.method == "POST":
        request.user.courses.remove(to_delete)
        return redirect('client_module:user_view')

    return render(request, 'profiles/student/abandon_course.html', context)


# Callendar view

class CalendarView(CreateView):
    template = 'profiles/student/calendar_view.html'

    def get(self, request, *args, **kwargs):
        courses_list = request.user.courses.all()
        days = [('Monday', [course for course in courses_list if course.days == '0']),
                ('Tuesday', [course for course in courses_list if course.days == '1']),
                ('Wednesday', [course for course in courses_list if course.days == '2']),
                ('Thursday', [course for course in courses_list if course.days == '3']),
                ('Friday', [course for course in courses_list if course.days == '4'])
                ]
        for day in days:
            day[1].sort(key=attrgetter('start_date'))

        context = {'days': days, 'user': request.user}

        return render(request, self.template, context=context)

class ReportAbsenceView(CreateView):
    def get(self, request, *args, **kwargs):
        form = ReportAbsenceForm
        context = {'form': form}
        return render(request, 'profiles/student/report_absence_view.html', context)

    def post(self, request, *args, **kwargs):
        form = ReportAbsenceForm(request.POST)
        form.instance.related_student = request.user
        if form.is_valid():
            form.save()
            return redirect("client_module:user_view")
        return HttpResponse('blad')