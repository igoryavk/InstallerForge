# import scriptengine
# scriptengine.ScriptProject.export_native()
from os import system
from os import popen
from shutil import rmtree
from os import mkdir
from os.path import exists


#Here we are getting the project name for future use
info=projects.primary.get_project_info()
project_name=info.values["Project"]


PATH="C://parse//{0}".format(project_name)
SAVER_PATH="C://parse//exec//saver.py"

#Create folder for project storing
if exists(PATH):
    rmtree(PATH)
mkdir(PATH)

objects=" "
for item in projects.primary.get_children():
    objects=objects+" "+item.get_name().replace(" ","_")

output=popen("C://parse//exec//Selector.exe {0}".format(objects)).read()
selected=output.split("\n")
export_list=[]
#Collecting list of export objects
for object in projects.primary.get_children():
    for name in selected:
        if object.get_name()==name:
            export_list.append(object)
#print(projects.primary.active_application.get_name())

#Temporary limiting to 1 selected object
one_export_object=export_list[0]
print(type(one_export_object))
projects.primary.export_native(objects=export_list,destination=PATH,recursive=True,one_file_per_subtree=True)

#Drop folder befor export

path="C://parse//{0}//ExportFiles".format(project_name)
if exists(path):
    rmtree(path)
mkdir(path)

#Separated export for second-level objects
for elementLevel1 in projects.primary.get_children():
    if elementLevel1.get_name()==one_export_object.get_name():
        for elementLevel2 in elementLevel1.get_children():
            elementLevel2.export_native("C://parse//{1}//ExportFiles//{0}.export".format(elementLevel2.get_name(),project_name))

system("python {0} \"{1}\" \"{2}\"".format(SAVER_PATH,"Plc Logic",project_name))


