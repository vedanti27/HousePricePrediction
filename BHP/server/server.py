#Flask file

#import flask
from flask import Flask,request,jsonify
import util

#create app
app = Flask(__name__)

#expose http end point
@app.route('/get_location_names')
def get_location_names():
    #return loc values from json
    response = jsonify({
        'locations' : util.get_locations_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price',methods = ['POST'])
def predict_home_price():
    total_sqft=float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath =int(request.form['bath'])

    response = jsonif({
        'estimated_price':util.get_est_price(location,total_sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("Starting Python Flask server for House Price Prediction...")
    app.run()


#run commands
#Go to Server folder on terminal and execute it
# python server.py
#it returns an url,go to that and mention the func name
#http://127.0.0.1:5000/hello