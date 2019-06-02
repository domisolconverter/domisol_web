import threading
from .models import *
from django.core.files.storage import FileSystemStorage
from .emailThread import *
from subprocess import Popen, PIPE
import os


class ConverterThread(threading.Thread):


    def __init__(self, fileName, savedLocation, email, melody):

        self.fileName = fileName
        self.savedLocation = savedLocation
        self.email = email
        self.melody = melody
        self.old_path = os.getcwd()
        threading.Thread.__init__(self)


    def run(self):

        print("ConverterThread Start")

        # 도레미 컨버터 함수 실행시키기 -> 파일경로, 변경할 조 사용
        input_fileName = self.old_path + "/" + self.savedLocation + "/" + self.fileName
        input_melody = self.melody

        ############ (수정) ###############
        p = Popen(["domisolConverter.exe", input_fileName, input_melody], shell=True, stdout=PIPE, stdin=PIPE)

        # 원래 파일 삭제
        old_fileName = self.old_path + "/" + self.savedLocation + "/" + self.fileName
        if os.path.isfile(old_fileName):
            os.remove(old_fileName)
            print("변환전 파일 삭제")

        # 변환된 파일을 찾기 -> result_파일명.pdf
        result_path = self.old_path + "/" + self.savedLocation
        new_fileName = self.fileName.replace(".jpg", "")
        new_fileName = result_path + "/result_" + new_fileName + ".pdf"
        if os.path.isfile(new_fileName):
          print ("변환된 파일 있습니다")
        else:
          print ("그런 이름의 파일은 없습니다")

        # 이메일로 전송해주기
        send_email('Domisol Converter Result Image', 'Domisol Converter를 이용해주셔서 감사합니다.', 'domisolConverter@gmail.com',
        [self.email], fail_silently = False, path=new_fileName)

        # 변환된 파일 삭제
        if os.path.exists(new_fileName):
            os.remove(new_fileName)
            print("변환된 파일 삭제")

        print("ConverterThread End !!!")

def exe_Converter(fileName, savedLocation, email, melody):

    ConverterThread(fileName, savedLocation, email, melody).start()
