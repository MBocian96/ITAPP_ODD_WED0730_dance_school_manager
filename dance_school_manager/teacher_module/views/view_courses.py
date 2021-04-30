# Create your views here.

# Create your views here.
from django.views.generic import CreateView


class ViewCourses(CreateView):
    template_name = 'profiles/teacher/view_courses.html'