# Text-to-Ascii
Convert your normal text into an ASCII masterpiece

Firstly, I import the `pyfiglet` module so that making ASCII text art is possible. On top of that, I also initiate an input for the user to type in text they want to convert into ASCII art.

```python
import pyfiglet
word = input("What word do you want transformed to ASCII: ")
mresult = pyfiglet.figlet_format(word) 
```
I declare a function `fun()` to prompt the user to choose which ASCII font they wish to convert their inputted text into based on the fonts available in the `pyfiglet` module.

```python
def fun():
  font = input('''What font?
  1) Normal
  2) Slant                  (Say the Number)
  3) 5 Line Oblique
  4) 3D
  5) Banner 3D 
  6) Isometric1
  7) Bulbhead
  ''')
```
There are 7 options in the menu above. Users are to input the numbers as stipulated above, or otherwise the output would be invalid.

```python
  if font == "2":
    newword = pyfiglet.figlet_format(word, font = 'slant')
    print (newword)
  elif font == "1":
    print(mresult)
  elif font == '3':
    newword = pyfiglet.figlet_format(word, font = '5lineoblique')
    print(newword)
  elif font == '4':
    newword = pyfiglet.figlet_format(word, font = '3-d')
    print(newword)
  elif font == '5':
    newword = pyfiglet.figlet_format(word, font = 'banner3-D')
    print(newword)
  elif font == '6':
    newword = pyfiglet.figlet_format(word, font = 'isometric1')
    print(newword)
  elif font == '7':
    newword = pyfiglet.figlet_format(word, font = 'bulbhead')
    print(newword)
  else:
      print("Not a valid number. Try again")
      fun()
```
I list down the `if` statements and the respective actions for each of the options. If none of the input is based on the options above, the function will be re-declared, forming a functional loop.

## Outputs
> All outputs will be based on the test input below:

```python
word = input("What word do you want transformed to ASCII: ")
```

`What word do you want transformed to ASCII: hello world`


1. Normal
```
 _          _ _                            _     _ 
| |__   ___| | | ___   __      _____  _ __| | __| |
| '_ \ / _ \ | |/ _ \  \ \ /\ / / _ \| '__| |/ _` |
| | | |  __/ | | (_) |  \ V  V / (_) | |  | | (_| |
|_| |_|\___|_|_|\___/    \_/\_/ \___/|_|  |_|\__,_|
```

2. Slant
```
    __         ____                             __    __
   / /_  ___  / / /___     _      ______  _____/ /___/ /
  / __ \/ _ \/ / / __ \   | | /| / / __ \/ ___/ / __  / 
 / / / /  __/ / / /_/ /   | |/ |/ / /_/ / /  / / /_/ /  
/_/ /_/\___/_/_/\____/    |__/|__/\____/_/  /_/\__,_/  
```

3. 5 Line Oblique
```                         
   / __      ___     // //  ___    
  //   ) ) //___) ) // // //   ) ) 
 //   / / //       // // //   / /  
//   / / ((____   // // ((___/ /   
                                              
                                              
                                              
                 ___      __     //  ___   /  
  //  / /  / / //   ) ) //  ) ) // //   ) /   
 //  / /  / / //   / / //      // //   / /    
((__( (__/ / ((___/ / //      // ((___/ /
```

4. 3D
```
 **               **  **                                        **      **
/**              /** /**                                       /**     /**
/**       *****  /** /**  ******    ***     **  ******  ****** /**     /**
/******  **///** /** /** **////**  //**  * /** **////**//**//* /**  ******
/**///**/******* /** /**/**   /**   /** ***/**/**   /** /** /  /** **///**
/**  /**/**////  /** /**/**   /**   /****/****/**   /** /**    /**/**  /**
/**  /**//****** *** ***//******    ***/ ///**//****** /***    ***//******
//   //  ////// /// ///  //////    ///    ///  //////  ///    ///  ////// 
```

5. Banner 3D
```
'##::::'##:'########:'##:::::::'##::::::::'#######::
 ##:::: ##: ##.....:: ##::::::: ##:::::::'##.... ##:
 ##:::: ##: ##::::::: ##::::::: ##::::::: ##:::: ##:
 #########: ######::: ##::::::: ##::::::: ##:::: ##:
 ##.... ##: ##...:::: ##::::::: ##::::::: ##:::: ##:
 ##:::: ##: ##::::::: ##::::::: ##::::::: ##:::: ##:
 ##:::: ##: ########: ########: ########:. #######::
..:::::..::........::........::........:::.......:::
'##:::::'##::'#######::'########::'##:::::::'########::
 ##:'##: ##:'##.... ##: ##.... ##: ##::::::: ##.... ##:
 ##: ##: ##: ##:::: ##: ##:::: ##: ##::::::: ##:::: ##:
 ##: ##: ##: ##:::: ##: ########:: ##::::::: ##:::: ##:
 ##: ##: ##: ##:::: ##: ##.. ##::: ##::::::: ##:::: ##:
 ##: ##: ##: ##:::: ##: ##::. ##:: ##::::::: ##:::: ##:
. ###. ###::. #######:: ##:::. ##: ########: ########::
:...::...::::.......:::..:::::..::........::........:::
```
6. Isometric1
```
      ___           ___           ___       ___       ___     
     /\__\         /\  \         /\__\     /\__\     /\  \    
    /:/  /        /::\  \       /:/  /    /:/  /    /::\  \   
   /:/__/        /:/\:\  \     /:/  /    /:/  /    /:/\:\  \  
  /::\  \ ___   /::\~\:\  \   /:/  /    /:/  /    /:/  \:\  \ 
 /:/\:\  /\__\ /:/\:\ \:\__\ /:/__/    /:/__/    /:/__/ \:\__\
 \/__\:\/:/  / \:\~\:\ \/__/ \:\  \    \:\  \    \:\  \ /:/  /
      \::/  /   \:\ \:\__\    \:\  \    \:\  \    \:\  /:/  / 
      /:/  /     \:\ \/__/     \:\  \    \:\  \    \:\/:/  /  
     /:/  /       \:\__\        \:\__\    \:\__\    \::/  /   
     \/__/         \/__/         \/__/     \/__/     \/__/    
      ___           ___           ___           ___       ___     
     /\__\         /\  \         /\  \         /\__\     /\  \    
    /:/ _/_       /::\  \       /::\  \       /:/  /    /::\  \   
   /:/ /\__\     /:/\:\  \     /:/\:\  \     /:/  /    /:/\:\  \  
  /:/ /:/ _/_   /:/  \:\  \   /::\~\:\  \   /:/  /    /:/  \:\__\ 
 /:/_/:/ /\__\ /:/__/ \:\__\ /:/\:\ \:\__\ /:/__/    /:/__/ \:|__|
 \:\/:/ /:/  / \:\  \ /:/  / \/_|::\/:/  / \:\  \    \:\  \ /:/  /
  \::/_/:/  /   \:\  /:/  /     |:|::/  /   \:\  \    \:\  /:/  / 
   \:\/:/  /     \:\/:/  /      |:|\/__/     \:\  \    \:\/:/  /  
    \::/  /       \::/  /       |:|  |        \:\__\    \::/__/   
     \/__/         \/__/         \|__|         \/__/     ~~    
```

7. Bulbhead
``` _   _  ____  __    __    _____    _    _  _____  ____  __    ____  
( )_( )( ___)(  )  (  )  (  _  )  ( \/\/ )(  _  )(  _ \(  )  (  _ \ 
 ) _ (  )__)  )(__  )(__  )(_)(    )    (  )(_)(  )   / )(__  )(_) )
(_) (_)(____)(____)(____)(_____)  (__/\__)(_____)(_)\_)(____)(____/ 
```
