#ASSIGNMENT STATEMENT:
'''
Test data:
	AESOPTABLES.txt

Need to create interfaces:

1) Find length of the text:
	function declaration : 
		Find_length_of_text(txtfile) ->
			* normalize multiple blank chars to single char
			* Remove webiste URL's that have infected the text file using FSA based Regex matcher.
		motto of the function ->
			To trim the data set.	
		approach:
			

2) Find pattern:
	function declaration:
		Find_pattern(pattern , InTextRange , algo) ->
			pattern -> pattern to be searched 
			algo -> function pointer to be passed in which the pattern finding algo is defined.
			IntextRange-> can be indices OR two patterns(ultimately finding indices!! using the same function pointer!!!)
		approach:	

3) Build cross index

	
	

4) Find Maximal palindrome

	//TODO!!

5) Print stats
	//Weird stuff!!


'''
import re
class Strings:
	def __init__(self):
		self.stats = {}
		self.newfile =''
	def Find_length_of_text(self , txtfile):
		file_ptr = open(txtfile).read()
		original = len(file_ptr)
		weblink=[]
		#new_file_interm = re.sub('\n+',' ',new_file_interm)	
		new_ptr=open("modified-"+txtfile,'w')
		new_ptr.write(new_file_interm)
		modified = len(new_file_interm)
		print("The length of the text file before modifying is:" , original)
		print("The length of the text file after modifying is:" , modified)
		self.stats["Infected_Weblinks"] = weblink
		self.stats["len_original"] = original
		self.stats["len_modified"] = modified
		self.newfile = new_file_interm
	def Rabin_karp(self,pattern , index_begin , index_final):
		m = len(pattern)
		n = index_final  - index_begin
		h = 1  
		d = 256
		q = 97
		p = 0
		t = 0
		no_of_occurences = 0
		text = file_one[index_begin:index_final]
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

	def Find_pattern(self,pattern,begin,end,algo):
		index_start = 0 
		index_end = 0 
		print(self.newfile)	
		if(not isinstance(begin,int) and not isinstance(end,int)):
			for i in [m.start(0) for m in re.finditer(begin,self.newfile)]:
				index_start = i
			for i in [m.end(0) for m in re.finditer(end,self.newfile)]:
				index_end = i
		else:
			index_start = begin
			index_end  = end
		found=algo(pattern , index_start , index_end)
		if(found == 0):
			print("No Match")
		else:
			print("No of patterns in the given substring is : " ,found)
			



if __name__ == '__main__':
	s = Strings()
	text_file=input("Enter the text file:")    	#Testing!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	s.Find_length_of_text(text_file)    		#	Testing!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	#s.Find_pattern("hey","hello","there",s.Rabin_karp)
	s.Find_pattern("gh","cd","jk",s.Rabin_karp)	





















