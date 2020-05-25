from firebase import firebase

firebase = firebase.FirebaseApplication("https://first-project-d85f5.firebaseio.com/",None)
data={
    'Name' :'test' ,
    'Percentage' : 64 ,
    'RollNo' : 22
}
result = firebase.post('/students',data)
print(result)
