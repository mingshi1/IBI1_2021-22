# creat class named stuff
# def init with first name, last name, location, role
# print
class Stuff():
    def __init__(self,first_name,last_name,location,role):
        self.first_name=first_name
        self.last_name=last_name
        self.location=location
        self.role=role  # give names

    def printinfo(self):
        print('first name: ',self.first_name )
        print('last name: ',self.last_name )
        print('location: ',self.location)
        print('role: ',self.role)   # print
### example
a=Stuff('X', 'xx', 'International Campus', 'faculty')
a.printinfo()
