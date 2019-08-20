import sys
import os
import numpy as np
from PIL import Image


"""
Start of the ConverterBinary() programm
Note: The selection of the file and options will be moved to main(). Right now they're here to have less steps to work
with. But in the future ConverterBinary() should receive an np.array filled with booleans for black/white. 
"""

print("[START - ConvertBinary()]")
#inputFile = "input.txt"  # harcoded
print("[LOAD] Selecting input file")
inputFile = input("\tPlease enter the filepath (only name is enough if it's in the same folder): ")

"""
Step ?
    Check the input file and chose based on the file ending which procedure to follow.
    Note: This will be done later by main() so ConvertBinary() won't know what type the input was.
"""
filename, file_extension = os.path.splitext(inputFile)
if file_extension == '.txt':
    try:
        # read file into matrix form
        # TODO!: works only with boolean (0,1) now. Adapt to don't care about way black/white are saved in .txt.
        # TODO!: check first line (last for our script) and select the more often appearing char as black
        #  (bool True or int 1)
        # TODO!: after selecting which char is black (True) fill up matrix with True/ones for black
        data = np.loadtxt(inputFile, dtype=bool, delimiter=' ')
    except Exception as e:
        print("\t[ERROR] Loading failed! Following exception occured: \n\t {:s} \n[END]".format(str(e)))
        sys.exit(1)  # right now only boolean .txt works

elif file_extension == '.jpg' or file_extension == '.png':  # TODO!: extend by more image formats which are supported
    im = Image.open(inputFile)
    pix = im.load()
    width, hight = im.size  # Get the width and hight of the image for iterating over
    # TODO!: have a look at first line (last for our script) and select the most common color as black (True)
    # TODO!: based on selected color (True) fill up a boolean matrix
    # TODO!: If two similar colors appear, e.g. yellow and orange, decide how to make sure which is 1 or 0.

    for w in range(0, width):
        for h in range(0, hight):
            print(pix[w, h])  # print RGBA Value of each pixel
    sys.exit(1)  # That's it for the images as input. Will be added soon.

"""
Other usefull information:
    pix[x, y] = value  # Set the RGBA Value of the image (tuple)
    im.save('alive_parrot.png')  # Save the modified pixels as .png

    white 	#FFFFFF 	rgb(255,255,255)
    black                 rgb(0, 0, 0)
    grey                  rgb(128,128,128)

    In case of a .gif file it has first to be converted to a RGB scale:
    if  '.gif':   rgb_im = im.convert('RGB') 
"""


"""
This is the part which ConvertBinary() will take care in the future.
Input: np.array with booleans
Output: np.array with booleans
The Output can be checked in the terminal using printpattern(dataConv).
"""

"""
1.Step
    Invert all even rows (python is 0-index based, so for us all uneven rows)
"""
print("\n[INVERTING] The even lines are being inverted.")
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


"""
2.Step
    Flip the picture horizontally.
"""
print("[FLIP] Flip pattern horizontally")
dataConv = np.fliplr(dataConv)
#printpattern(dataConv)


"""
This would be it, end of ConvertBinary(). It would return the binary array.
But due to the fact we're still figuring stuff out it's all together. Sorry :3
Next step is to save the output file.
"""

"""
Step ?
    Save file with new pattern. Location and name to be specialized in the future work.
"""
# TODO!: Ask where to store file, how to name it and maybe even which (image) format to use.
print("[SAVE] Save new pattern as \"output.txt\"")
try:
    np.savetxt("examples/output.txt", dataConv, fmt="%i")
except Exception as e:
    print("\t[ERROR] Saving failed! Following exception occured: \n\t %s\n[END]".format(str(e)))
    sys.exit(1)

print("[END - successfully]")



########################################################################################################################
"""
function printpattern()
input:
    patternBoolean  it's an boolean array in the np.ndarray format
output:
    -
This helper function just takes the boolean array and prints it on the console in a more readable way using "x" and "-".
It can be changed to something more readable or maybe extended in the future to store it this way in the output.txt file
instead of using 1 and 0.
"""

def printpattern(patternBoolean):
    print("function printpattern")
    for row in patternBoolean:
        row_tmp = []
        for pxl in row:
            if pxl:
                row_tmp.append('x')
            else:
                row_tmp.append('-')
        print(row_tmp)

