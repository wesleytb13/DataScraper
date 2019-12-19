from tkinter import *
from tkinter import filedialog


root = Tk()
root.title('Top 10 Data Users')
root.iconbitmap('icons/logo.ico')
root.geometry("240x70")
header = Label(root, text='Below are the top 10 data users!', font=('Verdana', 10), padx=5).grid(row=0, column=0, columnspan=2)

frame = LabelFrame(root, padx=5, pady=5, bd=1, bg='white', relief='sunken')
frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

def openFile():
    fileInput = filedialog.askopenfilename(initialdir='c:/', title='Select Your File', filetypes=(('csv files',
                        '*.csv'), ('all files', '*.*')))
    myFile = open(fileInput, 'r')

    newDict = {}
    newSortDict = {}
    x = 0
    i = 0
    for line in myFile:
        values = line.split(',')
        userName = values[2].title()
        if 'MB' in values[6]:
            pass
        else:
            overage = float(values[6].replace(' GB', ''))
        newDict.update({overage:userName})

    sortedDict = sorted(newDict, reverse=True)
    while x < len(sortedDict):
        newSortDict.update({sortedDict[x]: None})
        x += 1
    newSortDict.update(newDict)
    root.geometry("430x295")
    while i < 10:
        myLabel = Label(frame, text=([value for value in newSortDict.values()][i] + ' used ' + str([key for key in
                                    newSortDict.keys()][i]) + ' GB over their data limit.'),
                                    anchor='w', width=50, bg='white', font=('Verdana', 10)).pack()
        i += 1


openBtn = Button(root, text='Open File', command=openFile, font=('Verdana', 10)).grid(row=2, column=0, sticky=E, padx=5)
exitBtn = Button(root, text='Exit Program', command=root.quit, font=('Verdana', 10)).grid(row=2, column=1, sticky=W)

root.mainloop()
