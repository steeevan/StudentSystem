class Interaction:
    def __init__(self):
        self.choice = choice

    def identification(self,choice):
        print("Welcome to the student system")
        print("please tell wether you are a \n 1. Student \n 2. Admin")
        id = print(input("Please input the number to the left of the roles."))
        if id == 1:
            adminMenu()
        elif id == 2:
            studentMenu()
        else:
            print("Invalid input, try again.")
            identification(self)

    def adminMenu():
        print("Welcome to the admin menu")
        print("Press 1 to add a class \n Press 2 to manage a student's grades \n Press 3 to remove a class \n Press 4 to ")
    
    def studentMenu():
        pass
        
if __name__ == ("__main__"):
    identification()