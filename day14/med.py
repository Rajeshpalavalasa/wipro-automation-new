import xml.etree.ElementTree as ET

# Load and parse the XML file
xml_doc = ET.parse(
    r"E:\wipro_training\python_batch09\wipro-automation\wipro-automation-new\day14\md.xml"
)

root_node = xml_doc.getroot()

# Store diseases
disease_list = []

# Extract disease names from XML
for disease in root_node.findall(".//medicalIssue"):
    if disease.text:
        disease_list.append(disease.text.strip())

# Sort diseases alphabetically
disease_list.sort(key=str.lower)

# Display output
print("Diseases in Alphabetical Order:")
for d in disease_list:
    print(d)
