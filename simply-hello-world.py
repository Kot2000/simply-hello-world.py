def start():
    print('please write "hello world"')

    x = input("input: ")
    if x != "hello world":
        print("error")
        print("you are robot")
        return "error"
    print("hello world")
    return "hello world"
start()

