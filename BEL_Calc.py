import tkinter as tk;

##############
# Definitions:
##############

### some words used alot:
# This is useful because I may spot a new unicode character or something that is more suitable, therefore will need to change one instead of lots of things
ME_text = str("Matrix Element (eb^(L/2))");				# this is the better one
BEL_Wu_text = str("B(EL)\N{DOWNWARDS ARROW} (W.u.)");
BEL_e2fm2L_text = str("B(EL)\N{DOWNWARDS ARROW} (e^2 fm^(2L))");	# this is the better one?
ME_efmL_text = str("Matrix Element (e fm^L)");
BEL_e2bL_text = str("B(EL)\N{DOWNWARDS ARROW} (e^2 b^L)");
BEL_e2fm2L_UP_text = str("B(EL)\N{UPWARDS ARROW} (e^2 fm^(2L))");
BEL_e2bL_UP_text = str("B(EL)\N{UPWARDS ARROW} (e^2 b^L)");
###



def Director():		# This enormous lump is the part which says what to go to for every option. Haven't bothered trying to be smart, just all possibilities typed out. 
	Mass_num = int(Input_data_A.get());
	lamda = int(Input_data_L.get());
	J_initial = int(Input_data_Ji.get());
	J_final = int(Input_data_Jf.get());
	Input_num = float(Input_data_Main.get());

	input_selection = str(menu_test_variable.get());
	want_selection = str(want_menu_variable.get());

	if input_selection == "select option":	# Just a little reminder
		Output_data_1["text"] = "Fuck Off";
		Output_data_2["text"] = "(you forgot input)";
	if input_selection == "select option" and want_selection != "select option":	# Just a little reminder
		Output_data_1["text"] = "Fuck Off";
		Output_data_2["text"] = "(you forgot input)";
	if input_selection != "select option" and want_selection == "select option": # and is equivalent to &&
		Output_data_1["text"] = "Why do you hate me!?";
		Output_data_2["text"] = "(choose output quantity)";
	
	if input_selection == ME_text:
		# Output_data_1["text"] = "it worked? M.E.";
		if want_selection == ME_text:
			Output_data_1["text"] = "COME ON!?!?!?";
			Output_data_2["text"] = "Go Away.";
		if want_selection == BEL_Wu_text:
			Output_data_1["text"] = ME_BEL_Wu(Mass_num, lamda, J_initial, Input_num);
			Output_data_2["text"] = "W.u.";
		if want_selection == BEL_e2fm2L_text:
			Output_data_1["text"] = ME_BEL_e2fm2L(lamda, J_initial, Input_num);
			Output_data_2["text"] = "e^2 fm^"+f"{2*lamda}";
		if want_selection == ME_efmL_text:
			Output_data_1["text"] = ME_eb_efmL(lamda, Input_num);
			Output_data_2["text"] = "e fm^"+f"{lamda}";
		if want_selection == BEL_e2bL_text:
			Output_data_1["text"] = ME_BEL_e2bL(J_initial, Input_num);
			Output_data_2["text"] = "e^2 b^"+f"{lamda}";
		if want_selection == BEL_e2fm2L_UP_text:
			Output_data_1["text"] = ME_BEL_e2fm2L_UP(lamda, J_initial, J_final, Input_num);
			Output_data_2["text"] = "e^2 fm^"+f"{2*lamda}";
		if want_selection == BEL_e2bL_UP_text:
			Output_data_1["text"] = ME_BEL_e2bL_UP(J_initial, J_final, Input_num);
			Output_data_2["text"] = "e^2 b^"+f"{lamda}";

	if input_selection == ME_efmL_text:
		# Output_data_1["text"] = "it worked? M.E.";
		if want_selection == ME_text:
			Output_data_1["text"] = ME_efmL_eb(lamda, Input_num);
			Output_data_2["text"] = "eb^"+f"{lamda/2}";
		if want_selection == BEL_Wu_text:
			Output_data_1["text"] = ME_efmL_BEL_Wu(Mass_num, lamda, J_initial, Input_num);
			Output_data_2["text"] = "W.u.";
		if want_selection == BEL_e2fm2L_text:
			Output_data_1["text"] = ME_efmL_BEL_e2fm2L(lamda, J_initial, Input_num);
			Output_data_2["text"] = "e^2 fm^"+f"{2*lamda}";
		if want_selection == ME_efmL_text:
			Output_data_1["text"] = "COME ON!?!?!?";
			Output_data_2["text"] = "Go Away.";
		if want_selection == BEL_e2bL_text:
			Output_data_1["text"] =	ME_efmL_BEL_e2bL(lamda, J_initial, Input_num);
			Output_data_2["text"] = "e^2 b^"+f"{lamda}";
		if want_selection == BEL_e2fm2L_UP_text:
			Output_data_1["text"] = ME_efmL_BEL_e2fm2L_UP(lamda, J_initial, J_final, Input_num);
			Output_data_2["text"] = "e^2 fm^"+f"{2*lamda}";
		if want_selection == BEL_e2bL_UP_text:
			Output_data_1["text"] = ME_efmL_BEL_e2bL_UP(lamda, J_initial, J_final, Input_num);
			Output_data_2["text"] = "e^2 b^"+f"{lamda}";

	if input_selection == BEL_Wu_text:
		if want_selection == ME_text:
			Output_data_1["text"] = BEL_Wu_ME(Mass_num, lamda, J_initial, Input_num);
			Output_data_2["text"] = "eb^"+f"{lamda/2}";
		if want_selection == BEL_Wu_text:
			Output_data_1["text"] = "COME ON!?!?!?";
			Output_data_2["text"] = "Idiot.";
		if want_selection == BEL_e2fm2L_text:
			Output_data_1["text"] = BEL_Wu_e2fm2L(Mass_num, lamda, Input_num);
			Output_data_2["text"] = "e^2 fm^"+f"{2*lamda}";
		if want_selection == ME_efmL_text:
			Output_data_1["text"] = BEL_Wu_ME_efmL(Mass_num, lamda, J_initial, Input_num);
			Output_data_2["text"] = "e fm^"+f"{lamda}";
		if want_selection == BEL_e2bL_text:
			Output_data_1["text"] =	BEL_Wu_e2bL(Mass_num, lamda, Input_num);
			Output_data_2["text"] = "e^2 b^"+f"{lamda}";
		if want_selection == BEL_e2fm2L_UP_text:
			Output_data_1["text"] = BEL_Wu_e2fm2L_UP(Mass_num, lamda, J_initial, J_final, Input_num);
			Output_data_2["text"] = "e^2 fm^"+f"{2*lamda}";
		if want_selection == BEL_e2bL_UP_text:
			Output_data_1["text"] = BEL_Wu_e2bL_UP(Mass_num, lamda, J_initial, J_final, Input_num);
			Output_data_2["text"] = "e^2 b^"+f"{lamda}";

	if input_selection == BEL_e2fm2L_text:
		if want_selection == ME_text:
			Output_data_1["text"] = BEL_e2fm2L_ME(lamda, J_initial, Input_num);
			Output_data_2["text"] = "eb^"+f"{lamda/2}";
		if want_selection == BEL_Wu_text:
			Output_data_1["text"] = BEL_e2fm2L_Wu(Mass_num, lamda, Input_num);
			Output_data_2["text"] = "W.u.";
		if want_selection == BEL_e2fm2L_text:
			Output_data_1["text"] = "COME ON!?!?!?";
			Output_data_2["text"] = "Why do you try?";
		if want_selection == ME_efmL_text:
			Output_data_1["text"] = BEL_e2fm2L_ME_efmL(lamda, J_initial, Input_num);
			Output_data_2["text"] = "e fm^"+f"{lamda}";
		if want_selection == BEL_e2bL_text:
			Output_data_1["text"] = BEL_e2fm2L_e2bL(lamda, Input_num);
			Output_data_2["text"] = "e^2 b^"+f"{lamda}";
		if want_selection == BEL_e2fm2L_UP_text:
			Output_data_1["text"] = BEL_DWN_UP(J_initial, J_final, Input_num);	# going to same unit so bounce it to converter
			Output_data_2["text"] = "e^2 fm^"+f"{2*lamda}";
		if want_selection == BEL_e2bL_UP_text:
			Output_data_1["text"] = BEL_e2fm2L_e2bL_UP(lamda, J_initial, J_final, Input_num);
			Output_data_2["text"] = "e^2 b^"+f"{lamda}";

	if input_selection == BEL_e2bL_text:
		if want_selection == ME_text:
			Output_data_1["text"] = BEL_e2bL_ME(J_initial, Input_num);
			Output_data_2["text"] = "eb^"+f"{lamda/2}";
		if want_selection == BEL_Wu_text:
			Output_data_1["text"] = BEL_e2bL_Wu(Mass_num, lamda, Input_num);
			Output_data_2["text"] = "W.u.";
		if want_selection == BEL_e2fm2L_text:
			Output_data_1["text"] = BEL_e2bL_e2fm2L(lamda, Input_num);
			Output_data_2["text"] = "e^2 fm^"+f"{2*lamda}";
		if want_selection == ME_efmL_text:
			Output_data_1["text"] = BEL_e2bL_ME_efmL(lamda, J_initial, Input_num);
			Output_data_2["text"] = "e fm^"+f"{lamda}";
		if want_selection == BEL_e2bL_text:
			Output_data_1["text"] = "COME ON!?!?!?";
			Output_data_2["text"] = "Is your brain working?";
		if want_selection == BEL_e2fm2L_UP_text:
			Output_data_1["text"] = BEL_e2bL_e2fm2L_UP(lamda, J_initial, J_final, Input_num);
			Output_data_2["text"] = "e^2 fm^"+f"{2*lamda}";
		if want_selection == BEL_e2bL_UP_text:
			Output_data_1["text"] = BEL_DWN_UP(J_initial, J_final, Input_num);	# going to same unit so bounce it to converter
			Output_data_2["text"] = "e^2 b^"+f"{lamda}";

	if input_selection == BEL_e2fm2L_UP_text:
		if want_selection == ME_text:
			Output_data_1["text"] = BEL_e2fm2L_UP_ME(lamda, J_initial, J_final, Input_num);
			Output_data_2["text"] = "eb^"+f"{lamda/2}";
		if want_selection == BEL_Wu_text:
			Output_data_1["text"] = BEL_e2fm2L_UP_Wu(Mass_num, lamda, J_initial, J_final, Input_num);
			Output_data_2["text"] = "W.u.";
		if want_selection == BEL_e2fm2L_text:
			Output_data_1["text"] = BEL_UP_DWN(J_initial, J_final, Input_num);	# going to same unit so bounce it to converter
			Output_data_2["text"] = "e^2 fm^"+f"{2*lamda}";
		if want_selection == ME_efmL_text:
			Output_data_1["text"] = BEL_e2fm2L_UP_ME_efmL(lamda, J_initial, J_final, Input_num);
			Output_data_2["text"] = "e fm^"+f"{lamda}";
		if want_selection == BEL_e2bL_text:
			Output_data_1["text"] = BEL_e2fm2L_UP_e2bL(lamda, J_initial, J_final, Input_num);
			Output_data_2["text"] = "e^2 b^"+f"{lamda}";
		if want_selection == BEL_e2fm2L_UP_text:
			Output_data_1["text"] = "COME ON!?!?!?";
			Output_data_2["text"] = "I give up...";
		if want_selection == BEL_e2bL_UP_text:
			Output_data_1["text"] = BEL_e2fm2L_UP_e2bL_UP(lamda, J_initial, J_final, Input_num);
			Output_data_2["text"] = "e^2 b^"+f"{lamda}";

	if input_selection == BEL_e2bL_UP_text:
		if want_selection == ME_text:
			Output_data_1["text"] = BEL_e2bL_UP_ME(J_initial, J_final, Input_num);
			Output_data_2["text"] = "eb^"+f"{lamda/2}";
		if want_selection == BEL_Wu_text:
			Output_data_1["text"] = BEL_e2bL_UP_Wu(Mass_num, lamda, J_initial, J_final, Input_num);
			Output_data_2["text"] = "W.u.";
		if want_selection == BEL_e2fm2L_text:
			Output_data_1["text"] = BEL_e2bL_UP_e2fm2L(lamda, J_initial, J_final, Input_num);
			Output_data_2["text"] = "e^2 fm^"+f"{2*lamda}";
		if want_selection == ME_efmL_text:
			Output_data_1["text"] = BEL_e2bL_UP_ME_efmL(lamda, J_initial, J_final, Input_num);
			Output_data_2["text"] = "e fm^"+f"{lamda}";
		if want_selection == BEL_e2bL_text:
			Output_data_1["text"] = BEL_UP_DWN(J_initial, J_final, Input_num);	# going to same unit so bounce it to converter
			Output_data_2["text"] = "e^2 b^"+f"{lamda}";
		if want_selection == BEL_e2fm2L_UP_text:
			Output_data_1["text"] = BEL_e2bL_UP_e2fm2L_UP(lamda, J_initial, J_final, Input_num);
			Output_data_2["text"] = "e^2 fm^"+f"{2*lamda}";
		if want_selection == BEL_e2bL_UP_text:
			Output_data_1["text"] = "COME ON!?!?!?";
			Output_data_2["text"] = "Dont.";

	return # just in case nothing is accepted

			## Useful equations that do stuff: ##

def BEL_Wu_e2fm2L(Mass_num, lamda, Input_num):			# B(EL) in W.u. to B(EL) in e^2fm^2L
	Answer = float( Input_num * (( ((1.2)**(2 * lamda)) / (4*3.14159265359) ) * (( 3  / (lamda + 3)) **2 ) * ( Mass_num **( (2*lamda) / 3) )) );
	return Answer;

def BEL_e2fm2L_Wu(Mass_num, lamda, Input_num):			# B(EL) in e^2fm^2L to B(EL) in W.u.
	Answer = float( Input_num / (( ((1.2)**(2 * lamda)) / (4*3.14159265359) ) * (( 3  / (lamda + 3)) **2 ) * ( Mass_num **( (2*lamda) / 3) )) );
	return Answer;


def ME_BEL_e2bL(J_initial, Input_num):				# M.E. in eb^(L/2) to B(EL) in e^2b^L 
	Answer = float((Input_num **(2))/((2*J_initial)+1));
	return Answer;

def BEL_e2bL_ME(J_initial, Input_num):				# M.E. in e^2b^L to B(EL) in eb^(L/2)
	Answer = float( ((Input_num) * ( (2*J_initial) +1 ))**(0.5) );
	return Answer;


			## Equations made up of the useful ones: ##

def BEL_Wu_e2bL(Mass_num, lamda, Input_num):			# B(EL) in W.u. to B(EL) in e^2 b^L (via e^2fm^2L)
	Answer = float( UNIT_BEL_e2fm2L_e2bL(lamda, BEL_Wu_e2fm2L(Mass_num, lamda, Input_num)) );
	return Answer;

def BEL_e2bL_Wu(Mass_num, lamda, Input_num):			# B(EL) in e^2 b^L to B(EL) in W.u. (via e^2fm^2L)
	Answer = float( BEL_e2fm2L_Wu(Mass_num, lamda, UNIT_BEL_e2bL_e2fm2L(lamda, Input_num)) );
	return Answer;


def ME_eb_efmL(lamda, Input_num):				# just bounces to unit conversion
	Answer = float( UNIT_ME_eb_efmL(lamda, Input_num) );
	return Answer;

def ME_efmL_eb(lamda, Input_num):				# just bounces to unit conversion
	Answer = float( UNIT_ME_efmL_eb(lamda, Input_num) );
	return Answer;

def ME_BEL_e2fm2L(lamda, J_initial, Input_num):			# M.E. in eb^(L/2) to B(EL) in e^2fm^2L (via e^2b^L)
	Answer = float( UNIT_BEL_e2bL_e2fm2L(lamda, ME_BEL_e2bL(J_initial, Input_num)) );
	return Answer;

def BEL_e2fm2L_ME(lamda, J_initial, Input_num):			# B(EL) in e^2fm^2L to M.E. in eb^(L/2) (via e^2b^L)
	Answer = float( BEL_e2bL_ME(J_initial, UNIT_BEL_e2fm2L_e2bL(lamda, Input_num)) );


def ME_BEL_Wu(Mass_num, lamda, J_initial, Input_num):		# M.E. in eb^(L/2) to B(EL) in W.u. (via e^2b^L then e^2fm^2L)
	Answer = float( BEL_e2fm2L_Wu(Mass_num, lamda, UNIT_BEL_e2bL_e2fm2L(lamda, ME_BEL_e2bL(J_initial, Input_num))) );
	return Answer;

def BEL_Wu_ME(Mass_num, lamda, J_initial, Input_num):		# M.E. in eb^(L/2) to B(EL) in W.u. (via e^2fm^2L then e^2b^L)
	Answer = float( BEL_e2bL_ME(J_initial, UNIT_BEL_e2fm2L_e2bL(lamda, BEL_Wu_e2fm2L(Mass_num, lamda, Input_num))) );
	return Answer;


def ME_efmL_BEL_Wu(Mass_num, lamda, J_initial, Input_num):	# M.E. in efm^L to B(EL) in W.u. (via ME in eb^(L/2) then B(EL) in e^2b^L then e^2fm^2L)
	Answer = float( BEL_e2fm2L_Wu(Mass_num, lamda, UNIT_BEL_e2bL_e2fm2L(lamda, ME_BEL_e2bL(J_initial, UNIT_ME_eb_efmL(lamda, Input_num)))) );
	return Answer;

def BEL_Wu_ME_efmL(Mass_num, lamda, J_initial, Input_num):	# B(EL) in W.u. to M.E. in efm^L (via B(EL) in e^2fm^2L then e^2b^L then ME in eb^(L/2))
	Answer = float( UNIT_ME_eb_efmL(lamda, BEL_e2bL_ME(J_initial, UNIT_BEL_e2fm2L_e2bL(lamda, BEL_Wu_e2fm2L(Mass_num, lamda, Input_num)))) );
	return Answer;

def ME_efmL_BEL_e2bL(lamda, J_initial, Input_num):		# B(EL) in e^2b^L to M.E. in efm^L (via M.E. in eb^(L/2))
	Answer = float( ME_BEL_e2bL(J_initial, UNIT_ME_efmL_eb(lamda, Input_num)) );
	return Answer;

def BEL_e2bL_ME_efmL(lamda, J_initial, Input_num):		# M.E. in efm^L to B(EL) in e^2b^L (via M.E. in eb^(L/2))
	Answer = float( UNIT_ME_eb_efmL(lamda, BEL_e2bL_ME(J_initial, Input_num)) );
	return Answer;

def ME_efmL_BEL_e2fm2L(lamda, J_initial, Input_num):		# M.E. in efm^L to B(EL) in e^2fm^2L (via M.E. in eb^(L/2) then B(EL) in e^2b^L)
	Answer = float( ME_BEL_e2fm2L(lamda, J_initial, UNIT_ME_efmL_eb(lamda, Input_num)) );
	return Answer;

def BEL_e2fm2L_ME_efmL(lamda, J_initial, Input_num):		# B(EL) in e^2fm^2L to M.E. in efm^L (via B(EL) in e^2b^L then M.E. in eb^(L/2))
	Answer = float( UNIT_ME_eb_efmL(lamda, BEL_e2fm2L_ME(lamda, J_initial, Input_num)) );
	return Answer;

def BEL_e2fm2L_e2bL(lamda, Input_num):				# just bounces to unit conversion
	Answer = float( UNIT_BEL_e2fm2L_e2bL(lamda, Input_num) );
	return Answer;

def BEL_e2bL_e2fm2L(lamda, Input_num):				# just bounces to unit conversion
	Answer = float( UNIT_BEL_e2bL_e2fm2L(lamda, Input_num) );
	return Answer;

def ME_BEL_e2fm2L_UP(lamda, J_initial, J_final, Input_num):	# M.E. in eb^(L/2) to B(EL) in e^2fm^2L UP (using ME_BEL_e2fm2L() )
	Answer = float( BEL_DWN_UP(J_initial, J_final, ME_BEL_e2fm2L(lamda, J_initial, Input_num)) );
	return Answer;

def ME_BEL_e2bL_UP(J_initial, J_final, Input_num):		# M.E. in eb^(L/2) to B(EL) in e^2b^L UP (using ME_BEL_e2bL() )
	Answer = float( BEL_DWN_UP(J_initial, J_final, ME_BEL_e2bL(J_initial, Input_num)) );
	return Answer;

def ME_efmL_BEL_e2fm2L_UP(lamda, J_initial, J_final, Input_num):
	Answer = float( BEL_DWN_UP(J_initial, J_final, ME_efmL_BEL_e2fm2L(lamda, J_initial, Input_num)) );
	return Answer;

def ME_efmL_BEL_e2bL_UP(lamda, J_initial, J_final, Input_num):
	Answer = float( BEL_DWN_UP(J_initial, J_final, ME_efmL_BEL_e2bL(lamda, J_initial, Input_num)) );
	return Answer;

def BEL_Wu_e2fm2L_UP(Mass_num, lamda, J_initial, J_final, Input_num):
	Answer = float( BEL_DWN_UP(J_initial, J_final, BEL_Wu_e2fm2L(Mass_num, lamda, Input_num)) );
	return Answer;

def BEL_Wu_e2bL_UP(Mass_num, lamda, J_initial, J_final, Input_num):
	Answer = float( BEL_DWN_UP(J_initial, J_final, BEL_Wu_e2bL(Mass_num, lamda, Input_num)) );
	return Answer;

def BEL_e2fm2L_e2bL_UP(lamda, J_initial, J_final, Input_num):
	Answer = float( BEL_DWN_UP(J_initial, J_final, UNIT_BEL_e2fm2L_e2bL(lamda, Input_num)) );
	return Answer;

def BEL_e2bL_e2fm2L_UP(lamda, J_initial, J_final, Input_num):
	Answer = float( BEL_DWN_UP(J_initial, J_final, UNIT_BEL_e2bL_e2fm2L(lamda, Input_num)) );
	return Answer;

def BEL_e2fm2L_UP_ME(lamda, J_initial, J_final, Input_num):
	Answer = float( BEL_e2fm2L_ME(lamda, J_initial, BEL_UP_DWN(J_initial, J_final, Input_num)) );
	return Answer;

def BEL_e2fm2L_UP_Wu(Mass_num, lamda, J_initial, J_final, Input_num):
	Answer = float( BEL_e2fm2L_Wu(Mass_num, lamda, BEL_UP_DWN(J_initial, J_final, Input_num)) );
	return Answer;

def BEL_e2fm2L_UP_ME_efmL(lamda, J_initial, J_final, Input_num):
	Answer = float( BEL_e2fm2L_ME_efmL(lamda, J_initial, BEL_UP_DWN(J_initial, J_final, Input_num)) );
	return Answer;

def BEL_e2fm2L_UP_e2bL(lamda, J_initial, J_final, Input_num):
	Answer = float( UNIT_BEL_e2fm2L_e2bL(lamda, BEL_UP_DWN(J_initial, J_final, Input_num)) );
	return Answer;

def BEL_e2fm2L_UP_e2bL_UP(lamda, J_initial, J_final, Input_num):	# The middle steps here can probably be skipped but I am too sleepy to double check my thinking.
	Answer = float( BEL_DWN_UP(J_initial, J_final, UNIT_BEL_e2fm2L_e2bL(lamda, BEL_UP_DWN(J_initial, J_final, Input_num))) );
	return Answer;

def BEL_e2bL_UP_ME(J_initial, J_final, Input_num):
	Answer = float( BEL_e2bL_ME(J_initial, BEL_UP_DWN(J_initial, J_final, Input_num)) );
	return Answer;

def BEL_e2bL_UP_Wu(Mass_num, lamda, J_initial, J_final, Input_num):
	Answer = float( BEL_e2bL_Wu(Mass_num, lamda, BEL_UP_DWN(J_initial, J_final, Input_num)) );
	return Answer;

def BEL_e2bL_UP_e2fm2L(lamda, J_initial, J_final, Input_num):
	Answer = float( UNIT_BEL_e2bL_e2fm2L(lamda, BEL_UP_DWN(J_initial, J_final, Input_num)) );
	return Answer;

def BEL_e2bL_UP_ME_efmL(lamda, J_initial, J_final, Input_num):
	Answer = float( BEL_e2bL_ME_efmL(lamda, J_initial, BEL_UP_DWN(J_initial, J_final, Input_num)) );
	return Answer;

def BEL_e2bL_UP_e2fm2L_UP(lamda, J_initial, J_final, Input_num):	# The middle steps here can probably be skipped but I am too sleepy to double check my thinking.
	Answer = float( BEL_DWN_UP(J_initial, J_final, UNIT_BEL_e2bL_e2fm2L(lamda, BEL_UP_DWN(J_initial, J_final, Input_num))) );
	return Answer;


				## Up and Down B(EL) converters: ##

def BEL_DWN_UP(J_initial, J_final, Input_num):			# converter rather than caring about unit, so can be used for e^2b^L and e^2fm^2L if the same before and after units
	Answer = float( Input_num * (   ( (2*J_initial)  +1 ) / ( (2*J_final)  +1)  ) );
	return Answer;

def BEL_UP_DWN(J_initial, J_final, Input_num):			# converter rather than caring about unit, so can be used for e^2b^L and e^2fm^2L if the same before and after units
	Answer = float( Input_num / (   ( (2*J_initial)  +1 ) / ( (2*J_final)  +1)  ) );
	return Answer;


				## Unit converters: ##

#####################################################
#####	B(EL) numbers:	1 b^L = 100^L * fm^2L	#####
#####################################################################
#####	Matrix Element:	1 b^(L/2) = 100^(L/2) * fm^(2L/2)	#####
#####################################################################
#####	B(ML) number has unit of: mu_N fm^((2L-2)/2) only?	#####
#####################################################################


def UNIT_ME_eb_efmL(lamda, Input_num):
	Answer = float( Input_num *( 100 ** (lamda/2) ));
	return Answer;

def UNIT_ME_efmL_eb(lamda, Input_num):
	Answer = float( Input_num / ( 100 ** (lamda/2) ) );	# if L=2, equivalent to /100
	return Answer;

def UNIT_BEL_e2bL_e2fm2L(lamda, Input_num):
	Answer = float(Input_num * ( 100 **lamda ));
	return Answer;

def UNIT_BEL_e2fm2L_e2bL(lamda, Input_num):
	Answer = float(Input_num / ( 100 **lamda ));
	return Answer;


##########################
# End of Equations and definitions
##########################

##############
# windows, buttons, boxes, etc.:
##############

window = tk.Tk();	# declares window
window.title("B(EL) Calculator");

window.rowconfigure(0, minsize = 50, weight = 1);
window.columnconfigure(0, minsize = 50, weight = 1);

WRITING = tk.Frame(relief = tk.RAISED, master = window);	# Writing and explanation
INPUTS = tk.Frame(relief = tk.RAISED, master = window);		# Input values
WANTS = tk.Frame(relief = tk.RAISED, master = window);		# What output do you want?
BUTTON = tk.Frame(relief = tk.RAISED, master = window);		# Go button
OUTPUTS = tk.Frame(relief = tk.RAISED, master = window);	# The output
BOTTOM = tk.Frame(relief = tk.RAISED, master = window);		# bottom blank space, maybe good for credits

######################################################

# Top_Writing = tk.Label(bg = "white", master = WRITING, border = 1, width = 50, height = 5);


##############
# Sizing:
column1_width = int(25);
column2_width = int(25);
column3_width = int(5); # button location (not same width as the others?)
column4_width = int(20);
total_width = int(95);
##############
title_words = str("Test Calculator for B(EL)\n");
disclaimer_words = str("While every precaution has been taken, there may be bugs so check first with known values.\n\n");
spin_words = str("NOTE: J_i (initial) and J_f (final) are treated as J_i being the higher energy level, with J_f the lower.");
words = str(disclaimer_words + spin_words);
Top_Writing_words1 = tk.Label(text = title_words, master = WRITING, bg = "white", width = total_width-28, height = 2, font = ("arial",15,"bold"));
Top_Writing_words2 = tk.Label(text = words, master = WRITING, bg = "white", width = total_width, height = 3);
Top_Writing_words1.pack();
Top_Writing_words2.pack();
# Top_Writing.pack(padx = 1, pady = 1);

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
menu_options = [ME_text, ME_efmL_text, BEL_Wu_text, BEL_e2fm2L_text, BEL_e2bL_text, BEL_e2fm2L_UP_text, BEL_e2bL_UP_text];
menu_test_variable = tk.StringVar(INPUTS);
menu_test_variable.set("select option");
menu = tk.OptionMenu(INPUTS, menu_test_variable, *menu_options);

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


######################################################

want_label_1 = tk.Label(text = "What Output\n Do You Want?\n", fg = "black", width = column2_width, master = WANTS);	#, bg = "white"

want_label_2 = tk.Label(text = "Quantity:", fg = "black", width = column2_width, master = WANTS);			#, bg = "white"
want_menu_options = [ME_text, ME_efmL_text, BEL_Wu_text, BEL_e2fm2L_text, BEL_e2bL_text, BEL_e2fm2L_UP_text, BEL_e2bL_UP_text];
want_menu_variable = tk.StringVar(WANTS);
want_menu_variable.set("select option");
want_menu = tk.OptionMenu(WANTS, want_menu_variable, *want_menu_options);

want_label_1.pack();
want_label_2.pack();
want_menu.pack();




######################################################

The_Button = tk.Button(text = "GO", font = ("default",20,"bold"), width = column3_width, height = 3, command = Director, master = BUTTON, bg = "green3");
The_Button.pack();


######################################################

# Output_box = tk.Label(bg = "white", master = OUTPUTS, borderwidth = 1, width = 20, height = 10);
Output_data_label1 = tk.Label(text = "Output", fg = "black", width = column4_width, master = OUTPUTS);			#, bg = "white"
Output_data_1 = tk.Label(text = "--", fg = "black", bg = "white", width = column4_width, master = OUTPUTS);
Output_data_label2 = tk.Label(text = "Units", fg = "black", width = column4_width, master = OUTPUTS);			#, bg = "white"
Output_data_2 = tk.Label(text = "--", fg = "black", bg = "white", width = column4_width, master = OUTPUTS);

Output_data_label1.pack();
Output_data_1.pack();
Output_data_label2.pack();
Output_data_2.pack();
# Output_box.pack(padx = 1, pady = 1);



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