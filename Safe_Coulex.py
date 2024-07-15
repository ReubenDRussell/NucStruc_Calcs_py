import tkinter as tk;
import numpy as np;

##############
# Definitions:
##############

E_BOMB_text = str("Bombarding Energy (MeV)");	# inputting bombarding energy, wanting separation in fm
SEPARATION_text =str("Separation (fm)");	# inputting separation, wanting bombarding energy in MeV


def Director():
	Mass1 = int(Input_data_A1.get());	#projectile
	Mass2 = int(Input_data_A2.get());	#target
	Prot1 = int(Input_data_Z1.get());	#projectile
	Prot2 = int(Input_data_Z2.get());	#target
	Theta = float(Input_data_Theta.get());

	Input_num = float(Input_data_B.get());
	input_selection = str(want_menu_variable.get());

	if input_selection == "select option":
		Output_data_A["text"] = "Select Something.\n OR I WILL FIND YOU!";
		Output_data_B["text"] = "(Do what he says, he means it?)";

	if input_selection == SEPARATION_text:
		Output_data_A["text"] = E_bomb_sep(Mass1,Mass2,Prot1,Prot2,Theta,Input_num);
		Output_data_B["text"] = "MeV";

	if input_selection == E_BOMB_text:
		Output_data_A["text"] = Sep_E_bomb(Mass1,Mass2,Prot1,Prot2,Theta,Input_num);
		Output_data_B["text"] = "fm";
	return










def E_bomb_sep(Mass1,Mass2,Prot1,Prot2,Theta,Input_num):	# manually input separation distance AND manually input Theta
	Answer = float( 0.72*(1+ (1/(np.sin(np.radians(Theta/2)))))*((Mass1 + Mass2)/Mass2)*( (Prot1*Prot2)/( (1.25*((Mass1**(1/3))+(Mass2**(1/3)))) +Input_num) ) );
	return Answer;


# def E_bomb_Cline(Mass1,Mass2,Prot1,Prot2,Theta):	# use separation = 5fm AND manually input Theta
# 	Answer = float( 0.72*(1+ (1/(np.sin(Theta/2))))*((Mass1 + Mass2)/Mass2)*( (Prot1*Prot2)/( 1.25*((Mass1**(1/3))+(Mass2**(1/3))) +5) ) );
# 	return Answer;


# def E_max_sep(Mass1,Mass2,Prot1,Prot2,Separation):	# manually input separation AND using Theta = 180deg
# 	Answer = float( 1.44*((Mass1 + Mass2)/Mass2)*( (Prot1*Prot2)/( 1.25*((Mass1**(1/3))+(Mass2**(1/3))) +Separation) ) );
# 	return Answer;


# def E_max_Cline(Mass1,Mass2,Prot1,Prot2):	# use separation = 5fm AND using Theta = 180deg
# 	Answer = float( 1.44*((Mass1 + Mass2)/Mass2)*( (Prot1*Prot2)/( 1.25*((Mass1**(1/3))+(Mass2**(1/3))) +5) ) );
# 	return Answer;


def Sep_E_bomb(Mass1,Mass2,Prot1,Prot2,Theta,Input_num):	# manually put in Bombarding Energy AND Theta
	Answer = float( (0.72*(1+ (1/(np.sin(np.radians(Theta/2)))))*((Mass1 + Mass2)/Mass2)*( (Prot1*Prot2)/(Input_num)) - (1.25*((Mass1**(1/3))+(Mass2**(1/3)))))  );
	return Answer;






##############
# windows, buttons, boxes, etc.:
##############

window = tk.Tk();	# declares window
window.title("Safe Coulex Energy Calculator");

window.rowconfigure(0, minsize = 50, weight = 1);
window.columnconfigure(0, minsize = 50, weight = 1);

WRITING = tk.Frame(relief = tk.RAISED, master = window);	# Writing and explanation
INPUTS = tk.Frame(relief = tk.RAISED, master = window);		# The input
INPUTS2 = tk.Frame(relief = tk.RAISED, master = window);
BUTTON = tk.Frame(relief = tk.RAISED, master = window);		# Go button
OUTPUTS = tk.Frame(relief = tk.RAISED, master = window);	# The output
BOTTOM = tk.Frame(relief = tk.RAISED, master = window);		# Bottom band

######################################################
# Sizing:
total_width = int(105);
column1_width = int(10);
column2_width = int(20);
column3_width = int(5); # button location (not same width as the others - because of text size)
column4_width = int(20);
###########

title_words = str("Safe Coulex Calculator");		# cant use \N{LEFT RIGHT ARROW} as it looks very bad
disclaimer_words = str("While every precaution has been taken,\nthere may be bugs so check first with known values.\n\n");
unit_words = str("Input the bombarding energy or separation you want to find the other for\n");
other_words = str("Bombarding energy is in MeV and is the energy of the projectile before interaction with the target (Max at Theta = 180 degrees)\n");
more_words = str("Separation is in fm, this is the gap between the approximate edges of the nuclei (5fm for Cline criterion)");
words = disclaimer_words + unit_words + other_words + more_words;
Top_Writing_words1 = tk.Label(text = title_words, master = WRITING, bg = "white", width = total_width-31, height = 1, font = ("Arial",15,"bold")); # total width minus something due to text size
Top_Writing_words2 = tk.Label(text = words, master = WRITING, bg = "white", width = total_width, height = 9);
Top_Writing_words1.pack();
Top_Writing_words2.pack();

######################################################


Input_data_labelA1 = tk.Label(master = INPUTS, text = "Projectile Mass Number (A)");
Input_data_A1 = tk.Entry(master = INPUTS, width = column1_width);
Input_data_labelA2 = tk.Label(master = INPUTS, text = "Target Mass Number (A)");
Input_data_A2 = tk.Entry(master = INPUTS, width = column1_width);
Input_data_labelZ1 = tk.Label(master = INPUTS, text = "Projectile Proton Number (Z)");
Input_data_Z1 = tk.Entry(master = INPUTS, width = column1_width);
Input_data_labelZ2 = tk.Label(master = INPUTS, text = "Target Proton Number (Z)");
Input_data_Z2 = tk.Entry(master = INPUTS, width = column1_width);
Input_data_labelTheta = tk.Label(master = INPUTS, text = "Scattering Angle (\N{GREEK SMALL LETTER THETA})");
Input_data_Theta = tk.Entry(master = INPUTS, width = column1_width);


want_label = tk.Label(text = "What are you inputting?", fg = "black", width = column2_width, master = INPUTS2);			#, bg = "white"
want_menu_options = [SEPARATION_text, E_BOMB_text];
want_menu_variable = tk.StringVar(INPUTS2);
want_menu_variable.set("select option");
want_menu = tk.OptionMenu(INPUTS2, want_menu_variable, *want_menu_options);

Input_data_labelB = tk.Label(master = INPUTS2, text = "Input");
Input_data_B = tk.Entry(master = INPUTS2, width = column2_width);

Input_data_B.insert(0,"0"); # starting value to prevent bug






Input_data_labelA1.pack();
Input_data_A1.pack();
Input_data_labelA2.pack();
Input_data_A2.pack();
Input_data_labelZ1.pack();
Input_data_Z1.pack();
Input_data_labelZ2.pack();
Input_data_Z2.pack();
Input_data_labelTheta.pack();
Input_data_Theta.pack();


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


WRITING.grid(row = 0, column = 0, columnspan = 4);
INPUTS.grid(row = 1, column = 0);
INPUTS2.grid(row =1, column = 1);
BUTTON.grid(row = 1, column = 2);
OUTPUTS.grid(row = 1, column = 3);
BOTTOM.grid(row = 2, column = 0, columnspan = 4);



##############
# end bit:
##############
window.mainloop();	# opens the window (keep at end?)