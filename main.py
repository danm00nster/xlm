# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import xml.etree.ElementTree as ET


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
tree = ET.parse('test.xml')

Buyer=tree.findall('Buyer')

root=tree.getroot()
#print(root.tag)
#for child in root:
#    print(child.tag,child.attrib)

#print([elem.tag for elem in root.iter()])
#for TaxID in root.iter('TaxID'):
#    print('TaxID', TaxID.text )

#for TaxID in root.findall('./Document-Invoice/Invoice-Parties/Buyer/'):
#    print('test', TaxID.attrib)

print('taxID=',root[1][0][2].text)
#print('taxID=',root.findall('./Document-Invoice/Invoice-Parties/Buyer/TaxID'))
# calling the root element


