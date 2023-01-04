import email
import re
import requests
def get_domain_from_email(email):
    # Use a regular expression to extract the domain from the email
    domain = re.search("@([^@]+)", email).group(1)
    return domain
    
def extract_domain(eml_file):
    # Parse the email file
    with open(eml_file, "rb") as f:
        msg = email.message_from_binary_file(f)

    # Extract the domain name of the sender's email address
    sender = msg["From"]
    sender_domain = get_domain_from_email(sender[:-1])
    print(sender_domain)

def whois(domain):
    # Set up the API request
    api_key = "at_W0de4bcAd0NnhTE255S8nB6hEuAiV"
    url = f"https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={api_key}&domainName={domain}&outputFormat=JSON"
    
    # Send the request and receive the response
    response = requests.get(url)
    data = response.json()
    
    # Print the WHOIS data
    print(f"THe whois data of the {domain} is as following")
    print(f"Registrar: {data['registrarName']}")
    print(f"Creation Date: {data['createdDate']}")
    print(f"Expiration Date: {data['expirationDate']}")
    print(f"Registrant: {data['registrant']['name']}")
    print(f"Email: {data['registrant']['email']}")

# Test the function
whois("youtube.com")
