#1.0
import colorsys
import os
import pyautogui
import pyperclip
import tkinter as tk
import threading
from time import sleep
from pynput import mouse


close = False
button_pressed = False


def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        return False

def loop():
    while not close:
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
            sleep(0.2)
            if close:
                break
            if not button_pressed and not close:
                update_color_values()
thread = threading.Thread(target=loop)
thread.start()


def get_color_code():
    x, y = pyautogui.position()
    screenshot = pyautogui.screenshot(region=(x, y, 1, 1))
    r, g, b = screenshot.getpixel((0, 0))
    hex_code = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    rgb_code = 'rgb({},{},{})'.format(r, g, b)
    hsl_code = 'hsl({}, {}%, {}%)'.format(int(colorsys.rgb_to_hls(r / 255, g / 255, b / 255)[0] * 360), int(colorsys.rgb_to_hls(r / 255, g / 255, b / 255)[1] * 100), int(colorsys.rgb_to_hls(r / 255, g / 255, b / 255)[2] * 100))
    hsv_code = 'hsv({}, {}%, {}%)'.format(int(colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)[0] * 360), int(colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)[1] * 100), int(colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)[2] * 100))
    yiq_code = 'yiq({}, {}%, {}%)'.format(int(colorsys.rgb_to_yiq(r / 255, g / 255, b / 255)[0] * 360), int(colorsys.rgb_to_yiq(r / 255, g / 255, b / 255)[1] * 100), int(colorsys.rgb_to_yiq(r / 255, g / 255, b / 255)[2] * 100))
    return x, y, hex_code, rgb_code, hsl_code, hsv_code, yiq_code
x, y, hex_code, rgb_code, hsl_code, hsv_code, yiq_code = get_color_code()



def copy_hex():
    pyperclip.copy(hex_code)

def copy_rgb():
    pyperclip.copy(rgb_code)

def copy_hsl():
    pyperclip.copy(hsl_code)

def copy_hsv():
    pyperclip.copy(hsv_code)

def copy_yiq():
    pyperclip.copy(yiq_code)

def on_button_press(event):
    global button_pressed
    button_pressed = True
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button):
            widget.configure(state='disabled')
    if event.widget ==  hex_button:
        copy_hex()
    elif event.widget == rgb_button:
        copy_rgb()
    elif event.widget == hsl_button:
        copy_hsl()
    elif event.widget == hsv_button:
        copy_hsv()
    elif event.widget == yiq_button:
        copy_yiq()

def on_button_release(event):
    global button_pressed
    sleep(0.2)
    button_pressed = False
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button):
            widget.configure(state='normal')



def update_color_values():
    global x, y, hex_code, rgb_code, hsl_code, hsv_code, yiq_code
    x, y, hex_code, rgb_code, hsl_code, hsv_code, yiq_code = get_color_code()
    text = 'Pixel-Color at ({}, {})\n'.format(x, y)
    text += 'Hex-Code: {}\n'.format(hex_code)
    text += 'RGB-Code: {}\n'.format(rgb_code)
    text += 'HSL-Code: {}\n'.format(hsl_code)
    text += 'HSV-Code: {}\n'.format(hsv_code)
    text += 'YIQ-Code: {}\n'.format(yiq_code)

    label.config(text=text)
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)


def on_close():
    os._exit(0)


root = tk.Tk()
root.title('PixelColor')
root.resizable(False, False)
root.after_idle(root.attributes, '-topmost', False)
root.tk_setPalette(background='black', foreground='white')
root.protocol('WM_DELETE_WINDOW', on_close)
root.bind_all('<ButtonPress>', on_button_press)
root.bind_all('<ButtonRelease>', on_button_release)


text = 'Pixel-Color at ({}, {})\n'.format(x, y)
text += 'Hex-Code: {}\n'.format(hex_code)
text += 'RGB-Code: {}\n'.format(rgb_code)
text += 'HSL-Code: {}\n'.format(hsl_code)
text += 'HSV-Code: {}\n'.format(hsv_code)
text += 'YIQ-Code: {}\n'.format(yiq_code)

label = tk.Label(root, text=text, justify='left')
label.pack()

hex_button = tk.Button(root, text='Copy Hex', command=copy_hex)
rgb_button = tk.Button(root, text='Copy RGB', command=copy_rgb)
hsl_button = tk.Button(root, text='Copy HSL', command=copy_hsl)
hsv_button = tk.Button(root, text='Copy HSV', command=copy_hsv)
yiq_button = tk.Button(root, text='Copy YIQ', command=copy_yiq)

hex_button.pack(side='left')
rgb_button.pack(side='left')
hsl_button.pack(side='left')
hsv_button.pack(side='left')
yiq_button.pack(side='left')

root.mainloop()
