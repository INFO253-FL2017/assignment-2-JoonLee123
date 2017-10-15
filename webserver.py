import requests
import os


from flask import Flask, render_template, request
# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")

@app.route('/index', methods=['GET'])
def get_index():
	return render_template('index.html')

@app.route('/about', methods=['GET'])
def get_about():
	return render_template('about.html')

@app.route('/contact', methods=['GET'])
def get_contact():
	return render_template('contact.html')

@app.route('/blog/8-experiments-in-motivation', methods=['GET'])
def get_blog_1():
	return render_template('/blog/8-experiments-in-motivation.html')

@app.route('/blog/a-mindful-shift-of-focus', methods=['GET'])
def get_blog_2():
	return render_template('/blog/a-mindful-shift-of-focus.html')

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction', methods=['GET'])
def get_blog_3():
	return render_template('/blog/how-to-develop-an-awesome-sense-of-direction.html')

@app.route('/blog/training-to-be-a-good-writer', methods=['GET'])
def get_blog_4():
	return render_template('/blog/training-to-be-a-good-writer.html')

@app.route('/blog/what-productivity-systems-wont-solve', methods=['GET'])
def get_blog_5():
	return render_template('/blog/what-productivity-systems-wont-solve.html')


@app.route('/index')
def index_page():
    return render_template("index.html")

@app.route('/about')
def about_page():
	return render_template("about.html")

@app.route('/contact', methods=['POST'])
def contact_page():
	name = request.form.get('name')
	email = request.form.get('email')
	subject = request.form.get('subject')
	message = "Name: " + name + "\n" + "E-mail: " + email + "\n" + "Subject: " + subject + "\n" + "Message: " + request.form.get('message')
	

	data = {
		'from': os.environ["INFO253_MAILGUN_FROM_EMAIL"],
		'to': os.environ["INFO253_MAILGUN_TO_EMAIL"],
		'subject': subject,
		'text': message
	}


	auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])

	r = requests.post(
		'https://api.mailgun.net/v3/{}/messages'.format(os.environ["INFO253_MAILGUN_DOMAIN"]),
		auth=auth,
		data=data)

	if r.status_code == requests.codes.ok:
		notifications = "Hi " + name + ", your message has been sent"
	else:
		notifications = "Your email was not sent. Please try again later"

	return render_template("contact.html", notifications=notifications)

@app.route('/blog/8-experiments-in-motivation')
def blog_1():
	blog_1_form = request.form.get('blog_1_form')
	return render_template("8-experiments-in-motivation.html")


@app.route('/blog/a-mindful-shift-of-focus')
def blog_2():
	blog_2_form = request.form.get('blog_2_form')
	return render_template("/blog/a-mindful-shift-of-focus.html")

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
def blog_3():
	blog_3_form = request.form.get('blog_3_form')
	return render_template("/blog/how-to-develop-an-awesome-sense-of-direction")

@app.route('/blog/training-to-be-a-good-writer')
def blog_4():
	blog_4_form = request.form.get('blog_4_form')
	return render_template("/blog/training-to-be-a-good-writer.html")

@app.route('/blog/what-productivity-systems-wont-solve')
def blog_5():
	blog_5_form = request.form.get('blog_5_form')
	return render_template("/blog/what-productivity-systems-wont-solve")
