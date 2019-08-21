# MosaicKnittingConverter

This Project is meant to help people using knitting machines (like PASSAP E6000) that can do mosaic knitting techniques: perform tuck- and/or slip-stitch patterns with two or more colours. It convertes a mosaic pattern (how the right side of your knitting should look like) into the knitting chart equivalent you can then upload to your knitting machine. 
(friends, help! you know better what to write, heh)

# Functionality
1st Step: Right now it's meant to be a terminal application. The user will decide if he wants to use as input an image or text file with two (1) or three colors (2), or the colors have to be switched (3). For a text file it's easy to automatically figure out if two or free colors are used, but the images have to be tested properly. The colors are selected by the RGB values, and this might lead so some problems if the colors are very similar. The three color version isn't implemented yet.

2nd Step (Two colors): Based on the first line (last for the script) the most common color is selected as black/True/1 while the other one is set as white/False/0. This information is stored in a boolean matrix and is going to be the input for the ConverterBinary() function.

3rd Step: Every even line is being inverted (python is 0-indexed, sor for us it's uneven). In the end the image is flipped and this boolean Matrix returned to the original main function (not implemented yet).

3rd Step: The inverted pattern is stored with a specific extension (txt, image). This works right now only for text files and has to be implmented too.

# Whats works
You can load a textfile which uses 0 and 1 and you'll get the inverted "image" as a text file stored in the folder like the script with the name "output.txt". 
