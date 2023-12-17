from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    def validate_format(self):
        # Реалізуйте валідацію формату номера телефону
        pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]


# Приклад використання
address_book = AddressBook()

# Додавання записів
record1 = Record("John")
record1.add_phone("1234567890")
record1.add_phone("0987654321")
address_book.add_record(record1)

record2 = Record("Jane")
record2.add_phone("1112223333")
address_book.add_record(record2)

# Пошук запису за іменем
found_record = address_book.find("John")
if found_record:
    print("Знайдено запис:", found_record.name.value)
else:
    print("Запис не знайдено")

# Видалення запису за іменем
address_book.delete("Jane")

# Виконання редагування номера телефону
record = address_book.find("John")
if record:
    old_phone = "1234567890"
    new_phone = "9876543210"
    record.edit_phone(old_phone, new_phone)

# Пошук номера телефону
record = address_book.find("John")
if record:
    phone = "9876543210"
    found_phone = record.find_phone(phone)
    if found_phone:
        print("Знайдено номер телефону:", found_phone.value)
    else:
        print("Номер телефону не знайдено")
