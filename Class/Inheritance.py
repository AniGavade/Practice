class Family:
    def __init__(self, family_name, number_of_members, country):
        self.family_name = family_name
        self.number_of_members = number_of_members
        self.country = country

    def member_says(self):
        print(f"Hey, I am from {self.family_name} family and there are {self.number_of_members} members in family")


class Family_detailed(Family):
    def __init__(self, family_name, number_of_members, country, family_income):
        super().__init__(family_name, number_of_members, country)
        self.family_income = family_income

    def which_country(self):
        print(f"The {self.family_name} family has roots from {self.country}")

    def member_says(self):
        print(f"Hey, I am from {self.family_name} family and there are {self.number_of_members} members in family {self.family_income} income")
        super().member_says()


b = Family_detailed("Ambani", 10, "India", 1000000000000000000)
c = Family("Adani", 5, "India")
b.which_country()
b.member_says()
c.member_says()


