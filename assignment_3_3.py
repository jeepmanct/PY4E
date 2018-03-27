score = input("Enter Score: ")
try  :
	sc = float(score)
except :
    print("Enter a numeric between 0.0 and 1.0")
    quit()
#
if sc < 0.0 or sc > 1.0 :
    print("Score needs to be between 0.0 and 1.0")
    quit()
elif sc >= 0.9 :
    print("A")
elif sc >= 0.8 and sc < 0.9 :
	print("B")
elif sc >= 0.7 and sc < 0.8 :
	print("C")
elif sc >= 0.6 and sc < 0.7 :
    print("D")
elif sc < 0.6 :
    print("F")
