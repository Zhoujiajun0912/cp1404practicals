file_object = open(test_file)

name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()