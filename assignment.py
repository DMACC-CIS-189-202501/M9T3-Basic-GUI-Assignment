# TODO 1: Delete this and enter your DocString

import tkinter

# --- Start Function Defs Here

def pick_breakfast():
    label.config(text="Start your breakfast in style.")


# TODO 4: Come back to this, but you will create a function for second breakfast, lunch, and dinner similar to pick_breakfast
# Create a function for pick_second_breakfast, pick_lunch, and pick_dinner

# --- End Function Defs



# Ideally this would be main_gui_window = tkinter.Tk(), but that is a lot to type over and over;
# so we will use 'm'
m = tkinter.Tk()

# TODO 2: add a title of favorite meal here with m.title('Favorite Meal')



# Create a Check Button
var1 = tkinter.IntVar()
chk_btn_breakfast = tkinter.Checkbutton(m, text='Breakfast', variable=var1, command=pick_breakfast)
chk_btn_breakfast.grid(row=1)

# Note on the above -> We create a checkbutton, THEN we set a grid. If we do both in the same line but button mmight not render as it would be assigning
# the .grid() output to chk_btn_breakfast instead of the button itself
#said another way....DO NOT DO THIS:
# chk_btn_breakfast = tkinter.Checkbutton(m, text='Breakfast', variable=var1, command=pick_breakfast).grid(row=1)
# this will make chk_btn_breakfast == None

# TODO 3: Create a button for 'second breakfast', 'lunch', and 'dinner' on rows 2, 3, and 4; as well as a variable for them, and a command. Create a function for each command in TODO 4 above
# name them chk_btn_second_breakfast, chk_btn_lunch, and chk_btn_dinner


label = tkinter.Label(m, text='Waiting')
# TODO 5: set the label to be on grid row 5


# Exit Button
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=6)


# At the very end, this closes the loop and starts the GUI...however it is wrapped into a main driver so autograding code will work.
if __name__ == "__main__":
    m.mainloop()

# TODO 6: Optional, but make a copy of this called assignment2.py; but remove all/most of the commends and blank newline spaces to see what
# the GUI code looks like uncommented, and see if you can still follow the code.
# Additionally, look through tkinter guidance, there are ways to change button sizes, colors, etc.