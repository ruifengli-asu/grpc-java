import addressbook_pb2

person = addressbook_pb2.Person()
person.id = int(input("Enter person ID number: "))
person.name = "Ruifeng Li"
person.email = "li.rui.ce@gmail.com"
phone = person.phones.add()
phone.number = "4805168116"
phone.type = addressbook_pb2.Person.HOME

print str(person.id)