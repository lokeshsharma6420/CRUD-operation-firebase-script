from firebase import firebase

firebase = firebase.FirebaseApplication("https://first-project-d85f5.firebaseio.com/",None)
firebase.put('/students/-M5k7ohbIcmSini5VTQ2','Name','Ravi')
print('updated database')
