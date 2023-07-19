'''
                                                    Detetec Mouse After Hotkey
    
    This is the main file of the script, the one that will detect the keys input
    and execute the basic actions.

    Author: Zourethe
    Date: July, 17, 2023
'''

# Libraries imports.
from pynput import keyboard, mouse

# Variables definition.
shift_l = False
ctrl_l = False
toggle = False

# Pynput controller definition.
ms_ctrllr = mouse.Controller()

# On press function definition.
def on_press(key):
    global ctrl_l, shift_l, toggle
    if key == keyboard.Key.ctrl_l:
        ctrl_l = True
    elif key == keyboard.Key.shift_l and ctrl_l:
        shift_l = True
    elif key == keyboard.Key.f12 and ctrl_l and shift_l:
        if toggle == False:
            toggle = True
        else:
            toggle = False

# On release function definition.
def on_release(key):
    global ctrl_l, shift_l, toggle
    if key == keyboard.Key.ctrl_l:
        ctrl_l = False
    elif key == keyboard.Key.shift_l and ctrl_l:
        shift_l = False

# On click function definition.
def on_click(x, y, button, pressed):
    if pressed and toggle:
        print('Output')

# Pynput listeners definition.
kb_lstnr = keyboard.Listener(on_press = on_press, on_release = on_release)
ms_lstnr = mouse.Listener(on_click = on_click)

# Pynput listeners start.
ms_lstnr.start()
kb_lstnr.start()
ms_lstnr.join()
kb_lstnr.join()
