class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts: dict) -> None:
    Person.people = {}

    persons = []
    for pd in people_dicts:
        p1 = Person(pd["name"], pd["age"])
        persons.append(p1)

    for pd in people_dicts:
        p1 = Person.people[pd["name"]]
        if "wife" in pd and pd["wife"] is not None:
            p1.wife = Person.people[pd["wife"]]
        if "husband" in pd and pd["husband"] is not None:
            p1.husband = Person.people[pd["husband"]]

    return persons
