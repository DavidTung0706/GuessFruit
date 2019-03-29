fruit_list = ["西瓜","木瓜","蘋果","水蜜桃","香蕉"]
while True:
    usr_fruit = input("請輸入喜歡的水果(Enter 結束):")
    if(usr_fruit==""):
        break
    count = fruit_list.count(usr_fruit)
    if(count>0):
        item = fruit_list.index(usr_fruit)
        print(usr_fruit + " 在水果清單中的第 " + str(item+1) + " 項")
    else:
        print(usr_fruit + " 不在水果清單當中")
        fruit_list.append(usr_fruit)
        print("幫您把 "+ str(usr_fruit) +" 加入水果清單裡\n"  + str(fruit_list))