from datetime import datetime

def file_path(path: str):

        def log_check(func):

            def new_func(*args):
                result = func(*args)
                file = open(path, "a")
                file.write(f"date: {datetime.now()},name: {func.__name__},input: {args},output: {func(*args)}\n")
                return result
            return new_func
        return log_check

my_file_path = file_path("D:\decorator\logs.txt")

@my_file_path
def func(a, b):
    return (a + b)
if __name__ == '__main__':
    func(7,10)


