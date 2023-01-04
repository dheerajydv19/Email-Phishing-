# This code is used to check if the mail is not sended using any kind of spoofing.
import email
import dns.resolver
import dns.reversename

def is_phishing(email_file):

    with open(email_file, 'rb') as f:
        msg = email.message_from_binary_file(f)
    
    try :
        if "emkei.cz" in msg.get_all('Received')[6]:
            return "This is a phishing email."
    except :
        return "This is not a phishing email."

# Test the function

if __name__ == "__main__" : 

    print(is_phishing("test.eml"))
