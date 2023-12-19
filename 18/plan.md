# Attempt 1:


1. Create a function to take the problem input and generate a list of structs <direction, moves>

2. Determine the length and width of your grid via this loose code:

```
max_length = 0 # the current widest point
max_height = 0 # The current Deepest point
current_length = 0 # where we are in
current_height = 0
for struct in struct_list:
if(struct['direction'] == 'R'):
    current_length += struct['moves']
    if current_length > max_length:
        max_length = current_length

if(struct['direction'] == 'D'):
    current_height += struct['moves']
    if current_height > max_height:
        max_height = current_height

if(struct['direction'] == 'L'):
    current_length -= struct['moves']
    if current_length < 0 :
         raise Exception("Out of Bounds, Left move")

if(struct['direction'] == 'U'):
    current_height -= struct['moves']
    if current_height < 0:
        raise Exception("Out of Bounds, Up move")
```

```
0 X X X
X X X X
X X X X
X X X X
X X X X
This grid, has a height of 5, a length of 4, and '0' is at a point of 0,0
```


3. Initiate a data frame with the proper number of columns and rows with All 0s

Add an extra 100 rows and columns and force everything to be positive

4: Walk through the data frame and fill it in via the struct list

5: Find a way to fill it in

6. Count

