#import a library
from flask import Flask , render_template , request

#instance of an app
app = Flask(__name__)

@app.route('/')

def hello():
    return render_template('landing.html')   

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/gallery')
def gallary():
    return render_template('gallery.html')

@app.route('/data', methods = ['POST'])
def data():
    first_name = request.form.get('First_Name')
    second_name = request.form.get('second_Name')
    phone = request.form.get('Number')
    email = request.form.get('email')
    print(first_name)
    print(second_name)
    print(phone)
    print(email)

#@app.route('/method_data' , methods = ['Post'])
# def data():
#     preg = request.form.get('preg')
#     plas = request.form.get('plas')
#     pres = request.form.get('pres')
#     skin = request.form.get('skin')
#     test = request.form.get('test')
#     mass = request.form.get('mass')
#     pedi = request.form.get('pedi')
#     age = request.form.get('age')
#     class1 = request.form.get('class')

#     print(preg)
#     print(plas)
#     print(pres)
#     print(skin)
#     print(test)
#     print(mass)
#     print(pedi)
#     print(age)
#     print( class1)
#     return "Form Submitted"


    return 'form submitted'

if __name__ == '__main__':
     app.run()

