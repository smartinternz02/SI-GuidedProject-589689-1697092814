


from flask import Flask, render_template, request
import pickle
import datetime as dt
import calendar
import os


import pickle
from flask import Flask, render_template, url_for,request
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.


# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def index():
	return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    store = request.form.get('store')
    dept = request.form.get('dept')
    date = request.form.get('date')
    isHoliday = request.form['isHolidayRatio']
    size = request.form.get('size')
    temp = request.form.get('temp')
    d=dt.datetime.strptime(date, '%Y-%m-%d')
    year = (d.year)
    month = d.month
    month_name = calendar.month_name[month]
    print("year =", type(year))
    print("year val= ", year, type(year), month)
    X_test = pd.DateFrame({'Store':[store], 'Dept': [dept],  'Size': [size],
                           'Temperature':[temp], 'CPI':[212], 'Markdown4':[2050],
                           'IsHoliday': [isHoliday], 'Type_B': [0], 'Type_C': [1],
                           'month': [month], 'year': [year]})
    print("X_test =", X_test.head())
    print("type of X_test=", type(X_test))
    print("predict =", store, dept, date, isHoliday)

    y_pred = loaded_model.predict(X_test)
    output = round(y_pred[0],2)
    print("predicted = ", output)
    return render_template('index.html', output = output, store = store, dept = dept, month_name = month_name, year = year)
port = os.getenv('VCAP_APP_PORT', '8080')
# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run(debug=True)
