from sklearn.ensemble import RandomForestClassifier
import joblib


class Classifier:
    def __init__(self):
        # check if the model is exists on disk otherwise throw error
        try:
            self.forestModel = joblib.load('/models/forestModel.joblib')
        except FileNotFoundError:
            print('Model not found. Please train the model first.')
            raise FileNotFoundError

    # predict based on datetime with time zone +0000
    def predict(self, datetime):
        weekday = datetime.weekday()
        hour = datetime.hour
        minute = datetime.minute

        print(f'Predicting for: weekday: {weekday}, hour: {hour}, minute: {minute}')

        prediction =  self.forestModel.predict([[weekday,hour,minute]])[0]

        print (f'Prediction: {prediction}')

        return prediction