# -*- coding:utf-8 -*-

import six
import codecs


class File(object):
    """
    Usage:
        file = File(".bashrc")
        file.write("Hello, world!!")
        print(file.read())
        del file
    """
    class Mode:
        r = "r"
        w = "w"
        a = "a+"

    def __init__(self, path, encoding="utf-8"):
        self.path = path
        self.encoding = encoding
        self.mode = None
        self._fd   = None

    def __del__(self):
        self.ensure_close()

    def __str__(self):
        return "<File object: path={}, encoding={} mode={}".format(
            self.path, self.encoding, self.mode 
        )

    def __unicode__(self):
        return u"<File object: path={}, encoding={} mode={}".format(
            self.path, self.encoding, self.mode 
        )

    def top(self):
        """
        Usage:
            >>> file = File("hello.txt")
            >>> print(file.read())
            hello, world
            >>> print(file.read())

            >>> print(file.top())
            >>> print(file.read())
            hello, world
        """
        return self.seek(0)

    def end(self):
        """
        Usage:
            >>> file = File("hello.txt")
            >>> print(file.end())
            >>> print(file.read())

        """
        return self.seek(0, 2)

    def seek(self, *args, **kwargs):
        self.ensure_open(self.Mode.r)
        return self._fd.seek(*args, **kwargs)

    def read(self, *args, **kwargs):
        """
        Usage:
            >>> file = File("hello.txt")
            >>> print(file.read())
            hello, world
        """
        self.ensure_open(self.Mode.r)
        return self._fd.read(*args, **kwargs)

    def readline(self, *args, **kwargs):
        self.ensure_open(self.Mode.r)
        return self._fd.readline(*args, **kwargs)

    def readlines(self, *args, **kwargs):
        self.ensure_open(self.Mode.r)
        return self._fd.readlines(*args, **kwargs)

    def write(self, *args, **kwargs):
        """
        Usage:
            >>> file = File("hello.txt")
            >>> file.write("hello, world")
            >>> print(file.read())
            hello, world
        """
        self.ensure_open(self.Mode.w)
        return self._fd.write(*args, **kwargs)

    def writelines(self, seq, *args, **kwargs):
        """
        Usage:
            >>> file = File("hello.txt")
            >>> file.writelines(["hello", "world"])
            >>> print(file.read())
            hello
            world
        """
        self.ensure_open(self.Mode.w)
        seq = [self.__ensure_nl(line) for line in seq] 
        return self._fd.writelines(seq, *args, **kwargs)

    def append(self, *args, **kwargs):
        """
        Usage:
            >>> file = File("hello.txt")
            >>> print(file.read())
            hello
            >>> file.append(", world")
            >>> print(file.read())
            hello, world
        """
        self.ensure_open(self.Mode.a)
        return self._fd.write(*args, **kwargs)

    def appendlines(self, seq, *args, **kwargs):
        """
        Usage:
            >>> file = File("hello.txt")
            >>> print(file.read())
            hello
            >>> file.appendlines(["world", "!!"])
            >>> print(file.read())
            hello
            world
            !!
        """
        self.ensure_open(self.Mode.a)
        seq = [self.__ensure_nl("")] + [self.__ensure_nl(line) for line in seq] 
        return self._fd.write(*args, **kwargs)

    def open(self, mode, *args, **kwargs):
        """ An alias of ensure_open

        Usage:
            >>> file = File(path, encoding).open(File.Mode.R)
        """
        return self.ensure_open(mode, *args, **kwargs)

    def close(self, *args, **kwargs):
        """An alias of ensure_close

        Usage:
            >>> file.close()
        """
        self.ensure_close(*args, **kwargs)

    def ensure_open(self, mode, *args, **kwargs):
        """ Open the file with mode `mode` if not opend.
        Usually you don't have to use this method directly.
        Use read, write, append,.. methods instead.

        Usage:
            >>> file.ensure_open(File.Mode.R)
        """
        if self._fd and self.mode == mode:
            return self
        self.mode = mode
        self._fd = self.__open(
            self.path, mode, encoding=self.encoding, *args, **kwargs
        )
        return self

    def ensure_close(self, *args, **kwargs):
        """
        Close the file if opened.
        Usually you don't have to use this method directly.

        Usage:
            >>> file.ensure_close()
        """
        if not self._fd:
            return
        self._fd.close(*args, **kwargs)
        self._fd = None
        self.mode = None
        return

    def __ensure_nl(self, string):
        """Append new line chars to the end of `string`.

        Usage:
            >>> assert(self.__ensure_nl("") == "\n")
            >>> assert(self.__ensure_nl("hello") == "hello\n")
        """
        string = str(string)
        if not string.endswith("\n"):
            string += "\n"
        return string

    def __open(self, *args, **kwargs):
        if six.PY3:
            print(args)
            print(kwargs)
            return open(*args, **kwargs)
    
        return codecs.open(*args, **kwargs)

