from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):
	@method_decorator(login_required)

	def dispatch(self, request, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class StaffMemberRequiredMixin(object):
	@method_decorator(login_required)

	def dispatch(self, request, *args, **kwargs):
		return super(StaffMemberRequiredMixin, self).dispatch(request, *args, **kwargs)


class MultiSlugMixin(object):
	model = None

	def get_object(self, *args, **kwargs):
		
		slug = self.kwargs.get("slug")
		ModelClass = self.model

		if slug is not None:

			try:

				obj = get_object_or_404(ModelClass, slug=slug)

			except ModelClass.MultipleObjectsReturned:

				obj = ModelClass.objects.filter(slug=slug).order_by("-title").first()

		else:

			obj = super(MultiSlugMixin, self).get_object(*args, **kwargs)

		return obj