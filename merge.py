from os import walk

# get filenames
_, _, filenames = next(walk('./data'))


# append data file
def append(data):
    with open("data.txt", "a") as file:
        file.write(data)

# loop through files, read data, call append function
for filename in filenames:
    with open('./data/'+filename, 'r') as file:
        data = file.read()
        append(data)

print('Ran to end!')        