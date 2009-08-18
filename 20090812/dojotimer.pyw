#-*- coding: utf-8 -*-
#
#
# DojoTimer - a simple timer for Coding Dojos.
#
# Copyright (C) 2008 Flávio Amieiro <amieiro.flavio@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
# If you find any bugs or have any suggestions email: amieiro.flavio@gmail.com
from Tkinter import *
import tkSimpleDialog

class Clock(object):

    def __init__(self, master, default_time=1):

        # Create a frame
        self.frame = Frame(master)
        self.frame.pack()

        # Get the TopLevel window
        self.top = self.frame.winfo_toplevel()

        # Change some of it's attributes
        self.top.title("DojoTimer") # change the title
        self.top.attributes('-topmost', 1) # make it always on top
        self.top.resizable(0, 0) # make it unresizeable

        # A separate method is responsible for creating the other widgets
        self.__create_widgets()

        # Some default values
        self.running = False
        self.default_time = default_time # defaul time (in minutes)
        self.seconds = 60 * self.default_time
        self.labelstr.set('%02d:%02d' % ((self.seconds /60), (self.seconds % 60)))

    def __create_widgets(self):
        """ This function creates some widgets for the timer."""
        # self.labelstr is going to be used as text in the label (which shows the time left).
        # When this variable's value is modified (with the method .set('str')) the label
        # changes on the fly.
        self.labelstr = StringVar()
        self.label = Label(self.frame, textvariable=self.labelstr, fg='#198931', font=('Helvetica', '48'))
        self.label.pack()

        # Some buttons
        self.start_btn = Button(self.frame, text="Start", command=self.start)
        self.start_btn.pack(side=LEFT)

        self.stop_btn = Button(self.frame, text='Stop', command=self.stop)
        self.stop_btn.pack(side=LEFT)

        self.reset_btn = Button(self.frame, text='Reset', command=self.reset)
        self.reset_btn.pack(side=LEFT)

        self.set_time_btn = Button(self.frame, text='Set time', command=self.set_time)
        self.set_time_btn.pack(side=LEFT)

        self.quit_btn = Button(self.frame, text='Quit', command=self.frame.quit)
        self.quit_btn.pack(side=LEFT)

    def start(self):
        if not self.seconds:
            self.top.iconify()
            self.reset()
        if not self.running:
            self.top.iconify()
            self.running = True
            self.update()

    def update(self):
        if self.running:
            if 0 < self.seconds <= 30:
                self.label['fg']='#efbf16'
            elif self.seconds <= 0:
                self.top.deiconify()
                self.label['fg']='#d70505'
                self.running = False
            new_str = '%02d:%02d' % ((self.seconds / 60), (self.seconds % 60))
            self.labelstr.set(new_str)
            self.label.after(1000, self.update)
            if self.seconds: self.seconds -= 1

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.seconds = 60 * self.default_time
        self.label['fg']='#198931'
        new_str = '%02d:%02d' % ((self.seconds /60), (self.seconds % 60))
        self.labelstr.set(new_str)

    def set_time(self):
        try:
            self.default_time = tkSimpleDialog.askfloat('Set time', 'Specify the time (in minutes)', parent=self.top)
            self.reset()
        except TypeError:
            pass

if __name__ == '__main__':
    root = Tk()
    clock = Clock(root, 1)

    root.mainloop()
