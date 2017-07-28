def find_length(text_file):
	file_ptr = open(text_file)
	file_ptr = file_ptr.read()
	original_length = len(file_ptr)
	dict_states = { 0 : {'h' : 1 , 'f' : 4} , 1 : {'t' : 2 } , 2 : { 't' : 3 } , 4 : { 't' : 3} , 3 : { 'p' : 5 } , 5 : { 's' : 6 , ':' : 7 } , 6 : { ':' : 7} , 7 : { '/' : 8 } , 8 : { '/' : 9} , 9 : {' ' : 10 , '\n' : 10}  }
	index = 0
	starting_index = index 
	state = 0
	weblinks={}
	while( index < original_length):
		if(state != 9 and state != 10):
			try:
				state = dict_states[state][file_ptr[index]]
			except:
				state = 0
				starting_index = index
		elif(state == 9  and state != 10):
			try:
				m = dict_states[state][file_ptr[index]]
				state = 10
				weblinks[starting_index] =  index
				starting_index = index 
				state = 0
			except:
				state = 9	
		else:
			pass	
		index+=1	
	new_index = 0
	new_file_ptr = ''
	while (new_index < original_length):
		try :
				final_index = weblinks[new_index]
				new_file_ptr+= file_ptr[new_index]
				new_index = final_index - 1
				if file_ptr[new_index] == '\n':
					new_file_ptrn += '\n'
		except:
			new_file_ptr += file_ptr[new_index]
		new_index+=1
	new_ptr=open("modified-"+text_file,'w')
	new_ptr.write(new_file_ptr)
	
	#FOR MULTIPLE BLANK SPACES!!
	blank_states = {0 : { " " : 1 }  , 1 : { " " : 2 } , 2 : { " " : 2 } }
	b_index = 0
	b_state = 0
	b_starting_index = 0
	b_spaces = {}
	mod_len = len(new_file_ptr)
	while (b_index < mod_len):
		if(b_state == 1 or b_state == 0):
			try:
				b_state  = blank_states[b_state][new_file_ptr[b_index]]
			except:
				b_state = 0
				b_starting_index = b_index + 1
		elif(b_state == 2):
			try:
				m = blank_states[b_state][new_file_ptr[b_index]]
			except:
				b_spaces[b_starting_index] = b_index
				b_state = 0
		else:
			pass						
		b_index += 1
	n_index = 0
	n_f_ptr = ''
	while(n_index < mod_len):
		try:
			f_index = b_spaces[n_index]
			n_f_ptr+= new_file_ptr[n_index]
			n_index = f_index - 1
		except:
			n_f_ptr+=new_file_ptr[n_index]
		n_index+=1	
		n_n_ptr = open("modified-"+text_file,'w')
		n_n_ptr.write(n_f_ptr)
	print("original len:",original_length)
	print("modified len:",mod_len)								
	
print("Enter the file name:")
file_a = input()
find_length(file_a)
