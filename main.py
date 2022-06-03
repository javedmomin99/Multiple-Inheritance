#Multiple Inheritance:
class Parent1:
    def assign_string_one(self,str1):  #init method is not used since single parameter passed, use only when required to pass mutliple parameters
        self.str1 = str1  #Always write self first and not variable first
    def show_string_one(self):
        print(self.str1)

class Parent2:
    def assign_string_two(self,str2):  #init method is not used since single parameter passed, use only when required to pass mutliple parameters
        self.str2 = str2   #Always write self first and not variable first
    def show_string_two(self):
        print(self.str2)

class Child(Parent1,Parent2):
    def assign_string_three(self,str3):  #init method is not used since single parameter passed, use only when required to pass mutliple parameters
        self.str3 = str3  #Always write self first and not variable first
    def show_string_three(self):
        print(self.str3)

my_child = Child()   #Last Class Take
my_child.assign_string_one("I am string of Parent 1")
my_child.assign_string_two("I am string of Parent 2")
my_child.assign_string_three("I am string of Child")
my_child.show_string_one()
my_child.show_string_two()
my_child.show_string_three()
