# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.


sum=0
n=int(input("enter the number of item in list"))
list1=[] 
for i in range(1,n+1):
    item=int(input(f"enter the item at :{i} place"))
    print(i,item)
    list1.append(item)
print(list1)    


while True:
    
    print("you wants to continue ?")
    value=input("select(yes or no)") 
    if value=='yes':
        buy_day=int(input("enter the day on which you want to buy the item"))
        sell_day=int(input("enter the day on which you want to sell the item"))
        
        buy_price=list1[buy_day-1]
        print(f"buy price:{buy_price}")
        
        sell_price=list1[sell_day-1]
        print(f"sell price:{sell_price}")
        
        if 0<buy_day<sell_day and buy_day<sell_day<len(list1):
            profit=sell_price-buy_price
            print(profit)
            sum+=profit
            if sum>0:
                print(f"your profit{sum}")
            else:
                print(f"you have loss{sum}")  
        else:
            print(f"you sell the item before buying it")          
    
    elif value=='no':
        print(f"totalprofit is{sum}")
        break
    else:
        print("invalid input instead of yes or no")
    
    
        
        
        
      


