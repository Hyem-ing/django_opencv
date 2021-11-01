from django.shortcuts import render
from opencv_webapp.forms import SimpleUploadForm, ImageUploadForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .cv_functions import cv_detect_face


# Create your views here.
def first_view(request):

    return render(request, 'opencv_webapp/first_view.html', {})


def simple_upload(request):

    if request.method == 'POST':

        print(request.POST) # dict
        print(request.FILES) # dict

        form = SimpleUploadForm(request.POST, request.FILES)

        if form.is_valid():

            myfile = request.FILES['image'] # 유저가 업로드한 파일
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            # fs.save(myfile.name, myfile)
            # uploaded_file_url = fs.url(filename)



            context = {'form':form, 'uploaded_file_url':uploaded_file_url}
            return render(request, 'opencv_webapp/simple_upload.html', context)

    else: # 'GET' request
        form = SimpleUploadForm()
        return render(request, 'opencv_webapp/simple_upload.html', {'form':form})


def detect_face(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # ImageUploadModel's instance
            # post.description = papago.translate(post.description)
            post.save()
            # 괄호 안에 commit=True 생략되어있음 False로 하면 임시저장됨
            # ㅇㅇ
            imageURL = settings.MEDIA_URL + form.instance.document.name

            cv_detect_face(settings.MEDIA_ROOT_URL + imageURL)

            # print('\n\n--------------------------------\n\n')
            # print('** imageURL :', imageURL)
            # print('** + ROOT_URL :', settings.MEDIA_ROOT_URL + imageURL)
            # print()
            # print('* form.instance :', form.instance)
            # print('* form.instance.document :', form.instance.document)
            # print('* form.instance.document.name :', form.instance.document.name)
            # print('* form.instance.document.url :', form.instance.document.url)
            # print('* post.document :', post.document)
            # print('\n\n--------------------------------\n\n')
            context = {'form':form, 'post':post}
            return render(request, 'opencv_webapp/detect_face.html', context)
    else:
        form = ImageUploadForm()
        context = {'form':form}
        return render(request, 'opencv_webapp/detect_face.html', context)
