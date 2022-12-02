
import xml.etree.ElementTree as ET
import os, shutil
from os import listdir
from os.path import isfile, join
import pandas
import datetime as dt

#net use //192.168.68.199/homes/danielkwiecinski/wymiana/mbabc/faktury_11
#input("Press Enter to continue...")

today=dt.datetime.now()
MM=today.month
RR=today.year
actualDIR=str(str(RR)+str(MM))
print(actualDIR)
Local_dir="z:/mbabc/faktury_11"
outDIR="d:\majster\Testf"
#outDIR=os.path.join(outDIR_tmp, actualDIR)
Ldir=os.path.join(Local_dir, actualDIR)
testNIP=['7010355056','8890002504']
fileExist=0
fileCopy=0
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
        if dir2create in testNIP:
            partner_DIR = os.path.join(outDIR,dir2create)

            if os.path.isdir(partner_DIR):
                if os.path.isfile(os.path.join(partner_DIR,f)):
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++Plik Istnieje")
                    fileExist=fileExist+1
                else:
                    print('kopiowanie', fullpath,os.path.join(partner_DIR,f))
                    shutil.copyfile(fullpath,os.path.join(partner_DIR,f))
                    fileCopy=fileCopy+1
            else:
                print("Tworzę Katalog ",partner_DIR)
                os.mkdir(partner_DIR)
                print('kopiowanie', fullpath, os.path.join(partner_DIR, f))
                shutil.copyfile(fullpath, os.path.join(partner_DIR, f))

    #print('taxID=',root.findall('./Document-Invoice/Invoice-Parties/Buyer/TaxID'))
    # calling the root element
print("Skopiowane", fileCopy, "istnieją", fileExist)

