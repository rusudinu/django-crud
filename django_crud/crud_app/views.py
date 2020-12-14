from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm


def error_404(request, template_name='error_pages/404.html'):
    return render(request, template_name)


def error_400(request, template_name='error_pages/400.html'):
    return render(request, template_name)


def error_403(request, template_name='error_pages/403.html'):
    return render(request, template_name)


def error_500(request, template_name='error_pages/500.html'):
    return render(request, template_name)