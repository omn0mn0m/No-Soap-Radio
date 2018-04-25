import Tkinter as tk

root = tk.Tk()
root.title("No Soap Radio")
root.geometry("265x175")

mode = tk.StringVar()
radio_type = tk.StringVar()
frequency = tk.StringVar()

def print_mode(event=None):
    print mode.get()

def print_radio_type(event=None):
    print radio_type.get()

def start():
    if mode.get() == "Tx":
        print "Starting transmit at " + frequency.get()
    else:
        print "Starting receive at " + frequency.get()


def stop():
    if mode.get() == "Tx":
        print "Stopping transmit at " + frequency.get()
    else:
        print "Stopping receive at " + frequency.get()


frequency_label = tk.Label(root, text="Frequency").grid(column=1, row=0, columnspan=2)
frequency_entry = tk.Entry(root, textvariable=frequency).grid(column=1, row=1, columnspan=2)

mode_label = tk.Label(root, text="Mode").grid(column=0, row=0, padx=5)
mode_choice0 = tk.Radiobutton(root, text="Transmit", variable=mode, value="Tx", command=print_mode).grid(column=0, row=1, padx=5)
mode_choice1 = tk.Radiobutton(root, text="Receive", variable=mode, value="Rx", command=print_mode).grid(column=0, row=2, padx=5)

radio_type_label = tk.Label(root, text="Type").grid(column=0, row=3, padx=5)
radio_type_choice0 = tk.Radiobutton(root, text="AM", variable=radio_type, value="AM", command=print_radio_type).grid(column=0, row=4, padx=5)
radio_type_choice1 = tk.Radiobutton(root, text="FM", variable=radio_type, value="FM", command=print_radio_type).grid(column=0, row=5, padx=5)
radio_type_choice2 = tk.Radiobutton(root, text="USB/LSB", variable=radio_type, value="USB/LSB", command=print_radio_type).grid(column=0, row=6, padx=5)
radio_type_choice3 = tk.Radiobutton(root, text="CW", variable=radio_type, value="CW", command=print_radio_type).grid(column=0, row=7, padx=5)

start_button = tk.Button(root, text="Start", command=start).grid(column=1, row=2)
stop_button = tk.Button(root, text="Stop", command=stop).grid(column=2, row=2)

root.mainloop()
