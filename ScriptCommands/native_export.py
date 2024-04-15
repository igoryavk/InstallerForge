# import scriptengine
# scriptengine.ScriptProject.export_native()
from os import system
from os import popen

PATH="C://parse//"
SAVER_PATH="C://parse//exec//saver.py"

objects=" "
for item in projects.primary.get_children():
    objects=objects+" "+item.get_name().replace(" ","_")
output=popen("C://parse//exec//Selector.exe {0}".format(objects)).read()
selected=output.split("\n")
export_list=[]
for object in projects.primary.get_children():
    for name in selected:
        if object.get_name()==name:
            export_list.append(object)
#print(projects.primary.active_application.get_name())
projects.primary.export_native(objects=export_list,destination=PATH,recursive=True,one_file_per_subtree=True)
#system("python {0}".format(SAVER_PATH))

