def verify_libs():
    required = {'pyqt5', 'pyqtgraph'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

def start():
    create_window()


def create_window():
    app = QApplication(sys.argv)
    win = Interface()
    win.addButton("limpar tela", [50, 50], win.clear_screen)
    win.addLabel("label automatico", [50, 100])
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    try:
        from interface import Interface
        from functions import *
        import sys, subprocess, pkg_resources
        verify_libs()
        from PyQt5 import QtWidgets
        from PyQt5.QtWidgets import *
        import pyqtgraph as pg
        start()
    except Exception as e:
        print("Não foi possível importar as bibliotecas básicas")
        print(e)