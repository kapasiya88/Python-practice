# You are given an integer array coins representing coins different denominations and an integer 
# amount representing a total amount of money.
# Return the fewest number row coins that you need to make up that amount if that amount of money 
# cannot be made by any combination of the coins, return -1.  
from itertools import combinations_with_replacement
coins=[1,2,3]
amount=4
# coins=[2, 5, 3, 6]
# amount=10
def cal_min_coins(coins,amount):
    for i in range (1,len(coins)+1):
        coins_comb=list(combinations_with_replacement(coins,i))
        # print(coins_comb)
        # print('**********')
        cal_cum=[j for j in coins_comb if sum(j)==amount]
        # print(cal_cum)
        if len(cal_cum) > 0 and len(cal_cum[0]) > 0:
            return cal_cum[0]
    return (-1)
    
few_coin=cal_min_coins(coins,amount)
print(few_coin)
