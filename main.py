import sys 
from collections import UserDict

STOP_WORDS = ['exit', 'good bye', 'close']


class Field():
    def __init__(self, value=None):
        self.value = value
    
class Name(Field):
    def __init__(self, value):
        self.value = value
            
class Phone(Field):
    def __init__(self, value):
        self.value = value

class Record:
    
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        
    def remove_phone(self, phone):
        self.phone = [p for p in self.phone if p.value != phone]
        
    def edit_phone(self, old_phone, new_phone):
        for phone in self.phone:
            if phone.value == old_phone:
                phone.value = new_phone
                break

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

contacts = AddressBook()


def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            print("Enter user name")
        except ValueError:
            print("Give me name and phone please")
        except IndexError:
            print("Invalid input. Please try again.")    
    return inner

def greet():
    result = 'How can I help you?'
    return result

@input_error
def new_contact(user_input):
    parts = user_input.split(" ")
    if len(parts) != 3:
        raise ValueError
    name = parts[1]
    phone = parts[2]
    
    if name not in contacts:
        record = Record(name)
        record.add_phone(phone)
        contacts.add_record(record)
        
    if phone == '':
        raise ValueError
    
    result = 'Contact was successfully created'
    return result

@input_error
def change_contact(user_input):
    parts = user_input.split(" ")
    if len(parts) != 3: 
        raise IndexError
    name = parts[1]
    phone = parts[2]
    if name not in contacts:
        raise IndexError
    contacts[name] = phone
    result = 'Contact was successfully updated'
    return result 

@input_error
def show_contact(user_input):
    parts = user_input.split(" ")
    if len(parts) != 2:
        raise KeyError
    name = parts[1]
    if name is name.isdigit():
        raise IndexError
    return contacts[name]

def show_all():
        return contacts

    
def process_input(user_input):
    listed_user_input = user_input.split(' ')
    command = listed_user_input[0].lower()
    if command == 'hello':
        return greet()
    elif command == 'add':
        return new_contact(user_input)
    elif command == 'change':
        return change_contact(user_input)
    elif command == 'phone': 
        return show_contact(user_input)
    elif command == 'show':
        return show_all()
        

def run_bot():
    while True:
        user_input = input("Write your request: ")
        if user_input not in STOP_WORDS:
            print(process_input(user_input))
        elif user_input in STOP_WORDS:
            print('Good bye!')
            return sys.exit()
        
        
run_bot()