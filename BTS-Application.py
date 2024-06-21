class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.left = None
        self.right = None

class ContactBST:
    def __init__(self):
        self.root = None

    def insert(self, name, phone):
        new_contact = Contact(name, phone)
        if self.root is None:
            self.root = new_contact
        else:
            self.recursive_insert(self.root, new_contact)

    def recursive_insert(self, current, new_contact):
        if new_contact.name < current.name:
            if current.left is None:
                current.left = new_contact
            else:
                self.recursive_insert(current.right, new_contact)

    def search(self, name):
        return self.recursive_search(self.root, name)

    def recursive_search(self, current, name):
        if current is None:
            return None
        if current.name == name:
            return current
        elif name < current.name:
            return self.recursive_search(current.left, name)
        else:
            return self.recursive_search(current.right, name)

    def inorder_traversal(self):
        contacts = []
        self.recursive_traversal(self.root, contacts)
        return contacts
    
    def recursive_traversal(self, current, contacts):
        if current:
            self.recursive_traversal(current.left, contacts)
            contacts.append((current.name, current.phone))
            self.recursive_traversal(current.right, contacts)


def main(): 
    contacts = ContactBST()

    contacts.insert("Adauto", "1234-576867")
    contacts.insert("Lois", "5768-132445")
    contacts.insert("Clark", "5555-123412")
    contacts.insert("Mark", "9999-123412")

    search_name = "Adauto"
    contact = contacts.search(search_name)

    if contact:
        print(f"Found contact: {contact.name}, Phone: {contact.phone}")
    else:
        print(f"Contact {search_name} not found")

    all_contacts = contacts.inorder_traversal()
    print("All contacts in alphabetical order:")
    for name, phone in all_contacts:
        print(f"{name}: {phone}")

if __name__ == "__main__":
    main()
