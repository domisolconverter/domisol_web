from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.http import HttpResponseRedirect
from .converterThread import *
from .models import *
import datetime
# Create your views here.

def main(request):

    if request.method == 'POST':

        #print(request.POST)
        #print(request.FILES)
        #print(type(request.FILES['uploadedFile']))
        #print(request.FILES['uploadedFile'])
        print(request.FILES.getlist('uploadedFile'))

        # 이메일을 입력하지 않은 경우
        if request.POST['input_email'] == '':
            message = "이메일을 입력하세요"
            return render(request, 'main.html', { "message": message })

        # 파일을 업로드 한 경우
        if 'uploadedFile' in request.FILES:

            fileList = request.FILES.getlist('uploadedFile')
            email = request.POST['input_email']
            melody = request.POST['조이름']
            print(len(fileList))

            # jpg 파일이 아닌 파일이 업로드 되었는지 검사
            for i in range(0, len(fileList)):

                fileName = fileList[i]._name
                # jpg 파일이 아니라면
                if fileName.find('jpg') < 0 :
                    message = "파일 형식이 잘못되었습니다. JPG 파일을 업로드하세요."
                    return render(request, 'main.html', { "message": message })

            # jpg 파일이라면
            for i in range(0, len(fileList)):
                # DB에 파일명, 이메일, 변환하고 싶은 조, 파일 저장
                ## 파일 이름 겹치지 않게
                now = datetime.datetime.now()
                nowDatetime = now.strftime('%Y%m%d_%H_%M_%S.jpg')
                fileName = fileList[i]._name.replace(".jpg", "")
                fileName = fileName + nowDatetime
                file = fileList[i]
                fileModel = UploadFileModel.objects.create(title=fileName, email=email, melody=melody, file=file)
                fileModel.save()

                # jpg 파일을 서버에 저장
                savedLocation = 'uploadedJPG/'+email
                fs = FileSystemStorage(location=savedLocation)
                savedFileName = fs.save(fileName, file)
                uploaded_file_url = fs.url(savedFileName)

                # 스레드 실행
                exe_Converter(fileName, savedLocation, email)

            redirect_to = reverse('uploading', kwargs={'email':email})
            return HttpResponseRedirect(redirect_to)

        # 파일을 업로드하지 않은 경우
        else:
            message = "파일을 업로드하지 않았습니다. JPG 파일을 업로드하세요."
            return render(request, 'main.html', { "message": message })

    return render(request, 'main.html', { })


# 소켓 연결해서 로딩화면 띄우면서 서버에 있는 프로그램 돌리고 서버로부터 데이터 받아오는 것이 필요하당
def process_upload(request, email):

    return render(request, 'uploading.html', { "email" : email })
