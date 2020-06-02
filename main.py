  # __  __                __
  #/ /_/ /_  ____ _____  / /_______
 #/ __/ __ \/ __ `/ __ \/ //_/ ___/
#/ /_/ / / / /_/ / / / / ,< (__  )
#\__/_/ /_/\__,_/_/ /_/_/|_/____/






import pyfiglet
word = input("What word do you want transformed to ASCII: ")
mresult = pyfiglet.figlet_format(word) 


def fun():
  font = input('''What font?
  1) Normal
  2) Slant                  (Say the Number)
  3) 5 Line Oblique
  ''')

  if font == "2":
    newword = pyfiglet.figlet_format(word, font = 'slant')
    print (newword)
  elif font == "1":
    print(mresult)
  elif font == '3':
    newword = pyfiglet.figlet_format(word, font = '5lineoblique')
    print(newword)
  else:
      print("Not a valid number. Try again")
      fun()
fun()