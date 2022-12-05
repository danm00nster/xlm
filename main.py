import xml.etree.ElementTree as et
import os
import shutil
import sys
import datetime as dt

fLOG=open('log_python.txt' , 'a', encoding="utf-8")
today = dt.datetime.now()
fLOG.writelines(str(today)+" Strat \n")
MM = today.month
RR = today.year
fLOG.writelines("   sys.argv "+ str(len(sys.argv))+"\n")

if len(sys.argv) == 1:
    actualDIR = str(str(RR) + str(MM))
else:
    actualDIR = sys.argv[1]

fLOG.writelines("   Katalog wejściowy - data "+str(actualDIR)+"\n")
Local_dir = "z:/mbabc/faktury_11"
outDIR = "d:\majster\Testf"
# outDIR=os.path.join(outDIR_tmp, actualDIR)
Ldir = os.path.join(Local_dir, actualDIR)
testNIP = ['7010355056', '8890002504']
fileExist = 0
fileCopy = 0
if not os.path.isdir(outDIR):
    os.mkdir(outDIR)

if os.path.isdir(Ldir):
    files = os.listdir(Ldir)
    for f in files:
        isInvoice = 0
        test_f = f[0:2]


        if test_f == 'FS':
            isInvoice = 1

        if isInvoice:
            fullpath = os.path.join(Ldir, f)
            tree = et.parse(fullpath)
            Buyer = tree.findall('Buyer')
            root = tree.getroot()
            #print('taxID=', root[1][0][2].text)
            dir2create = root[1][0][2].text
            if dir2create in testNIP:
                partner_DIR = os.path.join(outDIR, dir2create)
                if os.path.isdir(partner_DIR):
                    if os.path.isfile(os.path.join(partner_DIR, f)):
                        fLOG.writelines("       Plik Istnieje "+str(f)+ " NIP " + str(dir2create) +"\n")
                        fileExist = fileExist + 1
                    else:
                        fLOG.writelines("   Kopiuję PLIK " + str(f) + " NIP " + str(dir2create) + "\n")
                        #print('kopiowanie', fullpath, os.path.join(partner_DIR, f))
                        shutil.copyfile(fullpath, os.path.join(partner_DIR, f))
                        fileCopy = fileCopy + 1
                else:
                    fLOG.writelines("   Tworzę Katalog " + str(partner_DIR))
                    os.mkdir(partner_DIR)
                    #print('kopiowanie', fullpath, os.path.join(partner_DIR, f))
                    shutil.copyfile(fullpath, os.path.join(partner_DIR, f))
else:
    print("brak katalogu",Ldir)
    fLOG.writelines("   Brak katalogu " + str(Ldir) +" \n")
    # print('taxID=',root.findall('./Document-Invoice/Invoice-Parties/Buyer/TaxID'))
    # calling the root element
fLOG.writelines(str(str(dt.datetime.now()) + " Skopiowane " + str(fileCopy) + " istnieją " + str(fileExist)+" END\n\n"))
print(actualDIR)
