from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Product
from .forms import ProductAddForm, ProductModelForm
from digitalmarket.mixins import MultiSlugMixin, StaffMemberRequiredMixin, LoginRequiredMixin


class ProductCreateView(LoginRequiredMixin, CreateView):
	model = Product
	form_class = ProductModelForm
	success_url = "/products/add/"

	def form_valid(self, form):
		user = self.request.user
		form.instance.user = user
		context = super(ProductCreateView, self).form_valid(form)
		return context


class ProductUpdateView(LoginRequiredMixin, MultiSlugMixin,  UpdateView):
	model = Product
	form_class = ProductModelForm
	success_url = "/products/"

	def get_object(self, *args, **kwargs):
		user = self.request.user
		obj = super(ProductUpdateView, self).get_object(*args, **kwargs)
		
		if obj.user == user:
			return obj
		else:
			raise Http404


class ProductDetailView(MultiSlugMixin, DetailView):
	model = Product


class ProductListView(ListView):
	model = Product

	def get_queryset(self, *args, **kwargs):
		qs = super(ProductListView, self).get_queryset(**kwargs)
		query = self.request.GET.get("q",  "")
		qs = qs.filter(
			Q(title__contains=query)| Q(description__contains=query))
		return qs


def home(request):

	print request

	template = "home.html"
	context = {}

	return render(request, template, context)


def create_view(request):

	form = ProductModelForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.sale_price = instance.price
		instance.save()

	template = "create_view.html"
	context ={
		"form": form
	}

	return render(request, template, context)


def edit_view(request, object_id=None):

	product = get_object_or_404(Product, id=object_id)

	form = ProductModelForm(request.POST or None, instance=product)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	template = "edit_view.html"

	context = {
		"object": product,
		"form": form,
	}

	return render(request, template, context)


def detail_slug_view(request, slug=None):
	try:
		product = get_object_or_404(Product, slug=slug)
	except Product.MultipleObjectsReturned:
		product = Product.objects.filter(slug=slug).order_by("-title").first()

	template = "detail_view.html"

	context = {
		"title": product.title,
		"description": product.description,
		"price": product.price,
		"sale_price" : product.sale_price,
		"media": product.media
	}

	return render(request, template, context)


def detail_view(request, object_id=None):

	product = get_object_or_404(Product, id=object_id)

	template = "detail_view.html"

	context = {
		"title": product.title,
		"description": product.description,
		"price": product.price,
		"sale_price" : product.sale_price,
		"media": product.media
	}

	return render(request, template, context)

	
def list_view(request):

	if request.user.is_authenticated():
		template = "list_view.html"
		queryset = Product.objects.all()
		context = {
			"queryset": queryset
		}
	else:
		template = "not_found.html"
		context = {
			
		}

	return render(request, template, context)
