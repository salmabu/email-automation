import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your Gmail infoS
EMAIL = "salmabud814@gmail.com"
APP_PASSWORD = "rhxg qdtl zdtv csfr"

# Open and read the CSV file
with open('contacts.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['Name']
        to_email = row['Email']
        message_body = row['Message']

        # Create the email with HTML and plain text
        msg = MIMEMultipart('alternative')
        msg['From'] = EMAIL
        msg['To'] = to_email
        msg['Subject'] = f"Hello {name}👋"

        # Plain version
        text = f"Hello {name},\n\n{message_body}"

        # HTML version
        html = f"""
        <html>
          <body>
            <h2>Hello {name} 👋</h2>
            <p>{message_body}</p>
            <p>
              <a href="https://your-link.com" style="
                 padding: 10px 20px;
                 background-color: #28a745;
                 color: white;
                 text-decoration: none;
                 border-radius: 5px;">
                 Click Here to Learn More
              </a>
            </p>
                <hr>
    <p style="font-size:12px; color:gray;">
      —<br>
      Salma from Somewhere.com<br>
      📧 salmabud814@gmail.com<br>
      📞 +971-XXX-XXXX
    </p>

          </body>
        </html>
        """

        # Attach both formats
        msg.attach(MIMEText(text, 'plain'))
        msg.attach(MIMEText(html, 'html'))

        # Send the email
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(EMAIL, APP_PASSWORD)
                server.send_message(msg)
            print(f"✅ Sent email to {name} at {to_email}")
        except Exception as e:
            print(f"❌ Failed to send email to {to_email}: {e}")
