def foo(num=0):
    try:
        if type(num) is int:
            return 5 + num
        else:
            return 'please enter a number'
    except TypeError as err:
        return err

if __name__ == "__main__":
    print("Hello World")