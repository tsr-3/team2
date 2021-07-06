
def second_warn(idm:str, accepted:list):
    return True if idm in accepted else False

if __name__ == '__main__':
    idmlist:list = ["2984661","7662116","6068508","9161342","1794178","6535499","6661178","1585646","1677090","5717551","1761995","9240810","4403061","7747700","10160168","2016545","3565809","3088534","4710122","10444238"]
    print(second_warn("5717551", idmlist))
    print(second_warn("2561011", idmlist))