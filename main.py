# Imports
from pynput import keyboard, mouse


# Variables
shift_l = False
ctrl_l = False
toggle = False
clicked = False


# Controller
ms_ctrllr = mouse.Controller()


# On press function
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


# On release function
def on_release(key):
    global ctrl_l, shift_l, toggle

    if key == keyboard.Key.ctrl_l:
        ctrl_l = False

    elif key == keyboard.Key.shift_l and ctrl_l:
        shift_l = False


# On click function
def on_click(x, y, button, pressed):
    global toggle, clicked

    if pressed and toggle:
        print('Output')


# Listeners definition
kb_lstnr = keyboard.Listener(on_press = on_press, on_release = on_release)
ms_lstnr = mouse.Listener(on_click = on_click)


# Listeners start
ms_lstnr.start()
kb_lstnr.start()
ms_lstnr.join()
kb_lstnr.join()
