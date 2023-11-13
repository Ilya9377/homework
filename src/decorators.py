import datetime


def log(filename="error.txt"):
    def my_decor(function):
        def inner(*args, **kwargs):
            with open(filename, "a") as f:
                data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                try:
                    result = function(args, kwargs)
                    f.write(f"{data} {function.__name__} ok\n")
                    return result
                except Exception as e:
                    f.write(f"{data} {function.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                    return None
        return inner
    return my_decor


@log(filename="src/mylog.txt")
def my_function(x, y):
    print(x, y)
    return x + y


my_function(1, 2)
