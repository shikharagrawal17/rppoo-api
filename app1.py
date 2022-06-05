import firebase_admin
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate('rppoop-112003005-06-firebase-adminsdk-toebh-4064762f69.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://rppoop-112003005-06-default-rtdb.firebaseio.com'
	})

ref = db.reference()

new_comp = ref.child('Company').push({
    'name' : 'Google', 
    'logo' : 'https://blog.hubspot.com/hubfs/image8-2.jpg',
    'placements' : '10',
    'averageSalary' : '100000000',
    'rounds' : '3'
})

new_comp1 = ref.child('Company').push({
    'name' : 'Microsoft',
    'logo' : 'http://blog.ncce.org/wp-content/uploads/2015/02/microsoft-logo.jpg',
    'placements' : '5',
    'averageSalary' : '500000000',
    'rounds' : '7'
})