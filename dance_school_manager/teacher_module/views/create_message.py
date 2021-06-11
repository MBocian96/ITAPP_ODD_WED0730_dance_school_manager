from django.contrib.auth.decorators import login_required
from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from authentication_module.models import CustomUser
from courses_module.models import Courses
from teacher_module.forms.create_message_form import CreateMessageForm


#def message_post_view( request, course_id: int):
   # template_name = 'profiles/teacher/certain_course/<int:course_id>/create_message.html'
#    course = get_object_or_404(Courses, id=course_id)
#    students_attended_to_this_course: QuerySet = CustomUser.objects.filter(courses__id=course_id)

#    certain_course = Courses.objects.get(id=course_id)
#    form = CreateMessageForm(request.POST or None)

#    if request.method == "POST":
#        if form.is_valid():
#            form.save()
#        return HttpResponseRedirect("/teacher/certain_course/<int:course_id>/")

#    context = {'form': form,
#               'course_id': course_id,
#               }

   # return render(request,self.template_name, context=context)
#    return render(request, '/certain_course/<int:course_id>/create_message.html', context)


def message_post_view(request):
    #userlist = CustomUser.objects.values('username').distinct().order_by('username')
    form = CreateMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
       # return HttpResponseRedirect("/teacher/certain_course.html")
       # return HttpResponseRedirect("/teacher/courses.html")
        return redirect("teacher_module:course_page_view")

    context = {'form': form,
              # 'userlist':userlist
               }

    return render(request, 'profiles/teacher/create_message.html', context)

