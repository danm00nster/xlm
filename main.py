
import xml.etree.ElementTree as ET
import os, shutil
from os import listdir
from os.path import isfile, join
import pandas
import datetime as dt

today=dt.datetime.now()
MM=today.month
RR=today.year
actualDIR=str(str(RR)+str(MM))
print(actualDIR)
Ldir="d:\XML_Faktury"
outDIR_tmp="d:\majster"
outDIR=os.path.join(outDIR_tmp, actualDIR)
testNIP=['7010355056','8890002504']

if not os.path.isdir(outDIR):
    os.mkdir(outDIR)

files=os.listdir(Ldir)
for f in files:
    isInvoice=0
    test_f=f[0:2]
    print('##########',test_f)

    if test_f=='FS':
        isInvoice=1

    if isInvoice:
        fullpath = os.path.join(Ldir, f)
        tree = ET.parse(fullpath)
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
        dir2create=root[1][0][2].text
        partner_DIR = os.path.join(outDIR,dir2create)

        if os.path.isdir(partner_DIR):
            print('kopiowanie', fullpath,os.path.join(partner_DIR,f))
            shutil.copyfile(fullpath,os.path.join(partner_DIR,f))
        else:
            print("Tworzę Katalog ",partner_DIR)
            os.mkdir(partner_DIR)
            print('kopiowanie', fullpath, os.path.join(partner_DIR, f))
            shutil.copyfile(fullpath, os.path.join(partner_DIR, f))

    #print('taxID=',root.findall('./Document-Invoice/Invoice-Parties/Buyer/TaxID'))
    # calling the root element


