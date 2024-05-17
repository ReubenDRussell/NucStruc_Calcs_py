import tkinter as tk;

##############
# Definitions:
##############

BE2_to_Q_text = str("B(E2)\N{UPWARDS ARROW} \N{RIGHTWARDS ARROW} Q_s");
Q_to_BE2_text =str("Q_s \N{RIGHTWARDS ARROW} B(E2)\N{UPWARDS ARROW}");


def Director():
	Input_num = float(Input_data_B.get());
	input_selection = str(want_menu_variable.get());

	if input_selection == "select option":
		Output_data_A["text"] = "Select Something.\n DO IT!";

	if input_selection == BE2_to_Q_text:
		Output_data_A["text"] = BE2_to_Q(Input_num);
		Output_data_B["text"] = "eb";

	if input_selection == Q_to_BE2_text:
		Output_data_A["text"] = Q_to_BE2(Input_num);
		Output_data_B["text"] = "e2b2";
	return


def BE2_to_Q(Input_num):
	Answer = float( (-2/7)*( ( (16*3.14159265359*Input_num)/5 )**(0.5) ) );
	return Answer;

def Q_to_BE2(Input_num):
	Answer = float( (5/(16*3.14159265359))*( ((-7/2)*Input_num)**2 ) );
	return Answer;




##############
# windows, buttons, boxes, etc.:
##############

window = tk.Tk();	# declares window
window.title("Q_s_rot_lim \N{LEFT RIGHT ARROW} B(E2) Calculator");

window.rowconfigure(0, minsize = 50, weight = 1);
window.columnconfigure(0, minsize = 50, weight = 1);

WRITING = tk.Frame(relief = tk.RAISED, master = window);	# Writing and explanation
INPUTS = tk.Frame(relief = tk.RAISED, master = window);		# The input
BUTTON = tk.Frame(relief = tk.RAISED, master = window);		# Go button
OUTPUTS = tk.Frame(relief = tk.RAISED, master = window);	# The output
BOTTOM = tk.Frame(relief = tk.RAISED, master = window);		# Bottom band

######################################################
# Sizing:
total_width = int(70);
column1_width = int(10);
column2_width = int(20);
column3_width = int(5); # button location (not same width as the others - because of text size)
column4_width = int(20);
###########

title_words = str("Q_s_rot_lim <--> B(E2) Calculator");		# cant use \N{LEFT RIGHT ARROW} as it looks very bad
disclaimer_words = str("While every precaution has been taken,\nthere may be bugs so check first with known values.\n\n");
unit_words = str("I know this works for B(E2;0^+_1 \N{RIGHTWARDS ARROW} 2^+_1), probably works for other B(E2)?\n");
other_words = str("This calculator is mainly for finding the axial rotor limit of Qs.\n Numbers given should be taken as |Q_s(2^+_1)|\n");
clebsch = str("If changing the equation to look at a non 2^+ state Q_s then look into\n Clebsch-Gordan coefficients (just to be sure)");
words = disclaimer_words + unit_words + other_words + clebsch;
Top_Writing_words1 = tk.Label(text = title_words, master = WRITING, bg = "white", width = total_width-21, height = 1, font = ("Arial",15,"bold")); # total width minus something due to text size
Top_Writing_words2 = tk.Label(text = words, master = WRITING, bg = "white", width = total_width, height = 9);
Top_Writing_words1.pack();
Top_Writing_words2.pack();

######################################################


want_label = tk.Label(text = "Choose Direction", fg = "black", width = column2_width, master = INPUTS);			#, bg = "white"
want_menu_options = [BE2_to_Q_text, Q_to_BE2_text];
want_menu_variable = tk.StringVar(INPUTS);
want_menu_variable.set("select option");
want_menu = tk.OptionMenu(INPUTS, want_menu_variable, *want_menu_options);

Input_data_labelB = tk.Label(master = INPUTS, text = "Input");
Input_data_B = tk.Entry(master = INPUTS, width = column2_width);

Input_data_B.insert(0,"0"); # starting value to prevent bug

want_label.pack();
want_menu.pack();
Input_data_labelB.pack();
Input_data_B.pack();




######################################################
The_Button = tk.Button(text = "GO", font = ("default",20,"bold"), width = column3_width, height = 3, command = Director, master = BUTTON, bg = "green3");
The_Button.pack();
######################################################


Output_data_labelA = tk.Label(text = "Output", fg = "black", width = column4_width, master = OUTPUTS);			#, bg = "white"
Output_data_A = tk.Label(text = "--", fg = "black", bg = "white", width = column4_width, master = OUTPUTS);
Output_data_B = tk.Label(text = "--", fg = "black", width = column4_width, master = OUTPUTS);			#, bg = "white"
Output_data_labelA.pack();
Output_data_A.pack();
Output_data_B.pack();



######################################################
bottom_label = tk.Label(text = "Made by Reuben", fg = "black", bg = "white", width = total_width, height = 1, master = BOTTOM);
bottom_label.pack();
######################################################


WRITING.grid(row = 0, column = 0, columnspan = 3);
INPUTS.grid(row = 1, column = 0);
BUTTON.grid(row = 1, column = 1);
OUTPUTS.grid(row = 1, column = 2);
BOTTOM.grid(row = 2, column = 0, columnspan = 3);



##############
# end bit:
##############
window.mainloop();	# opens the window (keep at end?)