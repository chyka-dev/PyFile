# PyFile

## More human-friendly file access interface.

You don't have to worry about if a file is open or close,  
its mode is read or write any more.  

## Install

```
git clone git@github.com:chyka-dev/PyFile.git
cd PyFile
python setup.py install
```

## Usage

### Read

```py
>>> file = File("hello.txt")
>>> print(file.read())
hello, PyFile !! 
```

### Write

```py
>>> file = File("hello.txt")
>>> file.write("hello, world !!")
>>> print(file.read())
hello, world !!
```

```py
>>> file = File("hello.txt")
>>> file.writelines(["hello", "world"])
>>> print(file.read())
hello
world
```

### Append

```py
>>> file = File("hello.txt")
>>> print(file.read())
hello
>>> file.append(", world")
>>> print(file.read())
hello, world
```

```py
>>> file = File("hello.txt")
>>> print(file.read())
hello
>>> file.appendlines(["world", "!!"])
>>> print(file.read())
hello
world
!!
```

