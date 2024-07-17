from django import forms
from django.forms import TextInput, Textarea, Widget

from courses.models import Course

# class CourseAddForm (forms.Form):

#     title = forms.CharField(
#         label = "kurs başlığı", 
#         required= True, 
#         error_messages={"required": "kurs başlığı girmelisiniz."}, 
#         widget = forms.TextInput(attrs={"class": "form-control"}))
    
#     description = forms.CharField(label= "açıklamalar",
#                                   widget = forms.Textarea(attrs={"class": "form-control"}),
#                                   error_messages={"required": "açıklama girmelisiniz."},
#                                      )
#     imageUrl = forms.CharField(label = "kurs resmi",  
#                                widget = forms.TextInput(attrs={"class": "form-control"}),
#                                 error_messages={"required": "resim uzantısı girmelisiniz."},
#                                 )
#     slug = forms.SlugField(label= "uzantı ismi"  , 
#                            widget = forms.TextInput(attrs={"class": "form-control"}),
#                             error_messages={"required": "takma ad girmelisiniz."},
#                             )


class CourseAddForm (forms.ModelForm):
    class Meta: 
        model = Course
        fields  = '__all__'
        #fields = ('title', 'description', 'imageUrl', 'slug',)
        labels = {
            "title": "Kurs Başlığı",
            "description": "Kurs Açıklaması",
            "imageUrl": "Resim Urlsi",
            "slug": "Uzantı adı",
        }
        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "imageUrl": TextInput(attrs={"class":"form-control"}),
            "slug": TextInput(attrs={"class":"form-control"}),
        }
        error_messages= {
            "title": {
                "required": "kurs başlığı girmelisiniz.",
                "max_length": "en fazla 50 karakter girebilirsiniz."
            },
            "description": {
                "required": "kurs için bir açıklama girmelisiniz.",
}
        }





