
wrong = input()
right = input()

button = 0
wrong_h, wrong_m = map(int, wrong.split(':'))
right_h, right_m = map(int, right.split(':'))

#분 
diff_m = right_m - wrong_m
button += diff_m if diff_m >= 0 else diff_m+60

#시간
wrong_h = wrong_h if diff_m >=0 else wrong_h+1
diff_h = right_h - wrong_h
button += diff_h if diff_h >= 0 else diff_h+24

print(button)

