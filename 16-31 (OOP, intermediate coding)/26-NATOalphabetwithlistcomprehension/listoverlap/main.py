
with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
    file1_list = [int(x.strip()) for x in file1.readlines()]
    file2_list = [int(x.strip()) for x in file2.readlines()]

result = [x for x in file1_list if x in file2_list]

print(result)