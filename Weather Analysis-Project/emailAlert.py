

import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Example weather alert function
def send_weather_alert(alert, email_config):
    try:
        subject = f"Weather Alert: {alert['Type']} Warning"
        body = (f"Weather Alert Details:\n"
                f"Type: {alert['Type']}\n"
                f"Date: {alert['Date'].strftime('%Y-%m-%d %H:%M')}\n"
                f"Location: {alert['Location']}\n"
                f"Severity: {alert['Severity']}\n"
                f"Details: {alert['Details']}")
        
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = email_config['sender_email']
        msg['To'] = email_config['receiver_email']
        
        with smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port']) as server:
            server.starttls()
            server.login(email_config['sender_email'], email_config['sender_password'])
            server.send_message(msg)
        print(f"Email sent for weather alert at {alert['Date']}")
    except Exception as e:
        print(f"Email error: {e}")


# Example usage: simulate alert condition and send
email_config = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'sender_email': 'abhaykush050804@gmail.com',
    'sender_password': 'kckjuyxwyjycalye',  # Use Gmail App password for SMTP
    'receiver_email': 'akks1925@gmail.com'
}

# Simulated weather alert data
weather_alert = {
    'Type': 'Heatwave',
    'Date': datetime.now(),
    'Location': 'New York City',
    'Severity': 'High',
    'Details': 'Temperatures expected to exceed 40°C for the next 3 days. Stay hydrated!'
}

# Send alert email
send_weather_alert(weather_alert, email_config)

