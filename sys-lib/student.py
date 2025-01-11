from classes import classes
class student:
    def __init__(self,name, age, address,phone,gender):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.gender = gender
        self.classtopicList = []
        self.classList = []
        self.gradeList = []

    def add_class(self,className):
        self.classtopicList.append(f"{className.topic}")
        self.classList.append(f"{className}")
        self.gradeList.append(f"{className}:{className.grade}")
        print(f"{className.topic} has been succesfully added in {self.name}'s classes")
    
    def remove_class(self,className):
        self.classtopicList.remove(f"{className.topic}")
        self.classList.remove(f"{className}")
        self.gradeList.remove(f"{className}:{className.grade}")
        print(f"{className.topic} has been sucessfully removed in {self.name}'s classes.")
    
    def view_class(self,className):
        if className.topic in self.classtopicList:
            print(f"Topic: {className.topic}")
            print(f"Teacher: {className.teacher}") 
            print(f"Description: {className.description}")
            print(f"Grade: {className.grade}")
        else:
            print(f"You are not enrolled in {className.topic}.")

    def view_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone}")
        print(f"Gender: {self.gender}")
        print(f"Classes: {self.classtopicList}")
if __name__ == "__main__":
    Yanming = student("Yanming", 50,"Disneyland Orlando", "11111111","Male")
    myclass = classes("Python","MR E","This is python plus for advanced students","A")
    yourclass = classes("Spanish", "Mr B","THis is my spansih class","A")