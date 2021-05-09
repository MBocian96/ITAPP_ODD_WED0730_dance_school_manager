from django import forms


class CreateCourseForm(forms.Form):
    name = forms.CharField(label='Course name', max_length=20)
    # room = forms.CharField(label='Room idx', max_length=100)
    description = forms.CharField(max_length=100)

    # teacher = forms.CharField(label='Course teacher', max_length=100)
    # start_date = forms.DateField()
    # end_date = forms.DateField()
    # distribution = forms.BinaryField()  # tells wich day in week the course takes place eg. 0100 0001 = means only in sundaty and monday
    def __init__(self, *args, **kwargs):
        super(CreateCourseForm, self).__init__(*args, **kwargs)
        for i in range(20):
            self.fields[f'{i}_student'] = forms.EmailField(max_length=100, label=f'Student {i} email: ', required=False)
