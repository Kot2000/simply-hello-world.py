def start():
    print('please write "hello world"')

    x = input("input: ")
    if x != "hello world":
        print("error")
        return "error"
    print("hello world")
start()

print("you are robot")