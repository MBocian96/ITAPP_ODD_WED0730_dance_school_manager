from django import forms

from authentication_module.models import CustomUser
from courses_module.models import Courses
from teacher_module.models import Message


class CreateMessageForm(forms.ModelForm):
    class Meta:
        model = Message
       # fields = ["title", "text", "user", "related_course"]
        exclude = ["user"]

# class CreateMessageForm(forms.ModelForm):
#        fields = ["title", "text", "user", "related_course"]
#        title = forms.CharField(max_length=100)
#        text = forms.CharField(max_length=600)
#        user = forms.ForeignKey()
#        related_course = forms.ForeignKey(Courses, on_delete=models.CASCADE, unique=False)

#class CreateMessageForm(forms.Form):
#    title = forms.CharField(max_length=100)
#    text = forms.CharField(max_length=100)
#    user = forms.ChoiceField(choices=CustomUser.objects.values('username').distinct().order_by('username'))
#    related_course = forms.Select(choices=Courses.objects.all())
