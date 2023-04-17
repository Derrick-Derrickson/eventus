#this file holds the supplier class
#each supplier can provide GAS (goods and services)
#each supplier has a list of contacts

#contacts are a subclass of supplier
#GAS is a subclass of supplier

class supplier:
    class contact:
        def __init__(self, name, email, phone, address):
            self.name = name
            self.email = email
            self.phone = phone
            self.address = address
    
    class GAS:
        def __init__(self, name, description, overhead_price, unit_price):
            self.name = name
            self.description = description
            self.overhead_price = overhead_price
            self.unit_price = unit_price
    
    def __init__(self, name, description, contacts, GASs):
        self.name = name
        self.description = description
        self.contacts = contacts
        self.GASs = GASs


