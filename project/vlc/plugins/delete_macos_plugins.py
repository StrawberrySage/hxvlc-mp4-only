import os

dlls = []
for directory in os.listdir("Windows"):
    if directory != "plugins.dat":
        for dll in os.listdir(os.path.join("Windows", directory)):
            dlls.append(dll.split(".")[0])

for file in os.listdir("MacOS"):
    dll = file.split(".")
    if dll[1] == "dylib":
        if not dll[0] in dlls:
            os.remove(os.path.join("MacOS", file))
    elif dll[1] == "jar":
        os.remove(os.path.join("MacOS", file))
