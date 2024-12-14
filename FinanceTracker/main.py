from gui import *



def main():
    window = Tk()
    window.title("Budget")
    window.geometry('290x270')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()