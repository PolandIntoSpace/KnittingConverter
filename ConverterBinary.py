import sys
import numpy as np

# input is np.array with bools
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


print("[START - ConvertBinary()]")
#inputFile = "input.txt"
print("[LOAD] Selecting input file")
inputFile = input("\tPlease enter the filepath (only name is enough if it's in the same folder): ")
#print("\tYour selected file is: " + inputFile)

try:
    # read file into matrix form
    data = np.loadtxt(inputFile, dtype=bool, delimiter=' ')
except Exception as e:
    print("\t[ERROR] Loading failed! Following exception occured: \n\t {:s} \n[END]".format(str(e)))
    sys.exit(1)


print("\n[INVERTING] The even lines are being inverted.")
# invert all even rows (python is 0-index based, so for us all uneven rows)
# range(start, end, step)
nbrRows = len(data)
nbrCols = len(data[0])
dataConv = data

for row in range(nbrRows-2, 0, -2):
    for pix in range(0, nbrCols):
        dataConv[row][pix] = not dataConv[row][pix]

# last line of the sketch is first line in the code due to how the txt file is read.
if nbrRows % 2 == 0:  # if even nbr of all rows invert first(python)/last(sketch) line
    for pix in range(0, nbrCols):
        dataConv[0][pix] = not dataConv[0][pix]

#printpattern(dataConv)

print("[FLIP] Flip pattern horizontally")
dataConv = np.fliplr(dataConv)
#printpattern(dataConv)

# Save file with new pattern
print("[SAVE] Save new pattern as \"output.txt\"")
try:
    np.savetxt("output.txt", dataConv, fmt="%i")
except Exception as e:
    print("\t[ERROR] Saving failed! Following exception occured: \n\t %s\n[END]".format(str(e)))
    sys.exit(1)

print("[END - successfully]")