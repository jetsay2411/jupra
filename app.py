#import a library
from flask import Flask , render_template , request
import joblib

#load the model
model = joblib.load('diabetic_79.pkl')

#instance of an app
app = Flask(__name__)

@app.route('/')

def form():
    return render_template('form.html')   

@app.route('/model_data' , methods = ['POST'])
def model_data():

    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    
    result = model.predict([[preg , plas , pres , skin , test , mass , pedi , age]])

    if result[0] == 0:
        output =  'not a diabetic'
    else:
        output = 'a diabetic'


    return render_template('result.html',predict = output)

if __name__ == '__main__':
     app.run(debug=True)

