from django import forms

class CourseAddForm (forms.Form):

    title = forms.CharField(
        label = "kurs başlığı", 
        required= True, 
        error_messages={"required": "kurs başlığı girmelisiniz."}, 
        widget = forms.TextInput(attrs={"class": "form-control"}))
    
    description = forms.CharField(label= "açıklamalar",
                                  widget = forms.Textarea(attrs={"class": "form-control"}),
                                  error_messages={"required": "açıklama girmelisiniz."},
                                     )
    imageUrl = forms.CharField(label = "kurs resmi",  
                               widget = forms.TextInput(attrs={"class": "form-control"}),
                                error_messages={"required": "resim uzantısı girmelisiniz."},
                                )
    slug = forms.SlugField(label= "uzantı ismi"  , 
                           widget = forms.TextInput(attrs={"class": "form-control"}),
                            error_messages={"required": "takma ad girmelisiniz."},
                            )





