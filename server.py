from flask import Flask, render_template, \
send_from_directory, request, redirect
import csv

app = Flask(__name__)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['GET', 'POST'])
def method_name():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect(f"/thankyou/{data['email']}")
    else:
        return "is the s"


@app.route('/<string:pagename>')
def html_page(pagename):
    return render_template(pagename)


@app.route('/thankyou/<string:name>')
def thankyou_page(name):
    return render_template('/thankyou.html', name=name)



        
