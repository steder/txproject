"""
Pretty prints directories like this:

    dirprint/
    |-- printer.py
    `-- testdir/
        |-- subdir/
        |-- |-- test3.txt
        |-- `-- test4.txt
        |-- test1.txt
        `-- test2.txt

"""

import os

lastCounter = {}
buffer = []


def printLine(path, lastFlags):
    #print "flags:", lastFlags
    tailChar = ""
    if os.path.isdir(path):
        tailChar = "/"
    trail = []
    for index, last in enumerate(lastFlags):
        icon = "|-- "
        if last:
            icon = "`-- "
        elif (index + 1) < len(lastFlags):
            icon = "|   "

        if index not in lastCounter:
            lastCounter[index] = {"value":last,
                                  "icon":icon,
                                  "count":0}
        else:
            if lastCounter[index]["value"] == last and last == True:
                lastCounter[index]["count"] += 1
                lastCounter[index]["icon"] = icon
            else:
                lastCounter[index]["value"] = last
                lastCounter[index]["count"] = 0
                lastCounter[index]["icon"] = icon

        #print "lastCounter[%s][\"count\"]: %s (%s)"%(index,
        #                                        lastCounter[index]["count"],
        # len(lastFlags))
        if lastCounter[index]["count"] > 0 and (index + 1) < len(lastFlags):
            icon = "    "
        trail.append(icon)
    name = os.path.basename(path)
    line = "".join(trail) + name + tailChar
    print line
    buffer.append(line)


def walk(top, flags):
    flags.append(False)
    contents = [os.path.join(top, name) for name in os.listdir(top)]
    contents.sort()
    for index, path in enumerate(contents):
        last = ((index+1)==len(contents))
        flags[-1] = last
        printLine(path, flags)
        if os.path.isdir(path):
            flags[-1] = last
            walk(path, flags)
            del flags[-1]


def printDirectory(path):
    """
    takes a single string argument: *path*
    
    returns a pretty formatted string representing the directory at *path*

    """
    global buffer, lastCounter
    buffer = []
    lastCounter = {}
    path = os.path.abspath(path)
    printLine(path, [])
    walk(path, [])
    return "\n".join(buffer)

