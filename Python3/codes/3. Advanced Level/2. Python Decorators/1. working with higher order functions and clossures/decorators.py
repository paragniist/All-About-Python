def email_decorators(func):
    def wrapper():
        print("Dear interns,")
        func()
        print("Best regards , ")
        print("your new boss")
    return wrapper

def greeting_meeting():
    print("Welcome to your new job!")

greeting_meeting = email_decorators(greeting_meeting)
greeting_meeting()