
import freecad_env

import FreeCAD, Part

import FreeCAD as App
import Part, PartDesign, Sketcher
from FreeCAD import Vector

import os

class FreecadDoc:
    def __init__(self, doc_name:str):
        self.doc_name=doc_name
        self.doc = App.newDocument(doc_name)
        App.setActiveDocument(doc_name)
        App.ActiveDocument=App.getDocument(doc_name)


        current_directory = os.getcwd()
        print("Current Working Directory:", current_directory)

        file_name=doc_name
        output_folder=f"{current_directory}/output/"
        os.makedirs(output_folder, exist_ok=True)

        self.output_folder=output_folder
        self.file_name=file_name

    def save(self):

        doc_file_name=f"{self.output_folder}/{self.file_name}.FCStd"
        self.doc.saveAs(doc_file_name)
        print(f"doc_file_name: {doc_file_name}")

    def export_gcode(self, gcode:str):
        # Save GCode
        cnc_file_name = f"{self.output_folder}/{self.file_name}.nc"
        with open(cnc_file_name, "w") as f:
            f.write(gcode)
        print(f"GCode successfully generated at {cnc_file_name}")

    def export_body(self, body):

        __objs__ = []
        __objs__.append(body)
        import importers.importOBJ

        obj_file_name=f"{self.output_folder}/{self.file_name}.obj"
        print(f"obj_file_name: {obj_file_name}")
        if hasattr(importers.importOBJ, "exportOptions"):
            options = importers.importOBJ.exportOptions(obj_file_name)
            importers.importOBJ.export(__objs__,obj_file_name, options)
        else:
            importers.importOBJ.export(__objs__, obj_file_name)

        del __objs__


        __objs__ = []
        __objs__.append(body)
        import Mesh
        stl_file_name=f"{self.output_folder}/{self.file_name}.stl"
        print(f"stl_file_name: {stl_file_name}")
        if hasattr(Mesh, "exportOptions"):
            options = Mesh.exportOptions(stl_file_name)
            Mesh.export(__objs__, stl_file_name, options)
        else:
            Mesh.export(__objs__, stl_file_name)

        del __objs__


        __objs__ = []
        __objs__.append(body)
        import importDXF
        dxf_file_name=f"{self.output_folder}/{self.file_name}.dxf"
        print(f"dxf_file_name: {dxf_file_name}")
        if hasattr(importDXF, "exportOptions"):
            options = importDXF.exportOptions(dxf_file_name)
            importDXF.export(__objs__, dxf_file_name, options)
        else:
            importDXF.export(__objs__, dxf_file_name)

        del __objs__


        # __objs__ = []
        # __objs__.append(body)

        # import ImportGui
        # step_file_name=f"{output_folder}/{file_name}.step"
        # print(f"step_file_name: {step_file_name}")
        # if hasattr(ImportGui, "exportOptions"):
        #     options = ImportGui.exportOptions(step_file_name)
        #     ImportGui.export(__objs__, step_file_name, options)
        # else:
        #     ImportGui.export(__objs__, step_file_name)

        # del __objs__


