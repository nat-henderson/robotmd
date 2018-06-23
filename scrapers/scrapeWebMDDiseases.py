import requests, re
from bs4 import BeautifulSoup

output = ''
result = requests.get("https://www.webmd.com/a-to-z-guides/common-topics")
soup = BeautifulSoup(result.content, "html.parser")
for link in soup.findAll('a'):
    output += str(link.string)
    output += '\n'
print("Diseases: " + "\n")
print(output)
text_file = open("diseases.txt", "w")
text_file.write(output)
text_file.close()
#this file will require some manual editing to remove non-disease links
