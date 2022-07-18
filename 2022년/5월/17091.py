h = ["","one","two","three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve","one"]
m = ["o' clock","one minute","two minutes","three minutes", "four minutes",
	"five minutes", "six minutes", "seven minutes", "eight minutes", "nine minutes",
	"ten minutes", "eleven minutes", "twelve minutes","thirteen minutes","fourteen minutes",
	"quarter","sixteen minutes" ,"seventeen minutes","eighteen minutes" ,"nineteen minutes",
	"twenty minutes","twenty one minutes", "twenty two minutes", "twenty three minutes", "twenty four minutes",
	"twenty five minutes", "twenty six minutes", "twenty seven minutes", "twenty eight minutes","twenty nine minutes"
	,"half" ]

x,y = int(input()),int(input())
if y == 0:
	print(h[x],m[y])
elif 1 <= y <= 30 :
	print(m[y]+" past "+h[x])
else:
	print(m[60-y] + " to "+h[x+1])