#read the file and store all the lines in list
#reverse the list
#write the list back to the file

file1 = open('textFile.txt')

with open('textFile.txt', 'r') as reader:
    content = reader.readline()
    reversed(content)
    with open('textFile.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)