Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> q

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> "modules"

Please wait a moment while I gather a list of all available modules...

__future__          _tkinter            getpass             runpy
_abc                _tracemalloc        gettext             sched
_ast                _uuid               glob                secrets
_asyncio            _warnings           grp                 select
_bisect             _weakref            gzip                selectors
_blake2             _weakrefset         hashlib             setuptools
_bootlocale         _xxtestfuzz         heapq               shelve
_bz2                abc                 hmac                shlex
_codecs             aifc                html                shutil
_codecs_cn          antigravity         http                signal
_codecs_hk          argparse            idlelib             site
_codecs_iso2022     array               imaplib             smtpd
_codecs_jp          ast                 imghdr              smtplib
_codecs_kr          asynchat            imp                 sndhdr
_codecs_tw          asyncio             importlib           socket
_collections        asyncore            inspect             socketserver
_collections_abc    atexit              io                  sqlite3
_compat_pickle      audioop             ipaddress           sre_compile
_compression        base64              itertools           sre_constants
_contextvars        bdb                 json                sre_parse
_crypt              binascii            keyword             ssl
_csv                binhex              lib2to3             stat
_ctypes             bisect              linecache           statistics
_ctypes_test        builtins            locale              string
_curses             bz2                 logging             stringprep
_curses_panel       cProfile            lzma                struct
_datetime           calendar            macpath             subprocess
_dbm                certifi             mailbox             sunau
_decimal            cgi                 mailcap             symbol
_dummy_thread       cgitb               marshal             symtable
_elementtree        chunk               math                sys
_functools          cmath               mimetypes           sysconfig
_hashlib            cmd                 mmap                syslog
_heapq              code                modulefinder        tabnanny
_imp                codecs              multiprocessing     tarfile
_io                 codeop              netrc               telnetlib
_json               collections         nis                 tempfile
_locale             colorsys            nntplib             termios
_lsprof             compileall          ntpath              test
_lzma               concurrent          nturl2path          textwrap
_markupbase         configparser        numbers             this
_md5                contextlib          opcode              threading
_multibytecodec     contextvars         operator            time
_multiprocessing    copy                optparse            timeit
_opcode             copyreg             os                  tkinter
_operator           create_spreadsheet  parser              token
_osx_support        crypt               pathlib             tokenize
_pickle             csv                 pdb                 trace
_posixsubprocess    ctypes              pickle              traceback
_py_abc             curses              pickletools         tracemalloc
_pydecimal          dataclasses         pip                 tty
_pyio               datetime            pipes               turtle
_queue              dbm                 pkg_resources       turtledemo
_random             decimal             pkgutil             types
_scproxy            difflib             platform            typing
_sha1               dis                 plistlib            unicodedata
_sha256             distutils           poplib              unittest
_sha3               doctest             posix               urllib
_sha512             dummy_threading     posixpath           uu
_signal             easy_install        pprint              uuid
_sitebuiltins       email               profile             venv
_socket             encodings           pstats              warnings
_sqlite3            ensurepip           pty                 wave
_sre                enum                pwd                 weakref
_ssl                errno               py_compile          webbrowser
_stat               faulthandler        pyclbr              wsgiref
_string             fcntl               pydoc               xdrlib
_strptime           filecmp             pydoc_data          xml
_struct             fileinput           pyexpat             xmlrpc
_symtable           fnmatch             queue               xxlimited
_sysconfigdata_m_darwin_darwin formatter           quopri              xxsubtype
_testbuffer         fractions           random              zipapp
_testcapi           ftplib              re                  zipfile
_testimportmultiple functools           readline            zipimport
_testmultiphase     gc                  reprlib             zlib
_thread             genericpath         resource            
_threading_local    getopt              rlcompleter         

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> q

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> clear all
SyntaxError: invalid syntax
>>> clear
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> clc
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    clc
NameError: name 'clc' is not defined
>>> cls
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> (239+538)**2
603729
>>> (239+588)**2
683929
>>> pyhton hello.py
SyntaxError: invalid syntax
>>> python hello.py
SyntaxError: invalid syntax
>>> import turtle
>>> turtle.forward(0)
>>> turtle.forwar(25)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    turtle.forwar(25)
AttributeError: module 'turtle' has no attribute 'forwar'
>>> turtle.forward(24)
>>> turtle.left(30)
>>> turtle.left(-30)
>>> turtle.shape("turtle")
>>> turtle.reset()
>>> motion.py
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    motion.py
NameError: name 'motion' is not defined
>>> python motion.py
SyntaxError: invalid syntax
>>> 
========= RESTART: /Users/pavan/Documents/Python_exercises/motion.py =========








>>> 
========= RESTART: /Users/pavan/Documents/Python_exercises/motion.py =========
>>> ========= RESTART: /Users/pavan/Documents/Python_exercises/motion.py =========

SyntaxError: invalid syntax
>>> 
>>>  
========= RESTART: /Users/pavan/Documents/Python_exercises/motion.py =========
SyntaxError: invalid syntax
>>> 
>>> 
========= RESTART: /Users/pavan/Documents/Python_exercises/motion.py =========
SyntaxError: invalid syntax
>>> 
======== RESTART: /Users/pavan/Documents/Python_exercises/motion.py =========
SyntaxError: invalid syntax
>>> ========= RESTART: /Users/pavan/Documents/Python_exercises/motion.py =========
SyntaxError: invalid syntax
>>> 
========= RESTART: /Users/pavan/Documents/Python_exercises/square.py =========
>>> 
======= RESTART: /Users/pavan/Documents/Python_exercises/rectangle.py =======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/more_squares.py ======
Traceback (most recent call last):
  File "/Users/pavan/Documents/Python_exercises/more_squares.py", line 6, in <module>
    turtle.forwad(30)
AttributeError: module 'turtle' has no attribute 'forwad'
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/more_squares.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/more_squares.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/more_squares.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/more_squares.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/more_squares.py ======
>>> 
== RESTART: /Users/pavan/Documents/Python_exercises/more_square_forloop.py ==
>>> 
== RESTART: /Users/pavan/Documents/Python_exercises/more_square_forloop.py ==
>>> 
== RESTART: /Users/pavan/Documents/Python_exercises/more_square_forloop.py ==
>>> 
== RESTART: /Users/pavan/Documents/Python_exercises/more_square_forloop.py ==
>>> 
== RESTART: /Users/pavan/Documents/Python_exercises/more_square_forloop.py ==
>>> 
 RESTART: /Users/pavan/Documents/Python_exercises/more_squares_with_variable.py 
>>> 
 RESTART: /Users/pavan/Documents/Python_exercises/more_squares_with_variables.py 
>>> 
 RESTART: /Users/pavan/Documents/Python_exercises/more_squares_with_variables.py 
>>> 
 RESTART: /Users/pavan/Documents/Python_exercises/more_squares_with_variables.py 
>>> 
========== RESTART: /Users/pavan/Documents/Python_exercises/home.py ==========
>>> 
========== RESTART: /Users/pavan/Documents/Python_exercises/home.py ==========
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_1.py ======
Hello John!
Hello Sam!
Hello Jill!
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_2.py ======
0
1
2
3
4
5
6
7
8
9
>>> help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |  
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __reduce__(...)
 |      Helper for pickle.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value, [start, [stop]]) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop

>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_3.py ======
5
7
11
13
36
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_4.py ======
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_5.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_5.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_5.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_5.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_6.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_6.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_6.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_6.py ======
0
1
2
3
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_6.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_7.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_7.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_7.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_7.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_7.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_7.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_8.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_8.py ======
Traceback (most recent call last):
  File "/Users/pavan/Documents/Python_exercises/Loops/Loop_8.py", line 12, in <module>
    turtle.left(th)
  File "<string>", line 5, in left
turtle.Terminator
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_8.py ======
Traceback (most recent call last):
  File "/Users/pavan/Documents/Python_exercises/Loops/Loop_8.py", line 3, in <module>
    turtle.shape("point")  #changing the shape of the turtle from arrow to turtle
  File "<string>", line 8, in shape
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named point
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_8.py ======
Traceback (most recent call last):
  File "/Users/pavan/Documents/Python_exercises/Loops/Loop_8.py", line 3, in <module>
    turtle.shape("dot")  #changing the shape of the turtle from arrow to turtle
  File "<string>", line 8, in shape
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named dot
>>> import turtle
>>> help(turtle.shape)
Help on function shape in module turtle:

shape(name=None)
    Set turtle shape to shape with given name / return current shapename.
    
    Optional argument:
    name -- a string, which is a valid shapename
    
    Set turtle shape to shape with given name or, if name is not given,
    return name of current shape.
    Shape with name must exist in the TurtleScreen's shape dictionary.
    Initially there are the following polygon shapes:
    'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
    To learn about how to deal with shapes see Screen-method register_shape.
    
    Example:
    >>> shape()
    'arrow'
    >>> shape("turtle")
    >>> shape()
    'turtle'

>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Loops/Loop_8.py ======
Traceback (most recent call last):
  File "/Users/pavan/Documents/Python_exercises/Loops/Loop_8.py", line 12, in <module>
    turtle.left(th)
  File "<string>", line 5, in left
turtle.Terminator
>>> help(turtle.size)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    help(turtle.size)
AttributeError: module 'turtle' has no attribute 'size'
>>> register_shape
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    register_shape
NameError: name 'register_shape' is not defined
>>> def line_without_moving():
	turtle.forward(50)
	turtle.backward(50)

	
>>> line_without_moving()
>>> line_without_moving()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    line_without_moving()
  File "<pyshell#35>", line 2, in line_without_moving
    turtle.forward(50)
  File "<string>", line 5, in forward
turtle.Terminator
>>> line_without_moving()
>>> 
>>> line_without_moving()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    line_without_moving()
  File "<pyshell#35>", line 2, in line_without_moving
    turtle.forward(50)
  File "<string>", line 5, in forward
turtle.Terminator
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Functions/1.py ======
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Functions/1.py ======
>>> line_without_moving()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    line_without_moving()
  File "/Users/pavan/Documents/Python_exercises/Functions/1.py", line 2, in line_without_moving
    turtle.forward(100)
NameError: name 'turtle' is not defined
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Functions/1.py ======
>>> line_without_moving()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    line_without_moving()
  File "/Users/pavan/Documents/Python_exercises/Functions/1.py", line 4, in line_without_moving
    turtle.backaward(20)
AttributeError: module 'turtle' has no attribute 'backaward'
>>> line_without_moving()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    line_without_moving()
  File "/Users/pavan/Documents/Python_exercises/Functions/1.py", line 4, in line_without_moving
    turtle.backward(20)
AttributeError: module 'turtle' has no attribute 'backaward'
>>> 
====== RESTART: /Users/pavan/Documents/Python_exercises/Functions/1.py ======
>>> line_without_moving()
>>> 
===== RESTART: /Users/pavan/Documents/Python_exercises/Functions/star.py =====
Traceback (most recent call last):
  File "/Users/pavan/Documents/Python_exercises/Functions/star.py", line 3, in <module>
    line_without_moving()
NameError: name 'line_without_moving' is not defined
>>> for i in range(4):
    line_without_moving()
    turtle.right(90)

    
Traceback (most recent call last):
  File "<pyshell#46>", line 2, in <module>
    line_without_moving()
NameError: name 'line_without_moving' is not defined
>>> line_without_moving()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    line_without_moving()
NameError: name 'line_without_moving' is not defined
>>> def line_without_moving():
	turtle.forward(50)
	turtle.backward(50)

	
>>> 
===== RESTART: /Users/pavan/Documents/Python_exercises/Functions/star.py =====
Traceback (most recent call last):
  File "/Users/pavan/Documents/Python_exercises/Functions/star.py", line 3, in <module>
    line_without_moving()
NameError: name 'line_without_moving' is not defined
>>> def line_without_moving():
	turtle.forward(50)
	turtle.backward(50)

>>> line_without_moving()
>>> for i in range(4):
    line_without_moving()
    turtle.right(90)

    
Traceback (most recent call last):
  File "<pyshell#53>", line 2, in <module>
    line_without_moving()
  File "<pyshell#50>", line 2, in line_without_moving
    turtle.forward(50)
  File "<string>", line 5, in forward
turtle.Terminator
>>> for i in range(4):
     line_without_moving()
     turtle.right(90)

     
>>> 
===== RESTART: /Users/pavan/Documents/Python_exercises/Functions/star.py =====
Traceback (most recent call last):
  File "/Users/pavan/Documents/Python_exercises/Functions/star.py", line 3, in <module>
    line_without_moving()
NameError: name 'line_without_moving' is not defined
>>> 
===== RESTART: /Users/pavan/Documents/Python_exercises/Functions/star.py =====
Traceback (most recent call last):
  File "/Users/pavan/Documents/Python_exercises/Functions/star.py", line 2, in <module>
    import line_without_moving
ModuleNotFoundError: No module named 'line_without_moving'
>>> 
