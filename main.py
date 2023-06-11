import sys 

contacts ={}
STOP_WORDS = ['exit', 'good bye', 'close']

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
    if phone == '':
        raise ValueError
    contacts[name] = phone
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

@input_error    
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
        if user_input in STOP_WORDS:
            print('Good bye!')
            return sys.exit()
        
        
run_bot()