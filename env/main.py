'''
                                                    Detetec Mouse After Hotkey
    
    This is the main file of the script, the one that will detect the keys input and execute the basic actions.

    Author: Zourethe
    Date: July, 17, 2023
'''

# Imports.
from pynput import keyboard, mouse

# Variables.
shift_l = False
ctrl_l = False
toggle = False

# Terminal interface.
print('\033[32m{}\033[0m'.format('                  Detetec Mouse After Hotkey'))
print('')
print('\033[0m{}\033[0m'.format('This is a script that start to detect your mouse click inputs\nafter you press a hotkey (CTRL + SHIFT + F12).'))
print('')
print('\033[0m{}\033[0m'.format('Script by Zourethe.'))
print('')

# On press function.
def on_press(key):
    global ctrl_l, shift_l, toggle
    if key == keyboard.Key.ctrl_l:
        ctrl_l = True
    elif key == keyboard.Key.shift_l and ctrl_l:
        shift_l = True
    elif key == keyboard.Key.f12 and ctrl_l and shift_l:
        if toggle == False:
            print('\033[93m{}\033[0m'.format('Hotkey toggled.'))
            toggle = True
        else:
            toggle = False
            print('\033[93m{}\033[0m'.format('Hotkey untoggled.'))

# On release function.
def on_release(key):
    global ctrl_l, shift_l, toggle
    if key == keyboard.Key.ctrl_l:
        ctrl_l = False
    elif key == keyboard.Key.shift_l and ctrl_l:
        shift_l = False

# On click function.
def on_click(x, y, button, pressed):
    if button == mouse.Button.left and toggle:
        print('\033[32m{}\033[0m'.format('Left click pressed/released.'))
    if button == mouse.Button.right and toggle:
        print('\033[31m{}\033[0m'.format('Right click pressed/released.'))

# Pynput listeners.
kb_lstnr = keyboard.Listener(on_press = on_press, on_release = on_release)
ms_lstnr = mouse.Listener(on_click = on_click)

# Listeners start.
ms_lstnr.start()
kb_lstnr.start()
ms_lstnr.join()
kb_lstnr.join()
