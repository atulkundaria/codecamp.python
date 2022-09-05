hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h <= 40:
     pay = h * r
if h > 40:
     o = h - 40
     p1 = 40 * r
     p2 = o * r * 1.5
     pay = p1 + p2
print(pay)
