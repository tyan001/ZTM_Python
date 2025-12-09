
# my_file = open('test.txt', 'r')
# print(my_file)
# print(my_file.read())
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())

# my_file.seek(0)
# print(my_file.readlines())
# my_file.close()


with open("test.txt", 'r') as f:
    print(f.readlines())
    
    
    