"""
poetry add resend
"""
import resend

resend.api_key = ""

params = {
  "from": "Acme <onboarding@resend.dev>",
  "to": ["email_address@gmail.com"],
  "subject": "hello world",
  "html": "<p>it works!</p>"
}

email = resend.Emails.send(params)
print(email)