from pynput import keyboard

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener when 'esc' key is pressed
        return False

# Create a listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# Start the listener
listener.start()

# Keep the program running
listener.join()
