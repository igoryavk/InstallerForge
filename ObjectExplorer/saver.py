from objectExplorer import ObjectExplorer
from explorer import Explorer
from sys import argv
from time import sleep


if __name__=="__main__":
    explorer=ObjectExplorer()
    showlist=[]
    explorer.createDOM(f"C://parse//{argv[2]}//ExportFiles//{argv[1]}.export")
    #explorer.exploreList()
    #explorer.printNames()
    #explorer.ExplorePlcPrg()
    #explorer.showTypeGuids()
    #explorer.findAllPous()
    explorer.cutPous(f"C://parse//{argv[2]}//POUs")
    #explorer.restoreDOM("C://parse//clear.xml")
    #explorer.createPouDom("C://parse//POUS//ARCH_AND_RETAIN.xml")
    #explorer.catchPouText()
    explorer.saveTexts(f"C://parse//{argv[2]}//sources",f"C://parse//{argv[2]}//POUs")
    #explorer.explorePou()
    #explorer.exploreObjectSection()
    #hide_list=[]
    #explorer.findText(hide_list)