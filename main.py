import smtplib
from email.message import EmailMessage

smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)

# 서버 연결을 설정하는 단계
smtp_gmail.ehlo()

# 연결을 암호화
smtp_gmail.starttls()

# 로그인
smtp_gmail.login('emailfordev2022@gmail.com', 'wqyrsdvbzdysvyqm')
#smtp_gmail.login('emailfordev2022@gmail.com', '2022emailfordev')

msg=EmailMessage()

# 제목 입력
msg['Subject']="제목입니다2"

# 내용 입력
msg.set_content("내용입니다")

# 보내는 사람
msg['From']='emailfordev2022@gmail.com'

# 받는 사람
msg['To']='hayarobys@gmail.com'

file='./sample.jpeg'
fp = open(file, 'rb')
file_data=fp.read()
msg.add_attachment(file_data, maintype='image', subtype='jpeg', filename="sample.jpeg")

smtp_gmail.send_message(msg)