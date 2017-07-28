def Prefix_fun(p):
	m=len(p);
	prefix_Arr=[-1]*(m)
	k=-1;# for 0 char match
	for i in range(1,m):
		while(k>-1 and (p[k+1] != p[i])) :
			k=prefix_Arr[k];
		if(p[k+1]==p[i]):
			k=k+1;
		prefix_Arr[i]=k;
	return prefix_Arr

def KMP_Matcher(t,p):
	n=len(t);
	m=len(p)
	occurence=[];
	prefix_Arr=Prefix_fun(p);
	k=-1;
	for i in range(0,n):
		while(k>-1 and (t[i]!=p[k+1])):
			k=prefix_Arr[k];	
		if(p[k+1]==t[i]) :
			k=k+1;
		if(k+1==m):
			occurence.append(i-k);
			k=prefix_Arr[k];
	return occurence;

t = input("Enter the text:")
p = input("Enter the pattern:")
print(KMP_Matcher(t,p))	