from flask import Flask, request, render_template
import joblib
import json
import pandas as pd

app = Flask(__name__)


model = joblib.load('eurovision_model.joblib')
with open('feature_columns.json', 'r') as f:
    feature_columns = json.load(f)


@app.route('/')
def home():
    return render_template('index.html', prediction_text='')


@app.route('/predict', methods=['POST'])
def predict():
    try:
       
        song_in_english = int(request.form.get('Song.In.English', 1))
        group_solo      = request.form.get('Group.Solo', 'Solo')
        artist_gender   = request.form.get('Artist.gender', 'Male')
        danceability    = float(request.form.get('danceability', 0.6))
        energy          = float(request.form.get('energy', 0.7))

      
        tempo        = 120.0
        acousticness = 0.2
        valence      = 0.6
        loudness     = -6.0
        liveness     = 0.15

        
        input_dict = {col: 0 for col in feature_columns}

        input_dict['Year']               = 2024
        input_dict['Is.Final']           = 1
        input_dict['Semi.Final.Number']  = 0
        input_dict['Song.In.English']    = song_in_english
        input_dict['Song.Quality']       = 0.5
        input_dict['energy']             = energy
        input_dict['duration']           = 180000
        input_dict['acousticness']       = acousticness
        input_dict['danceability']       = danceability
        input_dict['tempo']              = tempo
        input_dict['liveness']           = liveness
        input_dict['mode']               = 1
        input_dict['loudness']           = loudness
        input_dict['valence']            = valence

        
        input_dict['Artist.gender_Female'] = True if artist_gender == 'Female' else False
        input_dict['Artist.gender_Male']   = True if artist_gender == 'Male' else False
        input_dict['Group.Solo_Solo']      = True if group_solo == 'Solo' else False

        
        input_df = pd.DataFrame([input_dict])
        prediction = model.predict(input_df)[0]
        output = round(prediction, 2)

        prediction_text = f"Predicted Eurovision Points: {output}"

    except Exception as e:
        prediction_text = f"An error occurred: {e}"

    return render_template('index.html', prediction_text=prediction_text)


if __name__ == "__main__":
    app.run(debug=True)
