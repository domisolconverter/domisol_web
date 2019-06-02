import threading
from .models import *
from django.core.files.storage import FileSystemStorage

class ConverterThread(threading.Thread):


    def __init__(self, fileName, email):

        self.fileName = fileName
        self.email = email
        threading.Thread.__init__(self)


    def run(self):

        print("ConverterThread Start")

        # 도레미 컨버터 함수 실행시키기 -> 파일명+pk 포함되어있는거 찾기

        # 변환된 파일을 찾기 -> 파일명+pk.pdf
        # + 뒤에 있는 pk로 DB를 뒤져서
        # 이메일로 전송해주기


def exe_Converter(fileName, email):

    ConverterThread(fileName, email).start()
