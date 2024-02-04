import pyrebase

config = {
  "apiKey": "AIzaSyDU9UiHKqcivMMc7xdVZ1AzvVQP-LEkOII",
  "authDomain": "task-rn-fd3f2.firebaseapp.com",
  "projectId": "task-rn-fd3f2",
  "storageBucket": "task-rn-fd3f2.appspot.com",
  "messagingSenderId": "209748548575",
  "appId": "1:209748548575:web:73b856e69d7c676f61026a",
  "databaseURL":"https://task-rn-fd3f2-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(config)