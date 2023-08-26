from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder


app = Flask('FLIGHT-PROJECT', template_folder='./templates')

@app.route('/')
def home():
    return render_template('./web.html')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        model = joblib.load('RF_model.pkl')
        Encoder = joblib.load('LinerEncoder.pkl')

        data = request.json        
        
        departure_date = data['departureDate']
        month_name = data['monthName']
        airlines = data['airlines']
        departure_time = data['departureTime']
        time_periods = data['time_periods']
        departure = data['departure']
        duration = data['duration']
        duration_inmin = data['duration_inmin']
        stops = data['stops']
        arrival_time = data['arrivalTime']
        arrival = data['arrival']
        ticket_type = data['ticketType']

        input_features = [departure_date, month_name, airlines, departure_time, time_periods,
                  departure, duration, duration_inmin, stops, arrival_time, arrival, ticket_type]
        print(input_features)
        
        

        encoded_features = Encoder.fit_transform(input_features)
        encoded_features_array = np.array([encoded_features])
        encoded_features_reshape = encoded_features_array.reshape(1, -1)

        # Perform prediction using the model
        prediction = model.predict(encoded_features_reshape)
        print(encoded_features)


        # Return the prediction as a JSON response
        return jsonify({'prediction': prediction.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)