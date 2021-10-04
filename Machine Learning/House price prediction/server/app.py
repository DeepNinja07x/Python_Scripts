from flask import Flask , request , jsonify,render_template
import util
app=Flask(__name__)

@app.route('/')
def get_location_names():
    response = util.get_location_names()
    print(response)
    #response.headers.add('Access-control-Allow-origin','*')
    return render_template('app.html',response=response)

@app.route('/predict_house_price',methods=['POST'])
def predict_house_price():
    total_sqft=float(request.form['total_sqft'])
    location = float(request.form['location'])
    bhk = int(request.form['bhk'])
    bath = float(request.form['bhk'])
    response = util.get_location_names()
    #response =jsonify({
    estimated_price = util.get_estimateud_price(location,total_sqft,bhk,bath)
    #})
    return render_template('app.html', response=response,price=estimated_price)
if __name__=="__main__":
    print("Starting Python flask server from Home proce prediction...")
    app.run()