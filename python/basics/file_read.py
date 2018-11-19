with open("file.txt", mode='rb') as file_handle:
	file_content = file_handle.read()
file_handle.close()

# or 
import fileinput

for line in fileinput.input():
    print line

