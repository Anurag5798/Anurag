class Person:
    def __init__(self, name, gender, dob, location):
        self.id = None
        self.name = name
        self.gender = gender
        self.dob = dob
        self.location = location

class Db_operations:
    def __init__(self):
        self._persons = []
        self._next_id = 1

    def create_table(self):
        self._persons = []
        self._next_id = 1

    def insert_row(self, person):
        person.id = self._next_id
        self._next_id += 1
        self._persons.append(person)
        return person.id

    def search_row(self, person_id):
        person_id = int(person_id)
        for p in self._persons:
            if p.id == person_id:
                return (p.id, p.name, p.gender, p.dob, p.location)
        return None

    def list_all_rows(self):
        return [(p.id, p.name, p.gender, p.dob, p.location) for p in self._persons]

    def update_row(self, updated_person_tuple):
        # updated_person_tuple: (name, gender, location, dob, id)
        person_id = int(updated_person_tuple[4])
        for p in self._persons:
            if p.id == person_id:
                p.name = updated_person_tuple[0]
                p.gender = updated_person_tuple[1]
                p.location = updated_person_tuple[2]
                p.dob = updated_person_tuple[3]
                return True
        return False

    def delete_row(self, person_id):
        person_id = int(person_id)
        for i, p in enumerate(self._persons):
            if p.id == person_id:
                del self._persons[i]
                return True
        return False
