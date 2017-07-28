import os
import math
import re
import time
def print_choices():
	print("1.Find the length of the text file (Removing of url's and multiple blank spaces)")
	print("2.Search for a pattern in a text")
	print("3.Build Cross index for the entire text file")
	print("4.Get the maximal palindrome")
	print("5.Print stats.")
	print("6.Exit")
class String:
	def __init__(self):
		self.stats = {}
		self.text_file = ''
		self.file = open("Random_AESOPTALES.txt").read()

#1)FINDING LENGTH AND REMOVING OF WEBLINKS AND MULTIPLE BLANK SPACES
########################################################################################################################################		
	def find_length(self,text_file):
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
		new_file_ptr = re.sub(" +"," ",new_file_ptr) ## only for removing blank spaces!	
		new_ptr=open("modified-"+text_file,'w')
		new_ptr.write(new_file_ptr)
		self.stats["Infected_weblinks"] = weblinks
		'''
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
		self.newfile = n_n_ptr
		'''	
		mod_len = len(new_file_ptr)
		self.stats["Modified length of the text"] = mod_len
		self.stats["Original length of the text"] = original_length

#2)PATTERN MATCHING WITH RABIN KARP, KMP , SUFFIX ARRAYS		
#####################################################################################################################################		
	def Rabin_karp(self,pattern , index_begin , index_final):
			start = time.time()
			m = len(pattern)
			n = index_final  - index_begin
			h = 1  
			d = 256
			q = 97
			p = 0
			t = 0
			no_of_occurences = 0
			text = self.file[index_begin:index_final]
			for i in range(m-1):
				h = (h * d)%q	
			for i in range(m):
				t = (d * t  + ord(text[i]))%q
				p = (d * p  + ord(pattern[i]))%q
			end  = time.time()
			self.stats["Pre Processing time for Rabin-karp"] = str(round((end - start)*1000 , 6 )) + " milliseconds"
			start = time.time()	
			for i in range(n - m + 1):
				if p == t:
					for j in range(m):
						if(pattern[j] != text[j + i ]):
							break		
					if j == m - 1:
						no_of_occurences+=1
				if( i < n - m):
					t = (d * (t - ord(text[i]) * h ) + ord(text[i+ m]))%q
					if t<0:
						t = t + q
			end = time.time()
			self.stats["Rabin-karp execution time"]	= str(round((end - start)*1000 , 6 )) + " milliseconds"		
			return no_of_occurences

	def compute_prefix_function(self,pattern):
		p_len = len(pattern)
		prefix_array = [0] * (p_len)
		k = 0
		for q in range(1 , p_len):
			while(k > 0 and pattern[k] != pattern[q]):
				k = prefix_array[k - 1]
			if(pattern[k] == pattern[q]):
				k = k + 1
			prefix_array[q] = k
		return prefix_array

	def KnuthMorrisPratt(self,pattern,index_begin,index_final):
			number_of_occurences = 0
			text_length = index_final - index_begin
			pattern_length = len(pattern)
			start = time.time()
			prefix_array = self.compute_prefix_function(pattern)
			end  = time.time()
			self.stats["Pre processing time for KMP"] = str(round((end - start)*1000 , 6 )) + " milliseconds"
			start = time.time()
			q = 0
			text = self.file[index_begin:index_final]
			text = " " + text
			for i in range(text_length):
				while(q>0 and pattern[q] != text[i]):
					q = prefix_array[q - 1]
				if(pattern[q] == text[i]):
					q = q + 1
				if q == pattern_length:
					number_of_occurences+=1
					q = prefix_array[q - 1]
			end = time.time()
			self.stats["KMP Pattern searching time"] = str(round((end - start)*1000 , 6 )) + " milliseconds"		
			return number_of_occurences

	def build_suffix_array(self,text):
		text_length = len(text)
		suffixes = []
		for i in range(text_length):
			suffixes.append([])
			suffixes[i].append(i)
			suffixes[i].append(ord(text[i]) - ord('a'))
			if i + 1 < text_length:
				suffixes[i].append(ord(text[i+1]) - ord('a'))
			else:
				suffixes[i].append(-1)
		suffixes = sorted(suffixes , key= lambda x : (x[1],x[2]))		
		ind = []
		for i in range(text_length):
			ind.append(0)
		k = 4
		while(k < 2 * text_length):
			rank = 0
			p_rank = suffixes[0][1]
			suffixes[0][1] = rank
			ind[suffixes[0][0]] = 0
			for i in range(1,text_length):
				if(suffixes[i][1] == p_rank and suffixes[i][2] == suffixes[i-1][2]):
					p_rank = suffixes[i][1]
					suffixes[i][1] = rank
				else:
					p_rank = suffixes[i][1]
					rank += 1
					suffixes[i][1] = rank
				ind[suffixes[i][0]] = i
			for i in range(text_length):
				n_i = int(suffixes[i][0] + k/2);
				if(n_i < text_length):
					suffixes[i][2]=suffixes[ind[n_i]][1]
				else:
					suffixes[i][2] = -1	 		
			suffixes = sorted(suffixes , key= lambda x : (x[1],x[2]))		
			k = k * 2
		suffix_array = []		
		for i in range(text_length):
			suffix_array.append(suffixes[i][0])
		return suffix_array

	def lcp(self,string_one , string_two):
		n = len(string_two)
		number = 0
		i = 0 
		while(  i < n and string_one[i] == string_two[i]):
			i+=1	
		return i

	def suffix_pattern(self,pattern ,t):
		count = 0
		start = time.time() 
		s_a=self.build_suffix_array(t)
		end  = time.time()
		self.stats["Pre Processing Suffix Array time"] = str(round((end - start)*1000 , 6 )) + " milliseconds"
		#print(s_a)
		start = time.time()
		L = 0 #indicates the starting index of the suffix array..
		R = len(s_a) - 1 # indicates the last index of the suffix array..
		L1 = L
		R1 = R
		lower_bound = 0 
		p_len = len(pattern)
		#print(p_len)
		if( pattern < t[s_a[L]: s_a[L] + p_len]):
			lower_bound = 0
		elif( pattern > t[s_a[R]:s_a[R] + p_len ]):
			lower_bound = R + 1
		else:
			while(R - L >= 0):
				M = math.ceil((R + L) / 2)
				M = int(M)
				#print(M)
				if(pattern <= t[s_a[M] : s_a[M]+p_len]):
					R = M - 1
				else:
					L = M + 1
			lower_bound = R + 1
		done = True
		indices = []
		while(lower_bound < R1 + 1 and done):
			if(self.lcp(pattern , t[s_a[lower_bound] : s_a[lower_bound] + p_len ]) == p_len):
				indices.append(t[s_a[lower_bound] : s_a[lower_bound] + p_len ])
				indices.append(lower_bound)
				lower_bound += 1
				count += 1
			else:
				done = False
		end = time.time()
		self.stats["Suffix Array Pattern searching time"] = str(round((end - start)*1000 , 6 )) + " milliseconds"		
		return count

	def Find_pattern(self,pattern,InTextRange,algo):
			begin = InTextRange[0]
			end = InTextRange[1]
			index_start = 0 
			index_end = 0		
			if(not isinstance(begin,int) and not isinstance(end,int)):
				for i in [m.start(0) for m in re.finditer(begin,file)]:
					index_start = i
				for i in [m.end(0) for m in re.finditer(end,file)]:
					index_end = i
			else:
				index_start = begin
				index_end  = end + 1
			if(index_end - index_start <= 1 ):
				print("Not Possible")	
			else:
				if algo != self.suffix_pattern :		
					found=algo(pattern , index_start , index_end)
				else:
					text_f = self.file[index_start:index_end]
					found = algo(pattern,text_f)	
				if(found == 0):
					print("No Match")
				else:
					print("No of patterns in the given substring is : " ,found)
#3)BUILD CROSS INDEX USING DIFFERENT STRING PATTERN MATCHING ALGO				
############################################################################################################################################				
	def KMP(self,text,pattern):
		number_of_occurences = 0
		text_length = len(text)
		pattern_length = len(pattern)
		prefix_array=[]
		for i in range(pattern_length):
			prefix_array.append(0)
		prefix_array[0] = 0
		k = 0
		q = 1
		while( q < pattern_length):
			while ( k > 0 and pattern[k] != pattern[q]):
				k = prefix_array[k]
			if(pattern[k] == pattern[q]):
				k+=1
			prefix_array[q] = k
			q+=1
		q = 0
		i = 0 
		while( i < text_length):
			while(q > 0 and pattern[q] != text[i]):
				q = prefix_array[q]
			if(pattern[q] == text[i]):
				q += 1
			if q == pattern_length:
				number_of_occurences+=1
				#print("Occurs @",i - pattern_length + 1)
				q = prefix_array[q-1]		
			i+=1
		return number_of_occurences

	def R_k(self,text,pattern):
		m = len(pattern)
		n = len(text)
		h = 1  
		d = 256
		q = 97
		p = 0
		t = 0
		no_of_occurences = 0
		#text = file_one[index_begin:index_final]
		for i in range(m-1):
			h = (h * d)%q
		for i in range(m):
			t = (d * t  + ord(text[i]))%q
			p = (d * p  + ord(pattern[i]))%q	
		for i in range(n - m + 1):
			if p == t:
				for j in range(m):
					if(pattern[j] != text[j + i ]):
						break		
				if j == m - 1:
					no_of_occurences+=1
			if( i < n - m):
				t = (d * (t - ord(text[i]) * h ) + ord(text[i+ m]))%q
				if t<0:
					t = t + q
		return no_of_occurences
	def suffix_pattern_new(self,t,pattern):
		count = 0 
		s_a=self.build_suffix_array(t)
		#print(s_a)
		L = 0 #indicates the starting index of the suffix array..
		R = len(s_a) - 1 # indicates the last index of the suffix array..
		L1 = L
		R1 = R
		lower_bound = 0 
		p_len = len(pattern)
		#print(p_len)
		if( pattern < t[s_a[L]: s_a[L] + p_len]):
			lower_bound = 0
		elif( pattern > t[s_a[R]:s_a[R] + p_len ]):
			lower_bound = R + 1
		else:
			while(R - L >= 0):
				M = math.ceil((R + L) / 2)
				M = int(M)
				#print(M)
				if(pattern <= t[s_a[M] : s_a[M]+p_len]):
					R = M - 1
				else:
					L = M + 1
			lower_bound = R + 1
		done = True
		indices = []
		while(lower_bound < R1 + 1 and done):
			if(self.lcp(pattern , t[s_a[lower_bound] : s_a[lower_bound] + p_len ]) == p_len):
				indices.append(t[s_a[lower_bound] : s_a[lower_bound] + p_len ])
				indices.append(lower_bound)
				lower_bound += 1
				count += 1
			else:
				done = False		
		return count		

	def cross_index(self,txt_file , algo):
		file_ptr = open(txt_file).read()
		file_ptr = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),#]|(?:%[0-9a-fA-F][0-9a-fA-F]))+' , " " , file_ptr)
		file_ptr = re.sub('ftp[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),#]|(?:%[0-9a-fA-F][0-9a-fA-F]))+' , " ", file_ptr)
		file_ptr = file_ptr.replace('"' , " ")
		file_ptr = file_ptr.replace("' " , " ")
		file_ptr = file_ptr.replace("." , " ")
		file_ptr = file_ptr.replace("," , " ")
		file_ptr = file_ptr.replace("!" , " ")
		file_ptr = file_ptr.replace(" '" , " ")
		file_ptr = file_ptr.replace(":" , " ")
		file_ptr = file_ptr.replace(";" , " ")
		file_ptr = file_ptr.replace("?" , " ")
		file_ptr = file_ptr.replace("(" , "")
		file_ptr = file_ptr.replace(")" , "")
		#print( list(i.start(0)) for i in re.finditer("\n\n\n\n" , file_ptr))
		#file_ptr = file_ptr.replace('\n\n\n\n' , '\n\n\n')
		file_ptr = re.sub(" +\n" , "\n" , file_ptr)
		file_ptr = re.sub("\n\n\n+" , "\n\n\n" , file_ptr)
		file_ptr = re.sub(" +" , " " , file_ptr)
		#k = open("some_text.txt",'w')
		#k.write(file_ptr.strip())
		file_ptr = file_ptr.strip()
		story = file_ptr.split("\n\n\n")
		words = {}
		story_name = "TALES"
		#print(len(story[0]))
		for j in story[0].split():
			try:
				count = words[j][story_name]			
			except:
				no_of_occurence = algo(story[0],j)
				words[j]= {}
				words[j][story_name] = no_of_occurence
		#print(words)
		story = story[1:]
		story_name =""
		prev_story = ""
		for i in story:
			ind_story = i.split("\n\n" , 1)
			if(len(ind_story) == 1):
				for k in ind_story[0].split():
					try:
						count = words[k][story_name]
					except:
						ind_story[0] += prev_story
						ind_story[0] = re.sub("\n" , " " , ind_story[0])
						no_of_occurence = algo(' ' + ind_story[0] + ' ' , ' ' +k+' ')
						if k not in words:
							words[k] = {}
						words[k][story_name] = no_of_occurence			 	
			elif(len(ind_story[1].split("\n\n")) != 3):
				story_name = ind_story[0]
				for j in ind_story[1].split():
					try:
						count = words[j][story_name]
					except:
						ind_story[1] = re.sub("\n"," " , ind_story[1])
						no_of_occurence = algo(' '+ind_story[1] + ' ', " "+j+" ")
						if j not in words:
							words[j] = {}
						words[j][story_name] = no_of_occurence
				prev_story = ind_story[1]			
			else:			
				story_name_one = ind_story[0]
				new_story=ind_story[1].split("\n\n")
				for j in new_story[1].split():
					try:
						count = words[j][story_name_one]
					except:
						new_story[0] = re.sub("\n" , " " , new_story[0])
						no_of_occurence = algo(" "+new_story[0] + " " , " "+j + " ")
						if j not in words:
							words[j] = {}
						words[j][story_name_one] = no_of_occurence
				story_name_two = new_story[1]
				for j in new_story[2].split():
					try:
						count = words[j][story_name_two]
					except:
						new_story[2] = re.sub("\n" , " " , new_story[2])
						no_of_occurence = algo(' '+new_story[2]+' ' , ' ' + j + ' ')
						if j not in words:
							words[j] = {}	
						words[j][story_name_two] = no_of_occurence		
		ind_words=sorted(words.keys())
		n_c_i = open("INDEX_T_testing.txt",'w')
		for j in ind_words:
			n_c_i.write(j)
			n_c_i.write("              "+str(words[j]))
			n_c_i.write("\n")
#4)FINDING MAXIMAL PALINDROME			
#############################################################################################################################			
	def FindMaximalPalindromes(self,palindrome_size,IntextRange):
		begin = IntextRange[0]
		end = IntextRange[1]
		index_start = 0
		index_end = 0 
		if(not isinstance(begin,int) and not isinstance(end,int)):
			for i in [m.start(0) for m in re.finditer(begin,self.file)]:
				index_start = i
			for i in [m.end(0) for m in re.finditer(end,self.file)]:
				index_end = i
		else:
			index_start = begin
			index_end  = end + 1
		f = open("modified-Random_AESOPTALES.txt")
		f.seek(index_start)
		text = f.read(index_end  - index_start)
		#print(text[-30: -1])
		palindromes = []
		index = index_start
		for li in text.split('\n')[:-1]:
			t = index
			l_of_line = len(li) + 1
			for ind_word in li.strip().split():
				length = len(ind_word) + 1
				for i in range(palindrome_size,length):
					for j in range(0, i - palindrome_size + 1):
						p = ind_word[j:i]
						if p == p[::-1] :
							palindromes.append((t + j, t + i))
				t += length
			index += l_of_line
		#print(palindromes)			
		for i in palindromes:
			print(text[i[0]-begin:i[1]-begin]," ->   Index range  ->  (",i[0] , "," , i[1] ,") ")
#5)PRINT STATS			
########################################################################################################
	def print_stats(self):
		print("Printing stats uptil now:")
		for i in self.stats:
			if i == "Infected_weblinks":
				print("    Infected Weblinks are:")
				for j in self.stats[i]:
					print("        ",self.file[j:self.stats[i][j]].strip())
				print()	
			else:
				#print("????")
				print("    ",i , " : " , self.stats[i])
				print()								
#MAIN FUNCTION
########################################################################################################																	
if __name__  == "__main__":
	#DECLARE THE OBJECT!!!!
	s = String()
	print("-----------------String Operations-----------------")	
	print_choices()
	print("Enter any valid choice:")
	in_choice = int(input())
	while(in_choice != 6):
		if(in_choice == 1):
			text_file = input("Enter the text file:")
			start = time.time()
			s.find_length(text_file)
			end = time.time()
			s.stats["Time taken to remove Infected URL's and multiple blank spaces"] = str(round((end - start)*1000 , 6 )) + " milliseconds"
		elif(in_choice == 2):
			print("Which algorithm do you want to use?(any one choice):")
			print("""
				1)Rabin karp:
				2)Knuth-Morris-Pratt:
				3)Suffix array:
				""")
			algo_in = int(input("Enter the choice:"))
			if(algo_in == 1):
				print("Enter the range:")
				print("do you wish to enter:")
				print("1.Beginning Index and Ending index:")
				print("2.two story titles:")
				index_range = int(input("Enter the choice:"))
				if(index_range == 1):
					b_i = int(input("Enter the begining index:"))
					e_i = int(input("Enter the ending index:"))
					pat = input("Enter the pattern:")
					in_text_range = [b_i , e_i]
					start = time.time()
					s.Find_pattern(pat,in_text_range ,s.Rabin_karp)
					end = time.time()
					###########
				else:
					b_t = input("Enter the beginning story title:")
					e_t = input("Enter the ending story title:")
					pat = input("Enter the pattern:")
					in_text_range = [b_t , e_t]
					start = time.time()
					s.Find_pattern(pat , in_text_range , s.Rabin_karp)
					end  = time.time()
					#####################
			elif(algo_in == 2):
				print("Enter the range:")
				print("do you wish to enter:")
				print("1.Beginning Index and Ending index:")
				print("2.two story titles:")
				index_range = int(input())
				if(index_range == 1):
					b_i = int(input("Enter the begining index:"))
					e_i = int(input("Enter the Ending index:"))
					pat = input("Enter the pattern:")
					in_text_range = [b_i , e_i]
					s.Find_pattern(pat,in_text_range ,s.KnuthMorrisPratt)
				else:
					b_t = input("Enter the beginning story title:")
					e_t = input("Enter the ending story title:")
					pat = input("Enter the pattern:")
					in_text_range = [b_t , e_t]
					s.Find_pattern(pat , in_text_range , s.KnuthMorrisPratt)
			elif(algo_in == 3):
				print("Enter the range:")
				print("do you wish to enter:")
				print("1.Beginning Index and Ending index:")
				print("2.two story titles:")
				index_range = int(input())
				if(index_range == 1):
					b_i = int(input("Enter the begining index:"))
					e_i = int(input("Enter the Ending index:"))
					pat = input("Enter the pattern:")
					in_text_range = [b_i , e_i]
					s.Find_pattern(pat,in_text_range ,s.suffix_pattern)
				else:
					b_t = input("Enter the beginning story title:")
					e_t = input("Enter the ending story title:")
					pat = input("Enter the pattern:")
					in_text_range = [b_t , e_t]
					s.Find_pattern(pat , in_text_range , s.suffix_pattern)
			else:
				print("Cancelled due to wrong entry")		
		elif(in_choice == 3):
			print("Which algorithm is to be implemented in cross index?")
			print("1.Rabin karp:")
			print("2.KMP:")
			print("3.Suffix array:")
			print("Enter the choice:")
			c_i_in = int(input())
			t = input("Enter the text file:")
			if c_i_in == 1:
				start = time.time()
				s.cross_index(t , s.R_k)
				end = time.time()
				s.stats["Build cross index using Rabin-karp"] = str(round((end - start)*1000 , 6 )) + " milliseconds"
			elif c_i_in == 2:
				start = time.time()
				s.cross_index(t , s.KMP)
				end = time.time()
				s.stats["Build cross index using KMP"] = str(round((end - start)*1000 , 6 )) + " milliseconds"
			elif c_i_in == 3:
				start = time.time()
				s.cross_index(t , s.suffix_pattern_new)
				end = time.time()
				s.stats["Build cross index using suffix arrays"] = str(round((end - start)*1000 , 6 )) + " milliseconds" 	
			else:
				print("Cancelled...")
		elif(in_choice == 4):
			length = int(input("Enter the max length:"))
			print("Enter the choice:")
			print("1.Starting index and ending Index:")
			print("2.Two Story titles!:")
			c = int(input())
			if c==1:
				c_in_one = int(input("Enter the starting index:"))
				c_in_two = int(input("Enter the ending index:"))
				start = time.time()
				s.FindMaximalPalindromes(length , [c_in_one , c_in_two])
				end = time.time()
				s.stats["Time to find Maximal palindromes"] = str(round((end - start)*1000 , 6 )) + " milliseconds"
			elif c == 2:
				c_i_in = input("ENter the first story title:")
				c_in_two = input("Enter the second story title:")
				start = time.time()
				s.FindMaximalPalindromes(length , [c_i_in , c_in_two])
				end = time.time()
				s.stats["Time to find Maximal palindromes"] = str(round((end - start)*1000 , 6 )) + " milliseconds"	
			else:
				print("Cancelled due to wrong option entry")	
		elif(in_choice == 5):
			s.print_stats()
		else:
			print("Enter any proper choice!!")
		print_choices()		
		print("Enter any valid next choice..")
		in_choice = int(input())
