import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    c = test.split()
    if len(c)!=3:
        continue
    a = int(c[0])
    b = int(c[1])
    n = int(c[2])
    line_out = ""
    for i in range(1,n+1):
        flag = 0
        if i%a == 0:
            line_out += "F"
            flag = 1
        if i%b == 0:
            line_out += "B"
            flag = 1
        if flag != 1:
            line_out = "%s%d"%(line_out,i)
        line_out += " "
    print line_out

test_cases.close()