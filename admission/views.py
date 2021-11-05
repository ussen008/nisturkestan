from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import InternatDocuments
from django.contrib import messages
from .forms import InternatForm
from django.http import HttpResponseRedirect


def main_page(request):
    student_data = InternatDocuments.objects.all()
    return render(request, 'index.html', {'student_data' : student_data})


def student_detail(request, id):
    student = InternatDocuments.objects.get(pk=id)
    return render(request, 'student_detail.html', {'student': student})


def upload_files(request):
    if request.method == "POST":
        form = InternatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admission:main_page')
        else:
            return HttpResponse("Form is not valid")
    else:
        form = InternatForm()
    return render(request, 'upload.html', {'form': form})