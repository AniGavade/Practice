def build_person(first_name, last_name, age=None):
    """Return a dictionry of information about a person"""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person

musician = build_person("Pushparaj", "Patil", age=31)
print(musician)