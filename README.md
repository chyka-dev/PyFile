# PyFile

## More human-friendly file access interface.

## Install

TODO

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

