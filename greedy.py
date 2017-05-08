def coinGreedy(money, cash_type, count):
    if count >= len(cash_type):
        return res
    dvmd = divmod(money, cash_type[count])
    res[cash_type[count]] = dvmd[0]
    money = dvmd[1]
    return coinGreedy(money, cash_type, count + 1)


money = int(input('액수입력 : '))
cash_type = [int(x) for x in input('화폐단위를 입력하세요 : ').split(' ')]
cash_type.sort(reverse=True)
res = {}
res = coinGreedy(money, cash_type, 0)
for key in res:
    print('{0}원 : {1}개'.format(key, res[key]))