import Webhook, sys

class Enrollment:

    def display(self):
        app = Webhook.QtWidgets.QApplication(sys.argv)
        Dialog = Webhook.QtWidgets.QDialog()
        ui = Webhook.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
        
E = Enrollment()
E.display()
