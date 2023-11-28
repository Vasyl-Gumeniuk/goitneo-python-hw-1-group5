def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments! Please try again."
    
    name, phone = args
    contacts[name] = phone
    return (f"Contact with name '{name}' added.")


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments! Please try again."
    
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return (f"Contact with name '{name}' updated.")
    else:
        return (f"The contact with name '{name}' does not exist")
    

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid arguments! Please try again."
    
    name = args[0]

    if name in contacts:
        return (f"Contact with name '{name}' has phone number '{contacts[name]}'.")
    else:
        return (f"The contact with name '{name}' does not exist")


def show_all(contacts):
    if not contacts:
        return "No contact yet! Please add a contact."
    
    message_all_contacts = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
        
    return message_all_contacts
    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")
    


if __name__ == "__main__":
    main()