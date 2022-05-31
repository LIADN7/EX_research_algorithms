import gspread
account = gspread.service_account("credentials.json")
from demo_shapley import demo_shapley



#-------------------------------------
#MAIN
#-------------------------------------

if __name__ == "__main__":
    # spreadsheet = account.open_by_key("a0493999e0f47535a3e4eeecd478e934184ab2f3") # same as above, but safer (unique)

    spreadsheet = account.open("LiadSheet") # open by sheet name
    sheet1 = spreadsheet.get_worksheet(0) # get Sheet1 with the values from the user
    sheet2 = spreadsheet.get_worksheet(1) # set in Sheet2 result
    sheet2.clear() # clear the sheet

    
    shap = demo_shapley()

    arr = sheet1.get_all_values()
    abc = {"": 0}
    agents = []
    cont=0
    # build the game from Sheet1
    for i,j in zip(arr[0],arr[1]):
        if cont>1:
            abc[i]=float(j)
        cont+=1
    cont=0
    for i in arr[2]:
        if (cont>0) and (not i == ""):
            agents.append(i)
        cont+=1
        


    print("Game:")
    print(abc)
    res = shap.values(abc, agents)
    sheet2.update("A1", "Shapley values")
    sheet2.update("B1", "Agent name")
    sheet2.update("C1", "Agent cost")
    k=2
    print("------------")
    print("shapley result:")
    print(res)
    for i,j in res.items():
        sheet2.update("B"+str(k), str(i))
        sheet2.update("C"+str(k), str(j))
        k+=1
