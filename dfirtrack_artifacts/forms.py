import re

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy

from dfirtrack_artifacts.models import (
    Artifact,
    Artifactpriority,
    Artifactstatus,
    Artifacttype,
)
from dfirtrack_main.models import Case, System, Tag
from dfirtrack_main.widgets import TagWidget


class ArtifactForm(forms.ModelForm):
    # reorder field choices
    system = forms.ModelChoiceField(
        label=gettext_lazy('System (*)'),
        queryset=System.objects.order_by('system_name'),
        empty_label='Select system',
    )

    # reorder field choices
    artifactpriority = forms.ModelChoiceField(
        label=gettext_lazy('Artifactpriority (*)'),
        queryset=Artifactpriority.objects.order_by('artifactpriority_name'),
        widget=forms.RadioSelect(),
    )

    # reorder field choices
    artifactstatus = forms.ModelChoiceField(
        label=gettext_lazy('Artifactstatus (*)'),
        queryset=Artifactstatus.objects.order_by('artifactstatus_name'),
        widget=forms.RadioSelect(),
    )

    # reorder field choices
    artifacttype = forms.ModelChoiceField(
        label=gettext_lazy('Artifacttype (*)'),
        queryset=Artifacttype.objects.order_by('artifacttype_name'),
        empty_label='Select artifacttype',
    )

    # reorder field choices
    case = forms.ModelChoiceField(
        label=gettext_lazy('Case'),
        queryset=Case.objects.order_by('case_name'),
        empty_label='Select case (optional)',
        required=False,
    )

    # reorder field choices
    tag = forms.ModelMultipleChoiceField(
        label=gettext_lazy('Tags'),
        widget=TagWidget,
        queryset=Tag.objects.order_by('tag_name'),
        required=False,
    )

    # reorder field choices
    artifact_assigned_to_user_id = forms.ModelChoiceField(
        label=gettext_lazy('Assigned to user'),
        queryset=User.objects.order_by('username'),
        required=False,
        empty_label='Select user (optional)',
    )

    class Meta:
        # model
        model = Artifact

        # this HTML forms are shown
        fields = [
            'artifact_name',
            'artifactpriority',
            'artifactstatus',
            'artifacttype',
            'artifact_source_path',
            'system',
            'case',
            'tag',
            'artifact_md5',
            'artifact_sha1',
            'artifact_sha256',
            'artifact_note_internal',
            'artifact_note_external',
            'artifact_note_analysisresult',
            'artifact_assigned_to_user_id',
        ]

        # non default form labeling
        labels = {
            'artifact_name': gettext_lazy('Artifact name (*)'),
            'artifact_md5': gettext_lazy('MD5'),
            'artifact_sha1': gettext_lazy('SHA1'),
            'artifact_sha256': gettext_lazy('SHA256'),
            'artifact_note_internal': gettext_lazy('Internal note'),
            'artifact_note_external': gettext_lazy('External note'),
            'artifact_note_analysisresult': gettext_lazy('Analysis result'),
        }

        # special form type or option
        widgets = {
            'artifact_name': forms.TextInput(
                attrs={
                    'autofocus': 'autofocus',
                    'placeholder': 'Add artifact name',
                }
            ),
            'artifact_source_path': forms.TextInput(
                attrs={
                    'size': '100',
                    'style': 'font-family: monospace',
                }
            ),
            'artifact_md5': forms.TextInput(
                attrs={
                    'size': '32',
                    'style': 'font-family: monospace',
                }
            ),
            'artifact_sha1': forms.TextInput(
                attrs={
                    'size': '40',
                    'style': 'font-family: monospace',
                }
            ),
            'artifact_sha256': forms.TextInput(
                attrs={
                    'size': '64',
                    'style': 'font-family: monospace',
                }
            ),
        }

    def clean(self):
        """check provided hashes for their length"""

        super().clean()

        # build regular expression that excludes valid hexadecimal characters
        hex_re = re.compile(r'[^a-fA-F0-9.]')

        # check MD5
        artifact_md5 = self.cleaned_data.get('artifact_md5')
        # check if MD5 was provided
        if artifact_md5:
            # check for length
            if len(artifact_md5) < 32:
                self.errors['artifact_md5'] = self.error_class(
                    [
                        'MD5 is 32 alphanumeric characters in size ('
                        + str(len(artifact_md5))
                        + ' were provided)'
                    ]
                )
            # check for hexadecimal characters (only if there were enough characters submitted)
            else:
                match = hex_re.search(artifact_md5)
                if match:
                    self.errors['artifact_md5'] = self.error_class(
                        ['MD5 contains non-hexadecimal characters']
                    )

        # check SHA1
        artifact_sha1 = self.cleaned_data.get('artifact_sha1')
        # check if SHA1 was provided
        if artifact_sha1:
            # check for length
            if len(artifact_sha1) < 40:
                self.errors['artifact_sha1'] = self.error_class(
                    [
                        'SHA1 is 40 alphanumeric characters in size ('
                        + str(len(artifact_sha1))
                        + ' were provided)'
                    ]
                )
            # check for hexadecimal characters (only if there were enough characters submitted)
            else:
                match = hex_re.search(artifact_sha1)
                if match:
                    self.errors['artifact_sha1'] = self.error_class(
                        ['SHA1 contains non-hexadecimal characters']
                    )

        # check SHA256
        artifact_sha256 = self.cleaned_data.get('artifact_sha256')
        # check if SHA256 was provided
        if artifact_sha256:
            # check for length
            if len(artifact_sha256) < 64:
                self.errors['artifact_sha256'] = self.error_class(
                    [
                        'SHA256 is 64 alphanumeric characters in size ('
                        + str(len(artifact_sha256))
                        + ' were provided)'
                    ]
                )
            # check for hexadecimal characters (only if there were enough characters submitted)
            else:
                match = hex_re.search(artifact_sha256)
                if match:
                    self.errors['artifact_sha256'] = self.error_class(
                        ['SHA256 contains non-hexadecimal characters']
                    )

        return self.cleaned_data


class ArtifactCreatorForm(forms.ModelForm):
    """artifact creator form"""

    # reorder field choices
    artifactpriority = forms.ModelChoiceField(
        label=gettext_lazy('Artifactpriority (*)'),
        widget=forms.RadioSelect(),
        queryset=Artifactpriority.objects.order_by('artifactpriority_name'),
        required=True,
    )

    # reorder field choices
    artifactstatus = forms.ModelChoiceField(
        label=gettext_lazy('Artifactstatus (*)'),
        widget=forms.RadioSelect(),
        queryset=Artifactstatus.objects.order_by('artifactstatus_name'),
        required=True,
    )

    # show all existing artifacttype objects as multiple choice field
    artifacttype = forms.ModelMultipleChoiceField(
        label=gettext_lazy('Artifacttypes (*) - Will also be set as artifact names'),
        widget=forms.CheckboxSelectMultiple(),
        queryset=Artifacttype.objects.order_by('artifacttype_name'),
        required=True,
    )

    # reorder field choices
    artifact_assigned_to_user_id = forms.ModelChoiceField(
        empty_label='Select user (optional)',
        label=gettext_lazy('Assigned to user'),
        queryset=User.objects.order_by('username'),
        required=False,
    )

    # show all existing system objects as multiple choice field
    system = forms.ModelMultipleChoiceField(
        queryset=System.objects.order_by('system_name'),
        widget=forms.CheckboxSelectMultiple(),
        label='Systems (*)',
        required=True,
    )

    # reorder field choices
    tag = forms.ModelMultipleChoiceField(
        label=gettext_lazy('Tags'),
        widget=TagWidget,
        queryset=Tag.objects.order_by('tag_name'),
        required=False,
    )

    # choice for alternative artifact name
    alternative_artifact_name_choice = forms.BooleanField(
        label=gettext_lazy('Use alternative artifact name'),
        required=False,
    )

    # alternative artifact name
    alternative_artifact_name = forms.CharField(
        label=gettext_lazy('Alternative artifact name'),
        required=False,
    )

    class Meta:
        # model
        model = Artifact

        # this HTML forms are shown
        fields = (
            'artifactpriority',
            'artifactstatus',
            'artifact_assigned_to_user_id',
            'artifact_note_analysisresult',
            'artifact_note_external',
            'artifact_note_internal',
            'artifact_source_path',
            'tag',
        )

        # non default form labeling
        labels = {
            'artifact_note_analysisresult': gettext_lazy('Analysis result'),
            'artifact_note_external': gettext_lazy('External note'),
            'artifact_note_internal': gettext_lazy('Internal note'),
            'artifact_source_path': gettext_lazy(
                'Artifact source path (attention: will be set for all artifacts regardless of type)'
            ),
        }

        # special form type or option
        widgets = {
            'artifact_note_analysisresult': forms.Textarea(attrs={'rows': 10}),
            'artifact_note_external': forms.Textarea(attrs={'rows': 10}),
            'artifact_note_internal': forms.Textarea(attrs={'rows': 10}),
            'artifact_source_path': forms.TextInput(
                attrs={
                    'size': '100',
                    'style': 'font-family: monospace',
                }
            ),
        }

    def clean(self):
        """custom field validation"""

        # get form data
        cleaned_data = super().clean()

        # create dict for validation errors
        validation_errors = {}

        """ check for both fields filled """

        # get relevant values
        alternative_artifact_name_choice = self.cleaned_data[
            'alternative_artifact_name_choice'
        ]
        alternative_artifact_name = self.cleaned_data['alternative_artifact_name']

        # alternative_artifact_name and alternative_artifact_name_choice required (or none)
        if (alternative_artifact_name and not alternative_artifact_name_choice) or (
            alternative_artifact_name_choice and not alternative_artifact_name
        ):
            validation_errors[
                'alternative_artifact_name'
            ] = 'Either both or neither of the fields is required.'

        """ raise error """

        # finally raise validation error
        if validation_errors:
            raise forms.ValidationError(validation_errors)

        return cleaned_data


class ArtifacttypeForm(forms.ModelForm):
    class Meta:
        # model
        model = Artifacttype

        # this HTML forms are shown
        fields = [
            'artifacttype_name',
            'artifacttype_note',
        ]

        # non default form labeling
        labels = {
            'artifacttype_name': gettext_lazy('Artifacttype name (*)'),
        }

        # special form type or option
        widgets = {
            'artifacttype_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }
