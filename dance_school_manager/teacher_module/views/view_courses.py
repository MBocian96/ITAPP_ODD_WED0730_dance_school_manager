# Create your views here.

# Create your views here.
from django.views.generic import CreateView


class CoursesListViews(CreateView):
    template_name = 'profiles/teacher/view_courses.html'