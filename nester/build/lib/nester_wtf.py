def print_lol(the_list):
	for each_item in the_list:
		if isinstance (each_item, list):
			print_lol (each_item)
		else:
			print (each_item)

def print_lol4(the_list, indent=False, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol4(each_item, indent, level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='')
            print(each_item)