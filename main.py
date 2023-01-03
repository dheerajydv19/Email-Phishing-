# Phishing Email Analysis
import email
import email_headers
import analyzing_headers





# Usage
eml_file = "test.eml"
email_headers.print_email_headers(eml_file)
analyzing_headers.analyze_email_headers(eml_file)
