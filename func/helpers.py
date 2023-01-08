from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def add_product_frame(scrollAreaWidgetLayout, scrollAreaWidget):
	# Count widgets in scrollAreaWidgetLayout
	count = scrollAreaWidgetLayout.count() - 1
	# Style product frame widgets
	product_frame = QtWidgets.QFrame(scrollAreaWidget)
	sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
	sizePolicy.setHorizontalStretch(0)
	sizePolicy.setVerticalStretch(0)
	sizePolicy.setHeightForWidth(product_frame.sizePolicy().hasHeightForWidth())
	product_frame.setSizePolicy(sizePolicy)
	product_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
	font = QtGui.QFont()
	font.setFamily("Century Gothic")
	font.setPointSize(10)
	font.setBold(False)
	font.setWeight(50)
	product_frame.setFont(font)
	product_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
	product_frame.setFrameShadow(QtWidgets.QFrame.Raised)
	product_frame.setObjectName("product_frame")
	product_frame_horizontalLayout = QtWidgets.QHBoxLayout(product_frame)
	product_frame_horizontalLayout.setObjectName("product_frame_horizontalLayout")
	product_label = QtWidgets.QLabel(product_frame)
	sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
	sizePolicy.setHorizontalStretch(0)
	sizePolicy.setVerticalStretch(0)
	sizePolicy.setHeightForWidth(product_label.sizePolicy().hasHeightForWidth())
	product_label.setSizePolicy(sizePolicy)
	product_label.setMaximumSize(QtCore.QSize(16777215, 30))
	font = QtGui.QFont()
	font.setFamily("Century Gothic")
	font.setPointSize(10)
	font.setBold(True)
	font.setWeight(75)
	product_label.setFont(font)
	product_label.setObjectName("product_label")
	product_frame_horizontalLayout.addWidget(product_label)
	product_name_textBrowser = QtWidgets.QTextBrowser(product_frame)
	sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
	sizePolicy.setHorizontalStretch(0)
	sizePolicy.setVerticalStretch(0)
	sizePolicy.setHeightForWidth(product_name_textBrowser.sizePolicy().hasHeightForWidth())
	product_name_textBrowser.setSizePolicy(sizePolicy)
	product_name_textBrowser.setMaximumSize(QtCore.QSize(16777215, 24))
	font = QtGui.QFont()
	font.setFamily("Century Gothic")
	font.setPointSize(10)
	font.setBold(False)
	font.setWeight(50)
	product_name_textBrowser.setFont(font)
	product_name_textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
	product_name_textBrowser.setDocumentTitle("")
	product_name_textBrowser.setReadOnly(False)
	product_name_textBrowser.setObjectName("product_name_textBrowser")
	product_frame_horizontalLayout.addWidget(product_name_textBrowser)
	_translate = QtCore.QCoreApplication.translate
	product_label.setText(_translate("MainWindow", f"Product {count + 1}"))
	product_name_textBrowser.setPlaceholderText(_translate("MainWindow", "Enter the product name"))
	# Add product_frame widget to scrollAreaWidgetLayout
	scrollAreaWidgetLayout.addWidget(product_frame)

def remove_product_frame(scrollAreaWidgetLayout):
	# Count widgets in scrollAreaWidgetLayout
	count = scrollAreaWidgetLayout.count()
	# If there are more than two widgets (first product_frame and verticalSpacer), remove the last widget
	if count > 2:
		item = scrollAreaWidgetLayout.itemAt(count - 1)
		widget = item.widget()
		widget.deleteLater()
	else:
		return

def wait_for_element(driver, xpath, timeout=20):
	locator = (By.XPATH, xpath)
	element_located = EC.visibility_of_element_located(locator)
	wait = WebDriverWait(driver, timeout)
	return wait.until(element_located)