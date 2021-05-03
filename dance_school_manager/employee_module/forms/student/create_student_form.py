from django import forms


class CreateStudentForm(forms.Form):
    username = forms.CharField(label='User username', max_length=20)
    email = forms.EmailField(max_length=60)

    def __init__(self, *args, **kwargs):
        super(CreateStudentForm, self).__init__(*args, **kwargs)
        for i in range(20):
            self.fields[f'{i}_course'] = forms.CharField(label=f'Course {i} name', max_length=100, required=False)
