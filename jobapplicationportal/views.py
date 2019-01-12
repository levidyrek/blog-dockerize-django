from django import forms
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .models import JobApplication, JobReferral


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'relevant_experience']


class JobReferralForm(forms.ModelForm):
    is_referral = forms.BooleanField(
        label='Is this a referral?',
        required=False,
    )

    class Meta:
        model = JobReferral

        fields = [
            'name', 'email', 'relevant_experience', 'referrer_name',
            'referrer_email'
        ]


class SubmitJobApplicationView(FormView):
    success_url = reverse_lazy('Job Application Submission Success')
    template_name = 'submit_application.html'

    def get_form_class(self):
        # Always use JobReferralForm for GET requests,
        # so you can render all of the fields for either model.
        if self.request.method == 'GET':
            return JobReferralForm
        else:
            # On a POST request, return the form class used for validation.
            # Use JobApplicationForm if this is not a referral. Otherwise,
            # use JobReferralForm.
            is_referral = self.request.POST.get('is_referral')
            if is_referral:
                return JobReferralForm
            else:
                return JobApplicationForm

    def form_valid(self, form):
        # Save the form data to a new model instance in the database.
        form.save()
        return super().form_valid(form)


def application_success(request):
    return HttpResponse('Thanks for the application!')
