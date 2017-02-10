
 
feed1 = """0|20
0|Tom|BUY|5000
1|Tom|BUY|150000
3|25"""
 
from collections import defaultdict

def solve_challenge(feed, k):
    current_price = None
    day_dict = defaultdict(list)
    feed = feed.split('\n')
    result = []

    for each_line in feed:

        current_feed = each_line.split('|')
        if len(current_feed) == 2:
            current_price = current_feed[1]
            current_day = current_feed[0]
            profit  = get_profit(day_dict, current_day, current_price)
            print profit
        else:
            day = current_feed[0]
            name = current_feed[1]
            _type = current_feed[2]
            no_of_shares = current_feed[3]
            day_dict[day].append((name, _type, no_of_shares,current_price))



def get_profit(day_dict, current_day, current_price):
    result = []
    for each_day in range(int(current_day)-2, int(current_day)):
        feed = day_dict[str(each_day)]
        person_map = {}
        for each_feed in feed:
            current_profit = int(each_feed[2]) * int(each_feed[3]) - int(current_price) * int(each_feed[2])
            if abs(current_profit) > 500000:
                result.append((each_day, each_feed[0]))

    return result

    

print solve_challenge(feed1,0)