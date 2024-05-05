import tkinter as tk;

##############
# Definitions:
##############


### some words used alot:
ME_text = str("Matrix Element (\N{MICRO SIGN}_N fm^((2L-2)/2) ) ");
BML_Wu_text = str("B(ML)\N{DOWNWARDS ARROW} (W.u.)");
BML_DWN_text = str("B(ML)\N{DOWNWARDS ARROW} (\N{MICRO SIGN}_N^2 fm^(2L-2))");
BML_UP_text = str("B(ML)\N{UPWARDS ARROW} (\N{MICRO SIGN}_N^2 fm^(2L-2))");
###



def Director():

	Mass_num = int(Input_data_A.get());
	lamda = int(Input_data_L.get());
	J_initial = int(Input_data_Ji.get());
	J_final = int(Input_data_Jf.get());
	Input_num = float(Input_data_Main.get());

	input_selection = str(menu_input_variable.get());
	want_selection = str(want_menu_variable.get());

	if input_selection == "select option" and want_selection != "select option":
		Output_data_A["text"] = "Select Something.\n PLEASE!";
		Output_data_B["text"] = "I agree with above.";

	if input_selection == "select option" and want_selection == "select option":	# Just a little reminder
		Output_data_A["text"] = "Fuck Off";
		Output_data_B["text"] = "(you forgot both inputs)";

	if input_selection != "select option" and want_selection == "select option":
		Output_data_A["text"] = "Why do you do these things?";
		Output_data_B["text"] = "Select a quantity to output.";




	if input_selection == ME_text:
		if want_selection == ME_text:
			Output_data_A["text"] = "COME ON!?!?!?";
			Output_data_B["text"] = "Go Away.";
		if want_selection == BML_Wu_text:
			Output_data_A["text"] = ME_BML_Wu(Mass_num, lamda, J_initial, Input_num);
			Output_data_B["text"] = "W.u.";
		if want_selection == BML_DWN_text:
			Output_data_A["text"] = ME_BML_DWN(J_initial, Input_num);
			Output_data_B["text"] = "(\N{MICRO SIGN}_N)^2 fm^"+f"{(2*lamda) -2}";
		if want_selection == BML_UP_text:
			Output_data_A["text"] = ME_BML_UP(J_initial, J_final, Input_num);
			Output_data_B["text"] = "(\N{MICRO SIGN}_N)^2 fm^"+f"{(2*lamda) -2}";

	if input_selection == BML_Wu_text:
		if want_selection == ME_text:
			Output_data_A["text"] = BML_Wu_ME(Mass_num, lamda, J_initial, Input_num);
			Output_data_B["text"] = "\N{MICRO SIGN}_N fm^"+f"{((2*lamda) -2)/2}";
		if want_selection == BML_Wu_text:
			Output_data_A["text"] = "COME ON!?!?!?";
			Output_data_B["text"] = "Try again ... \N{WHITE SMILING FACE}";
		if want_selection == BML_DWN_text:
			Output_data_A["text"] = BML_Wu_DWN(Mass_num, lamda, Input_num);
			Output_data_B["text"] = "(\N{MICRO SIGN}_N)^2 fm^"+f"{(2*lamda) -2}";
		if want_selection == BML_UP_text:
			Output_data_A["text"] = BML_Wu_UP(Mass_num, lamda, J_initial, J_final, Input_num);
			Output_data_B["text"] = "(\N{MICRO SIGN}_N)^2 fm^"+f"{(2*lamda) -2}";

	if input_selection == BML_DWN_text:
		if want_selection == ME_text:
			Output_data_A["text"] = BML_DWN_ME(J_initial, Input_num);
			Output_data_B["text"] = "\N{MICRO SIGN}_N fm^"+f"{((2*lamda) -2)/2}";
		if want_selection == BML_Wu_text:
			Output_data_A["text"] = BML_DWN_Wu(Mass_num, lamda, Input_num);
			Output_data_B["text"] = "W.u.";
		if want_selection == BML_DWN_text:
			Output_data_A["text"] = "COME ON!?!?!?";
			Output_data_B["text"] = "Just; no.";
		if want_selection == BML_UP_text:
			Output_data_A["text"] = BML_DWN_UP(J_initial, J_final, Input_num);
			Output_data_B["text"] = "(\N{MICRO SIGN}_N)^2 fm^"+f"{(2*lamda) -2}";

	if input_selection == BML_UP_text:
		if want_selection == ME_text:
			Output_data_A["text"] = BML_UP_ME(J_initial, J_final, Input_num);
			Output_data_B["text"] = "\N{MICRO SIGN}_N fm^"+f"{((2*lamda) -2)/2}";
		if want_selection == BML_Wu_text:
			Output_data_A["text"] = BML_UP_Wu(Mass_num, lamda, J_initial, J_final, Input_num);
			Output_data_B["text"] = "W.u.";
		if want_selection == BML_DWN_text:
			Output_data_A["text"] = BML_UP_DWN(J_initial, J_final, Input_num);
			Output_data_B["text"] = "(\N{MICRO SIGN}_N)^2 fm^"+f"{(2*lamda) -2}";
		if want_selection == BML_UP_text:
			Output_data_A["text"] = "COME ON!?!?!?";
			Output_data_B["text"] = "Go and have a break\nthen try again";

	return




			## Useful equations that do stuff: ##

def ME_BML_DWN(J_initial, Input_num):
	Answer = float( (Input_num **(2))/((2*J_initial)+1) );
	return Answer;

def BML_Wu_DWN(Mass_num, lamda, Input_num):
	Answer = float( Input_num * ( ((10*(1.2**((2*lamda) -2)))/3) * ((3/(lamda +3))**2) * (Mass_num ** ( ((2*lamda) -2) /3)) ) );
	return Answer;

def BML_DWN_ME(J_initial, Input_num):
	Answer = float( (Input_num * ( (2*J_initial) +1 ))**(0.5) );
	return Answer;

def BML_DWN_Wu(Mass_num, lamda, Input_num):
	Answer = float( Input_num / ( ((10*(1.2**((2*lamda) -2)))/3) * ((3/(lamda +3))**2) * (Mass_num ** ( ((2*lamda) -2) /3)) ) );
	return Answer;


			## Equations made up of the useful ones: ##


def ME_BML_Wu(Mass_num, lamda, J_initial, Input_num):
	Answer = float( BML_DWN_Wu(Mass_num, lamda, ME_BML_DWN(J_initial, Input_num) ) );
	return Answer;

def ME_BML_UP(J_initial, J_final, Input_num):
	Answer = float( BML_DWN_UP(J_initial, J_final, ME_BML_DWN(J_initial, Input_num)) );
	return Answer;

def BML_Wu_ME(Mass_num, lamda, J_initial, Input_num):
	Answer = float( BML_DWN_ME(J_initial, BML_Wu_DWN(Mass_num, lamda, Input_num)) );
	return Answer;

def BML_Wu_UP(Mass_num, lamda, J_initial, J_final, Input_num):
	Answer = float( BML_DWN_UP(J_initial, J_final, BML_Wu_DWN(Mass_num, lamda, Input_num)) );
	return Answer;

def BML_UP_ME(J_initial, J_final, Input_num):
	Answer = float( BML_DWN_ME(J_initial, BML_UP_DWN(J_initial, J_final, Input_num)) );
	return Answer;

def BML_UP_Wu(Mass_num, lamda, J_initial, J_final, Input_num):
	Answer = float( BML_UP_DWN(J_initial, J_final, BML_DWN_Wu(Mass_num, lamda, Input_num)) );
	return Answer;



				## Up and Down B(ML) converters: ##

def BML_DWN_UP(J_initial, J_final, Input_num):			# converter rather than caring about unit, so can be used for e^2b^L and e^2fm^2L if the same before and after units
	Answer = float( Input_num * (   ( (2*J_initial)  +1 ) / ( (2*J_final)  +1)  ) );
	return Answer;

def BML_UP_DWN(J_initial, J_final, Input_num):			# converter rather than caring about unit, so can be used for e^2b^L and e^2fm^2L if the same before and after units
	Answer = float( Input_num / (   ( (2*J_initial)  +1 ) / ( (2*J_final)  +1)  ) );
	return Answer;








##############
# windows, buttons, boxes, etc.:
##############

window = tk.Tk();	# declares window
window.title("B(ML) Calculator");

window.rowconfigure(0, minsize = 50, weight = 1);
window.columnconfigure(0, minsize = 50, weight = 1);

WRITING = tk.Frame(relief = tk.RAISED, master = window);	# Writing and explanation
INPUTS = tk.Frame(relief = tk.RAISED, master = window);		# Input values
WANTS = tk.Frame(relief = tk.RAISED, master = window);		# What output do you want?
BUTTON = tk.Frame(relief = tk.RAISED, master = window);		# Go button
OUTPUTS = tk.Frame(relief = tk.RAISED, master = window);	# The output
BOTTOM = tk.Frame(relief = tk.RAISED, master = window);		# bottom blank space, maybe good for credits

######################################################
# Sizing:
total_width = int(75);
column1_width = int(20);
column2_width = int(20);
column3_width = int(5); # button location (not same width as the others - because of text size)
column4_width = int(20);
###########

title_words = str("B(ML) Calculator");		# cant use \N{LEFT RIGHT ARROW} as it looks very bad
disclaimer_words = str("While every precaution has been taken,\nthere may be bugs so check first with known values.\n\n");
unit_words = str("NOTE: J_i (initial) and J_f (final) are treated as higher and lower respectively.");
words = disclaimer_words + unit_words;
Top_Writing_words1 = tk.Label(text = title_words, master = WRITING, bg = "white", width = total_width-22, height = 1, font = ("Arial",15,"bold")); # total width minus something due to text size
Top_Writing_words2 = tk.Label(text = words, master = WRITING, bg = "white", width = total_width, height = 4);
Top_Writing_words1.pack();
Top_Writing_words2.pack();

######################################################

# Input_box = tk.Label(bg = "white", master = INPUTS, borderwidth = 1, width = 20, height = 10);
Input_data_labelA = tk.Label(master = INPUTS, text = "Mass Number (A)");
Input_data_A = tk.Entry(master = INPUTS, width = column1_width);
Input_data_labelL = tk.Label(master = INPUTS, text = "Multipolarity (L)");
Input_data_L = tk.Entry(master = INPUTS, width = column1_width);
Input_data_labelJi = tk.Label(master = INPUTS, text = "Initial Spin (J_i)");
Input_data_Ji = tk.Entry(master = INPUTS, width = column1_width);
Input_data_labelJf = tk.Label(master = INPUTS, text = "Final Spin (J_f)");
Input_data_Jf = tk.Entry(master = INPUTS, width = column1_width);
# Input_data_labelJf = tk.Label(master = INPUTS, text = "Final Spin (J_f)");



menu_option_label = tk.Label(master = INPUTS, text = "Select Main Input");
## Drop down menu is something like this:	check this out in the morning: https://www.tutorialsfreak.com/python-tutorial/drop-down-menus-in-python-tkinter
menu_options = [ME_text, BML_Wu_text, BML_DWN_text, BML_UP_text];
menu_input_variable = tk.StringVar(INPUTS);
menu_input_variable.set("select option");
menu = tk.OptionMenu(INPUTS, menu_input_variable, *menu_options);

Input_data_labelMain = tk.Label(master = INPUTS, text = "Main Input:");
Input_data_Main = tk.Entry(master = INPUTS, width = column1_width);


## a couple of bits to have a starting value and prevent errors
Input_data_A.insert(0,"0");
Input_data_L.insert(0,"0");
Input_data_Ji.insert(0,"0");
Input_data_Jf.insert(0,"0");
Input_data_Main.insert(0,"0");
#####


Input_data_labelA.pack();
Input_data_A.pack();
Input_data_labelL.pack();
Input_data_L.pack();
Input_data_labelJi.pack();
Input_data_Ji.pack();
Input_data_labelJf.pack();
Input_data_Jf.pack();
menu_option_label.pack();
menu.pack();
Input_data_labelMain.pack();
Input_data_Main.pack();
# Input_box.pack(padx = 1, pady = 1);


###############




want_label = tk.Label(text = "Choose Output", fg = "black", width = column2_width, master = WANTS);			#, bg = "white"
want_menu_options = [ME_text, BML_Wu_text, BML_DWN_text, BML_UP_text];
want_menu_variable = tk.StringVar(WANTS);
want_menu_variable.set("select option");
want_menu = tk.OptionMenu(WANTS, want_menu_variable, *want_menu_options);

Input_data_labelB = tk.Label(master = WANTS, text = "Output: ");
Input_data_B = tk.Entry(master = WANTS, width = column2_width);

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
Output_data_labelB = tk.Label(text = "Output", fg = "black", width = column4_width, master = OUTPUTS);			#, bg = "white"
Output_data_B = tk.Label(text = "--", fg = "black", bg = "white", width = column4_width, master = OUTPUTS);
Output_data_labelA.pack();
Output_data_A.pack();
Output_data_labelB.pack();
Output_data_B.pack();



######################################################
bottom_label = tk.Label(text = "Made by Reuben", fg = "black", bg = "white", width = total_width, height = 1, master = BOTTOM);
bottom_label.pack();
######################################################


WRITING.grid(row = 0, column = 0, columnspan = 4);
INPUTS.grid(row = 1, column = 0);
WANTS.grid(row = 1, column = 1);
BUTTON.grid(row = 1, column = 2);
OUTPUTS.grid(row = 1, column = 3);
BOTTOM.grid(row = 2, column = 0, columnspan = 4);



##############
# end bit:
##############
window.mainloop();	# opens the window (keep at end?)