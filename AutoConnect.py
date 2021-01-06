from pywinauto import application
import time
import os

os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
time.sleep(5)        

app = application.Application()
app.start('C:\CREON\STARTER\coStarter.exe /prj:cp /id:@@@ /pwd:@@@ /pwdcert:@@@@ /autostart')
'''
  #id: 본인 계정 아이디 / pwd: 계정 패스워드 / pwdcert: 공인인증서 패스워드
'''
time.sleep(60)
