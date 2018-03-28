# Data-Science
//A program that extracts seed tags from stack overflow using beatiful soup and url request
import urllib.request
from bs4 import BeautifulSoup
import csv
import operator

def main():
    
    PopularLanguages = ["JavaScript","Java","C#","Ruby","Python","C++","Pl/SQL","MatLab",
                        "C","PHP","Perl","Delphi","Visual Basic","Objective-C","Swift",
                        "Assembly Language","Scratch","Go","Visual Basic.Net","R"]
#Getting the links
    Java = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/java")
    C = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/c")
    CPlus = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/c%2b%2b")
    Python =  urllib.request.urlopen("https://stackoverflow.com/questions/tagged/python")
    CSharp = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/c%23")
    JavaScript = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/javascript")
    VisualBasic_Net = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/.net")
    R = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/r")
    PHP = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/php")
    Perl = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/perl")
    Ruby = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/ruby")
    Swift = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/swift")
    Delphi = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/delphi")
    VisualBasic = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/vba")
    Assembly =  urllib.request.urlopen("https://stackoverflow.com/questions/tagged/assembly")
    Obj_C = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/objective-c")
    Scratch = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/mit-scratch")
    MatLab = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/mit-scratch")
    Go = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/go")
    SQL = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/sql")
    
    Tags = [JavaScript,Java,CSharp,Ruby,Python,CPlus,SQL, MatLab,C,PHP,Perl,Delphi,VisualBasic,
            Obj_C,Swift,Assembly,Scratch,Go,VisualBasic_Net,R]
    seeds = ["javascript","java","c%23","ruby","python","c%2b%2b","sql","matlab","c",
            "php","perl","vba","objective-c","swift","assembly","mit-scratch","go",
            ".net","r"]
#Extracting the number of questions and putting the requirments in a list
    QuesNum = []
    Questions = []
    QuesTags = []
    AllSisterTag = []
    for Tag in Tags:
        Data = Tag.read()
        soup = BeautifulSoup(Data, 'lxml')
        QuestionNum = soup.find("div",{"class" : "summarycount al"}).text
        QuesNum.append(QuestionNum)
        QuestionAct = soup.find_all("a",{"class": "question-hyperlink"})
        for x in QuestionAct:
            QuesTags.append(x["href"])
            Questions.append(x.string)
        SisterTags = soup.find_all("a",{"class": "post-tag no-tag-menu"})
        SisterTag = []
        for x in SisterTags[:11]:
            SisterTag.append(x.text)
            AllSisterTag.append(SisterTag)
#Wrtiting into the csv file
    with open("Top20.csv","w") as WriteFile:
        writer = csv.writer(WriteFile, delimiter = ",")
        
        for v,h,d in zip(PopularLanguages,QuesNum,AllSisterTag):
            col = (v + "," + h.replace(",","") + "," + d[0]
            + "," + d[1] + "," + d[2] + "," + d[3] + "," + d[4] + "," 
            + d[5] + "," + d[6] + "," + d[7] + "," + d[8] + "," + d[9])
            writer.writerow(col.split(","))
            
main()
