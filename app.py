from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)
app.secret_key = 'jT4RzqLmR4B9bQwZH3fSgTUV8kHy'

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'contact.form2307@gmail.com'
app.config['MAIL_PASSWORD'] = 'wlfqkpkvfasoyvbp'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Initialize Flask-Mail
mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/service")
def service():
    return render_template("service.html")


@app.route("/containers")
def containers():
    return render_template("containers.html")


@app.route("/adr")
def adr():
    return render_template("adr.html")


@app.route("/slopage")
def slopage():
    return render_template("slopage.html")


@app.route("/sloservice")
def sloservice():
    return render_template("sloservice.html")


@app.route("/slocontainers")
def slocontainers():
    return render_template("slocontainers.html")


@app.route("/sloadr")
def sloadr():
    return render_template("sloadr.html")




@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process the form data
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        delivery_option = request.form['delivery_option']
        special_note = request.form['special_note']

        try:
            # Validate email address
            v = validate_email(email)
            email = v.email

            # Send the email
            msg = Message('Nov obrazec - spletna stran',
                          sender=('LeLog-spletna stran', 'contact.form2307@gmail.com'),
                          recipients=['amefis1991@gmail.com'])
            msg.body = f"Name: {name}\nEmail: {email}\nMobile: {mobile}\nDelivery Option: {delivery_option}\nSpecial Note: {special_note}"
            mail.send(msg)

            success_message = 'Thank you for your message!'
            flash(success_message, 'success')
            return redirect('/')
        except EmailNotValidError:
            flash('Please enter a valid email address.', 'error')
        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'error')

    return render_template('/')


if __name__ == '__main__':
    app.run(debug=True)
