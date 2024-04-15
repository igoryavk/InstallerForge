# import scriptengine
# scriptengine.ScriptProject.export_native()
from os import system

PATH="C://parse//"
IMPORTER_PATH="C://parse//exec//importer.py"
IMPORT_PATH="C://parse//Device.export"


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

projects.primary.close()
new_project=projects.create("NewProject")
native_import_handler=MyNativeImportHandler()

new_project.import_native(filename=IMPORT_PATH)

