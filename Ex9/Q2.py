import gspread
account = gspread.service_account("credentials.json")
from demo_shapley import demo_shapley



#-------------------------------------
#MAIN
#-------------------------------------

if __name__ == "__main__":

    spreadsheet = account.open("LiadSheet") # open by sheet name
    sheet1 = spreadsheet.get_worksheet(0) #get the first sheet
    sheet1.clear() # clear the sheet
    # Open spreadsheet by key:
    # spreadsheet = account.open_by_key("a0493999e0f47535a3e4eeecd478e934184ab2f3") # same as above, but safer (unique)
    
    shap = demo_shapley()
    abc = {"": 0,"a": 100,"b": 150,"c": 250,"ab": 200,"ac": 250,"bc": 300,"abc": 370}
    print("Game:")
    print(abc)
    agents = ["a","b","c"]
    res = shap.values(abc, agents)
    
    sheet1.update("A1", "Shapley values")
    sheet1.update("B1", "Agent name")
    sheet1.update("C1", "Agent cost")
    k=2
    print("------------")
    print("shapley result:")
    print(res)
    for i,j in res.items():
        sheet1.update("B"+str(k), str(i))
        sheet1.update("C"+str(k), str(j))
        k+=1
