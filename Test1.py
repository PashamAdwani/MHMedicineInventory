#==========================
import pandas as pd
#==========================

#==========================
pathInv=r'E:\pasham\MedicineHPF\Items\Inventory.csv'
pathNLF=r'E:\pasham\MedicineHPF\Items\NarvarLayerFarm.csv'
#==========================

#==========================
def selectProduct():
    print('Om')
    print('What would you like to make today? Please Select from the list')
    print('1. Layer Mash Conc')
    print('2. Layer Masala')
    print('3. New Chicks Medicine')
    print('4. Layer Masala with DLM')
    print('5. Colidox')
    print('6. Trace Mineral')
    print('7. Narvar Layer Farm')
    ch=int(input('Enter your choice:'))
    if(ch==7):
        path=pathNLF
        return path

def toDo():
    print('Om')
    print('What would you like to do today? Please Select from the list')
    print('1. Make a Mixture')
    print('2. Check Inventory')
    print('3. Sell Certain Item')
    ch=int(input('Enter your choice:'))
    if(ch==1):
        pathCh=selectProduct()
        bagsNum=int(input('How many bags?'))
        changeAmountInventory(pathCh,pathInv,bagsNum)
    elif(ch==2):
        showInventory()



def changeAmountInventory(pathCh,pathInv,bagsNum):
    #Opens file for Inventory
    dfInv=pd.read_csv(pathInv)
    dupInv=dfInv
    #Opens file for Mixture
    dfMix=pd.read_csv(pathCh)
    dupMix=dfMix
    dupMix['Quantity']=dupMix['Quantity']*bagsNum
    for i in range(len(dupInv)):
        for j in range(len(dupMix)):
            if(dupInv['Product'][i]==dupMix['Product'][j]):
                x=float(dupInv['Amount'][i])-float(dupMix['Quantity'][j])
                dupInv['Amount'][i]=x

    l=dupInv[['Product','Amount']]
    l.to_csv(path_or_buf=r'E:\pasham\MedicineHPF\Items\Inventory1.csv')
    print('The New Inventory is:')
    print(l)
    
    
    
#def sellItem(itemName):
    

def showInventory():
    #Opens file
    dfInv=pd.read_csv(pathInv)
    print(dfInv)

def main():
    toDo()

main()
