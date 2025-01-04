class Interaction:
    def __init__(self):
        self.id = id

    def identification(self):
        print("Welcome to the student system")
        print("please tell wether you are a \n 1. Student \n 2. Admin")
        id = print(input("Please input the number to the left of the roles."))
        if id == 1:
            adminMenu()
        elif id == 2:
            studentMenu()
        else:
            print("Invalid input, try again.")
            identification()

    def adminMenu():
        pass
    
    def studentMenu():
        pass
        
if __name__ == ("__main__"):
    identification()