import tkinter as tk;

##############
# Definitions:
##############

### some words used alot:
# This is useful because I may spot a new unicode character or something that is more suitable, therefore will need to change one instead of lots of things
BE2_text = str("B(E2)\N{DOWNWARDS ARROW} (e^2 fm^4)");	# this is the better one? e2fm4
Beta_text = str("\N{LATIN SMALL LETTER SHARP S}");
BE2_to_Beta_text = str("B(E2) \N{RIGHTWARDS ARROW} \N{LATIN SMALL LETTER SHARP S}");
Beta_to_BE2_text = str("\N{LATIN SMALL LETTER SHARP S} \N{RIGHTWARDS ARROW} B(E2)");
###



def Director():		# This enormous lump is the part which says what to go to for every option. Haven't bothered trying to be smart, just all possibilities typed out. 
	Prot_num = int(Input_data_Z.get());	# proton number
	Mass_num = int(Input_data_A.get());	# mass number
	e_num = 1;	# assuming electron's charge is still just 1
	Input_num = float(Input_data_Main.get());

	input_selection = str(want_menu_variable.get());

	if input_selection == "select option":
		Output_data_A["text"] = "Select Something.\n WHY!";

	if input_selection == BE2_to_Beta_text:
		Output_data_A["text"] = BE2_to_Beta(Prot_num, Mass_num, e_num, Input_num);

	if input_selection == Beta_to_BE2_text:
		Output_data_A["text"] = Beta_to_BE2(Prot_num, Mass_num, e_num, Input_num);
	return





def BE2_to_Beta(Prot_num, Mass_num, e_num, Input_num):
	Answer = float( ((4*3.14159265359)/(3*Prot_num*(R0_number(Mass_num)**2))) * (( Input_num/(e_num**2) )**(0.5)) );
	return Answer;

def Beta_to_BE2(Prot_num, Mass_num, e_num, Input_num):
	Answer = float( (((Input_num*3*Prot_num*(R0_number(Mass_num)**2))/(4*3.14159265359))**2)*(e_num**2) );
	return Answer;


def R0_number(Mass_num):
	Answer = 1.2 * (Mass_num**(1/3));
	return Answer;




##############
# windows, buttons, boxes, etc.:
##############

window = tk.Tk();	# declares window
window.title("BE2 \N{LEFT RIGHT ARROW} \N{LATIN SMALL LETTER SHARP S} Calculator");

window.rowconfigure(0, minsize = 50, weight = 1);
window.columnconfigure(0, minsize = 50, weight = 1);

WRITING = tk.Frame(relief = tk.RAISED, master = window);	# Writing and explanation
GENERAL = tk.Frame(relief = tk.RAISED, master = window);		# The GENERAL inputs
DIRECTION = tk.Frame(relief = tk.RAISED, master = window);		# The input
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

title_words = str("BE2 <--> \N{LATIN SMALL LETTER SHARP S} Calculator");		# cant use \N{LEFT RIGHT ARROW} as it looks very bad
disclaimer_words = str("While every precaution has been taken,\nthere may be bugs so check first with known values.\n\n");
unit_words = str("This only does B(E2), not sure if there is an equation for others");
words = disclaimer_words + unit_words;
Top_Writing_words1 = tk.Label(text = title_words, master = WRITING, bg = "white", width = total_width-21, height = 1, font = ("Arial",15,"bold")); # total width minus something due to text size
Top_Writing_words2 = tk.Label(text = words, master = WRITING, bg = "white", width = total_width, height = 4);
Top_Writing_words1.pack();
Top_Writing_words2.pack();

######################################################

Input_data_labelA = tk.Label(master = GENERAL, text = "Mass Number (A)");
Input_data_A = tk.Entry(master = GENERAL, width = column1_width);
Input_data_labelZ = tk.Label(master = GENERAL, text = "Proton Number (Z)");
Input_data_Z = tk.Entry(master = GENERAL, width = column1_width);

Input_data_A.insert(0,"0"); # starting value to prevent bug
Input_data_Z.insert(0,"0"); # starting value to prevent bug

Input_data_labelA.pack();
Input_data_A.pack();
Input_data_labelZ.pack();
Input_data_Z.pack();

####




want_label = tk.Label(text = "Choose Direction", fg = "black", width = column2_width, master = DIRECTION);			#, bg = "white"
want_menu_options = [BE2_to_Beta_text, Beta_to_BE2_text];
want_menu_variable = tk.StringVar(DIRECTION);
want_menu_variable.set("select option");
want_menu = tk.OptionMenu(DIRECTION, want_menu_variable, *want_menu_options);

Input_data_Main_label = tk.Label(master = DIRECTION, text = "Input Value");
Input_data_Main = tk.Entry(master = DIRECTION, width = column2_width);

Input_data_Main.insert(0,"0"); # starting value to prevent bug

want_label.pack();
want_menu.pack();
Input_data_Main_label.pack();
Input_data_Main.pack();




######################################################
The_Button = tk.Button(text = "GO", font = ("default",20,"bold"), width = column3_width, height = 3, command = Director, master = BUTTON, bg = "green3");
The_Button.pack();
######################################################


Output_data_labelA = tk.Label(text = "Output", fg = "black", width = column4_width, master = OUTPUTS);			#, bg = "white"
Output_data_A = tk.Label(text = "--", fg = "black", bg = "white", width = column4_width, master = OUTPUTS);
Output_data_labelA.pack();
Output_data_A.pack();



######################################################
bottom_label = tk.Label(text = "Made by Reuben", fg = "black", bg = "white", width = total_width, height = 1, master = BOTTOM);
bottom_label.pack();
######################################################


WRITING.grid(row = 0, column = 0, columnspan = 4);
GENERAL.grid(row = 1, column = 0);
DIRECTION.grid(row = 1, column = 1);
BUTTON.grid(row = 1, column = 2);
OUTPUTS.grid(row = 1, column = 3);
BOTTOM.grid(row = 2, column = 0, columnspan = 4);



##############
# end bit:
##############
window.mainloop();	# opens the window (keep at end?)