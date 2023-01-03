# This code is used to print all important email headers
import email

def print_email_headers(eml_file):
  # Parse the email file
  with open(eml_file, "rb") as f:
    msg = email.message_from_binary_file(f)

  # Print the email's headers
  print("Email Header Info -")
  print("From:", msg["From"])
  print("To:", msg["To"])
  print("Subject:", msg["Subject"])
  print("Date:", msg["Date"])
  print("Message-ID:", msg["Message-ID"])
