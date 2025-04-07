import json
import xml.etree.ElementTree as ET

try:
    with open("datos.json", "r") as archivo:
        datos = json.load(archivo)

    root = ET.Element("personas")

    for persona in datos["personas"]:
        p = ET.SubElement(root, "persona")
        for clave, valor in persona.items():
            ET.SubElement(p, clave).text = str(valor)

    tree = ET.ElementTree(root)
    tree.write("resultado.xml", encoding="utf-8", xml_declaration=True)
    print("Archivo resultado.xml generado exitosamente.")
except FileNotFoundError:
    print("Archivo JSON no encontrado.")
