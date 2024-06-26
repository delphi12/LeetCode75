
def findError(filepath):
    error = []
    with open(filepath, 'r') as file1:
        for lineNumber, line in enumerate(file1,1):
            if 'ERROR' in line:
                error.append(str(lineNumber)+" "+line.strip())
    with open('errorlog.txt', 'w+') as file2:
        for i in error:
            file2.write(i+"\n")
    print(error)

file_path = "loginfo.log"
findError(file_path)