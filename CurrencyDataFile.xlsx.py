#  Taking no. of  Questions and question papers from user
import xlrd
import os
loc=("C:\\Users\\hp\\Desktop\\CurrencyDataFile.xlsx")   #location of file
rs=xlrd.open_workbook(loc)
sheet=rs.sheet_by_index(0)
sheet.cell_value(0,0)
def storinganswer(n,k,d):
    rs= xlrd.open_workbook("C:\\Users\\hp\\Desktop\\CurrencyDataFile.xlsx")
    sheet =rs.sheet_by_index(0)
    ans.write(str(k)+":"+str(sheet.cell_value(n,1))+"\n")  
for i in range(0,302):
    for j in range(1,10):
         print(sheet.cell_value(i,j))
def Question(a,b,c,i,j):
     dict={'A':a,'B':b,'C':c}
     print("what is the symbol for" + " " + str(sheet.cell_value(i,j)) + " " + "?")
     print("A.",dict['A'])
     print("B.",dict['B'])
     print("C.",dict['C'])

#printing questions
for i in range (2,206):
        Question(sheet.cell_value(i-1,2),sheet.cell_value(i,2),sheet.cell_value(i+1,2),i,1)
n=int(input("Enter the Question paper number : "))
os.chdir("C:\\Users\\hp\\Desktop")
ans=open("Answerkey.txt",'w')
for i in range(1,13):
    if(n==i):
        print("The quetion paper of number is ",i)
        for k in range(i,270,17):                                 # 17 is step 
            Question(sheet.cell_value(k-1,2),sheet.cell_value(k,2),sheet.cell_value(k+1,2),k,1) 
        print("The answerkey of the question paper number ",i)
        for j in range (1,300,17):
                 ans.write("Answerkey"+str(sheet.cell_value(j,2))+"\n")
ans.close()
print("For Answer Key of the Entered question paper \n")
ans=open("Answerkey.txt",'r')
for i in range(1,13):
    if(n==i):
        for k in range(i,270,17):
            print(sheet.cell_value(k,2))
ans.close()