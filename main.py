import Webhook
import sys
import tkinter as tk

try:
    total1 = Webhook.total(method=1)
    Webhook.uploaded_documents()
    tk.messagebox.showerror("%s uploaded documents pulled." %(total1), "Complete!")

    total2 = Webhook.total(method=2)
    Webhook.fee_documents()
    tk.messagebox.showerror("%s fee documents pulled." %(total2), "Complete!")
except ValueError:
    tk.messagebox.showerror("ValueError encountered at entry %s. %s" %(len(Webhook.IDs), sys.exc_info()[1]), "Warning!")
    pass
except TypeError:
    tk.messagebox.showerror("TypeError encountered at entry %s. %s" %(len(Webhook.IDs), sys.exc_info()[1]), "Warning!")
    pass
except:
    tk.messagebox.showerror("Something terrible occurred at entry %s. %s, %s" %(len(Webhook.IDs), sys.exc_info()[0], sys.exc_info()[1]), "Warning!")
    pass
