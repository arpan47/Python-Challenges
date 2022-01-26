from tkinter import *
import os
from tkinter import messagebox
import tkinter as tk
import logging
import PyPDF2

class Exit_code_By_Default(Exception):
    pass


class list_all_files:
    """
    |   Level    | Numeric value |
    |------------|---------------|
    |   CRITICAL | 50            |
    |   ERROR    | 40            |
    |   WARNING  | 30            |
    |   INFO     | 20            |
    |   DEBUG    | 10            |
    |   NOTSET   | 0             |

    Provide value as 0 or 10 or 20 or 30 or 40 or 50 as per the criticality
    """

    def __init__(self, log):
        self.log = log
        logging.basicConfig(filename='list_all_files.log', level=self.log,
                            format='%(asctime)s - %(message)s - %(levelname)s')
        logging.debug('-----------------------------------------------------')
        logging.info("list_all_files object has been initialized")

    def check_dir(self):
        """
        To check all the files in the directory
        """
        try:
            root = tk.Tk()
            logging.info("tkinter object has been initialized")
            flag = 0
            w = Label(root, text='Please enter your directory path to see all files', font=('Consolas', 20), width=50)
            w.pack()
            e = Entry(root, font=('Consolas', 15), width=50)
            e.pack()
            logging.info("user directory path has been initialized")

            def onclik():
                try:
                    sb = Scrollbar(root)
                    sb.pack(side=RIGHT, fill=Y, ipadx=7)
                    mylist = Listbox(root, yscrollcommand=sb.set, font=('Consolas', 15), justify='left', width=50)
                    files = os.listdir(e.get())
                    for f in files:
                        mylist.insert(END, f)
                    mylist.pack(side=BOTTOM)
                    sb.config(command=mylist.yview)
                    logging.info("all files has been shown")
                except Exception as e1:
                    messagebox.showinfo("Error!!!", "\rPlease check the path!!")
                    logging.error("Error!!!-- inside -- {} -- {}".format(e1.__class__, e1))
                finally:
                    myButton['state'] = 'disabled'
                    logging.info("button state disabled")

            myButton = Button(root, text="Submit", command=onclik, font=('Consolas', 15))
            myButton.pack()
            root.mainloop()
        except Exception as ee:
            logging.error("Error!!!-- onclik -- {} -- {}".format(ee.__class__, ee))


class check_dir_pdf:
    """
    |   Level    | Numeric value |
    |------------|---------------|
    |   CRITICAL | 50            |
    |   ERROR    | 40            |
    |   WARNING  | 30            |
    |   INFO     | 20            |
    |   DEBUG    | 10            |
    |   NOTSET   | 0             |

    Provide value as 0 or 10 or 20 or 30 or 40 or 50 as per the criticality
    """

    def __init__(self, log):
        self.log = log
        logging.basicConfig(filename='check_dir_pdf.log', level=self.log,
                            format='%(asctime)s - %(message)s - %(levelname)s')
        logging.debug('-----------------------------------------------------')
        logging.info("check_dir_pdf object has been initialized")

    def merge(self):
        """
        To merge all pdf's in a given path to a new pdf doc.
        """
        try:
            root = tk.Tk()
            logging.info("tkinter object has been initialized")
            flag = 0
            pdfls = []
            w = Label(root, text='Please enter your directory path to see all files', font=('Consolas', 20), width=50)
            w.pack()
            e = Entry(root, font=('Consolas', 15), width=50)
            e.pack()
            logging.info("user directory path has been initialized")

            w1 = Label(root, text='Please provide merged pdf file name', font=('Consolas', 20), width=50)
            w1.pack()
            e3 = Entry(root, font=('Consolas', 15), width=50)
            e3.pack()
            logging.info("user file name has been initialized")

            def pdf_merge(pdf_final_file, pdf_dir, pdf_files):
                try:
                    logging.info("pdf_merge function initiated")
                    pdfWriter = PyPDF2.PdfFileWriter()
                    for i in pdf_files:
                        pdfil = open(pdf_dir + "/" + i, 'rb')
                        pyd = PyPDF2.PdfFileReader(pdfil)

                        for pageNum in range(pyd.numPages):
                            pageObj = pyd.getPage(pageNum)
                            pdfWriter.addPage(pageObj)
                            pdfOutputFile = open(pdf_dir + "/" + pdf_final_file, 'wb')
                            pdfWriter.write(pdfOutputFile)
                        pdfil.close()

                    pdfOutputFile.close()
                    logging.info("pdf_merge function terminated successfully")
                except Exception as exp:
                    logging.error("Error!!!-- pdf_merge function -- {} -- {}".format(exp.__class__, exp))
                    messagebox.showinfo("Error!!!", "\nPlease check the path!!", "\nPlease check the filename")
                    # raise Exit_code_By_Default

            def onclic():
                try:
                    try:
                        files = os.listdir(e.get())
                        for f in files:
                            cc = ''
                            for i in range(len(f) - 4, len(f)):
                                cc = cc + f[i]
                                if (cc.lower() == '.pdf'):
                                    pdfls.append(f)
                    except Exception as ess3:
                        logging.error("Error!!!-- list dirr issue -- {} -- {}".format(ess3.__class__, ess3))
                        messagebox.showinfo("Error!!!", "\nPlease check the path!!")

                    if (e3.get()[-4:].lower() != '.pdf'):
                        try:
                            pdf_merge(str(e3.get()) + str('.pdf'), e.get(), pdfls)
                        except Exception as ess1:
                            logging.error("Error!!!-- pdf_merge call 1 -- {} -- {}".format(ess1.__class__, ess1))
                            messagebox.showinfo("Error!!!", "\nPlease check the filename")
                    else:
                        try:
                            pdf_merge(e3.get(), e.get(), pdfls)
                        except Exception as ess2:
                            logging.error("Error!!!-- pdf_merge call 2 -- {} -- {}".format(ess2.__class__, ess2))
                            messagebox.showinfo("Error!!!", "\nPlease check the filename")

                    logging.info("all files has been been merged to single pdf")

                except Exception as e1:
                    messagebox.showinfo("Error!!!", "\nPlease check the path!!", "\nPlease check the filename")
                    logging.error("Error!!!-- inside -- {} -- {}".format(e1.__class__, e1))
                finally:
                    myButton['state'] = 'disabled'
                    logging.info("button state disabled")

            myButton = Button(root, text="Submit", command=onclic, font=('Consolas', 15))
            myButton.pack()
            root.mainloop()
        except Exception as ee:
            logging.error("Error!!!-- onclic -- {} -- {}".format(ee.__class__, ee))