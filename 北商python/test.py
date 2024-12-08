# with open ('北商python/ntub.csv','r',encoding="UTF-8") as infile:
#     data = infile.readlines()
#     all = ["男","女"]
#     male =[] ; female = []
#     for i in data:
#         gender, _, _, _, _, _, math, *_ = i.strip().split(",")
#         if gender == "男":male.append(int(math))
#         else:female.append(int(math))
#     print("男生共有%d人，數學平均=%.1f分" %(len(male), sum(male)/len(male)))
#     print("女生共有%d人，數學平均=%.1f分" %(len(female), sum(female)/len(female)))

with open('北商python/ntub.csv','r',encoding="UTF-8") as infile:
    data = infile.readlines()
    answer = [] ; ans = []
    project = {"作文":[0], "國文":[0], "英文":[0], "數學":[0], "社會":[0], "自然":[0]}
    for i in data:
        *_, word, chinese, english, math, social, scince  = i.strip().split(',')
        answer.append([int(word), int(chinese), int(english), int(math), int(social), int(scince)])
    total = [0]*6
    for i in range(len(answer)):
        for j in range(6):
            total[j] += answer[i][j]
    for i in range(6):
        ans.append(total[i]/len(data))
    print(ans)