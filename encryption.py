### Copyright 2020 Benjamin A. McGinty

### Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

### The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

### THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

text = input('Secret message: ')
key2 = input('Key: ')
endecry = input('Encrypt or Decrypt E/D: ')


#encrypting text string
if endecry == 'E':
  encrypted = ''
  for character in text:
    char_code = ord(character) + int(key2)
    encrypted = encrypted + chr(char_code)

#decryting text string
else:
  encrypted = ''
  for character in text:
    char_code = ord(character) - int(key2)
    encrypted = encrypted + chr(char_code)

#printing finished message

if endecry == "E":
    print("")
    print("The encryted message is "+encrypted)
else:
    print("")
    print("The decryted message is "+encrypted)


input('Press ENTER to exit')
