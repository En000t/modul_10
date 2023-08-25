class Field:
    def __init__(self, value=None):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phones = [phone]

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone_value):
        self.phones = [phone for phone in self.phones if phone.value != phone_value]

    def edit_phone(self, old_phone_value, new_phone_value):
        for phone in self.phones:
            if phone.value == old_phone_value:
                phone.value = new_phone_value
                break


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def __getitem__(self, name):
        return self.data.get(name)

    def search_by_name(self, name):
        results = []
        for record in self.data.values():
            if record.name.value == name:
                results.append(record)
        return results

    def search_by_phone(self, phone):
        results = []
        for record in self.data.values():
            for record_phone in record.phones:
                if record_phone.value == phone:
                    results.append(record)
                    break
        return results


if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'

    print('All Ok')
