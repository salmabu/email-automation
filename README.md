Email Automation with Python
-----------------------------
This project sends personalized emails to multiple contacts from a CSV file using Python and Gmail SMTP.


>> Features

- Reads contacts from a CSV file (contacts.csv) with columns: Name, Email, Message.
- Sends both plain text and nicely formatted HTML emails.
- Personalizes the email greeting for each contact.
- Supports adding attachments (like PDFs).
- Includes a clickable button and company signature in the email.
- Uses Gmail’s SMTP server with secure login (app password).



>> How to Use

1. Clone or download this repository. 
2. Create a contacts.csv file in the project folder with these columns:

Name,Email,Message
Alice,alice@example.com,Hello Alice! This is a test message.
Bob,bob@example.com,Hello Bob! This is another message.

3. Replace EMAIL and APP_PASSWORD in the Python script with your Gmail address and app password.
4. (Optional) Add any files you want to attach in the project folder (e.g., invoice.pdf).
5. Run the Python script: python send_emails.py
6. Check your console for success/failure messages.



>> Important Notes

- You must enable 2-step verification on your Gmail account and generate an app password to use with this script.
- Keep your app password secret. Don’t share it or upload it publicly.
- This script uses a secure SSL connection to Gmail.



>> How It Works

- The script reads each contact from the CSV.
- Creates a personalized email for each person.
- Sends the email through Gmail SMTP.
- Prints a success or error message for each email.



>> Contact

For questions, email: salmabud814@gmail.com