import os.path

import bs4
import json

from explorer import Explorer
from bs4 import BeautifulSoup
from colorama import Fore
from os.path import exists
from shutil import rmtree
from os import mkdir
from os import listdir

#Класс управляющий сохранением POU, их извлечением
# и восставновлением в основном экпортном файле, а
# также извлечением из них текстовой информации
class ObjectExplorer(Explorer):
    #Метод построения DOM из файла экспорта
    def createDOM(self,path:str):
        with open(path,mode="r",encoding="utf-8") as file:
            content=file.read()
        print("Wait please, DOM is building!!!")
        self.__DOM=BeautifulSoup(content,"xml")
        self.__root=self.__DOM.ExportFile

    def explore(self):

        mylist = self.__root.find_all("List2")
        drop_list = []
        #self.__dropFolder("C://parse//POUS")
        for elementLevel1 in [item for item in mylist[0].children if item.name is not None]:
            for elementLevel2 in [item for item in elementLevel1.children if item.name is not None]:
                if elementLevel2["Name"] == "MetaObject":
                    for elementLevel3 in [item for item in elementLevel2.children if item.name is not None]:
                        if elementLevel3["Name"] == "TypeGuid":
                            if elementLevel3.text == "f8a58466-d7f6-439f-bbb8-d4600e41d099":
                                pou = elementLevel3.parent.parent
                                pou_name = elementLevel3.parent.find_all("Single", {"Name": "Name"})[0].text
                                print("____________________")
                                for item in [item for item in pou.children if item.name is not None]:
                                    if item.name=="Array":
                                        print(type(item))
                                        for item2 in [item for item in item.children if item.name is not None]:
                                            print(f"{item2.attrs}")

                                # with open(f"C://parse//POUS//{pou_name}.xml", mode="w", encoding="utf-8") as file:
                                #     file.write(str(pou))
                                #     file.close()
                                # drop_list.append(pou)

    def exploreList(self):
        mylist = self.__root.find_all("List2")
        l1_iterator=0
        for elementLevel1 in [item for item in mylist[0].children if item.name is not None]:
             l1_iterator=l1_iterator+1
             if l1_iterator==2:
                print(f"{Fore.RED}Уровень 1 {elementLevel1.name}")
                print(f"{elementLevel1.attrs}")
                for elementLevel2 in [item for item in elementLevel1.children if item.name is not None]:
                     if elementLevel2["Name"]=="MetaObject":
                        print(f"{Fore.GREEN}Уровень 2 {elementLevel2.name}")
                        print(f"{elementLevel2.attrs}")
                        for elementLevel3 in [item for item in elementLevel2.children if item.name is not None]:
                            print(f"{Fore.YELLOW} Уровень 3 {elementLevel3.name}")
                            print(f"{elementLevel3.attrs}")
                            if elementLevel3["Name"]=="Name":
                                print(elementLevel3.text)

    def printNames(self):
        mylist=self.__root.find_all("List2")
        l1_iterator=0
        for elementLevel1 in [item for item in mylist[0].children if item.name is not None]:
            l1_iterator=l1_iterator+1
            print(l1_iterator)
            for elementLevel2 in [item for item in elementLevel1.children if item.name is not None]:
                if elementLevel2["Name"]=="MetaObject":
                    for elementLevel3 in [item for item in elementLevel2.children if item.name is not None]:
                        if elementLevel3["Name"]=="Name":
                            print(elementLevel3.text)

    def ExplorePlcPrg(self):
        mylist = self.__root.find_all("List2")
        iterator=0
        for elementLevel1 in [item for item in mylist[0].children if item.name is not None]:
            iterator=iterator+1
            if iterator==22:
                for elementLevel2 in [item for item in elementLevel1.children if item.name is not None]:
                    print(f"{Fore.YELLOW}{elementLevel2.attrs}")
                    for elementLevel3 in [item for item in elementLevel2.children if item.name is not None]:
                        print(f"{Fore.RED}{elementLevel3.attrs}")
                        print(f"{Fore.GREEN}{elementLevel3.text}")
    #Метод показывающий все присутствующие в проекте GUID типы(требовался для определения GUID типа POU)
    def showTypeGuids(self):
        mylist=self.__root.find_all("List2")
        iterator=0
        for elementLevel1 in [item for item in mylist[0].children if item.name is not None]:
            iterator=iterator+1
            print(f"{Fore.RED}{iterator}")
            #print(f"{Fore.LIGHTCYAN_EX}{elementLevel1.attrs}")
            for elementLevel2 in [item for item in elementLevel1.children if item.name is not None]:
                #print(f"{Fore.LIGHTBLUE_EX}{elementLevel2.name}{elementLevel2.attrs}")
                if elementLevel2["Name"]=="MetaObject":
                    for elementLevel3 in [item for item in elementLevel2.children if item.name is not None]:
                        if elementLevel3["Name"] == "Name":
                            print(f"{Fore.LIGHTMAGENTA_EX}{elementLevel3.text}")
                        if elementLevel3["Name"]=="TypeGuid":
                            #print(f"{Fore.LIGHTMAGENTA_EX}{elementLevel3.attrs}")
                            print(f"{Fore.LIGHTGREEN_EX}{elementLevel3.text}")

    def findAllPous(self):
        mylist=self.__root.find_all("List2")
        iterator=0
        pou_num = 0
        for elementLevel1 in [item for item in mylist[0].children if item.name is not None]:
            iterator=iterator+1
            print(f"{Fore.RED}Элемент №{iterator}")
            for elementLevel2 in [item for item in elementLevel1.children if item.name is not None]:
                if elementLevel2["Name"]=="MetaObject":
                    for elementLevel3 in [item for item in elementLevel2.children if item.name is not None]:
                        if elementLevel3["Name"]=="TypeGuid":
                            if elementLevel3.text=="6f9dac99-8de1-4efc-8465-68ac443b7d08":
                                pou_num=pou_num+1
                                name=elementLevel3.parent.find_all("Single",{"Name":"Name"})
                                print(f"{Fore.GREEN} №{pou_num} {name[0].text}")
    #Метод пересоздающий папку для хранения POU(приватный)
    def __dropFolder(self,path:str):
        if exists(path):
            rmtree(path)
        mkdir(path)
    #Метод извлечения POU объектов из экпортного файла и сохранения clear-файла(файл содержащий stub-болванки для POU)
    #Данный файл служит для восстановления экспортного файла
    def cutPous(self,pou_folder):
        mylist=self.__root.find_all("List2")
        drop_list=[]
        self.__dropFolder(pou_folder)
        for elementLevel1 in [item for item in mylist[0].children if item.name is not None]:
            for elementLevel2 in [item for item in elementLevel1.children if item.name is not None]:
                if elementLevel2["Name"]=="MetaObject":
                    for elementLevel3 in [item for item in elementLevel2.children if item.name is not None]:
                        if elementLevel3["Name"]=="TypeGuid":
                            #Если элемент является POU
                            if elementLevel3.text=="6f9dac99-8de1-4efc-8465-68ac443b7d08":
                                pou=elementLevel3.parent.parent
                                pou_name=elementLevel3.parent.find_all("Single",{"Name":"Name"})[0].text
                                with open(f"{pou_folder}//{pou_name}.xml",mode="w",encoding="utf-8") as file:
                                    file.write(str(pou))
                                    file.close()
                                drop_list.append(pou)
                            #Если элемент является методом
                            if elementLevel3.text=="f8a58466-d7f6-439f-bbb8-d4600e41d099":
                                method=elementLevel3.parent.parent
                                method_name=elementLevel3.parent.find_all("Single",{"Name":"Name"})[0].text
                                for element in [item for item in method.children if item.name is not None]:
                                    if element.name=="Array":
                                        path_to_method=[item for item in element.children if item.name is not None]
                                pou_name=path_to_method[-1].text
                                with open(f"{pou_folder}//{pou_name}.{method_name}.xml",mode="w",encoding="utf-8") as file:
                                    file.write(str(method))
                                    file.close()
                                drop_list.append(method)
        for pou in drop_list:
            stub=self.__DOM.new_tag("Stub")
            stub['name']=pou.find_all("Single",{"Name":"Name"})[0].text
            pou.parent.append(stub)
            pou.decompose()
        with open("C://parse//clear.xml",mode="w",encoding="utf-8") as file:
            file.write(str(self.__DOM))
            file.close()
    #Метод восстановления информации о POU и создания восстановленного файла output.export
    def restoreDOM(self,path:str):
        with open(path,mode='r',encoding='utf-8') as file:
            content=file.read()
            file.close()
        self._clearDOM=BeautifulSoup(content,'xml')
        self._rootClear=self._clearDOM.ExportFile
        self._readPous()

    #Метод чтения сохраненной информации о POU(приватный)
    def _readPous(self):
        stubs=self._rootClear.find_all("Stub")
        pous=listdir("C://parse//POUS")
        if stubs!=None:
            for stub in stubs:
               if exists(f"C://parse//POUS//{stub['name']}.xml"):
                    pou=self.openPouFile(f"C://parse//POUS//{stub['name']}.xml")
                    stub.parent.append(pou)
                    stub.decompose()
        with open("C://parse//output.export",mode="w",encoding="utf-8") as file:
            file.write(str(self._clearDOM))
            file.close()

    def openPouFile(self,path:str):
        with open(path,mode="r",encoding="utf-8") as file:
            content=file.read()
            file.close()
        return BeautifulSoup(content,"xml")
    def saveTexts(self,sources_folder,pou_folder):
        if exists(sources_folder):
            rmtree(sources_folder)
        mkdir(sources_folder)

        for filename in listdir(pou_folder):
            self._PouName=filename
            self.createPouDom(f"{pou_folder}//{filename}")
            self.catchPouText(sources_folder)

    def createPouDom(self,path:str):
        with open(path,mode="r",encoding="utf8") as file:
            content=file.read()
            file.close()
        self.__rootPouDom=BeautifulSoup(content,"xml")
    def catchPouText(self,sources_folder):
        text=""
        textDocuments=self.__rootPouDom.find_all("Single",{"Name":"TextDocument"})
        textDocuments.reverse()
        for textDocument in textDocuments:
            text=text+self.findPouText(textDocument)

        with open(f"{sources_folder}//{self._PouName}", "w") as file:
            file.write(text)
            file.close()
    def findPouText(self,rootElement:bs4.Tag):
        pou_text=""
        for elementLevel1 in [item for item in rootElement.children if item.name is not None]:
            for elementLevel2 in [item for item in elementLevel1.children if item.name is not None]:
                for elementLevel3 in [item for item in elementLevel2.children if item.name is not None]:
                    if elementLevel3["Name"]=="Text":
                        pou_text=pou_text+elementLevel3.text+"\n"
        return  pou_text

    def explorePou(self):
        for elementLevel1 in [item for item in self.__rootPouDom.children if item.name is not None]:
            print(f"{Fore.RED}{elementLevel1.name}")
            print(f"{Fore.RED}{elementLevel1.attrs}")
            for elementLevel2 in [item for item in elementLevel1.children if item.name is not None]:
                print(f"    {Fore.GREEN}{elementLevel2.name}")
                print(f"    {Fore.GREEN}{elementLevel2.attrs}")
                if elementLevel2["Name"]=="ParentSVNodeGuid":
                    print(f"    {Fore.LIGHTGREEN_EX}{elementLevel2.text}")
                if elementLevel2["Name"] == "IsRoot":
                    print(f"    {Fore.LIGHTGREEN_EX}{elementLevel2.text}")
                for elementLevel3 in [item for item in elementLevel2.children if item.name is not None]:
                    print(f"        {Fore.YELLOW}{elementLevel3.name}")
                    print(f"        {Fore.YELLOW}{elementLevel2.attrs}")
                    print(f"        {Fore.LIGHTWHITE_EX}{elementLevel3.text}")
                    for elementLevel4 in [item for item in elementLevel3.children if item.name is not None]:
                        print(f"            {Fore.LIGHTMAGENTA_EX}{elementLevel4.name}")
                        print(f"            {Fore.LIGHTMAGENTA_EX}{elementLevel4.attrs}")
                        print(f"            {Fore.CYAN}{elementLevel4.text}")

    def findText(self,hide:list):
        list_of_texts:list=self.__rootPouDom.find_all("Single",{"Name":"TextDocument"})
        list_of_texts.reverse()
        lines=[]
        jsonStr:str=""
        for elementLevel1 in list_of_texts:
            if not 1 in hide:
                print(f"{Fore.GREEN}{elementLevel1.name}")
                print(f"{Fore.GREEN}{elementLevel1.attrs}")
            jsonStr=f"{{'{elementLevel1.name}':{elementLevel1.attrs}}}"

            for elementLevel2 in [item for item in elementLevel1.children if item.name is not None]:
                if not 2 in hide:
                    print(f"{Fore.YELLOW}{elementLevel2.name}")
                    print(f"{Fore.YELLOW}{elementLevel2.attrs}")
                for elementLevel3 in [item for item in elementLevel2.children if item.name is not None]:
                    if not 3 in hide:
                        print(f"{Fore.CYAN}{elementLevel2.name}")
                        print(f"{Fore.CYAN}{elementLevel2.attrs}")
                    #print(f"{Fore.WHITE}{elementLevel2.text}")
                    for elementLevel4 in [item for item in elementLevel3.children if item.name is not None]:
                        if not 4 in hide:
                            print(f"{Fore.LIGHTMAGENTA_EX}{elementLevel4.name}")
                            print(f"{elementLevel4.attrs}")
                        if elementLevel4["Name"]=="Text":
                            print(f"{Fore.LIGHTWHITE_EX}{elementLevel4.text}")
                            with open("C://parse//POUS//ARCH_AND_RETAIN.xml",mode="a+") as file:
                                file.write(elementLevel4.text+"\n")
                                file.close()
    def exploreObjectSection(self):
        for elementLevel1 in [item for item in self.__rootPouDom.children if item.name is not None]:
            for elementLevel2 in [item for item in elementLevel1.children if item.name is not None]:
                if elementLevel2["Name"]=="Object":
                    print(f"{elementLevel2.name}")
                    print(f"{elementLevel2.attrs}")
                    for elementLevel3 in [item for item in elementLevel2.children if item.name is not None]:
                        print(f"    {elementLevel3.name}")
                        print(f"    {elementLevel3.attrs}")
                        if elementLevel3["Name"]=="Implementation":
                            for elementLevel4 in [item for item in elementLevel3.children if item.name is not None]:
                                print(f"        {elementLevel4.name}")
                                print(f"        {elementLevel4.attrs}")
                                for elementLevel5 in [item for item in elementLevel4.children if item.name is not None]:
                                    print(f"            {elementLevel5.name}")
                                    print(f"            {elementLevel5.attrs}")
                                    for elementLevel6 in [item for item in elementLevel5.children if item.name is not None]:
                                        print(f"                {elementLevel6.name}")
                                        print(f"                {elementLevel6.attrs}")
                                        for elementLevel7 in [item for item in elementLevel6.children if item.name is not None]:
                                            print(f"                    {elementLevel7.name}")
                                            print(f"                    {elementLevel7.attrs}")
                                            if elementLevel7["Name"]=="Text":
                                                print(f"                    {elementLevel7.text}")
                        if elementLevel3["Name"]=="Interface":
                            for elementLevel4 in [item for item in elementLevel4.children if item.name is not None]:
                                print(f"        {elementLevel4.name}")
                                print(f"        {elementLevel4.attrs}")
                                for elementLevel5 in [item for item in elementLevel4.children if item.name is not None]:
                                    print(f"            {elementLevel5.name}")
                                    print(f"            {elementLevel5.attrs}")
                                    for elementLevel6 in [item for item in elementLevel5.children if item.name is not None]:
                                        print(f"                {elementLevel6.name}")
                                        print(f"                {elementLevel6.attrs}")
                                        if elementLevel6["Name"]=="Tag":
                                            print(f"                  {elementLevel6.text}")



