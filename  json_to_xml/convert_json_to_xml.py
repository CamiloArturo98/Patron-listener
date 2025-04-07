import json
import xml.etree.ElementTree as ET

def dict_a_xml(tag, d):
    elem = ET.Element(tag)
    for clave, valor in d.items():
        subelem = ET.SubElement(elem, clave)
        subelem.text = str(valor)
    return elem

def convertir_json_a_xml(json_file, xml_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    
    raiz = dict_a_xml('root', datos)
    arbol = ET.ElementTree(raiz)
    arbol.write(xml_file, encoding='utf-8', xml_declaration=True)
    print(f"Archivo XML guardado como: {xml_file}")

# Ejecutar conversión
convertir_json_a_xml('datos.json', 'salida.xml')
