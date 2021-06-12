from django.contrib.auth.decorators import login_required
from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from authentication_module.models import CustomUser
from courses_module.models import Courses
from teacher_module.forms.create_message_form import CreateMessageForm




class MessagePostView(CreateView):

    def get(self, request, *args, **kwargs):
        form = CreateMessageForm(request.POST or None)
        context = {'form': form,
                   }
        return render(request, 'profiles/teacher/create_message.html', context)

    def post(self, request, *args, **kwargs):
        form = CreateMessageForm(request.POST )
        form.instance.user = request.userif request.method == "POST":
        related_course = form.cleaned_data.get("related_course")
            if form.is_valid():
                related_course = form.cleaned_data.get("related_course")
                form.save()
                return redirect("teacher_module:course_page_view", course_id=related_course.id)

    context = {'form': form,
              # 'userlist':userlist
               }

    return render(request, 'profiles/teacher/create_message.html', context)

