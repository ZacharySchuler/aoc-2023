import pandas as pd

class digObject:
    direction = ""
    spaces = 0

    def __init__(self,direction,spaces):
        self.direction = direction
        self.spaces = spaces


def problemStringToStruct(problem_string):
    # Takes in problem string and returns a list of structs <direction,number>
    rawList = problem_string.splitlines()
    struct_list = []
    for item in rawList:
        rowList = item.split()
        direction = rowList[0]
        spaces = rowList[1]
        digObj = digObject(direction, spaces)
        structList = struct_list.append(digObj)
    print(struct_list)
    return struct_list

def determineSizeOfMatrix(struct_list):
    max_length = 0 # the current widest point
    max_height = 0 # The current Deepest point
    max_neg_length = 0 # the current widest point
    max_neg_height = 0 # The current Deepest point
    current_length = 0 # where we are in
    current_height = 0
    for struct in struct_list:
        print("ran")
        if(struct.direction == 'R'):
            current_length += int(struct.spaces)
            if current_length > max_length:
                max_length = current_length
                print("new record, max_length=" + str(current_length))

        if(struct.direction == 'D'):
            current_height += int(struct.spaces)
            if current_height > max_height:
                max_height = current_height

        if(struct.direction == 'L'):
            current_length -= int(struct.spaces)
            if current_length < max_neg_length:
                max_neg_length = current_length

        if(struct.direction == 'U'):
            current_height -= int(struct.spaces)
            if current_height < max_neg_height:
                max_neg_height = current_height
    return [max_length,max_height, max_neg_length, max_neg_height]



def calculateMatrixSice():
    print("")

# Takes in the problem string and 
    

print("Hello World")

problem_string = """R 4 (#4b18e0)
U 4 (#0b4f93)
R 4 (#6d70b0)
U 12 (#86edc3)
R 4 (#435460)
U 3 (#07f023)
R 8 (#33dd00)
U 5 (#599aa3)
L 11 (#83c702)
U 5 (#3f0501)
L 7 (#4bf232)
U 9 (#3f0503)
L 2 (#4955d2)
U 5 (#24f2e3)
L 9 (#16abf2)
U 6 (#60f753)
L 3 (#678dd2)
U 3 (#736093)
L 3 (#007482)
D 7 (#446e11)
L 6 (#0482a2)
D 8 (#997fd1)
L 4 (#4891e2)
D 6 (#2547b1)
L 5 (#501bf2)"""



struct_list = problemStringToStruct(problem_string)
print(len(struct_list))
size_list = determineSizeOfMatrix(struct_list)
print(size_list)


