import json

f = open('data7', encoding="utf-8")
profit_dict = {}
damages_dict = {}
average_dict = {}
avg_profit = 0
profit_firms = 0
for i in f:
    a = i.split()
    profit = int(a[2]) - int(a[3])
    if profit > 0:
        profit_firms += 1
        avg_profit += profit
        profit_dict[a[0]] = profit
    else:
        damages_dict[a[0]] = profit
    average_dict['average_profit']= avg_profit / profit_firms
list = [profit_dict, average_dict, damages_dict]
print(list)
f.close()

with open('some_file.json', 'w') as opened_file:
    json.dump(list,opened_file)
