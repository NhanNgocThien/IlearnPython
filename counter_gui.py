# Date created: 27/01/2019
# A simple GUI counter provides two mode: count up, count down. It also has stop, and reset button

# Import modules
try:
    from tkinter import *
except:
    from Tkinter import *

# Constants 
SCREEN_W    = 350
SCREEN_H    = 200
BUTTON_W    = 10
BUTTON_H    = 1
S_START     = 1
S_STOP      = 2
S_RESET     = 3
S_UP        = 4
S_DOWN      = 5
M_UP        = True
M_DOWN      = False

# Counter class
class Counter():
    def __init__(self):
        # Create main window
        self.root = Tk()
        self.root.geometry(str(SCREEN_W) + 'x' + str(SCREEN_H))
        #self.root.resizable(False, False)
        self.root.title('Counter')

        # Declare attributes 
        self.state = S_STOP
        self.count_enable = False
        self.count_up_event = None
        self.count_down_event = None
        self.mode = M_UP
        self.count_value = StringVar()
        self.count_value.set('0')

        # Create main frame
        self.frame = Frame()

        # Create the display of counter's value
        self.label = Label(self.frame)
        self.label.config(textvariable = self.count_value, font = ("Helvetica", 36))

        # Create count up button
        self.b_up = Button(self.frame, command = self.count_up)
        self.b_up.config(text = 'COUNT UP', width = BUTTON_W, height = BUTTON_H)

        # Create count down button
        self.b_down = Button(self.frame, command = self.count_down)
        self.b_down.config(text = 'COUNT DOWN', width = BUTTON_W, height = BUTTON_H)

        # Create stop button
        self.b_stop = Button(self.frame, command = self.stop)
        self.b_stop.config(text = 'STOP', width = BUTTON_W, height = BUTTON_H)

        # Create reset button
        self.b_reset = Button(self.frame, command = self.reset)
        self.b_reset.config(text = 'RESET', width = BUTTON_W, height = BUTTON_H)

        # Display widgets
        self.frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        self.label.grid(row = 0, columnspan = 3)
        self.b_up.grid(row = 1, column = 0)
        self.b_down.grid(row = 1, column = 1)
        self.b_stop.grid(row = 2, column = 0)
        self.b_reset.grid(row = 2, column = 1)

    def count_up(self):
        if self.state != S_UP:  # To prevent rapid function callback because of rapid clicks
            self.state = S_UP
            self.count_enable = True
            self.mode = M_UP
            self.start_counting()

    def count_down(self):
        if self.state != S_DOWN:
            self.state = S_DOWN
            self.count_enable = True
            self.mode = M_DOWN
            self.start_counting()

    def stop(self):
        if self.state != S_STOP:
            self.state = S_STOP
            self.count_enable = False

    def reset(self):
        if self.state != S_RESET:
            self.state = S_RESET
            self.count_enable = False
            self.count_value.set('0')

    def start_counting(self):
        if (self.count_enable == True):
            self.temp_count_value = int(str(self.count_value.get()))
            self.temp_count_value += (1 if self.mode == M_UP else -1)
            self.count_value.set(str(self.temp_count_value))
            if self.mode == M_UP:
                self.count_up_event = self.root.after(1000,self.start_counting)
                if self.count_down_event is not None:
                    self.root.after_cancel(self.count_down_event)
            else:
                self.count_down_event = self.root.after(1000,self.start_counting)
                if self.count_up_event is not None:
                    self.root.after_cancel(self.count_up_event)
        else:
            self.root.after_cancel(self.count_up_event)
            self.root.after_cancel(self.count_down_event)

# Create counter object and run it
master = Counter()
master.root.mainloop()
