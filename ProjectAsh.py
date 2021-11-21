import keyboard as kb
import os 

input('press Enter to continue')
print("Hey Ash, Welcome To The AshProject, This Project Is Based And Named After You, Feel Free To Make Suggestions!")

print("press e to see how much i love you, press q to see my progress to canada, press r to run Ash.exe")
while (True):
        key = "e"

        if (kb.is_pressed(key)):
                os.system('Epress.py')
               

                
        key = "q"

        if (kb.is_pressed(key)):
                os.system('ProgCan.py')
                

        key = "r"

        if (kb.is_pressed(key)):
                os.system('Ash.exe.py')
                




