from django import forms

class QuizForm(forms.Form):
    def __init__(self, questions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for index, question in enumerate(questions):
            self.fields[f'question_{index}'] = forms.ChoiceField(
                choices=[(option, option) for option in question['options']],
                label=question['question'],
            )