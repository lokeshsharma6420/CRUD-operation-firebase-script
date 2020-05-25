from firebase import firebase

firebase = firebase.FirebaseApplication("https://first-project-d85f5.firebaseio.com/",None)
result = firebase.get('/students', '')
print(result)
