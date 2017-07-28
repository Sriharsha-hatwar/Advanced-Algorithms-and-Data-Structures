import math
def build_suffix_array(text):
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
def lcp(string_one , string_two):
	n = len(string_two)
	number = 0
	i = 0 
	while(  i < n and string_one[i] == string_two[i]):
		i+=1	
	return i	

def suffix_pattern(pattern ,t):
	count = 0 
	s_a=build_suffix_array(t)
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
	while(lower_bound < R1 + 1 and done):
		if(lcp(pattern , t[s_a[lower_bound] : s_a[lower_bound] + p_len ]) == p_len):
			lower_bound += 1
			count += 1
		else:
			done = False
	return count		
file_cntnts = open("modified-AESOPTALES.txt").read()
pattern = input("Enter the pattern :")
print("The number of occurences of the pattern is : " , suffix_pattern(pattern , file_cntnts))



	

			
			
