print("hello")

s = "hello"
s = s.upper()
print(s)
print("printing s..."+ s)

myint = 10
myfloat = 1.0

mystr = "shiva"

print("str+num..use repr >>>"+ mystr + ' ' + repr(myint))
f = "hello"
m = f.replace("hello", "cva")
print(m)

n = mystr.find("shiva")
print(n)

if(mystr.find("shia") > -1):
	print("it has")
else:
	print("it hasn't")

#list of arrays
nums = [2,3,4,5]
nums.append(6)
print(nums)
print(nums[2])

#dictionary
dict = set([2,3,4,5,6])
print(dict)

print("length func()>>"+' '+repr(len(dict)))
print("***************************************")
count = 0
'''
while count < 10:
	print(count)
	count = count + 1
'''
for numof in range(5, 10):
	print(numof)
	count = count + 1
	
print("num of times exec:"+repr(count))





