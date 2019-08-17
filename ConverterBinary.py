import numpy as np

def printpattern(patternBoolean):
    print("function printpattern")
    for row in patternBoolean:
        row_tmp = []
        for pxl in row:
            if pxl:
                row_tmp.append('X')
            else:
                row_tmp.append('0')
        print(row_tmp)
    #input is np.array with bools



#test for commit
print("Hello World!")
I = np.eye(3)
print(I)

inputFile = "input.txt"

# read file into matrix form
data = np.loadtxt(inputFile, dtype=bool, delimiter=' ')

print('[LOADING] The uploaded input from file {:s} is:'.format(inputFile))
print(data)
print("\n[INVERTING] The even lines are being inverted.")
# invert all even rows (python is 0-index based, so for us all uneven rows)
# range(start, end, step)
nbrRows = len(data)
nbrCols = len(data[0])
dataConv = data;
for row in range(nbrRows-2, 0, -2):
    print(row)
    #print(data[row])
    for pix in range(0, nbrCols):
        dataConv[row][pix] = not dataConv[row][pix]
        #print("Old pixel: {:d}, and new pixel on this spot {:d}".format(data[row][pix],dataConv[row][pix]))

# last line of the sketch is first line in the code due to how the txt file is read.
if nbrRows%2 == 0:  # if even nbr of all rows invert first(python)/last(sketch) line
    for pix in range(0, nbrCols):
        dataConv[0][pix] = not dataConv[0][pix]

print(dataConv)
print("\n")
printpattern(dataConv)

print("[FLIP] Flip pattern horizontally")
dataConv = np.fliplr(dataConv)
printpattern(dataConv)
