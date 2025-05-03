import requests
import xml.etree.ElementTree as ET

urls = [
    "https://epg.pw/api/epg.xml?channel_id=403626",
    "https://epg.pw/api/epg.xml?channel_id=400477",
    "https://epg.pw/api/epg.xml?channel_id=400480",
    "https://epg.pw/api/epg.xml?channel_id=405060",
    "https://epg.pw/api/epg.xml?channel_id=405134",
]

merged_tv = ET.Element("tv")

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        for elem in root:
            merged_tv.append(elem)

tree = ET.ElementTree(merged_tv)
tree.write("merged_epg.xml", encoding="utf-8", xml_declaration=True)
