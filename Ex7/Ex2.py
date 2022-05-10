import pandas as pd


def education_budget(year:int)->int:
    """
    The total education budget for a given year
    """
    df = pd.DataFrame(pd.read_csv("national-budget.csv"))
    res = -1*int(df[(df['שנה'] == year) & (df['שם רמה 2'] == 'חינוך') & (df['הוצאה נטו'] < 0)][['הוצאה נטו']].sum(axis=0))
    res += int(df[(df['שנה'] == year) & (df['שם רמה 2'] == 'חינוך') & (df['הוצאה נטו'] > 0)][['הוצאה נטו']].sum(axis=0))
    return res


def security_budget_ratio(year:int)->float:
    """
    The security budget in a given year, as a ratio of that year's total budget
    """
    df = pd.DataFrame(pd.read_csv("national-budget.csv"))
    security_budget = int(df[(df['שנה'] == year) & (df['שם רמה 2'] == 'בטחון') & (df['הוצאה נטו'] > 0)][['הוצאה נטו']].sum(axis=0))
    all_budget = -1*int(df[(df['שנה'] == year) & (df['הוצאה נטו'] < 0)][['הוצאה נטו']].sum(axis=0))
    all_budget += int(df[(df['שנה'] == year) & (df['הוצאה נטו'] > 0)][['הוצאה נטו']].sum(axis=0))
    res = float(security_budget/all_budget)*100
    return float(format(res, ".2f"))



def largest_budget_year(office:str)->int:
    """
    The budget year of a particular office that was the largest
    """
    first_year = 1997
    last_year = 2022
    max_year = first_year
    
    df = pd.DataFrame(pd.read_csv("national-budget.csv"))
    res = -1*int(df[(df['שנה'] == first_year) & (df['שם רמה 2'] == office) & (df['הוצאה נטו'] < 0)][['הוצאה נטו']].sum(axis=0))
    res += int(df[(df['שנה'] == first_year) & (df['שם רמה 2'] == office) & (df['הוצאה נטו'] > 0)][['הוצאה נטו']].sum(axis=0))
    max_bud = res
    first_year+=1
    last_year+=1
    for i in range(first_year, last_year):
        res=0
        res = -1*int(df[(df['שנה'] == i) & (df['שם רמה 2'] == office) & (df['הוצאה נטו'] < 0)][['הוצאה נטו']].sum(axis=0))
        res += int(df[(df['שנה'] == i) & (df['שם רמה 2'] == office) & (df['הוצאה נטו'] > 0)][['הוצאה נטו']].sum(axis=0))
        if(res>max_bud):
            max_bud=res
            max_year=i
    return max_year

def lowest_budget_year(office:str)->int:
    """"
    The budget year of a particular office that was the lowest
    """
    first_year = 1997
    last_year = 2022
    min_year = first_year
    
    df = pd.DataFrame(pd.read_csv("national-budget.csv"))
    res = -1*int(df[(df['שנה'] == first_year) & (df['שם רמה 2'] == office) & (df['הוצאה נטו'] < 0)][['הוצאה נטו']].sum(axis=0))
    res += int(df[(df['שנה'] == first_year) & (df['שם רמה 2'] == office) & (df['הוצאה נטו'] > 0)][['הוצאה נטו']].sum(axis=0))
    min_bud = res
    first_year+=1
    last_year+=1
    for i in range(first_year, last_year):
        res=0
        res = -1*int(df[(df['שנה'] == i) & (df['שם רמה 2'] == office) & (df['הוצאה נטו'] < 0)][['הוצאה נטו']].sum(axis=0))
        res += int(df[(df['שנה'] == i) & (df['שם רמה 2'] == office) & (df['הוצאה נטו'] > 0)][['הוצאה נטו']].sum(axis=0))
        if(res<min_bud):
            min_bud=res
            min_year=i
    return min_year

#-------------------------------------
#MAIN
#-------------------------------------

if __name__ == "__main__":
    """
    to run this main you neet to download national-budget.csv from this link:
    https://next.obudget.org/datapackages/budget/national/original/data/national-budget.csv
    (put him in the main folder.)
    """
    # Example education budget
    year = 1997
    print("The total education budget in",year,"is",education_budget(year=year),"₪")
    year = 2022
    print("But in this year is",education_budget(year=year),"₪")

    # Example security budget ratio
    year = 1997
    print("The security budget ratio in",year,"is",security_budget_ratio(year=year),"%")
    year = 2022
    print("But in this year is",security_budget_ratio(year=year),"%")
    
    # Example lowest budget year and largest budget year
    office = 'חינוך'
    print("The lowest budget year in",office,"is",lowest_budget_year(office=office))
    print("But the largest budget year is",largest_budget_year(office=office))

    pass