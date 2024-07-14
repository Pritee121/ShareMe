from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import FileUploadForm, CodeSearchForm
from .models import UploadedFile

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            return render(request, 'uploader/upload_success.html', {'code': uploaded_file.code})
    else:
        form = FileUploadForm()
    return render(request, 'uploader/upload.html', {'form': form})

def access_file(request, code):
    uploaded_file = get_object_or_404(UploadedFile, code=code)
    response = HttpResponse(uploaded_file.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def home(request):
    return render(request, 'uploader/home.html')

def search_code(request):
    if request.method == 'POST':
        form = CodeSearchForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            return redirect('access_file', code=code)
    else:
        form = CodeSearchForm()
    return render(request, 'uploader/search.html', {'form': form})
