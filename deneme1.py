# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deneme1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 560)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uyelik_layou = QtWidgets.QVBoxLayout()
        self.uyelik_layou.setObjectName("uyelik_layou")
        self.lbl_uyelik_sozlesmesi = QtWidgets.QLabel(self.centralwidget)
        self.lbl_uyelik_sozlesmesi.setObjectName("lbl_uyelik_sozlesmesi")
        self.uyelik_layou.addWidget(self.lbl_uyelik_sozlesmesi)
        self.pte_uyelik_kosullar = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pte_uyelik_kosullar.sizePolicy().hasHeightForWidth())
        self.pte_uyelik_kosullar.setSizePolicy(sizePolicy)
        self.pte_uyelik_kosullar.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pte_uyelik_kosullar.setSizeIncrement(QtCore.QSize(0, 200))
        self.pte_uyelik_kosullar.setObjectName("pte_uyelik_kosullar")
        self.uyelik_layou.addWidget(self.pte_uyelik_kosullar)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 250))
        self.groupBox_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.groupBox_2.setBaseSize(QtCore.QSize(0, 0))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.chb_uyelik_onay = QtWidgets.QCheckBox(self.groupBox_2)
        self.chb_uyelik_onay.setObjectName("chb_uyelik_onay")
        self.gridLayout.addWidget(self.chb_uyelik_onay, 0, 0, 1, 1)
        self.btn_yeni_kayit = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_yeni_kayit.setObjectName("btn_yeni_kayit")
        self.gridLayout.addWidget(self.btn_yeni_kayit, 3, 0, 1, 1)
        self.btn_ok = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_ok.setObjectName("btn_ok")
        self.gridLayout.addWidget(self.btn_ok, 4, 0, 1, 1)
        self.lbl_onay_check = QtWidgets.QLabel(self.groupBox_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lbl_onay_check.setPalette(palette)
        self.lbl_onay_check.setText("")
        self.lbl_onay_check.setObjectName("lbl_onay_check")
        self.gridLayout.addWidget(self.lbl_onay_check, 1, 0, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout.addWidget(self.btn_cancel, 5, 0, 1, 1)
        self.lbl_kayit_mesaj = QtWidgets.QLabel(self.groupBox_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lbl_kayit_mesaj.setPalette(palette)
        self.lbl_kayit_mesaj.setAccessibleDescription("")
        self.lbl_kayit_mesaj.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_kayit_mesaj.setText("")
        self.lbl_kayit_mesaj.setTextFormat(QtCore.Qt.PlainText)
        self.lbl_kayit_mesaj.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_kayit_mesaj.setObjectName("lbl_kayit_mesaj")
        self.gridLayout.addWidget(self.lbl_kayit_mesaj, 2, 0, 1, 1)
        self.uyelik_layou.addWidget(self.groupBox_2)
        self.gridLayout_2.addLayout(self.uyelik_layou, 2, 0, 1, 4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_layout = QtWidgets.QVBoxLayout()
        self.label_layout.setObjectName("label_layout")
        self.lbl_ad = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ad.setObjectName("lbl_ad")
        self.label_layout.addWidget(self.lbl_ad)
        self.lbl_soyad = QtWidgets.QLabel(self.centralwidget)
        self.lbl_soyad.setObjectName("lbl_soyad")
        self.label_layout.addWidget(self.lbl_soyad)
        self.lbl_cinsiyet = QtWidgets.QLabel(self.centralwidget)
        self.lbl_cinsiyet.setObjectName("lbl_cinsiyet")
        self.label_layout.addWidget(self.lbl_cinsiyet)
        self.lbl_med_durum = QtWidgets.QLabel(self.centralwidget)
        self.lbl_med_durum.setObjectName("lbl_med_durum")
        self.label_layout.addWidget(self.lbl_med_durum)
        self.lbl_mail = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mail.setObjectName("lbl_mail")
        self.label_layout.addWidget(self.lbl_mail)
        self.lbl_mail_again = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mail_again.setObjectName("lbl_mail_again")
        self.label_layout.addWidget(self.lbl_mail_again)
        self.lbl_password = QtWidgets.QLabel(self.centralwidget)
        self.lbl_password.setObjectName("lbl_password")
        self.label_layout.addWidget(self.lbl_password)
        self.lbl_password_again = QtWidgets.QLabel(self.centralwidget)
        self.lbl_password_again.setObjectName("lbl_password_again")
        self.label_layout.addWidget(self.lbl_password_again)
        self.horizontalLayout.addLayout(self.label_layout)
        self.giris_layout = QtWidgets.QVBoxLayout()
        self.giris_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.giris_layout.setSpacing(0)
        self.giris_layout.setObjectName("giris_layout")
        self.lne_ad = QtWidgets.QLineEdit(self.centralwidget)
        self.lne_ad.setObjectName("lne_ad")
        self.giris_layout.addWidget(self.lne_ad)
        self.lne_soyad = QtWidgets.QLineEdit(self.centralwidget)
        self.lne_soyad.setObjectName("lne_soyad")
        self.giris_layout.addWidget(self.lne_soyad)
        self.frame_cinsiyet = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_cinsiyet.sizePolicy().hasHeightForWidth())
        self.frame_cinsiyet.setSizePolicy(sizePolicy)
        self.frame_cinsiyet.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cinsiyet.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cinsiyet.setObjectName("frame_cinsiyet")
        self.formLayout = QtWidgets.QFormLayout(self.frame_cinsiyet)
        self.formLayout.setObjectName("formLayout")
        self.rdb_erkek = QtWidgets.QRadioButton(self.frame_cinsiyet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rdb_erkek.sizePolicy().hasHeightForWidth())
        self.rdb_erkek.setSizePolicy(sizePolicy)
        self.rdb_erkek.setChecked(True)
        self.rdb_erkek.setObjectName("rdb_erkek")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.rdb_erkek)
        self.rdb_kadin = QtWidgets.QRadioButton(self.frame_cinsiyet)
        self.rdb_kadin.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rdb_kadin.sizePolicy().hasHeightForWidth())
        self.rdb_kadin.setSizePolicy(sizePolicy)
        self.rdb_kadin.setMaximumSize(QtCore.QSize(50, 16777215))
        self.rdb_kadin.setSizeIncrement(QtCore.QSize(0, 0))
        self.rdb_kadin.setBaseSize(QtCore.QSize(0, 0))
        self.rdb_kadin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rdb_kadin.setChecked(False)
        self.rdb_kadin.setObjectName("rdb_kadin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.rdb_kadin)
        self.giris_layout.addWidget(self.frame_cinsiyet)
        self.cmb_med_durum = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_med_durum.sizePolicy().hasHeightForWidth())
        self.cmb_med_durum.setSizePolicy(sizePolicy)
        self.cmb_med_durum.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cmb_med_durum.setDuplicatesEnabled(False)
        self.cmb_med_durum.setObjectName("cmb_med_durum")
        self.cmb_med_durum.addItem("")
        self.cmb_med_durum.addItem("")
        self.giris_layout.addWidget(self.cmb_med_durum)
        self.lne_mail = QtWidgets.QLineEdit(self.centralwidget)
        self.lne_mail.setAutoFillBackground(True)
        self.lne_mail.setText("")
        self.lne_mail.setFrame(True)
        self.lne_mail.setDragEnabled(False)
        self.lne_mail.setReadOnly(False)
        self.lne_mail.setPlaceholderText("")
        self.lne_mail.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lne_mail.setClearButtonEnabled(False)
        self.lne_mail.setObjectName("lne_mail")
        self.giris_layout.addWidget(self.lne_mail)
        self.lne_mail_again = QtWidgets.QLineEdit(self.centralwidget)
        self.lne_mail_again.setObjectName("lne_mail_again")
        self.giris_layout.addWidget(self.lne_mail_again)
        self.lne_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lne_password.setObjectName("lne_password")
        self.giris_layout.addWidget(self.lne_password)
        self.lne_Password_again = QtWidgets.QLineEdit(self.centralwidget)
        self.lne_Password_again.setObjectName("lne_Password_again")
        self.giris_layout.addWidget(self.lne_Password_again)
        self.horizontalLayout.addLayout(self.giris_layout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ErrorMessageBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ErrorMessageBox.sizePolicy().hasHeightForWidth())
        self.ErrorMessageBox.setSizePolicy(sizePolicy)
        self.ErrorMessageBox.setTitle("")
        self.ErrorMessageBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ErrorMessageBox.setObjectName("ErrorMessageBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ErrorMessageBox)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_mail_again_check = QtWidgets.QLabel(self.ErrorMessageBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lbl_mail_again_check.setPalette(palette)
        self.lbl_mail_again_check.setText("")
        self.lbl_mail_again_check.setObjectName("lbl_mail_again_check")
        self.verticalLayout_2.addWidget(self.lbl_mail_again_check)
        spacerItem = QtWidgets.QSpacerItem(20, 85, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.lbl_mail_check = QtWidgets.QLabel(self.ErrorMessageBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lbl_mail_check.setPalette(palette)
        self.lbl_mail_check.setText("")
        self.lbl_mail_check.setObjectName("lbl_mail_check")
        self.verticalLayout_2.addWidget(self.lbl_mail_check)
        self.lbl_name_check = QtWidgets.QLabel(self.ErrorMessageBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lbl_name_check.setPalette(palette)
        self.lbl_name_check.setText("")
        self.lbl_name_check.setObjectName("lbl_name_check")
        self.verticalLayout_2.addWidget(self.lbl_name_check)
        self.lbl_pass_check = QtWidgets.QLabel(self.ErrorMessageBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lbl_pass_check.setPalette(palette)
        self.lbl_pass_check.setText("")
        self.lbl_pass_check.setObjectName("lbl_pass_check")
        self.verticalLayout_2.addWidget(self.lbl_pass_check)
        self.lbl_pass_again_check = QtWidgets.QLabel(self.ErrorMessageBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lbl_pass_again_check.setPalette(palette)
        self.lbl_pass_again_check.setText("")
        self.lbl_pass_again_check.setObjectName("lbl_pass_again_check")
        self.verticalLayout_2.addWidget(self.lbl_pass_again_check)
        self.verticalLayout.addWidget(self.ErrorMessageBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 20)
        self.horizontalLayout.setStretch(1, 20)
        self.horizontalLayout.setStretch(2, 60)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 21))
        self.menubar.setObjectName("menubar")
        self.menuDosya = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        self.menuGorunum = QtWidgets.QMenu(self.menubar)
        self.menuGorunum.setObjectName("menuGorunum")
        self.menuYardim = QtWidgets.QMenu(self.menubar)
        self.menuYardim.setObjectName("menuYardim")
        self.menuHakkinda = QtWidgets.QMenu(self.menuYardim)
        self.menuHakkinda.setObjectName("menuHakkinda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.act_yeni_kayit = QtWidgets.QAction(MainWindow)
        self.act_yeni_kayit.setObjectName("act_yeni_kayit")
        self.act_kaydet = QtWidgets.QAction(MainWindow)
        self.act_kaydet.setObjectName("act_kaydet")
        self.act_cikis = QtWidgets.QAction(MainWindow)
        self.act_cikis.setObjectName("act_cikis")
        self.act_yakinlastir = QtWidgets.QAction(MainWindow)
        self.act_yakinlastir.setObjectName("act_yakinlastir")
        self.act_uyg_bilgisi = QtWidgets.QAction(MainWindow)
        self.act_uyg_bilgisi.setObjectName("act_uyg_bilgisi")
        self.act_uzaklastir = QtWidgets.QAction(MainWindow)
        self.act_uzaklastir.setObjectName("act_uzaklastir")
        self.menuDosya.addAction(self.act_yeni_kayit)
        self.menuDosya.addAction(self.act_kaydet)
        self.menuDosya.addAction(self.act_cikis)
        self.menuGorunum.addAction(self.act_yakinlastir)
        self.menuGorunum.addAction(self.act_uzaklastir)
        self.menuHakkinda.addAction(self.act_uyg_bilgisi)
        self.menuYardim.addAction(self.menuHakkinda.menuAction())
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuGorunum.menuAction())
        self.menubar.addAction(self.menuYardim.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_uyelik_sozlesmesi.setText(_translate("MainWindow", "Uyelik Sozlesmesi"))
        self.pte_uyelik_kosullar.setPlainText(_translate("MainWindow", "Genel Koşullar\n"
"\n"
"Bu bölüm Kariyer.net\'in genel ve kanuni sorumluluklarını içerir. Lütfen, sitemizi kullanmadan önce aşağıda yazılı olanları dikkatli bir şekilde okuyunuz. Eğer aşağıda belirtilen şartları kısmen ve/veya tamamen kabul etmiyorsanız, Kariyer.net\'i herhangi bir amaçla kullanmayınız.\n"
"\n"
"Kariyer.net, bu sayfalarda belirtilen genel koşulları dilediği zaman ve şekilde değiştirme hakkını kendinde saklı tutar. Kariyer.net\'in www.kariyer.net adresini ziyaret ettiğinizde bu sayfayı da ziyaret etmeniz gerekmektedir. Bu nedenle www.kariyer.net adresini ziyaret ettiğinizde bu sayfayı da ziyaret ettiğiniz kabul edilir.\n"
"\n"
"Kopyalama\n"
"\n"
"Kariyer.net ticari amaçlarla olmamak koşulu ve sadece kendiniz tarafından kullanılmak şartı ile bir kereye mahsus olmak üzere, sitede belirtilen bilgilerin kopyalanmasına izin verir.\n"
"\n"
"Kariyer.net\'in içeriğinde yer alan bütün bilgilerin, yazıların, logoların, grafiklerin ve bunlarla sınırlı olmamak üzere her türlü görsel ve resimlerin her hakkı saklıdır. İzinsiz kullanılamaz. Bu sitede yer alan herhangi bir unsuru diğer bir internet sitesinde ve/veya başka bir mecrada yazılı, sözlü ve/veya elektronik olarak ve bunlarla sınırlı olmamak üzere her türlü şekilde yayınlamak ve/veya Kariyer.net\'in haberi olmadan link vermek kesinlikle yasaktır.\n"
"\n"
"Ayrıca bu sayfaların tasarımında ve veritabanı oluşturulmasında kullanılan bilgi ve/veya yazılımın kopyalanması ve/veya kullanılması kesinlikle yasaktır.\n"
"\n"
"Sitede bulunan yazılım, görsel ve tasarımların her türlü hakkı Kariyer.net\'e aittir.\n"
"\n"
"Kullanım\n"
"\n"
"Bu site herkese açıktır. Yalnızca aşağıdaki hallerde, Kariyer.net sitenin kullanımını geçici ve/veya sürekli olarak engelleyebilir:\n"
"Yanlış, düzensiz, eksik ve/veya yanıltıcı bilgi ve/veya uygun olmayan fotoğraf içeren özgeçmişin siteye kaydedilmesi halinde,\n"
"Özgeçmiş dışı bilgilerin; özel ve/veya genel duyuruların, reklam amaçlı firma bilgilerinin ve/veya üyelik satış formasyonları gibi bilgilerin ilave edilmesi halinde,\n"
"Diğer bir şahıs ve/veya kurum tarafından ilan edilen her türlü bilgi, görsel ve/veya logonun silinmesi tahrif edilmesi ve/veya değiştirilmesi halinde,\n"
"Internet Sitesi Güvenlik Kuralları\n"
"\n"
"Belirtilen güvenlik kurallarına kısmen ve/veya tamamen uyulmaması halinde ya da kasıtlı veya kasıtsız olarak aşağıda belirtilenlerden herhangi birini yapan kişi, kişiler ve/veya kurum, kurumlar hakkında Kariyer.net\'in her türlü kanuni hakkı saklıdır.\n"
"Kullanıcıların diğer özgeçmiş bilgilerine girme çabaları ve/veya sitenin genel güvenliğini tehdit edecek her türlü doğrudan ve/veya dolaylı çalışmalar,\n"
"Sitede kullanılan yazılımların çalışmasını engelleyebilecek her türlü doğrudan ve/veya dolaylı faaliyetler,\n"
"Virüs vasıtası ile sitenin çalışmasına engel olma,\n"
"Sitenin genel kurallarına uygun olmayan her türlü elektronik postanın yollanması ve/veya sitenin kilitlenmesini sağlama amacıyla aynı anda oldukça fazla ticari ve/veya kişisel elektronik postanın yollanması gibi.\n"
"Kariyer.net\'in Sorumlulukları;\n"
"\n"
"Kariyer.net, site üzerinde yer alan firma ve aday bilgilerinin içeriğinden hiçbir şekilde sorumlu tutulamaz. Bu sitede yer alan bilgilerle ilgili her türlü risk kullanıcılara aittir. Site üzerinde önceden herhangi bir haber vermeye gerek duyulmadan, istediği değişiklikleri yapma hakkı bizzat Kariyer.net\'e aittir.\n"
"\n"
"Özgeçmişini sitede bulunduran kullanıcı; özgeçmişinde bulunan her türlü bilginin tek sorumlusudur.\n"
"\n"
"Kariyer.net bir işveren değildir; sitede yer alan özgeçmişler Kariyer.net\'in sorumluluğu altında yer almamaktadır. İşveren firma ile kendi vasıtasıyla ilişkiye geçen özgeçmiş sahibi, bütün sorumluluğu üzerine almış olur.\n"
"\n"
"Kariyer.net, sitenin yazılımının her türlü hatadan arınmış olduğunu ve sitede herhangi bir virüs yer alıp almadığı konusunda herhangi bir sorumluluk yüklenmemektedir. Eğer bu sitede yer alan herhangi bir yazılım sebebi ile kullandığınız yazılım ve/veya donanım unsurlarına herhangi bir zarar gelirse firmamız bu konuda hiçbir sorumluluk yüklenmez.\n"
"\n"
"Bu sitede bulunan internet bağlantıları (linkler) ile ilgili her türlü risk kullanıcıya aittir. Kariyer.net özgeçmişinize bağlı olan bütün bilgileri kendi pazarlama faaliyetleri ile ilgili olarak kullanma hakkına sahiptir.\n"
"\n"
"Kariyer.net\'i tercih ederek bize gösterdiğiniz ilgi ve güven için çok teşekkür ederiz."))
        self.groupBox_2.setTitle(_translate("MainWindow", "Onay"))
        self.chb_uyelik_onay.setText(_translate("MainWindow", "Okudum Onayladim"))
        self.btn_yeni_kayit.setText(_translate("MainWindow", "YENI KAYIT"))
        self.btn_ok.setText(_translate("MainWindow", "KAYDET"))
        self.btn_cancel.setText(_translate("MainWindow", "CIKIS"))
        self.lbl_ad.setText(_translate("MainWindow", "Ad       :"))
        self.lbl_soyad.setText(_translate("MainWindow", "Soyad :"))
        self.lbl_cinsiyet.setText(_translate("MainWindow", "Cınsıyet"))
        self.lbl_med_durum.setText(_translate("MainWindow", "Medeni Durum :"))
        self.lbl_mail.setText(_translate("MainWindow", "Mail"))
        self.lbl_mail_again.setText(_translate("MainWindow", "Mail (Tekrar)"))
        self.lbl_password.setText(_translate("MainWindow", "Password"))
        self.lbl_password_again.setText(_translate("MainWindow", "Password Tekrar"))
        self.rdb_erkek.setText(_translate("MainWindow", "Erkek"))
        self.rdb_kadin.setText(_translate("MainWindow", "Kadin"))
        self.cmb_med_durum.setItemText(0, _translate("MainWindow", "Evli"))
        self.cmb_med_durum.setItemText(1, _translate("MainWindow", "Bekar"))
        self.menuDosya.setTitle(_translate("MainWindow", "Dosya"))
        self.menuGorunum.setTitle(_translate("MainWindow", "Gorunum"))
        self.menuYardim.setTitle(_translate("MainWindow", "Yardim"))
        self.menuHakkinda.setTitle(_translate("MainWindow", "Hakkinda"))
        self.act_yeni_kayit.setText(_translate("MainWindow", "Yeni Kayit"))
        self.act_yeni_kayit.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.act_kaydet.setText(_translate("MainWindow", "Kaydet"))
        self.act_kaydet.setShortcut(_translate("MainWindow", "Ctrl+K"))
        self.act_cikis.setText(_translate("MainWindow", "Cikis"))
        self.act_cikis.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.act_yakinlastir.setText(_translate("MainWindow", "Yakinlastir"))
        self.act_yakinlastir.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.act_uyg_bilgisi.setText(_translate("MainWindow", "Uygulama Bilgisi"))
        self.act_uzaklastir.setText(_translate("MainWindow", "Uzaklastir"))
        self.act_uzaklastir.setShortcut(_translate("MainWindow", "Ctrl+U"))
