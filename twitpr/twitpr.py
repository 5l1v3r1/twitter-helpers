import twitter
import random

conskey = "---" #API consumer key
conssec = "---" #API consumer secret

with open("auth.txt") as f:
  lines = f.readlines()
  for line in lines:
    acctokkey = line.split(",")[0]
    acctoksec = line.split(",")[1].strip("\n")
    print(acctoksec)
    api = twitter.Api(consumer_key=conskey,consumer_secret=conssec,access_token_key=acctokkey,access_token_secret=acctoksec)
    trendler = api.GetTrendsWoeid("2344116")
    for trend in trendler:
      print()
      print(trend.name)
      sonuclar = api.GetSearch(trend.name)
      rastgele = random.randint(1,5)
      if not sonuclar[rastgele].user_mentions:
        print(rastgele)
        print(sonuclar[rastgele].text)
        try:
          status = api.PostUpdate(sonuclar[rastgele].text)
          print(status)
        except:
          pass
      
