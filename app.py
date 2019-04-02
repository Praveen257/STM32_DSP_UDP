#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from tuning import Ui_TuningUI
import subprocess,shlex
import numpy as np
import socket
from struct import *
import pyqtgraph as pg
import os
import subprocess
import matplotlib.pyplot as plt


PRESCALAR_DEFLT = [("ADC_CLOCK_ASYNC_DIV6",6),("ADC_CLOCK_ASYNC_DIV8",8),("ADC_CLOCK_ASYNC_DIV10",10),("ADC_CLOCK_ASYNC_DIV12",12),("ADC_CLOCK_ASYNC_DIV16",16),("ADC_CLOCK_ASYNC_DIV32",32),("ADC_CLOCK_ASYNC_DIV64",64),("ADC_CLOCK_ASYNC_DIV128",128),("ADC_CLOCK_ASYNC_DIV256",256)]
TIMEST_DEF = [("ADC_SAMPLETIME_1CYCLES_5",1.5),("ADC_SAMPLETIME_2CYCLES_5",2.5),("ADC_SAMPLETIME_8CYCLES_5",8.5),("ADC_SAMPLETIME_16CYCLES_5",16.5),("ADC_SAMPLETIME_32CYCLES_5",32.5),("ADC_SAMPLETIME_64CYCLES_5",64.5),("ADC_SAMPLETIME_387CYCLES_5",387.5),("ADC_SAMPLETIME_810CYCLES_5",810.5)]
RESOL_CONVTIME = [8.5,10.5,12.5,14.5,16.5]
ADC_CLOCK1 = 152
ADC_CLOCK2 = 64
CONVTIME = 16.5

PC_ADDR = "192.168.0.11"
UDP_IP_ADDR = "192.168.0.10"
MESSAGE = "SF_20Khz"
UDP_PORT = 7
UDP_PORT_SEND = 8
SIZE = 4096	
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

flag_thread1 = 0;
newval = []

class AppWindow(QDialog):

	SamplingFreqvalue = 10;
	fftvalue = 1024;
	bdfeat = []
	apfeat = []
	SF1 = []
	SF2 = []
	a = []
	q = [1,2,3,4,5]
	usr_sfval = 0
	bool_timsel = 0
	sig1 = pyqtSignal([list]) #signal for comm b/w thread and app
	global flag_thread1
	global PC_ADDR
	global UDP_IP_ADDR
	global UDP_PORT
	global SIZE
	global sock
	global MESSAGE
	flag_gen_err = 0;
	flag_req_sf_err = 1;

	def __init__(self):
		super().__init__()
		self.ui = Ui_TuningUI()
		self.ui.setupUi(self)
		self.ui.radioButton.clicked.connect(self.on_radio_btn_tgd)
		self.ui.radioButton_2.clicked.connect(self.on_radio_btn_tgd)
		self.ui.radioButton_3.clicked.connect(self.on_radio_btn_tgd)
		self.ui.radioButton_4.clicked.connect(self.on_radio_btn_tgd)
		self.ui.radioButton_5.clicked.connect(self.on_radio_btn_tgd)
		self.ui.radioButton_6.clicked.connect(self.on_radio_btn_tgd)
		self.ui.checkBox_2.toggled.connect(self.on_chkbox_hw_toggled)
		self.ui.checkBox_3.toggled.connect(self.on_chkbox_hw_toggled)
		self.ui.checkBox_4.toggled.connect(self.on_chkbox_hw_toggled)
		self.ui.checkBox_5.toggled.connect(self.on_chkbox_hw_toggled)
		self.ui.checkBox_7.toggled.connect(self.on_chkbox_app_toggled)
		self.ui.checkBox_8.toggled.connect(self.on_chkbox_app_toggled)
		self.ui.pushButton_6.clicked.connect(self.on_start_clkd)
		self.ui.checkBox_9.toggled.connect(self.on_chkbox_app_toggled)
		self.ui.radioButton_7.clicked.connect(self.on_fft_size_clkd)
		self.ui.radioButton_8.clicked.connect(self.on_fft_size_clkd)
		self.ui.radioButton_9.clicked.connect(self.on_fft_size_clkd)
		self.ui.pushButton_7.clicked.connect(self.on_compl_clkd)
		#self.ui.radioButton_10.clicked.connect(self.on_tim_sel_clkd)
		#self.ui.radioButton_11.clicked.connect(self.on_tim_sel_clkd)
		self.thread = Worker()
		self.thread.sig1.connect(self.dispGraph)
		self.ui.pushButton.clicked.connect(self.on_quit_clkd)
		self.ui.pushButton_2.clicked.connect(self.on_gen_clkd)
		self.ui.pushButton_3.clicked.connect(self.on_flsh_clkd)
		self.ui.pushButton_4.clicked.connect(self.on_visual_start)
		self.ui.pushButton_5.clicked.connect(self.on_visual_stop)
		self.ui.pushButton_8.clicked.connect(self.on_update_sf_send)
		self.ui.pushButton_9.clicked.connect(self.on_reset_sf_send)
		self.ui.pushButton_11.clicked.connect(self.on_sw_reset_send)
		self.ui.pushButton_12.clicked.connect(self.on_boot_mode_send)
		self.ui.pushButton_2.setEnabled(True)
		self.ui.pushButton_3.setEnabled(True)
		self.ui.pushButton_3.setEnabled(True)
		self.show()


	def on_sw_reset_send(self):
		sock.sendto(b'bootoff',(UDP_IP_ADDR,UDP_PORT_SEND))
	
	def on_boot_mode_send(self):
		sock.sendto(b'booton',(UDP_IP_ADDR,UDP_PORT_SEND))
		
	def on_start_clkd(self):
		#QMessageBox.about(self,"INFORMATION","Not Implemented")
		a = subprocess.call(['fr.ac6.mcu.externaltools.openocd.linux64_1.21.0.201811131241/tools/openocd/bin/openocd','-f', 'trial_softwareRun.cfg', '-f' ,'start_run.cfg','-f','fr.ac6.mcu.debug_2.3.1.201811131241/resources/openocd/st_scripts/target/stm32h7x.cfg','-f','fr.ac6.mcu.debug_2.3.1.201811131241/resources/openocd/st_scripts/target/swj-dp.tcl'])
		print ("s")
		if a != 0:
			QMessageBox.about(self,"Error","Flash Error")
		else:
			QMessageBox.about(self,"INFORMATION","Target Running")


	def on_update_sf_send(self):
		str = []

		if self.usr_sfval == 0:

			if self.SamplingFreqvalue == 10:
				sock.sendto(b'SF_10Khz',(UDP_IP_ADDR,UDP_PORT_SEND))
			elif self.SamplingFreqvalue == 20:
				sock.sendto(b'SF_20Khz',(UDP_IP_ADDR,UDP_PORT_SEND))
			elif self.SamplingFreqvalue == 30:
				sock.sendto(b'SF_30Khz',(UDP_IP_ADDR,UDP_PORT_SEND))
			elif self.SamplingFreqvalue == 40:
				sock.sendto(b'SF_40Khz',(UDP_IP_ADDR,UDP_PORT_SEND))
			elif self.SamplingFreqvalue == 60:
				sock.sendto(b'SF_50Khz',(UDP_IP_ADDR,UDP_PORT_SEND))

	def on_reset_sf_send(self):
		sock.sendto(b'SF_20Khz',(UDP_IP_ADDR,UDP_PORT_SEND))
	def on_compl_clkd(self):
		'''	The Make commands have to be monitored and signal if there is an error and disable buttons'''
		a = subprocess.call(['make clean'],shell = True , stderr=subprocess.STDOUT)
		a = subprocess.call(['make'])
		if a!= 0:
			QMessageBox.about(self,"Error","Compilation error , Re check the parameters")
		else:
			QMessageBox.about(self,"INFORMATION","Compilation Successful")
			self.ui.pushButton_3.setEnabled(True)
			self.ui.pushButton_3.setEnabled(True)

	def on_flsh_clkd(self):
		a = subprocess.call(['fr.ac6.mcu.externaltools.openocd.linux64_1.21.0.201811131241/tools/openocd/bin/openocd','-f', 'trial_softwareRun.cfg', '-f' ,'blink.cfg','-f','fr.ac6.mcu.debug_2.3.1.201811131241/resources/openocd/st_scripts/target/stm32h7x.cfg','-f','fr.ac6.mcu.debug_2.3.1.201811131241/resources/openocd/st_scripts/target/swj-dp.tcl'])
		if a != 0:
			QMessageBox.about(self,"Error","Flash Error")
		else:
			QMessageBox.about(self,"INFORMATION","Flash Successful")


	def dispGraph(self,val):
		newval = []
		self.ui.graphicsView.clear()
		self.ui.graphicsView.plot(val[0:len(val)],pen = (255,255,255))



	def rbn_clicked(self):
		print("button Clicked")

	def on_radio_btn_tgd(self):
		if self.ui.radioButton.isChecked():
			self.SamplingFreqvalue = 10
			self.usr_sfval = 0
		elif self.ui.radioButton_2.isChecked():
			self.SamplingFreqvalue = 20
			self.usr_sfval = 0
		elif self.ui.radioButton_3.isChecked():
			self.SamplingFreqvalue = 30
			self.usr_sfval = 0
		elif self.ui.radioButton_4.isChecked():
			self.SamplingFreqvalue = 40
			self.usr_sfval = 0
		elif self.ui.radioButton_5.isChecked():
			self.SamplingFreqvalue = 60
			self.usr_sfval = 0
		elif self.ui.radioButton_6.isChecked():
			self.ui.lineEdit.setReadOnly(False)
			self.SamplingFreqvalue = int(self.ui.lineEdit.text())
			self.usr_sfval = 1

		print (self.SamplingFreqvalue)

	def on_chkbox_hw_toggled(self):
		if self.ui.checkBox_2.isChecked() ==  True:
			if ("UART_ENABLE" in self.bdfeat) == False:
				self.bdfeat.append("UART_ENABLE")
		else:
			if ("UART_ENABLE" in self.bdfeat) == True:
				self.bdfeat.remove("UART_ENABLE")

		if self.ui.checkBox_3.isChecked() ==  True:
			if ("I2C_ENABLE" in self.bdfeat) == False:
				self.bdfeat.append("I2C_ENABLE")
		else:
			if ("I2C_ENABLE" in self.bdfeat) == True:
				self.bdfeat.remove("I2C_ENABLE")

		if self.ui.checkBox_4.isChecked() ==  True:
			if ("DEBUG_ENABLE" in self.bdfeat) == False:
				self.bdfeat.append("DEBUG_ENABLE")
		else:
			if ("DEBUG_ENABLE" in self.bdfeat) == True:
				self.bdfeat.remove("DEBUG_ENABLE")

		if self.ui.checkBox_5.isChecked() ==  True:
			if ("USB_ENABLE" in self.bdfeat) == False:
				self.bdfeat.append("USB_ENABLE")
		else:
			if ("USB_ENABLE" in self.bdfeat) == True:
				self.bdfeat.remove("USB_ENABLE")
		print (self.bdfeat)

	def on_chkbox_app_toggled(self):
		if self.ui.checkBox_7.isChecked() == True :
			if ("WFE_ENABLE" in self.apfeat) == False :
				self.apfeat.append("WFE_ENABLE")
		else:
			if ("WFE_ENABLE" in self.apfeat) == True :
				self.apfeat.remove("WFE_ENABLE")

		if self.ui.checkBox_8.isChecked() == True :
			if ("ANC_ENABLE" in self.apfeat) == False :
				self.apfeat.append("ANC_ENABLE")
		else:
			if ("ANC_ENABLE" in self.apfeat) == True :
				self.apfeat.remove("ANC_ENABLE")

		if self.ui.checkBox_9.isChecked() == True :
			if ("HARMONICDETECT_ENABLE" in self.apfeat) == False :
				self.apfeat.append("HARMONICDETECT_ENABLE")
		else:
			if ("HARMONICDETECT_ENABLE" in self.apfeat) == True :
				self.apfeat.remove("HARMONICDETECT_ENABLE")
		print ("Selected Values : %s " %(" ".join(self.apfeat)))

	def on_fft_size_clkd(self):
		if self.ui.radioButton_7.isChecked():
			self.fftvalue = 1024
		elif self.ui.radioButton_8.isChecked():
			self.fftvalue = 2048
		elif self.ui.radioButton_9.isChecked():
			self.fftvalue = 2048

	def on_tim_sel_clkd(self):
		if self.ui.radioButton_10.isChecked():
			self.bool_timsel = 0;
			self.lineEdit_6.readOnly(True)
		elif self.ui.radioButton_8.isChecked():
			self.bool_timsel = 1;
			self.lineEdit_6.readOnly(False)

	def on_gen_clkd(self):
		self.gen_param_file()
		#QMessageBox.about(self,"INFORMATION","Yet to be implemented")



	def on_visual_start(self):
		#self.ui.lineEdit_5.readOnly(True)
		self.ui.pushButton_5.setEnabled(True)
		self.ui.pushButton_4.setEnabled(False)
		flag_thread1 = 1
		self.thread.start() #start the background udp read thread"

	def on_visual_stop(self):
		if self.thread.isRunning()==True :
			flag_thread1 = 0
			self.thread.terminate()
			self.ui.pushButton_5.setEnabled(False)
			self.ui.pushButton_4.setEnabled(True)
		else:
			QMessageBox.about(self,"INFORMATION","Thread not running")


	def on_quit_clkd(self):
		flag_thread1 = 0
		self.thread.terminate()
		sys.exit()


	def gen_param_file(self):
		f = open("Inc/feature.h","w+")
		f.write("#ifndef __FEATURE_H \n")
		f.write("#define __FEATURE_H \n \n")
		rbtn = self.sender()
        #if rbtn.isChecked():
		if self.usr_sfval == 0:
			if self.SamplingFreqvalue == 10:
				f.write("#define PRESCALAR_VALUE ADC_CLOCK_ASYNC_DIV16 \n")
				f.write("#define SAMPLING_TIME ADC_SAMPLETIME_387CYCLES_5 \n")
			elif self.SamplingFreqvalue == 20:
				f.write("#define PRESCALAR_VALUE ADC_CLOCK_ASYNC_DIV8 \n")
				f.write("#define SAMPLING_TIME ADC_SAMPLETIME_387CYCLES_5 \n")
			elif self.SamplingFreqvalue == 30:
				f.write("#define PRESCALAR_VALUE ADC_CLOCK_ASYNC_DIV128 \n")
				f.write("#define SAMPLING_TIME ADC_SAMPLETIME_8CYCLES_5 \n")
			elif self.SamplingFreqvalue == 40:
				f.write("#define PRESCALAR_VALUE ADC_CLOCK_ASYNC_DIV64 \n")
				f.write("#define SAMPLING_TIME ADC_SAMPLETIME_16CYCLES_5 \n")
			elif self.SamplingFreqvalue == 50:
				f.write("#define PRESCALAR_VALUE ADC_CLOCK_ASYNC_DIV32 \n")
				f.write("#define SAMPLING_TIME ADC_SAMPLETIME_32CYCLES_5 \n")

		elif self.usr_sfval == 1:
			reqsfval = self.ui.lineEdit.text()
			for pdtxt,pdval in PRESCALAR_DEFLT:
				for sttxt,stval in TIMEST_DEF:
					sfval =  1000/((stval+CONVTIME)/(ADC_CLOCK1/pdval))
					sfvalrd = round(sfval,0)

					if int(sfvalrd) >= int(reqsfval) and int(reqsfval)+10 >= int(sfvalrd) :

						print ("found")
						print (sfvalrd,sttxt,pdtxt)
						print (int(sfvalrd) - int(reqsfval))
						f.write("#define PRESCALAR_VALUE %s \n" %sttxt)
						f.write("#define SAMPLING_TIME %s \n" %pdtxt)
						QMessageBox.about(self,"INFORMATION","chosen approx sampling freq %d" %sfvalrd)
						self.flag_req_sf_err = 0
						break
						break

			if self.flag_req_sf_err != 0:
				self.flag_gen_err = 1

		f.write("#define FFTSIZE %d \n \n" %self.fftvalue)
		#generate IP address
		ipadr = self.ui.lineEdit_3.text()
		ad1 = []
		iterate = 0
		for x in ipadr:
			if x != '.' and x != '\n':
				ad1.append(x)
			else:
				str1 = ''.join(ad1)
				f.write('#define IP_ADDR{} {} \n' .format(iterate,str1))
				ad1 = []
				iterate = iterate+1
		str1 = ''.join(ad1)
		f.write('#define IP_ADDR{} {} \n \n' .format(iterate,str1))

		gwadr = self.ui.lineEdit_8.text()
		ad1 = []
		iterate = 0
		for x in gwadr:
			if x != '.' and x != '\n':
				ad1.append(x)
			else:
				str1 = ''.join(ad1)
				f.write('#define GW_ADDR{} {} \n' .format(iterate,str1))
				ad1 = []
				iterate = iterate+1
		str1 = ''.join(ad1)
		f.write('#define GW_ADDR{} {} \n \n' .format(iterate,str1))

		dtaddr = self.ui.lineEdit_9.text()
		ad1 = []
		iterate = 0
		for x in dtaddr:
			if x != '.' and x != '\n':
				ad1.append(x)
			else:
				str1 = ''.join(ad1)
				f.write('#define DEST_ADDR{} {} \n' .format(iterate,str1))
				ad1 = []
				iterate = iterate+1
		str1 = ''.join(ad1)
		f.write('#define DEST_ADDR{} {} \n \n' .format(iterate,str1))


		nmadr = self.ui.lineEdit_7.text()
		ad1 = []
		iterate = 0
		for x in nmadr:
			if x != '.' and x != '\n':
				ad1.append(x)
			else:
				str1 = ''.join(ad1)
				f.write('#define NETMASK_ADDR{} {} \n' .format(iterate,str1))
				ad1 = []
				iterate = iterate+1
		str1 = ''.join(ad1)
		f.write('#define NETMASK_ADDR{} {} \n \n' .format(iterate,str1))

		srcport = self.ui.lineEdit_4.text()
		f.write('#define SOURCE_PORT %s\n' %srcport)

		dstport = self.ui.lineEdit_10.text()
		f.write('#define DEST_PORT %s\n' %srcport)

		for txt in self.bdfeat:
			if txt != "" or txt != Null:
				f.write('#define %s \n \n' %txt)

		for nt in self.apfeat:
			if txt != ""  or txt != Null:
				f.write('#define %s \n \n' %nt)

		f.write('\n#endif \n')
		f.close()
		if self.flag_gen_err !=1:
			QMessageBox.about(self,"INFORMATION","Generated successfully")
			self.ui.pushButton_2.setEnabled(True)
			self.ui.pushButton_3.setEnabled(True)
			self.ui.pushButton_3.setEnabled(False)
		else:
			QMessageBox.about(self,"INFORMATION","Problem in generation")
'''
Class to run the UDP Server to receive the data packets from the STM port


'''
class Worker(QThread):
	global PC_ADDR
	global UDP_IP_ADDR
	global UDP_PORT
	global SIZE
	global flag_thread1
	global sock
	a = []
	sig1 = pyqtSignal([list])

	def __init__(self,parent = None):

		QThread.__init__(self,parent)
		self.exiting =  False
		sock.bind((PC_ADDR,UDP_PORT))
		print ("connected")


	def run(self):
		print ("connected")
		while True:
			print ("connected")
			data = sock.recvfrom(SIZE)
			data = data[0]
			print (len(data))
			iph = unpack('!1024B',data)
			newval = self.conv_8to16bit(iph)
			self.sig1.emit(newval)

	def conv_8to16bit(self,val):
		b = []
		for i in range(0,len(val)-1,2):
			b.append(val[i+1]<<8 | val[i])
		return b
app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
