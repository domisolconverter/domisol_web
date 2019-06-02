import threading
from .models import *
from django.core.files.storage import FileSystemStorage
from .emailThread import *
from subprocess import Popen, PIPE

class ConverterThread(threading.Thread):


    def __init__(self, fileName, savedLocation, email):

        self.fileName = fileName
        self.savedLocation = savedLocation
        self.email = email
        threading.Thread.__init__(self)


    def run(self):

        print("ConverterThread Start")

        # (수정) 도레미 컨버터 함수 실행시키기 -> 파일경로, 파일명 사용
        p = Popen(["test.exe"], shell=True, stdout=PIPE, stdin=PIPE)
        print(p.stdout.read())

        # (추가)원래 파일 삭제

        # 변환된 파일을 찾기 -> result_파일명.jpg
        

        # 이메일로 전송해주기
        send_email('안녕하세요', '내용입니다', 'domisolConverter@gmail.com',
        [self.email], fail_silently = False)

        # (추가)변환된 파일 삭제

        print("ConverterThread End !!!")

def exe_Converter(fileName, savedLocation, email):

    ConverterThread(fileName, savedLocation, email).start()
