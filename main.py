import Webhook
import sys
import tkinter as tk
import pymsgbox

try:
    upload_total = Webhook.total(method=1)
    Webhook.uploaded_documents()

    fee_total = Webhook.total(method=2)
    Webhook.fee_documents()

    pymsgbox.alert(f"{upload_total+fee_total} documents pulled.\n{upload_total} upload and {fee_total} fee.", "Complete!")
except BaseException as b:
    tk.messagebox.showerror("Something terrible occurred at entry %s. %s, %s" %(len(Webhook.IDs), sys.exc_info()[0], sys.exc_info()[1]), "Warning!")
