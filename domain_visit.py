from collections import defaultdict
from copy import deepcopy

def subdomain_visite(visits):
    
    mymap = defaultdict(int)
    for v in visits:
        c, domain = v.split(' ')
        i = -1
        while i < len(domain):
            if i == -1 or domain[i] == '.':
                mymap[domain[i+1:]] += int(c)
            i += 1
        
    res = []
    for k, v in mymap.items():
        res.append(' '.join([str(v), k]))
        
    return res


visits = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print (subdomain_visite(visits))


def longest_continuous_common_history(visits, u1, u2):
    v1 = visits[u1]
    v2 = visits[u2]
    
    l1 = len(v1)
    l2 = len(v2)
    
    dp = [[0 for i in range(l2+1)] for j in range(l1+1)]
    res = []
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if v1[i-1] == v2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > len(res):
                    res = v1[i-dp[i][j]:i]
    
    return res

visits = [["3234.html", "xys.html", "7hsaa.html"], ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"],
 ["3234.html", "xys.html", "csc.gbdt", "takes.cpp"], ["xys.html", "csc.gbdt", "takes.cpp", "7hsaa.html"]]

print(longest_continuous_common_history(visits, 0, 1))
print(longest_continuous_common_history(visits, 0, 2))
print(longest_continuous_common_history(visits, 1, 2))
print(longest_continuous_common_history(visits, 2, 3))




def parse_ads_data(completed_purchase_user_ids, ad_clicks, all_user_ips):
    
    user_ips = dict()
    for each in all_user_ips:
        user_id, ip = each.split(',')
        user_ips[ip] = user_id
        
    
    ad_cl = defaultdict(list)
    for ad in ad_clicks:
        ip, _, text = ad.split(',')
        ad_cl[text].append(ip)
    
    sta = defaultdict(list)    
    for text, ips in ad_cl.items():
        sta[text].append(len(set(ips)))
        cnt = 0
        for ip in ips:
            if ip in user_ips.keys():
                user_id = user_ips[ip]
                if user_id in completed_purchase_user_ids:
                    cnt += 1
        sta[text].append(cnt)
    
    res = []
    for k, v in sta.items():
        s = ' of '.join([str(v[1]), str(v[0])])
        s += ' '
        s += k
        res.append(s)
    return res




completed_purchase_user_ids = ["3123122444","234111110", "8321125440", "99911063"]
ad_clicks = [
  #"IP_Address,Time,Ad_Text",
  "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
  "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
  "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
  "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
  "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
  "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]
all_user_ips = [
  #"User_ID,IP_Address",
   "2339985511,122.121.0.155",
   "234111110,122.121.0.1",
   "3123122444,92.130.6.145",
   "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
   "8321125440,82.1.106.8",
   "99911063,92.130.6.144"
]

print(parse_ads_data(completed_purchase_user_ids, ad_clicks, all_user_ips))