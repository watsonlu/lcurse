from PyQt4 import Qt

WOW_FOLDER_KEY = "Preferences/wowfolder"
WOW_FOLDER_DEFAULT = "%s/.wine/drive_c/Program Files (x86)/World of Warcraft" % (Qt.QDir.homePath()) 

LCURSE_ADDONS = "%s/.lcurse/addons.json" % (Qt.QDir.homePath())