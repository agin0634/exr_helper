import os
import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import OpenEXR
import Imath
import logging
import time
import re
from mainUI import Ui_MainWindow
from pathlib import Path
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QObject, QThread, QTimer, pyqtSignal

class App():
    def removeAlpha(in_path, fileName, out_path):
        try:
            golden = OpenEXR.InputFile(in_path)
            check = len(golden.channel('R'))
            (a, r, g, b) = golden.channels('ARGB')
            exr = OpenEXR.OutputFile(out_path + '\\' + fileName, golden.header())
            exr.writePixels({'R': r, 'G': g, 'B': b})
            logging.warning(fileName +' write succeeded.')
            return True
        except Exception as e:
            logging.warning(fileName +' write failed.' )
            return False

    def exrChecker(file, bCheckR, bCheckG, bCheckB, bCheckA):
        LogMsg = ''
        bIsFileFine = False
        filePath = str(file)
        fileName = str(file.name)

        if not OpenEXR.isOpenExrFile(filePath):
                LogMsg = fileName +' is not image file.'
        else:
            try:
                if bCheckR:
                    r = len(OpenEXR.InputFile(filePath).channel('R'))
                if bCheckG:
                    g = len(OpenEXR.InputFile(filePath).channel('G'))
                if bCheckB:
                    b = len(OpenEXR.InputFile(filePath).channel('B'))
                if bCheckA:
                    a = len(OpenEXR.InputFile(filePath).channel('A'))
                LogMsg = fileName +' is fine.'
                bIsFileFine = True
            except Exception as e:        
                LogMsg = fileName +' is broken.'        
        logging.warning(LogMsg)
        return bIsFileFine
        
class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.bIsPathValid = False
        self.bIsAllFilesFine = False
        self.currOutPath = ''
        self.exrFiles = []
        self.options = ['Remove Alpha Channel']

        # ui
        self.setWindowTitle('EXR helper - v1.1.1')
        self.ui.BuildNumber.setText('v1.1.1')
        self.ui.OutputOption.addItems(self.options)

        # logger handler hook up
        handler = LogHandler(self)
        logging.getLogger().addHandler(handler)
        logging.getLogger().setLevel(logging.INFO)
        handler.new_record.connect(self.ui.plain.appendPlainText)

        # Qthreads 
        self.checkThread = check_Thread(self.checkProcess, ())
        self.outputThread = output_Thread(self.outputProcess, ())

    def IsPathValid(self, in_path):
        if not in_path:
            self.bIsPathValid = False
            logging.error('No input folder path.')
            return

        if not Path(in_path).exists():
            self.bIsPathValid = False
            logging.error('Not a valid input folder path.')
        else:
            self.bIsPathValid = True

    def getExrFiles(self, in_path):
        self.exrFiles.clear()
        if self.ui.EndFrame.value() == 0:
            frameEnd = 9999999
        else:
            frameEnd = self.ui.EndFrame.value()

        if self.ui.StartFrame.value() >= frameEnd:
            logging.info('FrameEnd must be greater than FrameStart.')
            return

        for x in Path(in_path).iterdir():
            if x.suffix == '.exr':
                frame = int(re.findall(r'\d+', str(x.name))[-1])
                if frame < self.ui.StartFrame.value() or frame > frameEnd:
                    continue
                self.exrFiles.append(x) 

        if self.exrFiles:
            self.exrFiles.sort()

    # events
    def eventInFolderBrowse(self):
        try:
            in_path = QtWidgets.QFileDialog.getExistingDirectory(None,'In folder', os.getcwd())
            self.ui.InFolderPath.setText(in_path)
        except:
            pass

    def eventFilesCheck(self):
        in_path = self.ui.InFolderPath.displayText()
        self.IsPathValid(in_path)

        if not self.bIsPathValid:
            return

        self.getExrFiles(in_path)
        
        if self.exrFiles:
            logging.info('--- Start files check. ---')
            logging.info('--- Check folder: %s. ---' % in_path)
            logging.info('--- Check %d files. ---' % len(self.exrFiles)) 
            self.checkThread.start()
            
    def eventStopCheck(self):
        self.checkThread.stop()
        self.checkThread.quit()
        self.ui.CheckButton.setEnabled(True)
        self.ui.StartButton.setEnabled(True)

    def eventOutFolderBrowse(self):
        try:
            out_path = QtWidgets.QFileDialog.getExistingDirectory(None,'Out folder', os.getcwd())
            self.ui.OutFolderPath.setText(out_path)
        except:
            pass

    def eventStartOutput(self):
        in_path = self.ui.InFolderPath.displayText()
        self.IsPathValid(in_path)

        if not self.bIsPathValid:
            return

        if not self.bIsAllFilesFine:
            if not self.ui.Unchecked.isChecked():
                logging.error('Files has not been checked.')
                return 
            
        if self.ui.Unchecked.isChecked():
            logging.info('Getting files...')
            self.getExrFiles(in_path)
            time.sleep(1.0)

        if not self.ui.OutFolderPath.displayText():
            self.currOutPath = in_path + '/out'
            Path(self.currOutPath).mkdir(parents=True, exist_ok=True)
        else:
           self.currOutPath = self.ui.OutFolderPath.displayText()

        logging.info('--- Start files Output. ---')
        logging.info('--- Output folder: %s. ---' % self.currOutPath)
        logging.info('--- Output %d files. ---' % len(self.exrFiles)) 
        self.outputThread.start()

    def eventStopOutput(self):
        self.outputThread.stop()
        self.outputThread.quit()
        self.ui.CheckButton.setEnabled(True)
        self.ui.StartButton.setEnabled(True)
        self.currOutPath = ''

    def eventClearLog(self):
        self.ui.plain.clear()

    # multi-thread works
    def checkProcess(self):
        self.ui.CheckButton.setEnabled(False)
        self.ui.StartButton.setEnabled(False)

        bCheckR = self.ui.checking_R.isChecked()
        bCheckG = self.ui.checking_G.isChecked()
        bCheckB = self.ui.checking_B.isChecked()
        bCheckA = self.ui.checking_A.isChecked()

        start_time = time.time()
        succeededFilesCount = 0

        for f in self.exrFiles:
            if not self.checkThread.bIsRunning:
                break

            if App.exrChecker(f, bCheckR, bCheckG, bCheckB, bCheckA):
                succeededFilesCount += 1
            time.sleep(0.01)

        if succeededFilesCount == len(self.exrFiles):
            self.bIsAllFilesFine = True
        else:
            self.bIsAllFilesFine = False
        
        logging.info('--- Completed: %d succeeded, %d failed ---' % (succeededFilesCount, len(self.exrFiles) - succeededFilesCount)) 
        logging.info("--- %s seconds ---" % (time.time() - start_time))

        self.eventStopCheck()

    def outputProcess(self):
        self.ui.CheckButton.setEnabled(False)
        self.ui.StartButton.setEnabled(False)

        start_time = time.time()
        succeededFilesCount = 0

        if self.ui.OutputOption.currentText() == self.options[0]:
            # remove alpha channel
            for f in self.exrFiles:
                if not self.outputThread.bIsRunning:
                    break
                if App.removeAlpha(str(f), str(f.name), self.currOutPath):
                    succeededFilesCount += 1
                time.sleep(0.01)
                
        logging.info('--- Completed: %d succeeded, %d failed ---' % (succeededFilesCount, len(self.exrFiles) - succeededFilesCount)) 
        logging.info("--- %s seconds ---" % (time.time() - start_time))

        self.eventStopOutput()

class LogHandler(QObject, logging.Handler):
    new_record = pyqtSignal(object)

    def __init__(self, parent):
        super().__init__(parent)
        super(logging.Handler).__init__()
        formatter = Formatter('%(asctime)s|%(message)s|', '%H:%M:%S')
        self.setFormatter(formatter)

    def emit(self, record):
        msg = self.format(record)
        self.new_record.emit(msg)

class Formatter(logging.Formatter):
    def formatException(self, ei):
        result = super(Formatter, self).formatException(ei)
        return result

    def format(self, record):
        s = super(Formatter, self).format(record)
        if record.exc_text:
            s = s.replace('\n', '')
        return s

class check_Thread(QThread):
    def __init__(self, func, args):
        super(check_Thread, self).__init__()
        self.func = func
        self.args = args
        self.bIsRunning = True

    def run(self):
        self.bIsRunning = True
        while self.bIsRunning == True:
            self.func(*self.args)

    def stop(self):
        self.bIsRunning = False

class output_Thread(QThread):
    def __init__(self, func, args):
        super(output_Thread, self).__init__()
        self.func = func
        self.args = args
        self.bIsRunning = True

    def run(self):
        self.bIsRunning = True
        while self.bIsRunning == True:
            self.func(*self.args)

    def stop(self):
        self.bIsRunning = False

if __name__=="__main__":
    app = QApplication(sys.argv)
    win = AppWindow()
    win.show()
    sys.exit(app.exec_())