from objectExplorer import ObjectExplorer
from explorer import Explorer
from sys import argv

if __name__=="__main__":
    explorer=ObjectExplorer()
    showlist=argv
    explorer.createDOM("C://parse//Device.export")
    explorer.explore()
    #explorer.exploreList()
    #explorer.printNames()
    #explorer.ExplorePlcPrg()
    #explorer.showTypeGuids()
    #explorer.findAllPous()
    #explorer.cutPous()
    #explorer.restoreDOM("C://parse//clear.xml")
    #explorer.createPouDom("C://parse//POUS//ARCH_AND_RETAIN.xml")
    #explorer.catchPouText()
    #explorer.saveTexts()
    #explorer.explorePou()
    #explorer.exploreObjectSection()
    #hide_list=[]
    #explorer.findText(hide_list)