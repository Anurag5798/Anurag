import sys

print(sys.argv)
print(type(sys.argv))
if len(sys.argv) > 1:
    print(sys.argv[0])
    print(sys.argv[1])
    print(type(sys.argv[1]))
else:
    print("No additional command line argument provided")
