from django import forms


class RecipeSearchForm(forms.Form):
    search_term = forms.CharField(
        max_length=120,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name or ingredient..."}
        ),
    )
