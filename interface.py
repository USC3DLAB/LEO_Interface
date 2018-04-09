import sys
import os
import  csv 
import time
import shutil
from pathlib import Path
import numpy as np
from pandas import DataFrame

import matplotlib.pyplot as plt

import scipy.stats
from PyQt5.QtWebEngineWidgets import QWebEngineView # pylint: disable=E0611
from PyQt5.QtCore import QUrl, Qt, pyqtSignal, QTimer # pylint: disable=E0611
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication, QWidget, QDesktopWidget, QFileDialog # pylint: disable=E0611
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QLineEdit       # pylint: disable-msg=E0611

class LEO(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.statusBar()
        self.compared_data = []
        self.compared_data_type = None
        self.test_data = []
        self.ERROR_term  = []
        self.test_data_type = None
        self.project = ''
        self.log_file_name = ''
        self.pysp_file = ''
        self.f = None
        self.tpye = None
        self.smps_name = ''
        self.SL_Data = ''
        

        self.browser = QWebEngineView()
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "intro.html"))
        local_url = QUrl.fromLocalFile(file_path)
        self.browser.load(local_url)
        self.setCentralWidget(self.browser)

    def initUI(self):

        # set window's size and position
        self.resize(1000, 800)
        self.center()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('New project')
        ##impMenu = QMenu('Import', self)
        # impAct = QAction('Import data file', self)
        ##impMenu.addAction(impAct)

        generate_new_project = QAction('Generate a new project', self)
        generate_new_project.triggered.connect(self.generate_new_project)
        fileMenu.addAction(generate_new_project)
        
        open_project= QAction('Open a existing project', self)
        open_project.triggered.connect(self.open_project)
        fileMenu.addAction(open_project)


        newAct = QAction('Generate a log file', self)
        newAct.setStatusTip('Generate a text file, which will contains all the output information from this software')
        newAct.triggered.connect(self.generate_log_file)
        fileMenu.addAction(newAct)
        # fileMenu.addMenu(impMenu)

        SLMenu = menubar.addMenu('SL data')
        SL_data_load = QAction('Import a SL data set(*.csv)', self)
        SL_data_load.triggered.connect(self.SL_data_load)
        SLMenu.addAction(SL_data_load)

        ERROR_term_load = QAction('Import test error terms and validation error terms data(*.csv)', self)
        ERROR_term_load.triggered.connect(self.ERROR_term_load)
        SLMenu.addAction(ERROR_term_load)

        CHI_for_error = QAction('χ2-test for error terms', self)
        CHI_for_error.triggered.connect(self.CHI_for_error)
        SLMenu.addAction(CHI_for_error)


        SPMenu = menubar.addMenu('SP Model')
        Load_SP = QAction('Load a SP model(*.py)', self)
        Load_SP.setStatusTip('Import your SP model(*.py)')
        Load_SP.triggered.connect(self.Load_SP)
        SPMenu.addAction(Load_SP)

        PySP = QAction('Generate SMPS files with PySP', self)
        PySP.setStatusTip('Generate SMPS files in folder ~./projects/your project/SP_input/*.  This software generates SMPS files with PySP')
        PySP.triggered.connect(self.PySP)
        SPMenu.addAction(PySP)

        # SMPS = QAction('Choose the SMPS folder', self)
        # SMPS.setStatusTip('Choose your SP model in *.py type, which will be used with PySP to generate SMPS files')
        # SMPS.triggered.connect(self.SMPS)
        # SPMenu.addAction(SMPS)

        SD = QAction('Slove the SMPS files with a SD Solver', self)
        SD.setStatusTip('Using a SD solver to slove the SMPS files. Files are stored in ~./projects/your project/SP_output/*')
        SD.triggered.connect(self.SD)
        SPMenu.addAction(SD)


        """"
        StatiticalmodelMenu = menubar.addMenu('Predictive Models')
        timeseries = QAction('Time Series', self)
        StatiticalmodelMenu.addAction(timeseries)
        lr = QAction('Linear Regression', self)
        StatiticalmodelMenu.addAction(lr)

        SOMenu = menubar.addMenu('Prescriptive Models')
        lp = QAction('Linear Programming', self)
        SOMenu.addAction(lp)
        sdndu = QAction('Stochastic Decomposition(Normally Distributed and Uncorrelated)', self)
        SOMenu.addAction(sdndu)
        sdndc = QAction('Stochastic Decomposition(Normally Distributed and Correlated)', self)
        SOMenu.addAction(sdndc)
        sdeae = QAction('Stochastic Decomposition(Empirical Additive Errors)', self)
        SOMenu.addAction(sdeae)
        saa = QAction('Sampling Average Approximation(Empirical Additive Errors)', self)
        SOMenu.addAction(saa)

        dataMenu = menubar.addMenu('Data')
        outputdata = QAction('Load output data', self)
        dataMenu.addAction(outputdata)
        """

        testMenu = menubar.addMenu('Model Validation')

        ## data for validation
        data_validation = QAction('*Import training and validation cost-to-go data sets', self)
        data_validation.setStatusTip('Import training data set and validation data sets(*.csv) for test')
        data_validation.triggered.connect(self.open_file)
        testMenu.addAction(data_validation)

        chi = QAction('χ2 test for the cost-to-go function', self)
        chi.triggered.connect(self.chisquaredtest)
        testMenu.addAction(chi)
        ttest = QAction('T-test for the mean of cost-to-go function', self)
        ttest.triggered.connect(self.ttest)
        testMenu.addAction(ttest)
        ftest = QAction('F-test for the variance of cost-to-go function', self)
        ftest.triggered.connect(self.ftest)
        testMenu.addAction(ftest)
       

        # Compare data performance
        ComparationMenu = menubar.addMenu('Compare')

        data_folder = QAction('*Import data sets for comparison', self)
        data_folder.setStatusTip('Import all the cost-to-go output files for validation data generated by all models')
        data_folder.triggered.connect(self.open_compared_file)
        ComparationMenu.addAction(data_folder)

        kwtest = QAction('Kruskal-Wallis test', self)
        kwtest.triggered.connect(self.kwtest)
        ComparationMenu.addAction(kwtest)
        cdf = QAction('CDF', self)
        cdf.triggered.connect(self.cdf)
        ComparationMenu.addAction(cdf)


        helpMenu = menubar.addMenu('Help')
        helpdoc = QAction('Documents', self)
        # helpdoc.triggered.connect(self.helpdoc)
        helpMenu.addAction(helpdoc)
        examples = QAction('Examples', self)
        helpMenu.addAction(examples)


        self.setWindowTitle('Learning Enabled Optimization')
        self.show()


    def generate_new_project(self):
        self.project, ok = QInputDialog.getText(self, "Generate a new project", "Please input the name of your project:", QLineEdit.Normal, '')
        if os.path.exists(Path('./projects')/self.project):
            reply = QMessageBox.warning(self,
                                    "WARNING",  
                                    "Project "+ self.project + ' exists. Do you want to overwrite it?',  
                                    QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                shutil.rmtree(Path('./projects')/self.project)
            else:
                return

        project_floder = './projects/' + self.project
        os.makedirs(Path(project_floder))
        child_folder = ['SL', 'SP_input', 'SP_output', 'Val_output_within_run', 'Val_output_across_run']
        for i in child_folder:
            os.makedirs(Path(project_floder)/i)
        
        QMessageBox.information(self, "Return",   'Generated a new project\nPlease check project folder\n\n Suggestion: \n Put the error terms data sets(.csv) and SL models(.py) in ./projects/your project/SL folder' , QMessageBox.Ok )                  

    def open_project(self):
        self.project, ok = QInputDialog.getText(self, "Open a existing project", "Please input the name of the project which you want to open:", QLineEdit.Normal, '')
        child_folder = ['SL', 'SP_input', 'SP_output', 'Val_output_within_run', 'Val_output_across_run'] 
        if os.path.exists(Path('./projects')/self.project):
            index = 0
            for i in child_folder:
                if not os.path.exists(Path('./projects')/self.project/i):
                    index = 1
            if index == 1:
                QMessageBox.information(self,
                                    "Tips",  
                                    "This is not a project folder.\n Please make sure open a existing project",  
                                    QMessageBox.ok)
            else:
                QMessageBox.information(self,
                                        "Tips",  
                                        "Successfully opened project "+ self.project ,  
                                        QMessageBox.ok)
        else:
            QMessageBox.information(self,
                                    "Tips",  
                                    "This project does not exist.\n Please make sure open a existing project" ,  
                                    QMessageBox.ok)
    

    def generate_log_file(self):
            string = time.strftime('%b_%d_%Y_%H_%M_%S',time.localtime(time.time()))
            log_file_name, ok = QInputDialog.getText(self, "Log file name", "Please input the log file name:", QLineEdit.Normal, 'log_data_' + string)
            
            self.log_file_name = log_file_name + '.txt'
            if self.project == '':
                QMessageBox.information(self, "Return",   'Please generate a new project first' , QMessageBox.Ok )                  
            else: 
                file = os.path.join('./projects/' + self.project, self.log_file_name)
                self.f = open(file,'a')
                self.f.close()  
                
               
            #self.save_folder = QFileDialog.getExistingDirectory(self,
                                                                #"Open folder",
                                                                #"./")

    
        
        
    def Load_SP(self):
        #l = './projects/' + self.project 
        #if os.path.exists(Path(l)/'SL'):
            #print('good')
        self.pysp_file, self.type = QFileDialog.getOpenFileName(self,
                                                            "Choose a SD model(*.py)",
                                                            './projects/' + self.project + '/SL',
                                                            "Python Files (*.py);;Python Files (*.py)")  ## open file, set file type filter
        if self.pysp_file != '':
            QMessageBox.information(self, "Return",   'Imported the following SP model:\n' + self.pysp_file + '\n\n Next step: please generate SMPS files(PySP is provided)', QMessageBox.Ok )        
            if self.f != None:
                file = os.path.join('./projects/' + self.project, self.log_file_name)
                self.f = open(file,'a')
                self.f.write('Imported the following SP model:\n')
                self.f.write(self.pysp_file + '\n')
                self.f.close()
        else: 
            QMessageBox.information(self, "Return",   'No SP model is choosed', QMessageBox.Ok )        
            
            #else:
                #print('bad')


    def PySP(self):
        if self.pysp_file != None:
            self.smps_name, ok = QInputDialog.getText(self, "Name your model", "Please input the name of your SP model:", QLineEdit.Normal, os.path.basename(self.pysp_file).split('.')[0])
            project_floder_SP_input = './projects/' + self.project + '/SP_input'
            #os.makedirs(Path(project_floder_SP_input)/self.smps_name)
            os.system('python smps.py --basename ' +  self.smps_name  +  ' -m ' + self.pysp_file)
            
            
            if os.path.exists(Path(project_floder_SP_input)/self.smps_name):
                shutil.rmtree(Path(project_floder_SP_input)/self.smps_name)
            
            if not os.path.exists(Path('./smps')/self.smps_name):
                raise ValueError("SL model does not work")
            shutil.copytree(Path('./smps')/self.smps_name, Path(project_floder_SP_input)/self.smps_name)
            # if not os.path.exists(Path('./smps')):
            #     os.mkdir(Path('./smps'))
            QMessageBox.information(self, "Return",   'Generated the SMPS files for :\n  ' + self.smps_name + '\nFiles are stored in ./projects/your project/SP_input folder\n\n Next step: Solve the SP problem(SD solver is provided) ', QMessageBox.Ok )        
        else: 
            QMessageBox.information(self, "Return",   'Please import your SP model first', QMessageBox.Ok )        


    def SMPS(self):
        return

    def SD(self):

        if os.path.exists(Path('./sd/Build/Products/Debug/sdinput/')/ self.smps_name):
            shutil.rmtree(Path('./sd/Build/Products/Debug/sdinput/')/ self.smps_name)
        
        project_floder = './projects/' + self.project 
        if os.path.exists(Path(project_floder + '/SP_input')/self.smps_name):
            shutil.copytree(Path(project_floder + '/SP_input')/self.smps_name, Path('./sd/Build/Products/Debug/sdinput')/ self.smps_name)
        os.system('cd ./sd/Build/Products/Debug && ./sd ' +  self.smps_name)
        if os.path.exists(Path(project_floder + '/SP_output')/  self.smps_name):
            shutil.rmtree(Path(project_floder + '/SP_output')/  self.smps_name)
        if not os.path.exists(Path('./sd/Build/Products/Debug/sdoutput/')/ self.smps_name):
            raise ValueError("SMPS files do not work")
        else: 
            shutil.copytree(Path('./sd/Build/Products/Debug/sdoutput/')/self.smps_name, Path(project_floder + '/SP_output')/self.smps_name)
        QMessageBox.information(self, "Return",   'Solved the SP problem:\n  ' + self.smps_name + '\nResults are stored in ./projects/your project/SP_output folder', QMessageBox.Ok )        
        

    def SL_data_load(self):
        self.SL_Data, self.type = QFileDialog.getOpenFileName(self,
                                                            "Import a SL data set(*.csv)",
                                                            "./",
                                                            "CSV Files (*.CSV);;CSV Files (*.csv)")  ## open file, set file type filter
        print(str(type(self.SL_Data)))
        if self.SL_Data != '':
            QMessageBox.information(self, "Return",  'Imported the following SL data set:\n' + self.SL_Data + '\n', QMessageBox.Ok )        
            if self.f != None:
                file = os.path.join('./projects/' + self.project, self.log_file_name)
                self.f = open(file,'a')
                self.f.write('Imported the following SL data:\n')
                self.f.write(self.SL_Data + '\n')
                self.f.close()


    def ERROR_term_load(self):
        self.ERROR_term, self.type = QFileDialog.getOpenFileNames(self,
                                                            "Import two error terms data sets(*.csv)",
                                                            "./",
                                                            "CSV Files (*.CSV);;CSV Files (*.csv)")  ## open file, set file type filter
        if self.ERROR_term != []:
            j = ''
            for i in self.ERROR_term:
                j = j + i +'\n'
            QMessageBox.information(self, "Return",  'Imported the following error terms data sets:\n'+j, QMessageBox.Ok ) 
            
            if self.f != None:
                file = os.path.join('./projects/' + self.project, self.log_file_name)
                self.f = open(file,'a')
                self.f.write('Imported the following error terms data files:\n')
                for i in self.ERROR_term:  
                    self.f.write(i)
                    self.f.write('\n')
                self.f.close()
        
    
    def CHI_for_error(self):
        if self.ERROR_term != []:
            train_data = self.readcsv(self.ERROR_term[0])
            val_data = self.readcsv(self.ERROR_term[1])
            output = scipy.stats.chisquare(val_data, train_data)
            QMessageBox.information(self, "Return",  'The p-value of Chi-Squared Test for error terms is ' + str(output.pvalue) + '\n', QMessageBox.Ok )  
            if self.f != None:
                file = os.path.join('./projects/' + self.project, self.log_file_name)
                self.f = open(file,'a')
                self.f.write('The p-value of Chi-Squared Test for error terms is ' + str(output.pvalue) + '\n')
                self.f.close()
        else:
            QMessageBox.information(self, "Return",  'Please import error terms data sets first', QMessageBox.Ok ) 
            

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    

    ## open the data folder which contains all the data files that need to be compared, self.compared_data is a list contains the path of the file
    def open_compared_file(self):
        self.compared_data, self.compared_data_type = QFileDialog.getOpenFileNames(self,
                                                                                   "Import data sets for compare",
                                                                                   "./",
                                                                                   "CSV Files (*.csv)")  ## open file, set file type filter
        if self.compared_data != []:
            j = ''
            for i in self.compared_data:
                j = j + i + '\n'
            QMessageBox.information(self, "Return",  'Imported the following data files for comparison:\n'+j, QMessageBox.Ok )  

            if self.f != None:
                file = os.path.join('./projects/' + self.project, self.log_file_name)
                self.f = open(file,'a')
                self.f.write('Imported the following data sets for comparison:')
                self.f.write('\n')
                for i in self.compared_data:
                    self.f.write(i)
                    self.f.write('\n') 
                self.f.close()
        else:
            QMessageBox.information(self, "Return",  'Please import data sets for comparison', QMessageBox.Ok ) 
            

    ##open the two data files for test
    def open_file(self):
        self.test_data, self.test_data_type = QFileDialog.getOpenFileNames(self,
                                                                           "Import two data sets",
                                                                           "./",
                                                                           "CSV Files (*.CSV);;CSV Files (*.csv)")  ## open file, set file type filter
        if self.test_data != []:
            j = ''
            for i in self.test_data:
                j = j + i + '\n'
            QMessageBox.information(self, "Return",  'Imported the following data sets for test:\n'+j, QMessageBox.Ok )          

            if self.f != None:
                file = os.path.join('./projects/' + self.project, self.log_file_name)
                self.f = open(file,'a')
                self.f.write('Imported the following data sets for test:\n') 
                for i in self.test_data:
                    #print(i)
                    self.f.write(i)
                    self.f.write('\n')
                self.f.close()  
        else: 
            QMessageBox.information(self, "Return",  'Please import two data sets for test', QMessageBox.Ok ) 
              

    def ftest(self):
        if self.test_data != []:
            train_data = self.readcsv(self.test_data[0])
            val_data = self.readcsv(self.test_data[1])
            output = scipy.stats.f_oneway(train_data, val_data)
            QMessageBox.information(self, "Return",  'The p-value of F-Test is ' + str(output.pvalue) + '\n', QMessageBox.Ok )          
            if self.f != None:
                file = os.path.join('./projects/' + self.project, self.log_file_name)
                self.f = open(file,'a')
                self.f.write('The p-value of F-Test is ' + str(output.pvalue) + '\n')
                self.f.close()
        else:
            QMessageBox.information(self, "Return",  'Please import data sets for test first', QMessageBox.Ok ) 

    def chisquaredtest(self):
        if self.test_data != []:
            train_data = self.readcsv(self.test_data[0])
            val_data = self.readcsv(self.test_data[1])
            output = scipy.stats.chisquare(val_data, train_data)
            QMessageBox.information(self, "Return",  'The p-value of Chi-Squared-Test is ' + str(output.pvalue) + '\n', QMessageBox.Ok )   
            if self.f != None:
                file = os.path.join('./projects/' + self.project, self.log_file_name)
                self.f = open(file,'a')
                self.f.write('The p-value of Chi-Squared-Test is ' + str(output.pvalue) + '\n')
                self.f.close()
        else:
            QMessageBox.information(self, "Return",  'Please import data sets for test first', QMessageBox.Ok ) 


    def ttest(self):
        if self.test_data != []:
            train_data = self.readcsv(self.test_data[0])
            val_data = self.readcsv(self.test_data[1])
            output = scipy.stats.ttest_ind(train_data, val_data)
            QMessageBox.information(self, "Return",  'The p-value of T-Test is ' + str(output.pvalue) + '\n', QMessageBox.Ok )  
            if self.f != None:
                file = os.path.join('./projects/' + self.project, self.log_file_name)
                self.f = open(file,'a')
                self.f.write('The p-value of T-Test is ' + str(output.pvalue) + '\n')
                self.f.close()
        else:
            QMessageBox.information(self, "Return",  'Please import data sets for test first', QMessageBox.Ok ) 

    def kwtest(self):
        if self.compared_data != []:
            files_nb = len(self.compared_data)
            model_types = []
            for i in range(files_nb):
                model_types.append(os.path.basename(self.compared_data[i]).split('.')[0])
            df = DataFrame(index=model_types, columns=model_types)
            printout = ''

            for i in range(files_nb):
                data1 = self.readcsv(self.compared_data[i])
                for j in range(i + 1, files_nb):
                    data2 = self.readcsv(self.compared_data[j])
                    output = scipy.stats.kruskal(data1, data2)
                    df[model_types[i]][model_types[j]] = output.pvalue
                    printout = printout + str(model_types[i]) + '/' + str(model_types[j]) + ': ' + str(output.pvalue) + '\n'

            QMessageBox.information(self, "Return",  'The p-value of Kruskal-Wallis Test are\n' + printout + '\n(If p>0.05, reject the hypothesis.)', QMessageBox.Ok )   
            if self.f != None: 
                file = os.path.join('./projects/' + self.project, self.log_file_name)
                self.f = open(file,'a')
                self.f.write('The p-value of Kruskal-Wallis Test are:\n')
                self.f.write(df.to_string())
                self.f.close()
        else:
            QMessageBox.information(self, "Return",  'Please import data sets for compare first', QMessageBox.Ok ) 
            

    def cdf(self):
        if self.compared_data != []:
            for i in self.compared_data:
                data = self.readcsv(i)
                num_bins = int(np.max(data) - np.min(data))
                counts, bin_edges = np.histogram(data, bins=num_bins, normed=True)
                cdf = np.cumsum(counts)
                plt.plot(bin_edges[1:], cdf / cdf[-1], label=i.split('/')[-1])
            plt.title("Frequency of Validated objective functions")
            plt.xlabel("Validated Objective")
            plt.ylabel("Cumulative frequency")
            plt.legend()
            files_nb = len(self.compared_data)
            model_types = []
            fig_name = ''
            for i in range(files_nb):
                model_types.append(os.path.basename(self.compared_data[i]).split('.')[0])
                fig_name =  fig_name + '_' + model_types[i]
            fig_name = 'cdf' + fig_name + '.png'
            cur = os.getcwd() 
            os.chdir(Path('./projects')/self.project/'Val_output_across_run')
            plt.savefig(fig_name)
            os.chdir(cur)
            QMessageBox.information(self, "Return",  'Generated the figure for Frequency of Validated objective functions.\n' + 'Saved as: ' + fig_name, QMessageBox.Ok )                  
            plt.close()
        else:
            QMessageBox.information(self, "Return",  'Please import data sets for compare first', QMessageBox.Ok ) 
     
        #shutil.move(fig_name,'./projects/' + self.project + '/Val_output_across_run')  

    # def helpdoc(self):
    #     subprocess.Popen(['LEO.pdf],shell=True)

    def readcsv(self, filename):
        results = []
        with open(filename) as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
            for row in reader:  # each row is a list
                results.append(row[0])
        a = np.array(results)
        return a


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = LEO()
    sys.exit(app.exec_())
