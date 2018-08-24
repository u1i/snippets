from os import walk

f = []
for (dirpath, dirnames, filenames) in walk("/Users/uli/Desktop"):
    f.extend(filenames)
    break

print f
