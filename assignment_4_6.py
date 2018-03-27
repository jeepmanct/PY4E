def computepay(h,r):
	spay = float(40 * r)
	othrs = float(h - 40)
	otrate = r * 1.5
	otpay = otrate * othrs
	p = spay + otpay
	return float(p)
#
#
#
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
#
#
#
if h <= 40 :
    p = float(h*r)
    print(p)
elif h > 40 :
	p = computepay(h,r)
	print(p)
#
#
#
