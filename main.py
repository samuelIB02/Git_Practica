print("Welcome to my Git practice project!")

def greet(name):
    if not name.strip():
        return "Please enter a valid name."
    return f"Welcome, {name.strip()}!"

print("Hi, Github")

name = input("What's your name?")
print(greet(name))

print("I'm learning Git and Github with Cursor.")

print("This change has been made from Github.")
