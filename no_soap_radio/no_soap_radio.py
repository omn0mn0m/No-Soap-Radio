import Tkinter as tk

root = tk.Tk()
root.title("No Soap Radio")
root.geometry("460x320")

mode = tk.StringVar()
enabled = tk.BooleanVar()
radio_type = tk.StringVar()
frequency = tk.IntVar()

# =============== Variable Setup ================
mode.set('Rx')
enabled.set(False)
radio_type.set('FM')
frequency.set(0)

def select_mode(event=None):
    enabled.set(False)
    
    print mode.get()

def select_radio_type(event=None):
    enabled.set(False)
    
    print radio_type.get()

def start():
    if mode.get() == "Tx":
        print "Starting transmit at " + str(frequency.get())
    else:
        print "Starting receive at " + str(frequency.get())

def stop():
    if mode.get() == "Tx":
        print "Stopping transmit at " + str(frequency.get())
    else:
        print "Stopping receive at " + str(frequency.get())

# ================ Frequency Specification ==================
frequency_frame = tk.Frame(root)

frequency_label = tk.Label(frequency_frame, text="Frequency", font=(None, 18)).pack()
frequency_entry = tk.Entry(frequency_frame, textvariable=frequency, width=11, font=(None, 18), justify=tk.CENTER).pack()
start_button = tk.Radiobutton(frequency_frame, text="Start", variable=enabled, value=True,
                              command=start, indicatoron=0, font=(None, 18), width=5).pack(side=tk.LEFT)
stop_button = tk.Radiobutton(frequency_frame, text="Stop", variable=enabled, value=False,
                             command=stop, indicatoron=0, font=(None, 18), width=5).pack(side=tk.RIGHT)

frequency_frame.grid(column=3, row=0, columnspan=2, rowspan=3)

# ================ Mode Selection ===============
mode_frame = tk.Frame(root)

mode_label = tk.Label(mode_frame, text="Mode", font=(None, 18)).grid(column=0, row=0, sticky='W')
mode_choice0 = tk.Radiobutton(mode_frame, text="Transmit", variable=mode, value="Tx",
                              command=select_mode, indicatoron=0, font=(None, 18), width=10).grid(column=0, row=1, columnspan=2, sticky='W')
mode_choice1 = tk.Radiobutton(mode_frame, text="Receive", variable=mode, value="Rx",
                              command=select_mode, indicatoron=0, font=(None, 18), width=10).grid(column=0, row=2, columnspan=2, sticky='W')

mode_frame.grid(column=0, row=0, rowspan=3, columnspan=2)

# ================ Signal Type ==================
radio_type_frame = tk.Frame(root)

radio_type_label = tk.Label(radio_type_frame, text="Type", font=(None, 18)).grid(column=0, row=0, padx=5)

radio_type_values = (('AM', 'FM', 'USB'), ('LSB', 'CW', 'OTH'))

for i, radio_type_row in enumerate(radio_type_values):
    for j, radio_type_value in enumerate(radio_type_row):
        radio_type_choice = tk.Radiobutton(radio_type_frame, text=radio_type_value, variable=radio_type, value=radio_type_value,
                                           command=select_radio_type, indicatoron=0, font=(None, 18), width=10).grid(column=j*2, row=2, columnspan=i, sticky='W')

radio_type_frame.grid(column=0, row=4, rowspan=3, columnspan=6)

# ================ Main Loop ==================

root.mainloop()
