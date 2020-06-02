# Text-to-Ascii
Convert your normal text into an ASCII masterpiece

Firstly, I import the `pyfiglet` module so that making ASCII text art is possible. On top of that, I also initiate an input for the user to type in text they want to convert into ASCII art.

```python
import pyfiglet
word = input("What word do you want transformed to ASCII: ")
mresult = pyfiglet.figlet_format(word) 
```
I declare a function
