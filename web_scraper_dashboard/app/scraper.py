import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from flask_mail import Mail, Message

def create_app():
    app = Flask(__name__)
    mail = Mail(app)

    app.config['MAIL_SERVER'] = 'your-mail-server'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'your-email-username'
    app.config['MAIL_PASSWORD'] = 'your-email-password'

    def send_mail(subject: str, body: str):
        msg = Message(subject, sender='your-email-username', recipients=['your-email-recipient'])
        msg.body = body
        mail.send(msg)
        return 'Message sent successfully'

    def scrape_website():
        try:
            response = requests.get('https://exemplo.com')
            response.raise_for_status()
        except (requests.HTTPError, requests.ConnectionError) as e:
            send_mail('Error Scraping Website', str(e))
            print(f"Error occurred during website scraping: {e}")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1').text
        description = soup.find('p').text
        price = soup.find('span', class_='price').text

        data = {
            'title': title,
            'description': description,
            'price': price
        }

        return data

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']

            msg_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
            send_mail('New Contact Message', msg_body)

            # Call the scrape_website function when a message is sent
            data = scrape_website()
            if data is not None:
                print(f"Scraped data: {data}")

            return 'Message sent successfully'

        return render_template('contact.html')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)