def for_loop (end, increment):
	i = 0
	numbers = []

	while i < end:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + increment
		print "Numbers now: ", numbers
		print "At the bottom, i is %d" % i


	print "The numbers: "

	for num in numbers:
		print num

print "What should I count to?"
end = int(raw_input("> "))
print "By what increment?"
step = int(raw_input("> "))
for_loop(end, step)
