class classes:
    def __init__(self,topic,teacher,description,grade):
        self.topic = topic
        self.teacher = teacher
        self.description = description
        self.grade = grade # added grade
        print("Class has been made succesfully")
        pass
    # the 4 __repr__ are to change the class to a string
    def __repr__(self):
        return self.topic
    
    def __repr__(self):
        return self.teacher
    
    def __repr__(self):
        return self.description
    
    def __repr__(self):
        return self.grade
    
    def add_class(self, nameOfClass, nameOfTeacher):
        print("name of class:", nameOfClass, "name of teacher:", nameOfTeacher)
        pass

    def remove_class(self,nameOfClass):
        pass
    
    def print_class_info(self):
        print(f"Class: {self.topic} - Teacher: {self.teacher} - Description: {self.description}")
        pass

if __name__ == "__main__":
    myclass = classes("Python","MR E","This is python plus for advanced students")
    yourclass = classes("Spanish", "Mr B","THis is my spansih class")
    testclasses = [myclass,yourclass]
    for item in testclasses:
        item.print_class_info()
    
