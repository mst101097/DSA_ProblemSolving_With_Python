def replaceChar(str,a,b):
	if len(str)==0:
		return str

	smalloutput = replaceChar(str[1:],a,b)

	if str[0]==a:
		return b+smalloutput
	else:
		return str[0]+smalloutput

str = "dacdxca"
a = 'c'
b = 'x'
print(replaceChar(str,a,b))
