from classes import classes
class student:
    def __init__(self,name, age, address,phone,gender):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.gender = gender
        self.classList = []
        self.gradeList = []
    
    def add_class(self,className):
        self.classList.append(className)
        self.gradeList.append("A")
        print(f"Class has been succesfully added to {self.name} classes")

if __name__ == "__main__":
    Yanming = student("Yan Ming", 50,"Disneyland Orlando", "11111111","Male")
    myclass = classes("Python","MR E","This is python plus for advanced students")
    yourclass = classes("Spanish", "Mr B","THis is my spansih class")
    Yanming.add_class(myclass)
    Yanming.add_class(yourclass)