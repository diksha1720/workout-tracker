import requests
from datetime import datetime

#retrieve your api keys

APP_ID = 'APP ID'
API_KEY = 'API KEY'
SHEETY_AUTH = 'Authorization header'
sheety_endpoint = 'sheety endpoint'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did")
config = {
    "query": exercise_text,
    "gender": 'female',
    "weight_kg": '62',
    "height_cm": '163',
    "age": '21'
}

response = requests.post(url=exercise_endpoint, json=config, headers=headers)
data = response.json()['exercises']

today = datetime.now()

for ex in data:
    body = {
        'workout': {
            'date': today.strftime('%d/%m/%Y'),
            'time': today.strftime('%H:%M:%S'),
            'exercise': str(ex['user_input']).title(),
            'duration': str(ex['duration_min']),
            'calories': str(ex['nf_calories'])

        }
    }
    response = requests.post(url=sheety_endpoint, json=body, headers=SHEETY_AUTH)
    print(response.text)


