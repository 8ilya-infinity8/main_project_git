from user_class import Registration


def add(a, b):
    print(a + b)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    add(4, 5)
    user1 = Registration('Ден', 'Колесников', 89223456363, 'userx@gmail.com')
    print(user1)
