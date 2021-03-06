import Tkinter as tk
import subprocess as sp

root = tk.Tk()
root.title("No Soap Radio")
root.geometry("1260x720") # Was 460x260

mode = tk.StringVar()
enabled = tk.BooleanVar()
radio_type = tk.StringVar()
frequency = tk.IntVar()
unit = tk.StringVar()

# =============== Variable Setup ================
mode.set('Rx')
enabled.set(False)
radio_type.set('FM')
frequency.set(0)
unit.set('Hz')

metric_conversions = {'Hz':1e0, 'kHz': 1e3, 'MHz':1e6, 'GHz':1e9}

def start():
    global p
    global p2

    stop()
    
    if mode.get() == "Tx":
        p = sp.Popen(["ping", "www.google.com"])
        
        print "Starting transmit at " + str(frequency.get() * metric_conversions[unit.get()])
    else:
        if radio_type.get() == 'FM':
            p = sp.Popen(["rtl_fm", "-f", str(frequency.get() * metric_conversions[unit.get()]), "-M", "wbfm", "-s", "200000", "-r", "48000", "-"], stdout=sp.PIPE)
            p2 = sp.Popen(["aplay", "-r", "48000", "-f", "S16_LE"], stdin=p.stdout)
        else:
            p = sp.Popen(["ping", "www.bing.com"])
        
        print "Starting receive at " + str(frequency.get() * metric_conversions[unit.get()])

def stop():
    global p
    global p2
    
    if mode.get() == "Tx":
        try:
            p.terminate()

            print "Stopping transmit at " + str(frequency.get() * metric_conversions[unit.get()])
        except:
            print "No process to close..."
    else:
        try:
            p.terminate()
            p2.terminate()
            
            print "Stopping receive at " + str(frequency.get() * metric_conversions[unit.get()])
        except:
            print "No process to close..."
        
def select_mode(event=None):
    enabled.set(False)
    
    stop()
    
    print mode.get()

def select_radio_type(event=None):
    enabled.set(False)
    
    stop()
    
    print radio_type.get()

def select_unit(event=None):
    enabled.set(False)

    stop()

    print unit.get()

def cleanup():
    stop()

# ================ Mode Selection ===============
mode_frame = tk.Frame(root)

mode_label = tk.Label(mode_frame, text="Mode", font=(None, 30)).grid(column=0, row=0, sticky='W')
mode_choice0 = tk.Radiobutton(mode_frame, text="Transmit", variable=mode, value="Tx",
                              command=select_mode, indicatoron=0, font=(None, 30), width=15).grid(column=0, row=1, columnspan=2, sticky='W')
mode_choice1 = tk.Radiobutton(mode_frame, text="Receive", variable=mode, value="Rx",
                              command=select_mode, indicatoron=0, font=(None, 30), width=15).grid(column=2, row=1, columnspan=2, sticky='W')

start_button = tk.Radiobutton(mode_frame, text="Start", variable=enabled, value=True,
                              command=start, indicatoron=0, font=(None, 30), width=15).grid(column=0, row=2, columnspan=2, sticky='W')
stop_button = tk.Radiobutton(mode_frame, text="Stop", variable=enabled, value=False,
                             command=stop, indicatoron=0, font=(None, 30), width=15).grid(column=2, row=2, columnspan=2, sticky='W')

mode_frame.grid(column=0, row=0, rowspan=3, columnspan=4, pady=10)

# ================ Frequency Specification ==================
frequency_frame = tk.Frame(root)

frequency_label = tk.Label(frequency_frame, text="Frequency", font=(None, 30)).grid(column=0, row=0, columnspan=2, sticky='W')
frequency_entry = tk.Entry(frequency_frame, textvariable=frequency, width=13, font=(None, 30), justify=tk.CENTER).grid(column=0, row=1, columnspan=2, sticky='W')


unit_choice0 = tk.Radiobutton(frequency_frame, text="Hz", variable=unit, value="Hz",
                              command=select_unit, indicatoron=0, font=(None, 30), width=8).grid(column=2, row=1, sticky='W')
unit_choice1 = tk.Radiobutton(frequency_frame, text="kHz", variable=unit, value="kHz",
                              command=select_unit, indicatoron=0, font=(None, 30), width=8).grid(column=3, row=1, sticky='W')
unit_choice2 = tk.Radiobutton(frequency_frame, text="MHz", variable=unit, value="MHz",
                              command=select_unit, indicatoron=0, font=(None, 30), width=8).grid(column=4, row=1, sticky='W')
unit_choice3 = tk.Radiobutton(frequency_frame, text="GHz", variable=unit, value="GHz",
                              command=select_unit, indicatoron=0, font=(None, 30), width=8).grid(column=5, row=1, sticky='W')

frequency_scale = tk.Scale(frequency_frame, variable=frequency, from_=0, to=999, orient=tk.HORIZONTAL, width=40, length=1095, sliderlength=60, resolution=0.1, font=(None, 30)).grid(column=0, row=2, columnspan=6, sticky='W')

frequency_frame.grid(column=0, row=3, rowspan=2, columnspan=6, pady=10)

# ================ Signal Type ==================
radio_type_frame = tk.Frame(root)

radio_type_label = tk.Label(radio_type_frame, text="Type", font=(None, 30)).grid(column=0, row=0, sticky='W')

radio_type_values = (('AM', 'FM', 'USB'), ('LSB', 'CW', 'OTH'))

for i, radio_type_row in enumerate(radio_type_values):
    for j, radio_type_value in enumerate(radio_type_row):
        radio_type_choice = tk.Radiobutton(radio_type_frame, text=radio_type_value, variable=radio_type, value=radio_type_value,
                                           command=select_radio_type, indicatoron=0, font=(None, 30), width=15).grid(column=j*2, row=i+1, columnspan=2, sticky='W')

radio_type_frame.grid(column=0, row=6, rowspan=3, columnspan=6, pady=10)

# ================ Main Loop ==================

root.mainloop()

cleanup()
