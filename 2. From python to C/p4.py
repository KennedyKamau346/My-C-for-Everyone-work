# prints max value in a number of values each input in a separate line
# type done to get the results
maxval = None
minval = None
while True:
    line = input()
    line = line.strip()
    if line == "done" : break
    ival = int(line)
    if (maxval is None or ival > maxval) :
        maxval = ival
    if (minval is None or ival < minval) :
        minval = ival

print("Maximum", maxval)
print("Minimum", minval)