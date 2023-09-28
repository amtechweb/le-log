from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message
from email_validator import validate_email, EmailNotValidError
app = Flask(__name__)

app.secret_key = 'jT4RzqLmR4B9bQwZH3fSgTUV8kHy'

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'contact.form2307@gmail.com'  # Enter your Gmail address here
app.config['MAIL_PASSWORD'] = 'wlfqkpkvfasoyvbp'  # Enter your Gmail password here
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Initialize Flask-Mail
mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process the form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        try:
            # Validate email address
            v = validate_email(email)
            email = v.email

            # Send the email
            msg = Message('New Contact Form Submission',
                          sender=('Zarometix', 'contact.form2307@gmail.com'),
                          recipients=['amefis1991@gmail.com'])
            msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
            mail.send(msg)

            success_message = 'Hvala za vaše sporočilo!'
            flash(success_message, 'success')
            return redirect('/contact')
        except EmailNotValidError:
            flash('Vnesite veljaven e-poštni naslov.', 'error')
        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'error')

    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)
