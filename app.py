from flask import Flask, render_template, url_for, redirect, request, flash
from forms import EmailForm
from flask_mail import Mail, Message
import os

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'Secrt_key😅'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

mail = Mail(app)

@app.route("/")
@app.route("/home")
def home():
	return render_template('about.html', title='Mahmoud AL-Mokdad')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = EmailForm()
    if form.validate_on_submit():
        msg = Message(form.subject.data, sender='sender@gmail.com', recipients=['recipient@gmail.com'])
        msg.body= f"""{form.email.data}
{form.name.data}
{form.message.data}"""

        mail.send(msg)
        flash('Your Email Has Been Sent, Thanks!', 'flashed-success')
        form.name.data = ""
        form.email.data = ""
        form.subject.data = ""
        form.message.data = ""
    elif request.method == 'POST':
        flash('Your Email Is Invalid please Check of Its!', 'flashed-danger')
    return render_template('contact.html', title='Mahmoud - Contact Me', form=form)



@app.route("/about_me")
def about():
    return render_template('about.html', title='Mahmoud AL-Mokdad')


@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html', title='Mahmoud - Portfolio')
@app.route("/youtube")
def youtube():
    return render_template ('youtube.html', title='Youtube Channel')
#---------------------------------------------------------------------------
#                  ERORRS
# app name
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(error):
# defining function
    return render_template("error_404.html", title='Not found')

@app.errorhandler(500)
# inbuilt function which takes error as parameter
def not_found(error):
# defining function
    return render_template("error_500.html", title='Somthing Wrong')

if __name__ == "__main__":
    app.run()

