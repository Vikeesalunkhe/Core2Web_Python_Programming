print("start code")
try:

    fileobj = open("not_file.txt", "r")

except FileNotFoundError:
    print("file not found")

print("End code")
