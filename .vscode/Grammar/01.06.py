# from random import *
# cong = range(1, 21)
# cong = list(cong)
# # print(type(cong))
# shuffle(cong)
# cong_1 = sample(cong,4)
# print("\n-- 당첨자 발표 --\n" + "치킨 당첨자: {0}".format(cong_1[0]))
# print("커피 당첨자: {0}".format(cong_1[1:]))
# print("-- 축하합니다 --")

# from random import *
# customer_no = 0
# for i in range(1, 51):
#     customer_time  = int(randrange(5, 51))
#     if 5 <= customer_time <= 15:
#         print("[O] " + "{0}번째 손님 (소요시간 : {1}분".format(i, customer_time))
#         customer_no += 1
#     elif customer_time > 15:
#         print("[ ] " + "{0}번째 손님 (소요시간 : {1}분".format(i, customer_time))    
# print("총 승객 수는 {0}".format(customer_no))

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance + money))
#     return balance + money

# balance =0
# balance = deposit(balance, 1000)
# print(balance)

# def std_weight (height, gender):
#     if gender=="남자" or gender=="남성":
#         weight = (height/100) * (height/100) * 22
#         print("키 {0} cm 남자의 표준 체중은 {1} kg 입니다.".format(height, round(weight,2)))
#         return height, round(weight, 2)
#     elif gender=="여자" or gender=="여성":
#         weight = (height/100) * (height/100) * 21
#         print("키 {0} cm 여자의 표준 체중은 {1} kg 입니다.".format(height, round(weight,2)))
#         return height, round(weight,2)

# std_weight(175, "남자")