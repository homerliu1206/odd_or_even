while True:
	number = input("請輸入一個數字：")
	number = int(number)
	if number % 2 == 0:
		print ('偶數')
	elif number == 'q' or number == 'Q':
		break
	else:
		print ('奇數')