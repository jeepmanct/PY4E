hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)

#
if h <= 40 :
    pay = float(h*r)
    print("Pay:",pay)
elif h > 40 :
	spay = float(40 * r)
	othrs = float(h - 40)
	otrate = r * 1.5
	otpay = otrate * othrs
	pay = spay + otpay
	print("Pay:",pay)
