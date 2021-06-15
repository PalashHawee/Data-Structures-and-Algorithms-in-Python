#Write a function that takes in a non-empty
#string representing a valid Unix-Shell path and
#returns a shortened version of that path
#Time and Space Complexity is O(n)
def shortenPath(path):
    
    startWithSlash=path[0]=='/'
	tokens=filter(isImportant,path.split("/"))
	stack=[]
	if startWithSlash:
		stack.append("")
	for token in tokens:
		if token=="..":
			if len(stack)==0 or stack[-1]=="..":
				stack.append(token)
			elif stack[-1]!="":
				stack.pop()
		else:
			stack.append(token)
	if len(stack)==1 and stack[-1]=="":
		return "/"
	return "/".join(stack)
def isImportant(token):
	return len(token)>0 and token!="."