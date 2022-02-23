import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다" # 제목
msg["From"] = EMAIL_ADDRESS # 발신자
msg["To"] = "pjh940114@naver.com" # 수신자

# 여러 명에게 메일을 보낼 때
# msg["To"] = "pjh940114@naver.com", "pjh940114@gmail.com"
# to_list = ["pjh940114@naver.com", "pjh940114@gmail.com"]
# msg["To"] = ", ".join(to_list)

# 참조
# msg["Cc"] = "pjh940114@gmail.com"

# 숨은 참조
# msg["Bcc"] = "pjh940114@gmail.com"

msg.set_content("테스트 본문입니다") # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
