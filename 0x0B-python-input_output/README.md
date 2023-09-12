### this readme file about file handling in python

## File Handling
how to open a file there are two ways to open a file
```python
 file = open("filename","mode" , buffering)
```
```python
 with open("filename","mode" , buffering ) as file:
    # perform file operations
```

## Modes
1. **`r`** : read mode
2. **`w`** : write mode
3. **`a`** : append mode
4. **`r+`** : read and write mode
5. **`w+`** : write and read mode
6. **`a+`** : append and read mode
7. **`x`** : exclusive mode (create a new file)
8. **`t`** : text mode
9. **`b`** : binary mode
10. **`+`** : open a file for updating (reading and writing)


## File Operations
1. `read()` : read the entire file
2. `readline()` : read a single line
3. `readlines()` : read all lines and return a list
4. `write()` : write a string to the file
5. `writelines()` : write a list of lines to the file
6. `close()` : close the file
7. `flush()` : flush the internal buffer
8. `seek()` : change the cursor to given byte
9. `tell()` : return the current file position
10. `truncate()` : truncate the file's size



## File Attributes
1. closed : check whether the file is closed or not
2. mode : return the access mode with which the file was opened
3. name : return the name of the file
4. encoding : return the encoding of the file
5. errors : return the error mode of the file
6. newlines : return newlines mode of the file
7. softspace : return space flag

## File Methods
1. `fileno()` : return the file descriptor
2. `isatty()` : check whether the file is connected to a tty device
3. `readable()` : check whether the file is readable or not
4. `seekable()` : check whether the file is seekable or not
5. `writable()` : check whether the file is writable or not

## File Exceptions
1. BlockingIOError
2. BrokenPipeError
3. FileExistsError
4. FileNotFoundError
5. InterruptedError
6. IsADirectoryError
7. NotADirectoryError
8. PermissionError
9. ProcessLookupError
10. TimeoutError
11. UnsupportedOperation


### difference between open and with open
```python
file = open("filename","mode" , buffering)
# perform file operations
```
the above code is not safe because if any error occurs in the file operations then the file will not be closed and it will cause memory leak so we use with with open


```python
with open("filename","mode" , buffering ) as file:
    # perform file operations
```
the above code is safe because if any error occurs in the file operations then the file will be closed automatically and it will not cause memory leak



### cotributor
- **Abdullah Faik** : [Abdullah-Faik](https://www.github.com/abdullah-faik)

