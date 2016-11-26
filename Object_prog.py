class Contact(object):
    def __init__(self, first_name, last_name, phone, birth_year, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.birth_year = birth_year
        self.email = email

    def get_full_name(self):
        return self.first_name + " " + self.last_name

john = Contact(first_name="John", last_name="Jackson", phone="00000", birth_year="1987", email="jj@jj.com")
lara = Contact(first_name="Lara", last_name="Jackson", phone="12345", birth_year="2009", email="jj@jj.com")
jaka = Contact(first_name="Jaka", last_name="Marinsek", phone="987654", birth_year="1975", email="jj@jj.com")

contacts = [john, lara, jaka]

for person in contacts:
    print person.get_full_name()