# Adding notes for future references.
name_ext = input("File name: ").lower().strip()

# Not sure if this is the best method, but did I really want to do if/elif? No!
ext = {"gif": "image/gif", "jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "pdf": "application/pdf", "zip": "application/zip", "txt": "text/plain"}

# Splits the input name into filename and extensions.
f_ext = name_ext.rsplit(".")[-1]

# This helped me ensure that the extension was being separated.
# print(f_ext)

# Using the built-in .keys() and .values() methods for dictionaries.
ext_keys = ext.keys()
ext_values = ext.values()

# I used these to print the dictionary values being printed. They helped me make sure I was on the right track.
# print(ext_keys)
# print(ext_values)

# Looks for the file extension, created via f_ext, in the keys of the ext dictionary.
if f_ext in ext_keys:
    # Hey, it works!
    print(ext[f_ext])

# Print everything else.
else:
    print("application/octet-stream")
