from person_dao import Person, Db_operations

class PersonService:
    def __init__(self):
        self.db_ops = Db_operations()
        self.db_ops.create_table()

    def create_person(self, name, gender, dob, location):
        new_person = Person(name, gender, dob, location)
        person_id = self.db_ops.insert_row(new_person)
        return self.get_person_by_id(person_id)

    def get_person_by_id(self, person_id):
        person = self.db_ops.search_row(person_id)
        if person is None:
            return None
        return {
            'id': person[0],
            'name': person[1],
            'gender': person[2],
            'dob': person[3],
            'location': person[4]
        }

    def get_all_persons(self):
        persons_list = self.db_ops.list_all_rows()
        return [
            {'id': p[0], 'name': p[1], 'gender': p[2], 'dob': p[3], 'location': p[4]}
            for p in persons_list
        ]

    def update_person(self, person_id, name, gender, dob, location):
        if self.db_ops.search_row(person_id) is None:
            return None
        updated_person = (name, gender, location, dob, person_id)
        self.db_ops.update_row(updated_person)
        return self.get_person_by_id(person_id)

    def delete_person(self, person_id):
        if self.db_ops.search_row(person_id) is None:
            return False
        self.db_ops.delete_row(person_id)
        return True
