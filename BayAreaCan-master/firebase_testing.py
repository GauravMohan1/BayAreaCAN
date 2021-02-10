import pyrebase

config = {
  "apiKey": "AIzaSyDQBcsCLRd-yOPcMTAkGdp1zm3blzyT-g8",
  "authDomain": "bayareacan-35619.firebaseapp.com",
  "databaseURL": "https://bayareacan-35619.firebaseio.com/",
  "storageBucket": "bayareacan-35619.appspot.com",
  "serviceAccount": "./ServiceAccountKey.json"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
data = {"phone_number": "+14088056887", "county": "San Francisco"}
db.child("users").push(data)

data = {"phone_number": "+187", "county": "Cisco"}
db.child("users").push(data)
