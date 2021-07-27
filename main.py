import Webhook
import sys
import timeit

class Enrollment:

    def display(self):
        start = timeit.default_timer()
        app = Webhook.QtWidgets.QApplication(sys.argv)
        Dialog = Webhook.QtWidgets.QDialog()
        ui = Webhook.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        stop = timeit.default_timer()
        print("Time: %s" %(stop - start))
        sys.exit(app.exec_())

E = Enrollment()
E.display()
