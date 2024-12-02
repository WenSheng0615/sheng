with open ('北商python/ntub.csv','r',encoding="UTF-8") as infile:
    data = infile.readlines()
    for i in data:
        print(i.strip().split(","))