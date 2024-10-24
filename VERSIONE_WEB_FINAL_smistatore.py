######################################################################################################################
##########Cliccare sul tasto "play" qui a sinistra, apparirà in fondo al codice un tasto "Scegli  file"###############
#####Selezionare tutti i documenti inviati per la settimana da Tom Ford, così come scaricati dal loro sharepoint######
##Attendere il caricamento di tutti i PDF, alla fine in automatico verrà scaricato uno zip con tutti i docs smistati##
##########################Una volta completato il download, puoi chiudere questa pagina###############################
###############NON MODIFICARE IL CODICE ED AVVISARE IN CASO DI NUOVE DESTINAZIONI NON PREVISTE########################
######################################################################################################################

from google.colab import files
import os
import shutil
import glob

#delete previosly created files
try:
  os.remove("file.zip")
except:
  pass

try:
  shutil.rmtree("HongKong")
except:
  pass

try:
  shutil.rmtree("china")
except:
  pass

try:
  shutil.rmtree("japan")
except:
  pass

try:
  shutil.rmtree("korea")
except:
  pass

try:
  shutil.rmtree("Macao")
except:
  pass

try:
  os.remove("list_invoices_per_destination.txt")
except:
  pass

upload = files.upload()


files = upload

#Create lists for invoices
china_inv = []
hong_inv = []
japan_inv = []
korea_inv = []
macao_inv = []


#create list of destinations from the 28th character in the invoice name
dest_list = []
for file in files:
   dest_list += file[28]
   dest_list = list(dict.fromkeys(dest_list))
#smista i docs ed aggiunge numero fattura al file di riepilogo
for i in dest_list:
    if i == "G":
        os.mkdir("china")
        for file in files:
            if file[28] == "G":
                src_path = os.path.join("",file)
                dst_path = os.path.join("china",file)
                shutil.move(src_path, dst_path)
                inv_string= file[33:37]+"-"+file[38:41]+"-"+file[42:49]
                china_inv.append(inv_string)
        china_inv = list(dict.fromkeys(china_inv))
    elif i == "H":
        os.mkdir("HongKong")
        for file in files:
            if file[28] == "H":
                src_path = os.path.join("",file)
                dst_path = os.path.join("HongKong",file)
                shutil.move(src_path, dst_path)
                inv_string= file[33:37]+"-"+file[38:41]+"-"+file[42:49]
                hong_inv.append(inv_string)
        hong_inv = list(dict.fromkeys(hong_inv))
    elif i == "J":
        os.mkdir("japan")
        for file in files:
            if file[28] == "J":
                src_path = os.path.join("",file)
                dst_path = os.path.join("japan",file)
                shutil.move(src_path, dst_path)
                inv_string= file[33:37]+"-"+file[38:41]+"-"+file[42:49]
                japan_inv.append(inv_string)
        japan_inv = list(dict.fromkeys(japan_inv))
    elif i == "K":
        os.mkdir("korea")
        for file in files:
            if file[28] == "K":
                src_path = os.path.join("",file)
                dst_path = os.path.join("korea",file)
                shutil.move(src_path, dst_path)
                inv_string= file[33:37]+"-"+file[38:41]+"-"+file[42:49]
                korea_inv.append(inv_string)
        korea_inv = list(dict.fromkeys(korea_inv))
    elif i == "M":
        os.mkdir("Macao")
        for file in files:
            if file[28] == "M":
                src_path = os.path.join("",file)
                dst_path = os.path.join("Macao",file)
                shutil.move(src_path, dst_path)
                inv_string= file[33:37]+"-"+file[38:41]+"-"+file[42:49]
                macao_inv.append(inv_string)
        macao_inv = list(dict.fromkeys(macao_inv))
    else:
        pass
#scrivi file di testo con i numeri fattura
with open("list_invoices_per_destination.txt", "w") as file:
    file.write("\n"+"China invoices: "+",".join(china_inv))
    file.write("\n"+"Hong Kong invoices: "+",".join(hong_inv))
    file.write("\n"+"Japan invoices: "+",".join(japan_inv))
    file.write("\n"+"korea invoices: "+",".join(korea_inv))
    file.write("\n"+"Macao invoices: "+",".join(macao_inv))

#Try to add files to the zip for download
try:
  !zip -r /content/file.zip /content/HongKong
except:
  pass
try:
  !zip -r /content/file.zip /content/china
except:
  pass
try:
  !zip -r /content/file.zip /content/korea
except:
  pass
try:
  !zip -r /content/file.zip /content/Macao
except:
  pass
try:
  !zip -r /content/file.zip /content/japan
except:
  pass
try:
  !zip -r /content/file.zip /content/list_invoices_per_destination.txt
except:
  pass
#scarica tutto
from google.colab import files
files.download("/content/file.zip")