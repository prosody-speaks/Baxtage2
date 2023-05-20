from django import forms
from django.forms import TimeInput

from producer.models import Performance


class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = ['act', 'start_time', 'end_time', 'contact_name']
        widgets = {
            'start_time': TimeInput(attrs={'type': 'time'}),
            'end_time': TimeInput(attrs={'type': 'time'}),
        }

PerformanceFormSet = forms.formset_factory(PerformanceForm, extra=1)


# class PerformanceForm(forms.ModelForm):
#
#     acts = forms.ModelMultipleChoiceField(
#         queryset=Act.objects.all(),
#         widget=ActWidget(),
#     )
#     show = forms.ModelChoiceField(
#         queryset=Show.objects.all(),
#         # widget=ModelSelect2Widget(
#         #     model=Show,
#         #     search_fields=['name__icontains'],
#         # )
#     )
#     tech_spec = forms.ModelChoiceField(
#         queryset=TechSpec.objects.all(),
#         # widget=ModelSelect2Widget(
#         #     model=TechSpec,
#         #     search_fields=['name__icontains'],
#         # )
#     )
#     class Meta:
#         model = Performance
#         fields = ['acts', 'show', 'tech_spec', 'start_time']
#         widgets = {
#             'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         }
