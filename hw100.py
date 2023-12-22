
def remove_contacts(self, id):
    self.contacts = [contact for contact in self.contacts if contact.get("id") != id]

