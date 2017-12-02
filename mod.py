# modular arithmetic toolset
import math
import sys

def calculator(mod_value, a, b):
	# add
	print "-- Addition --"
	added = a + b
	added_mod = added

	if added >= mod_value:
		added_mod = get_mod_value(added, mod_value)

	print str(a) + " + " + str(b) + " = " + str(int(added_mod))

	# multiplied
	print "-- Multiplied --"
	multiplied = a * b
	multiplied_mod = multiplied

	if multiplied >= mod_value:
		multiplied_mod = get_mod_value(multiplied, mod_value)

	print str(a) + " * " + str(b) + " = " + str(int(multiplied_mod))

def get_mod_value(total, mod_val):
	added_mod = total - (math.floor(total / mod_val) * mod_val)
	return added_mod

print "This tool will compute the mod value of your specified input."
print "Current operators: + *"

mod_value = int(raw_input("Enter your mod value: "))
value_a = int(raw_input("Enter value A: "))
value_b = int(raw_input("Enter value B: "))

calculator(mod_value, value_a, value_b)