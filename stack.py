'''stack = []

while True:
    print("\nOptions:")
    print("1. Push")
    print("2. Pop")
    print("3. View Stack")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        element = input("Enter element to push: ")
        stack.append(element)
        print(f"{element} pushed onto stack.")
    
    elif choice == '2':
        if len(stack) == 0:
            print("Stack is empty. Nothing to pop.")
        else:
            popped = stack.pop()
            print(f"Popped: {popped}")
    
    elif choice == '3':
        print("Current Stack:", stack)
    
    elif choice == '4':
        print("Exiting program.")
        break
    
    else:
        print("Invalid choice. Try again.")
'''

myList=[]

def add_list(value):
    myList.append(value)
def remove_stack():
    myList.pop()
add_list(5)
add_list(7)
add_list(8)
add_list(9)
print(myList)
remove_stack()
print(myList)