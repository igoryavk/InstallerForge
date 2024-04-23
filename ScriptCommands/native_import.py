
# import scriptengine
# scriptengine.ScriptProject.export_native()
from os import system
from os import popen
from os import listdir
from os.path import exists
from os.path import normpath
PATH="C://parse//"
PROJECT_SELECTOR_PATH="C://parse//exec//Import_Selector.exe"
IMPORTER_PATH="C://parse//exec//importer.py"




class MyNativeImportHandler(NativeImportHandler):
    """Handler callback for the native XML import.

    This interface is exposed under the name NativeImportHandler.

    """

    def conflict(self, name, existingObject, newguid):
        print("There is a conflict")

    def progress(self, name, pastedObject, exception):
        print("It works")

    def skipped(self, name):
        print("Object is skipping")

#print(projects.primary.active_application.get_name())
#projects.primary.export_native(objects=objects,destination=PATH,recursive=True,one_file_per_subtree=True)
#system("python {0}".format(IMPORTER_PATH))


def CallSelector(DirPath,SelectorPath):
    import_list = " "
    for item in listdir(DirPath):
        import_list = import_list + " " + item
    return popen("{1} {0}".format(import_list,SelectorPath)).read()


# import_list=" "
# for item in listdir(PATH):
#     import_list=import_list+" "+item.replace(" ","_")
# project=CallSelector(PATH,PROJECT_SELECTOR_PATH)
# print(project)
project=CallSelector("C://parse","C://parse//exec//Import_ProjectSelector.exe")

project=project.replace('\n','')
DEVICE_PATH="C://parse//{0}".format(project)

DEVICE_SELECTOR_PATH="C://parse//exec//Import_DeviceSelector.exe"


device=CallSelector(r"C:\parse\{0}".format(project),DEVICE_SELECTOR_PATH)
device=device.replace('\n','')
IMPORT_PATH="C://parse//{0}//{1}".format(project,device)

projects.primary.close()
new_project=projects.create(project)
native_import_handler=MyNativeImportHandler()

new_project.import_native(filename=IMPORT_PATH)

