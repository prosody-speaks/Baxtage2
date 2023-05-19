from django import forms
from django_select2.forms import ModelSelect2MultipleWidget

from lineup.models import Act, Performance

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = ['act', 'show', 'start_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
#
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
