from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		Blog,
	)
from django.db.models import Q
from django.views import generic
from django.views.generic import ListView
from django.core.paginator import Paginator

# from . forms import ContactForm


class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		# testimonials = Testimonial.objects.filter(is_active=True)
		# certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		# portfolio = Portfolio.objects.filter(is_active=True)
		
		# context["testimonials"] = testimonials
		# context["certificates"] = certificates
		context["blogs"] = blogs
		# context["portfolio"] = portfolio
		return context


# class PortfolioView(generic.ListView):
# 	model = Portfolio
# 	template_name = "main/portfolio.html"
# 	paginate_by = 10

# 	def get_queryset(self):
# 		return super().get_queryset().filter(is_active=True)


# class PortfolioDetailView(generic.DetailView):
# 	model = Portfolio
# 	template_name = "main/portfolio-detail.html"

class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		# return super().get_queryset().filter(is_active=True)
		return super().get_queryset()


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"


from django.views.generic import ListView
from .models import Blog

# class SearchResultsView(ListView):
class SearchResultsView(ListView):
    model = Blog
    template_name = 'main/blog.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Blog.objects.filter(name__icontains=query)
        return object_list


from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter
def add_copy_code_button(html):
    # find all code blocks in the HTML and add the button to each block
    # assuming that code blocks are wrapped in <pre><code> tags
    code_blocks = html.findall("//pre/code")
    for code_block in code_blocks:
        # add a button with class "copy-code-button" to the top right of the code block
        button_html = '<button class="copy-code-button" data-clipboard-target="#{}">Copy</button>'.format(code_block.get("id"))
        code_block.addprevious(format_html('<div class="copy-code-container">{}</div>', button_html))
        # add an ID to the code block for the "data-clipboard-target" attribute of the button
        code_block.set("id", "code-block-{}".format(id(code_block)))
    return html
