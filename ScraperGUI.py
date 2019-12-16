from tkinter import *
from tkinter import filedialog


root = Tk()
root.title('Top 10 Data Users')
root.iconbitmap('icons/logo.ico')
root.geometry("400x290")

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

header = Label(root, text='Below are the top 10 data users!', font=18).grid(row=0, column=0)

frame = LabelFrame(root, padx=5, pady=5, bd=1, bg='white', relief='sunken')
frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

while i < 10:
    myLabel = Label(frame, text=([value for value in newSortDict.values()][i] + ' used ' + str([key for key in
                                newSortDict.keys()][i]) + ' GB over their data limit.'),
                                anchor='w', width=61, bg='white').pack()
    i += 1

exitBtn = Button(root, text='Exit Program', command=root.quit).grid(row=2, column=0)

root.mainloop()
