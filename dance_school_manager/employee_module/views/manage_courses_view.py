# Create your views here.

# Create your views here.
from django.views.generic import CreateView


class ManageCoursesViews(CreateView):
    template_name = 'profiles/employee/manage_courses_view.html'
