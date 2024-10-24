import os
import shutil
import tkinter as tk
from tkinter import filedialog

china_inv = []
hong_inv = []
japan_inv = []
korea_inv = []
macao_inv = []

def process_files():
    global china_inv, hong_inv, japan_inv, korea_inv, macao_inv  # Declare lists as global
    
    selected_files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    for selected_file in selected_files:
        dest_folder = None
        dest_code = os.path.basename(selected_file)[28]
        
        if dest_code == "G":
            dest_folder = "china"
        elif dest_code == "H":
            dest_folder = "Hong Kong"
        elif dest_code == "J":
            dest_folder = "japan"
        elif dest_code == "K":
            dest_folder = "korea"
        elif dest_code == "M":
            dest_folder = "Macao"
        
        if dest_folder:
            if not os.path.exists(dest_folder):
                os.mkdir(dest_folder)
            
            dst_path = os.path.join(dest_folder, os.path.basename(selected_file))
            shutil.move(selected_file, dst_path)
            
            inv_string = os.path.basename(selected_file)[33:37] + "-" + \
                         os.path.basename(selected_file)[38:41] + "-" + \
                         os.path.basename(selected_file)[42:49]
            
            if dest_code == "G":
                china_inv.append(inv_string)
            elif dest_code == "H":
                hong_inv.append(inv_string)
            elif dest_code == "J":
                japan_inv.append(inv_string)
            elif dest_code == "K":
                korea_inv.append(inv_string)
            elif dest_code == "M":
                macao_inv.append(inv_string)
    
    # Remove duplicates from the invoice lists
    china_inv = list(dict.fromkeys(china_inv))
    hong_inv = list(dict.fromkeys(hong_inv))
    japan_inv = list(dict.fromkeys(japan_inv))
    korea_inv = list(dict.fromkeys(korea_inv))
    macao_inv = list(dict.fromkeys(macao_inv))
    
    with open("list of invoices per destination.txt", "w") as file:
        file.write("\n" + "China invoices: " + ",".join(china_inv))
        file.write("\n" + "Hong Kong invoices: " + ",".join(hong_inv))
        file.write("\n" + "Japan invoices: " + ",".join(japan_inv))
        file.write("\n" + "Korea invoices: " + ",".join(korea_inv))
        file.write("\n" + "Macao invoices: " + ",".join(macao_inv))

# Create tkinter window
root = tk.Tk()
root.title("PDF File Organizer")

# Create and place buttons
select_button = tk.Button(root, text="Select PDF Files", command=process_files)
select_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

root.mainloop()
