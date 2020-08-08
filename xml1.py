import urllib.request
import xml.etree.ElementTree as ET

# url = ''


uh = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_795662.xml')
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

results = tree.findall('.//count')
nums = [int(node.text) for node in results]
counts = sum(nums)
print(counts)
