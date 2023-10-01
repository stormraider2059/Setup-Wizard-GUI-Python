from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import threading
import time
import psutil
import webbrowser


def actWin():
    installationWin.destroy()
    activationWindow = Tk()
    activationWindow.title("Activation (Optional)")
    activationWindow.geometry("600x300")
    labelAct = Label(activationWindow,
                     text="Enter your 16-digit activation key (XXXX-XXXX-XXXX-XXXX)",
                     font=("Arial", 10),
                     width=50,
                     )
    labelAct.place(x=20, y=50)
    keyEntry = Entry(activationWindow,
                     font=("Arial", 15),
                     width=30,
                     border=2,
                     )
    keyEntry.place(x=60, y=100)
    actFinishBtn = Button(activationWindow,
                          text="Finish",
                          font=("Arial", 10),
                          cursor="hand2",
                          state=DISABLED,
                          command=activationWindow.destroy,
                          width=5
                          )
    actCancelBtn = Button(activationWindow,
                          text="Cancel",
                          font=("Arial", 10),
                          cursor="hand2",
                          command=activationWindow.destroy,
                          width=5
                          )
    actFinishBtn.place(x=500, y=250)
    actCancelBtn.place(x=440, y=250)

    def gotoActSuccess():
        keyEntry.config(state=DISABLED)
        actBtn.config(state=DISABLED)
        actFinishBtn.config(state=ACTIVE)
        actCancelBtn.config(state=DISABLED)

    def activationSuccess():
        messagebox.showinfo(title="Activation successful",
                            message="Activation successful. Click OK to exit.")
        gotoActSuccess()

    def activationFailed():
        messagebox.showerror(title="Activation failed",
                             message="Activation failed. Please check your activation key and try again.")

    def activationMatch():
        if keyEntry.get() == "ABCD-1234-EFGH-5678":
            activationSuccess()
        elif keyEntry.get() == "":
            pass
        else:
            activationFailed()

    actBtn = Button(activationWindow,
                    text="Activate",
                    font=("Arial", 10),
                    cursor="hand2",
                    command=activationMatch
                    )
    labelAct2 = Label(activationWindow,
                      text="Don't have an activation key?",
                      font=("Arial", 10),
                      width=30
                      )
    labelAct3 = Label(activationWindow,
                      text="Get the product key",
                      fg="blue",
                      font=("Arial", 10, "underline"),
                      width=20,
                      cursor="hand2",
                      )

    labelAct3.bind(
        "<Button-1>", lambda event: webbrowser.open_new(
            "https://www.cracklicense.org")
    )
    labelAct3.place(x=37, y=210)
    labelAct2.place(x=20, y=170)
    actBtn.place(x=450, y=97)
    keyEntry.place(x=60, y=100)
    activationWindow.mainloop()


def installation():
    dualTabsWin.destroy()
    global installationWin
    installationWin = Tk()
    installationWin.title("Installing SillyPy")
    installationWin.geometry("750x500")
    installationLabel = Label(installationWin,
                              text="Installing SillyPy",
                              font=("Arial", 15, "bold"),
                              width=15,
                              pady=20

                              )
    installationLabel.pack(anchor=W, padx=10, pady=25)

    installBar = ttk.Progressbar(installationWin,
                                 orient=HORIZONTAL,
                                 length=650,
                                 value=0


                                 )
    installBar.pack(anchor=W, padx=25, pady=5)

    installationLists = ["Unpacking gortok.dll", "Unpacking fyg.dll", "Unpacking snakeSRC.py", "Unpacking snake.exe", "Unpacking snake.ico", "Unpacking silly.py", "Unpacking sillypyconfig.pyw", "Unpacking crosLvl.pyw",
                         "Unpacking coelesced.config", "Unpacking sillyPy.exe", "Unpacking uninstall08.exe", "Unpacking unins08.bat", "Unpacking readme.txt", "Installing VCRedistx86", "Installing VCRedistx64", "Finishing up "]
    installingTask = Label(installationWin,
                           text="Starting",
                           font=("Arial", 10),
                           width=28,
                           padx=5,

                           )
    installingTask.pack(anchor=W, pady=30)

    message = Label(installationWin,
                    text="Please wait until the installation is completed.",
                    font=("Arial", 10, "italic"),
                    width=40,
                    pady=5,
                    )
    message.pack(anchor=W, padx=20, pady=45)

    finaleButtonNext = Button(installationWin,
                              text="Finish",
                              font=("Arial", 10),
                              width=10,
                              cursor="hand2",
                              state=DISABLED,
                              command=actWin
                              )
    finaleButtonNext.place(x=600, y=440)

    def startInstalling():
        toInstall = len(installationLists)
        counter = 0
        while (counter < toInstall):
            time.sleep(1.5)
            installingTask.config(text=installationLists[counter])
            installBar['value'] += 100/toInstall
            counter += 1
            installBar.update_idletasks()
        time.sleep(1.5)
        installingTask.config(text="Installation completed")
        installBar['value'] = 100
        installBar.update_idletasks()
        time.sleep(0.5)
        if (installBar['value'] == 100):
            message.config(
                text="Thank you for being patient. Click Finish to exit.")
            finaleButtonNext.config(state=ACTIVE)

    installThread = threading.Thread(target=startInstalling)
    installThread.start()

    installationWin.mainloop()


def dualTabs():

    choosePath.destroy()
    global dualTabsWin
    dualTabsWin = Tk()
    dualTabsWin.title("Updates and Feedback")
    dualTabsWin.geometry("820x510")
    global dualNoteBook
    dualNoteBook = ttk.Notebook(dualTabsWin)
    updatesTab = Frame(dualNoteBook)
    feedbackTab = Frame(dualNoteBook)
    dualNoteBook.add(updatesTab, text="Updates")
    dualNoteBook.add(feedbackTab, text="Feedback", state=DISABLED)
    dualNoteBook.pack(expand=True, fill=BOTH)
    updatesTabLabel = Label(updatesTab,
                            text="This is the current and beta version (v1.0.1) of the program. The version updates with patches and features will be available soon.",
                            font=("Arial", 10),
                            width=100,
                            height=5,
                            padx=5,
                            pady=5,

                            )
    updatesTabLabel.grid(row=0, column=0, sticky=W)
    patchesLabel = Label(updatesTab,
                         text="Patches and updates:",
                         font=("Arial", 12, "bold"),
                         width=22,
                         height=2,
                         padx=5,
                         pady=1,
                         )
    patchesLabel.grid(row=1, column=0, sticky=W)
    patchesNotes = Text(updatesTab,
                        font=("Arial", 10),
                        width=85,
                        height=5,
                        wrap=WORD,
                        padx=30,
                        pady=30
                        )
    patchesNotes.insert(
        INSERT, "Version 1.0.1 (beta)\n\n 1. Simplified GUI for program\n 2. Improved performances for testing version\n 3. Bug fixes and other enhancements ")
    patchesNotes.config(state=DISABLED, fg="#404040", bg="whitesmoke")
    patchesNotes.grid(row=2, column=0, sticky=W, padx=32, pady=5)

    updateInfoSiteLabel = Label(updatesTab,
                                font=("Arial", 10),
                                text="Visit my GitHub link mentioned below for more information.",
                                width=50,
                                height=2,
                                padx=5,
                                pady=3)
    updateInfoSiteLabel.grid(row=3, column=0, sticky=W, pady=8)

    gitHubLink = Label(updatesTab,
                       text="https://www.github.com/stormraider2059/SillyPy",
                       font=("Arial", 10, "underline"),
                       width=42,
                       height=2,
                       padx=5,

                       cursor="hand2",
                       fg="blue"
                       )
    gitHubLink.grid(row=4, column=0, sticky=W, pady=2)
    gitHubLink.bind("<Button-1>", lambda event: webbrowser.open_new(
        "https://www.github.com/stormraider2059/SillyPy"))

    def goto_FeedBacktab():

        dualNoteBook.tab(1, state="normal")  # to enable the feedback tab
        dualNoteBook.select(feedbackTab)
        dualNoteBook.tab(0, state="disabled")  # to disable the updates tab

    updatesTabNext = Button(updatesTab,
                            text="Next",
                            font=("Arial", 10),
                            width=10,
                            cursor="hand2",
                            command=goto_FeedBacktab
                            )
    updatesTabNext.grid(row=8, column=0, sticky=E, padx=125, pady=25)
    updatesTabCancel = Button(updatesTab,
                              text="Cancel",
                              font=("Arial", 10),
                              width=10,
                              cursor="hand2",
                              command=dualTabsWin.destroy
                              )
    updatesTabCancel.grid(row=8, column=0, sticky=E, padx=25, pady=25)

    feedbackTabLabel = Label(feedbackTab,
                             text="Remember to give your feedback and suggestions for the program. Your feedback is valuable to us.",
                             font=("Arial", 10),
                             width=80,
                             height=4,
                             padx=3,
                             pady=3,
                             )
    feedbackTabLabel.grid(row=0, column=0, sticky=W)

    feedbackFollowLabel = Label(feedbackTab,
                                text="Follow us on social medias for your feedback and suggestions.",
                                font=("Arial", 10),
                                width=55,
                                height=4,
                                padx=3,
                                pady=3

                                )
    feedbackFollowLabel.grid(row=1, column=0, sticky=W)
    fbIcon = PhotoImage(file="facebook.png").subsample(30, 30)
    instaIcon = PhotoImage(file="instagram.png").subsample(30, 30)
    twitterIcon = PhotoImage(file="twitter.png").subsample(30, 30)
    discordIcon = PhotoImage(file="discord.png").subsample(30, 30)

    def socialMedias():
        facebookLabel = Label(feedbackTab,
                              text="facebook.com/SillyPy",
                              font=("Arial", 9),
                              width=250,
                              image=fbIcon,
                              compound="left",
                              padx=10,


                              )
        facebookLabel.grid(row=2, column=0, sticky=W, padx=10, pady=8)

        instagramlabel = Label(feedbackTab,
                               text="instagram.com/sillyPy_69",
                               font=("Arial", 9),
                               width=250,
                               image=instaIcon,
                               compound="left",
                               padx=10,
                               )
        instagramlabel.grid(row=3, column=0, sticky=W, padx=22, pady=8)

        twitterlabel = Label(feedbackTab,
                             text="twitter.com/silly.Py",
                             font=("Arial", 9),
                             width=230,
                             image=twitterIcon,
                             compound="left",
                             padx=10,
                             )
        twitterlabel.grid(row=4, column=0, sticky=W, padx=12, pady=8)

        discordLabel = Label(feedbackTab,
                             text="discord.gg/SillyPy#404",
                             font=("Arial", 9),
                             width=250,
                             image=discordIcon,
                             compound="left",
                             padx=10,

                             )
        discordLabel.grid(row=5, column=0, sticky=W, padx=13, pady=8)

    socialMedias()

    def goto_updatesTab():
        dualNoteBook.tab(0, state="normal")  # to enable the updates tab
        dualNoteBook.select(updatesTab)
        dualNoteBook.tab(1, state="disabled")  # to disable the feedback tab

    feedbackHidden = Button(feedbackTab,
                            text="Hidden",
                            font=("Arial", 10),
                            width=10,
                            cursor="hand2",
                            command=goto_updatesTab
                            )
    feedbackHidden.grid(row=7, column=0, sticky=W, padx=20, pady=25)
    feedbackHidden.config(fg=feedbackHidden.master.cget('bg'), bg=feedbackHidden.master.cget(
        'bg'), bd=0)  # used to hide the button without removing it

    feedbackTabPrevious = Button(feedbackTab,
                                 text="Previous",
                                 font=("Arial", 10),
                                 width=10,
                                 cursor="hand2",
                                 command=goto_updatesTab
                                 )
    feedbackTabPrevious.grid(row=8, column=0, sticky=W, padx=20, pady=25)

    feedbackTabNext = Button(feedbackTab,
                             text="Install",
                             font=("Arial", 10),
                             width=10,
                             cursor="hand2",
                             command=installation
                             )
    feedbackTabNext.grid(row=8, column=0, sticky=E, padx=(600, 0))

    feedbackTabCancel = Button(feedbackTab,
                               text="Cancel",
                               font=("Arial", 10),
                               width=10,
                               cursor="hand2",
                               command=dualTabsWin.destroy
                               )
    feedbackTabCancel.grid(row=8, column=1, sticky=E, padx=10)

    dualTabsWin.mainloop()


def chooseDir():
    global choosePath
    choosePath = Tk()
    choosePath.title("Installation Path")
    choosePath.geometry("750x550")
    choosePathLabel = Label(choosePath,
                            text="Installation Path",
                            font=("Arial", 18, "bold"),
                            width=15,
                            padx=25,
                            pady=25

                            )
    choosePathLabel.pack(anchor=W)
    choosePathLabel2 = Label(choosePath,
                             text="Select or change the path or the destination folder for installation.",
                             font=("Arial", 10),
                             width=52,
                             padx=25,
                             pady=2
                             )
    choosePathLabel2.pack(anchor=W)

    dirShow = Text(choosePath,
                   font=("Arial", 10),
                   width=70,
                   height=1.4,
                   wrap=WORD,
                   padx=5,
                   pady=3,
                   )
    dirShow.insert(INSERT, "C:/Program Files (x86)/SillyPy")
    dirShow.config(state=DISABLED, fg="#404040")
    dirShow.place(x=50, y=150)

    def selectFolder():
        destPath = filedialog.askdirectory(
            title="Select a folder", initialdir="C:/", mustexist=TRUE)
        dirShow.config(state=NORMAL)

        if destPath == "":
            dirShow.delete("1.0", END)
            dirShow.insert(INSERT, "C:/Program Files (x86)/SillyPy")
            dirShow.config(state=DISABLED, fg="#404040")
        else:
            dirShow.delete("1.0", END)
            dirShow.insert(INSERT, destPath)
            dirShow.config(state=DISABLED, fg="#404040")

        if destPath:
            disk = psutil.disk_usage(destPath)
            freeSpace = disk.free/(1024 * 1024 * 1024)
            freeSpaceText = Label(choosePath,
                                  text="At least 600 MB of free memory space is required for installation. Selected disk has {:.2f} GB free memory".format(
                                      freeSpace),
                                  font=("Arial", 9, "italic"),
                                  width=90,
                                  padx=5,

                                  )

            freeSpaceText.place(x=25, y=300)

    changeBtn = Button(choosePath,
                       text="Change",
                       font=("Arial", 10),
                       width=8,
                       cursor="hand2",
                       command=selectFolder
                       )
    changeBtn.place(x=580, y=145)

    defaultDisk = psutil.disk_usage("C:/")
    defaultFreeSpace = defaultDisk.free/(1024 * 1024 * 1024)
    freeSpaceText = Label(choosePath,
                          text="At least 600 MB of free memory space is required for installation. Selected disk has {:.2f} GB free memory".format(
                              defaultFreeSpace),
                          font=("Arial", 9, "italic"),
                          width=90,
                          padx=5,

                          )

    freeSpaceText.place(x=25, y=300)

    choosePathNextButton = Button(choosePath,
                                  text="Next",
                                  font=("Arial", 10),
                                  width=10,
                                  cursor="hand2",
                                  command=dualTabs
                                  )
    choosePathNextButton.place(x=500, y=500)
    choosePathCancelButton = Button(choosePath,
                                    text="Cancel",
                                    font=("Arial", 10),
                                    width=10,
                                    cursor="hand2",
                                    command=choosePath.destroy
                                    )
    choosePathCancelButton.place(x=600, y=500)

    choosePath.mainloop()


def memoryChoose():
    archChoose.destroy()
    memoryScale = Tk()
    memoryScale.title("Memory Allocation")
    memoryScale.geometry("750x550")
    memoryScaleLabel = Label(memoryScale,
                             text="Choose the amount of memory to be used for installation.",
                             font=("Arial", 15, "bold"),
                             width=50,
                             padx=20,
                             pady=25
                             )
    memoryScaleLabel.pack(anchor=W)
    memoryScaleLabel2 = Label(memoryScale,
                              text="Memory allocation ranges from 1GB to 8GB. Adjust the slider to select the amount of memory to be used.",
                              font=("Arial", 10),
                              width=80,
                              padx=30,
                              pady=5
                              )
    memoryScaleLabel2.pack(anchor=W)
    GBarr = ["1", "2", "3", "4", "5", "6", "7", "8"]

    def updatememory(value):

        if memoryScaler.get() == 1024:
            memoryAlloc.config(state=NORMAL)
            memoryAlloc.delete("1.0", END)
            memoryAlloc.insert(
                INSERT, f"{memoryScaler.get()} MB = {GBarr[0]} GB")
            memoryAlloc.config(state=DISABLED)
        elif memoryScaler.get() == 2048:
            memoryAlloc.config(state=NORMAL)
            memoryAlloc.delete("1.0", END)
            memoryAlloc.insert(
                INSERT, f"{memoryScaler.get()} MB = {GBarr[1]} GB")
            memoryAlloc.config(state=DISABLED)
        elif memoryScaler.get() == 3072:
            memoryAlloc.config(state=NORMAL)
            memoryAlloc.delete("1.0", END)
            memoryAlloc.insert(
                INSERT, f"{memoryScaler.get()} MB = {GBarr[2]} GB")
            memoryAlloc.config(state=DISABLED)
        elif memoryScaler.get() == 4096:
            memoryAlloc.config(state=NORMAL)
            memoryAlloc.delete("1.0", END)
            memoryAlloc.insert(
                INSERT, f"{memoryScaler.get()} MB = {GBarr[3]} GB")
            memoryAlloc.config(state=DISABLED)
        elif memoryScaler.get() == 5120:
            memoryAlloc.config(state=NORMAL)
            memoryAlloc.delete("1.0", END)
            memoryAlloc.insert(
                INSERT, f"{memoryScaler.get()} MB = {GBarr[4]} GB")
            memoryAlloc.config(state=DISABLED)
        elif memoryScaler.get() == 6144:
            memoryAlloc.config(state=NORMAL)
            memoryAlloc.delete("1.0", END)
            memoryAlloc.insert(
                INSERT, f"{memoryScaler.get()} MB = {GBarr[5]} GB")
            memoryAlloc.config(state=DISABLED)
        elif memoryScaler.get() == 7168:
            memoryAlloc.config(state=NORMAL)
            memoryAlloc.delete("1.0", END)
            memoryAlloc.insert(
                INSERT, f"{memoryScaler.get()} MB = {GBarr[6]} GB")
            memoryAlloc.config(state=DISABLED)
        elif memoryScaler.get() == 8192:
            memoryAlloc.config(state=NORMAL)
            memoryAlloc.delete("1.0", END)
            memoryAlloc.insert(
                INSERT, f"{memoryScaler.get()} MB = {GBarr[7]} GB")
            memoryAlloc.config(state=DISABLED)
        else:
            print("Error")

    memoryScaler = Scale(memoryScale,
                         from_=1024, to=8192,
                         resolution=1024,
                         width=20,
                         font=("Arial", 10),
                         command=updatememory,
                         length=600,

                         orient=HORIZONTAL,
                         tickinterval=1024,
                         showvalue=0,
                         troughcolor="#d3d3d3",
                         cursor="hand2",
                         sliderrelief="raised",
                         sliderlength=30,
                         bd=0,
                         borderwidth=2,
                         highlightthickness=0,


                         )

    memoryScaler.place(x=50, y=180)
    memoryAlloc = Text(memoryScale,
                       font=("Arial", 10),
                       width=15,
                       height=1,
                       wrap=WORD,
                       padx=10,
                       pady=10,
                       fg="black",
                       bg="whitesmoke",


                       )

    memoryAlloc.place(x=550, y=300)
    memoryAlloc.insert(INSERT, f"{memoryScaler.get()} MB = {GBarr[0]} GB")
    memoryAlloc.config(state=DISABLED)
    memoryUnits = Label(memoryScale,
                        text="Memory units:",
                        font=("Arial", 10),
                        width=8,
                        padx=10,
                        pady=10
                        )
    memoryUnits.place(x=450, y=300)
    memoryNote = Label(memoryScale,
                       text="Note: If you have a device with low memory, it is recommended to use 1GB of memory for installation.",
                       font=("Arial", 10, "italic"),
                       width=80,
                       padx=10,
                       pady=10,
                       fg="red"
                       )
    memoryNote.place(x=20, y=380)

    def memoDecision():
        if (memoryScaler.get() == 1024 or memoryScaler.get() == 2048):
            messagebox.showwarning(
                title="Warning !", message="Low memory detected! Only the essential programs will be installed.")
            confirmation = messagebox.askyesno(
                title="Continue setup?", message="The additional programs won't be installed due to insufficient memory. Do you want to continue the setup?")
            if (confirmation):
                memoryScale.destroy()
                chooseDir()
            else:
                messagebox.showinfo(title="Setup aborted",
                                    message="Setup was cancelled")
                memoryScale.destroy()
        else:
            messagebox.showinfo(
                title="Sufficient memory", message="You have sufficient memory. The additional programs will be installed by the setup.")
            memoryScale.destroy()
            chooseDir()

    memoryNextButton = Button(memoryScale,
                              text="Next",
                              font=("Arial", 10),
                              width=10,
                              cursor="hand2",
                              command=memoDecision
                              )
    memoryNextButton.place(x=500, y=500)
    memoryCancelButton = Button(memoryScale,
                                text="Cancel",
                                font=("Arial", 10),
                                width=10,
                                cursor="hand2",
                                command=memoryScale.destroy
                                )
    memoryCancelButton.place(x=600, y=500)
    memoryScale.mainloop()


def archSelect():
    agWin.destroy()
    architectures = ["x86 (32-bit system)", "x64 (64-bit system)"]
    global archChoose
    archChoose = Tk()
    archChoose.title("Installation Options")
    archChoose.geometry("600x500")
    archChooseLabel = Label(archChoose,
                            text="Choose the architecture of your system",
                            font=("Arial", 12, "bold"),
                            width=35,
                            )
    archChooseLabel.place(x=15, y=50)
    archFilesMenu = Label(archChoose,
                          text="Files for installation:",
                          font=("Arial", 12, "bold"),
                          width=20,
                          )
    archFilesMenu.place(x=18, y=210)
    archVar = IntVar()  # this is a variable to check which architecture the user has selected
    systemText = Text(archChoose,
                      background="whitesmoke",
                      border=1,
                      font=("Arial", 10),
                      width=70,
                      height=10,
                      wrap=WORD,
                      )
    systemText.place(x=50, y=250)

    def arch32():
        systemText.config(state=NORMAL)
        systemText.delete("1.0", END)
        systemText.insert(INSERT, "For a x86 (32-bit) system, the following with 32-bit programs will be installed.\n\n \t1. aprf86.dll\n \t2. config32.dll \n \t3. profig32.exe \n \t4. nefist.dll \n \t5. VCRedistx86(2012-2015) ")
        systemText.config(state=DISABLED)

    def arch64():
        systemText.config(state=NORMAL)
        systemText.delete("1.0", END)
        systemText.insert(INSERT, "For a x64 (64-bit) system, the following with 64-bit programs will be installed.\n\n \t1. aprf64.dll\n \t2. config64.dll \n \t3. profig64.exe \n \t4. nefist.dll \n \t5. VCRedistx64(2012-2015) \n \t6. cachehandlerx64.prg")
        systemText.config(state=DISABLED)

    def updateTextBox():

        if archVar.get() == 0:
            arch32()
        elif archVar.get() == 1:
            arch64()
        else:
            print("Error")
    updateTextBox()

    for arch in range(len(architectures)):
        chooseArchOpt = Radiobutton(archChoose,
                                    text=architectures[arch],
                                    variable=archVar,
                                    value=arch,
                                    padx=25,
                                    pady=10,
                                    font=("Arial", 10),
                                    command=updateTextBox,
                                    cursor="hand2"
                                    )

        # +arch*50 is used to place the next option 50 pixels below the previous option
        chooseArchOpt.place(x=30, y=100+arch*40)
    archNextButton = Button(archChoose,
                            text="Next",
                            font=("Arial", 10),
                            width=10,
                            cursor="hand2",
                            command=memoryChoose

                            )
    archNextButton.place(x=350, y=450)
    archCancelButton = Button(archChoose,
                              text="Cancel",
                              font=("Arial", 10),
                              width=10,
                              cursor="hand2",
                              command=archChoose.destroy

                              )
    archCancelButton.place(x=450, y=450)
    archChoose.mainloop()


def agreement():
    global agWin
    agWin = Tk()
    agWin.title(" User License Agreement")
    agWin.geometry("700x650")
    agLabel = Label(agWin,
                    text="USER LICENSE AGREEMENT",

                    font=("Arial", 15, "bold"),
                    width=25,
                    )
    agLabel.place(x=15, y=50)
    TextAg = Text(agWin,
                  background="whitesmoke",
                  width=87,
                  height=20,
                  font=("Arial", 10),
                  wrap=WORD,
                  state=NORMAL,
                  insertwidth=0
                  )
    # def disableInput(event):
    #     TextAg.tag_remove("sel", "1.0", END)  # Remove any selected text
    #     return "break"  # Prevent any input from the user

    # TextAg.bind("<Key>", disableInput)

    TextAg.place(x=30, y=100)
    TextAg.insert(INSERT, "SOFTWARE USER LICENSE AGREEMENT\nIMPORTANT: READ THIS AGREEMENT CAREFULLY BEFORE INSTALLING OR USING THE SOFTWARE.\nThis Software User License Agreement (Agreement) is a legal agreement between you (either an individual or a single entity) and [Software Company Name] (\"Licensor\") for the software product(s) identified above which may include associated software components, media, printed materials, and \'online\' or electronic documentation (\'Software\').\n By installing, copying, or otherwise using the Software, you agree to be bound by the terms of this Agreement. If you do not agree to the terms of this Agreement, do not install or use the Software.\n1. LICENSE GRANT. Licensor grants to you a non-exclusive, non-transferable license to use the Software on a single computer or device at a time, unless otherwise specified in writing by Licensor.\n2. RESTRICTIONS. You may not copy, modify, distribute, sell, or transfer the Software or any portion thereof without the prior written consent of Licensor. You may not reverse engineer, decompile, or disassemble the Software, except to the extent that such activity is expressly permitted by applicable law.\n3. OWNERSHIP. The Software is owned and copyrighted by Licensor or its third-party suppliers. Your license confers no title or ownership in the Software and is not a sale of any rights in the Software.\n4. WARRANTY DISCLAIMER. THE SOFTWARE IS PROVIDED \"AS IS\" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. LICENSOR DOES NOT WARRANT THAT THE SOFTWARE WILL MEET YOUR REQUIREMENTS OR THAT THE OPERATION OF THE SOFTWARE WILL BE UNINTERRUPTED OR ERROR-FREE.\n5. LIMITATION OF LIABILITY. IN NO EVENT SHALL LICENSOR BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF OR IN CONNECTION WITH THE USE OR INABILITY TO USE THE SOFTWARE (INCLUDING, BUT NOT LIMITED TO, LOSS OF PROFITS, BUSINESS INTERRUPTION, OR LOSS OF DATA), EVEN IF LICENSOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.\n6. TERMINATION. This Agreement will terminate automatically if you fail to comply with any of the terms and conditions of this Agreement. Upon termination, you must immediately cease all use of the Software and destroy all copies of the Software in your possession.\n7. GOVERNING LAW. This Agreement shall be governed by and construed in accordance with the laws of the [State/Province/Country] without giving effect to any choice of law or conflict of law provisions.\n8. ENTIRE AGREEMENT. This Agreement constitutes the entire agreement between you and Licensor with respect to the Software and supersedes all prior or contemporaneous communications and proposals, whether oral or written, between you and Licensor.\nIf you have any questions about this Agreement, please contact [Software Company Name] at [Contact Information].\nBy clicking \"I Agree\" or installing or using the Software, you acknowledge that you have read this Agreement, understand it, and agree to be bound by its terms and conditions.")
    # this is used to disable the text box so that the user cannot edit the text. Must be used after inserting the text otherwise the entire text will be disabled.
    TextAg.config(state=DISABLED)

    def actNext():
        if x.get() == 1 and y.get() == 1:
            nextButton.config(state=ACTIVE)
        else:
            nextButton.config(state=DISABLED)

    x = IntVar()  # this is a variable to check if the user has agreed to the agreement or not
    checkAg = Checkbutton(agWin,
                          text="I agree to User License Agreement.",
                          font=("Arial", 10),
                          variable=x,  # this variable is used to check if the user has agreed to the agreement or not
                          onvalue=1,  # if the user has agreed to the agreement then the value of x will be 1
                          offvalue=0,  # if the user has not agreed to the agreement then the value of x will be 0
                          cursor="hand2",
                          command=actNext

                          )
    checkAg.place(x=30, y=450)
    y = IntVar()  # this is a variable to check if the user has agreed to the agreement or not
    checkTerms = Checkbutton(agWin,
                             text="I agree to Terms and Conditions, Privacy Policy and Cookie Policy.",
                             font=("Arial", 10),
                             variable=y,
                             onvalue=1,
                             offvalue=0,
                             cursor="hand2",
                             command=actNext,
                             )

    checkTerms.place(x=30, y=475)
    nextButton = Button(agWin,
                        text="Next",
                        font=("Arial", 10,),
                        width=10,
                        state=DISABLED,
                        cursor="hand2",
                        command=archSelect
                        )
    nextButton.place(x=450, y=600)
    cancelButton = Button(agWin,
                          text="Cancel",
                          font=("Arial", 10),
                          width=10,
                          cursor="hand2",
                          command=agWin.destroy

                          )
    cancelButton.place(x=550, y=600)
    agWin.mainloop()


agreement()
