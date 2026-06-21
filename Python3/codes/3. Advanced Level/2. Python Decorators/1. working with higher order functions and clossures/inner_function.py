def outer():
    def inner():
        print("inner function")
    return inner

func = outer()
func()
print(func)