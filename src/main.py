# start flask
from datetime import datetime, timezone
from flask import Flask, request, jsonify
from flask_cors import CORS
from classifier import Classifier

# start server at port 8080
app = Flask(__name__)
CORS(app)

# classifier.py run the prediction. GET endpoint with datetime as parameter
@app.route('/predict', methods=['GET'])

def predict():
    # get datetime from query string
    input_datetime = request.args.get('datetime')

    # if datetime is not provided, return 400
    # if no datetime use current datetime with zulu timezone
    if input_datetime is None:
        input_datetime = datetime.now(timezone.utc)

        # handle FileNotFoundError thrown by Classifier
    try:    
        prediction_result = Classifier().predict(input_datetime)

        return jsonify({
            'prediction': prediction_result,
            'datetime': input_datetime.strftime('%Y-%m-%d %H:%M:%S')
        })
    except FileNotFoundError:
        return jsonify({
            'error': 'Model not found. Please train the model first.'
        }), 500
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


# return 404 if the endpoint is not found
@app.errorhandler(404)

def not_found(e):
    return jsonify({
        'error': 'Endpoint not found'
    }), 404

if __name__ == '__main__':
    print('Server is running on port 8080')
    app.run(port=8080, debug=True, host='0.0.0.0')

