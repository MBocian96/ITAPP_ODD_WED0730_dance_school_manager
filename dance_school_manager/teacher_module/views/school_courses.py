
# Create your views here.
from django.views.generic import CreateView


class SchoolCoursesViews(CreateView):
    template_name = 'profiles/teacher/school_courses_view.html'