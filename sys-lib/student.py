from classes import classes

class Student:
    def __init__(self, name, age, address, phone, gender):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.gender = gender
        self.classList = []
        self.gradeList = []

    def view_info(self):
        print(f"")
    
    def view_class(self, class_name):
        pass

    def add_class(self, class_name):
        self.classList.append(class_name)
        self.gradeList.append("A")
        print(f"class has been sucessfully added to {self.name}'s classes")

    def remove_class(self, class_name):
        pass

if __name__ == "__main__":
    student = Student("Yanming", 50,"Disneyland, Orlando", "11111111", "Male")
    