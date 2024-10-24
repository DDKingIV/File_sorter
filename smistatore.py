import os
import shutil
import glob

files = glob.glob("*.pdf")

#Create lists for invoices
china_inv = []
hong_inv = []
japan_inv = []
korea_inv = []
macao_inv = []


#create list of destinations
dest_list = []
for file in files:
   dest_list += file[28]
   dest_list = list(dict.fromkeys(dest_list))

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
        os.mkdir("Hong Kong")
        for file in files:
            if file[28] == "H":
                src_path = os.path.join("",file)
                dst_path = os.path.join("Hong Kong",file)
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

with open("list of invoices per destination.txt", "w") as file:
    file.write("\n"+"China invoices: "+",".join(china_inv))
    file.write("\n"+"Hong Kong invoices: "+",".join(hong_inv))
    file.write("\n"+"Japan invoices: "+",".join(japan_inv))
    file.write("\n"+"korea invoices: "+",".join(korea_inv))
    file.write("\n"+"Macao invoices: "+",".join(macao_inv))