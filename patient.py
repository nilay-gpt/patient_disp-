class Patient:
	def __init__(self,pid,name,gender,age,phone):

		self.mbr_id = pid
		self.name = name
		self.gender = gender
		self.age = age
		self.phone = phone

	def read(self):
		return "".join(["display-->","Id : ",str(self.mbr_id),"\nName : ",self.name,"\nGender : ",self.gender,"\nAge : ",self.age,"...Phone : ",self.phone ])


from bottle import get, post, request,route, run, template,put,delete
pat_dict = {}

@route('/')
@route('/patient')
def patient():
    return '<b>do the /create,/update,/delete</b>!'

@post('/patient')
def create():
    pid  = request.POST['pid']
    name = request.POST['name']
    gender = request.POST['gender']
    age = request.POST['age']
    phone = request.POST['phone']
    temp_pat = Patient(pid,name,gender,age,phone)
    pat_dict.update({pid:temp_pat})
    return '<b>Patient Created with ID {0}'.format(pid)

@get('/patient/<pid>')
def read(pid):
	return pat_dict[pid].read()

@put('/patient/<pid>')
def update(pid):
	mbr_id = request.POST['mbr_id']
	if mbr_id != pid:
		return "Access Denied"
	pat_dict[pid].name = request.POST['name']
	pat_dict[pid].gender = request.POST['gender']
	pat_dict[pid].age = request.POST['age']
	pat_dict[pid].phone = request.POST['phone']

	return "Updated Sucessfully ".join([str(mbr_id)])

@delete('/patient/<pid>')
def delete(pid):
	del(pat_dict[pid])
	return "Deleted Sucessfully"

run(host='0.0.0.0', port=9977)
