from django import forms
from .models import Product

PUBLISH_CHOICES = (
	('',""),
	('publish', "Publish"),
	('draft', "Draft"),
)

TERM_CHOICES = (
	('agree', "Agree"),
	('disagree', "Disagree"),
)

class ProductAddForm(forms.Form):

	title = forms.CharField()
	description = forms.CharField(widget=forms.Textarea)
	media = forms.FileField()
	price = forms.DecimalField()
	publish = forms.ChoiceField(choices=PUBLISH_CHOICES, required=False)
	terms = forms.ChoiceField(widget=forms.RadioSelect, choices=TERM_CHOICES, required=False)

	def clean_price(self):

		price = self.cleaned_data.get("price")

		if price <= 1.00:
			raise forms.ValidationError("Price must be greater than 1")
		else:
			return price

	def clean_title(self):

		title = self.cleaned_data.get("title")

		if len(title) > 5:
			return title
		else:
			raise forms.ValidationError("Title must be greater than 5 characters")

class ProductModelForm(forms.ModelForm):
	
	publish = forms.ChoiceField(choices=PUBLISH_CHOICES, required=False)
	terms = forms.ChoiceField(widget=forms.RadioSelect, choices=TERM_CHOICES, required=False)

	class Meta:
		model = Product
		fields = [
		"title",
		"media",
		"description",
		"price",
		]

		def clean_price(self):
			price = self.cleaned_data.get("price")
			if price <= 1.00:
				raise forms.ValidationError("Price must be greater than 1")
			else:
				return price

		def clean_title(self):
			title = self.cleaned_data.get("title")
			if len(title) > 5:
				return title
			else:
				raise forms.ValidationError("Title must be greater than 5 characters")





