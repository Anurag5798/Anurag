def my_function(*args):
    print(args, end='  ')
    print(type(args), end='  ')
    if args:
        print(args[0], end='  ')
        print(args[-1])
    else:
        print("No arguments provided")

my_function(10)
my_function(1, 2, 3)
my_function([1, 2, 3, 5], 4, 5, 8)
my_function()
