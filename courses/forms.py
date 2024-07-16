from django import forms

class CourseAddForm (forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget =forms.Textarea)
    imageUrl = forms.CharField()
    slug = forms.CharField()





