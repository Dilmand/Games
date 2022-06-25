import tkinter as tk


class App(tk.Frame):
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry("365x400")
        self.master.resizable(0,0)
        self.master.title("XO")
        
        self.Anfang = True
        self.gewonen = False
        self.list_button_alle = []  
        self.list_button_alle_schonveraendert = []

        self.list_x_alle_Positionen = []
        self.list_x_alle_moeglichkeiten = []
        self.list_o_alle_Positionen = []
        self.list_o_alle_moeglichkeiten= []

        self.position = {
                 0 : "0/0",
                 1 : "1,0",
                 2 : "2/0",
                 3 : "0/1",
                 4 : "1/1",
                 5 : "2/1",
                 6 : "0/2",
                 7 : "1/2",
                 8 : "2/2",
            }
        self.Moeglichkeit= [
                ["0/0","1,0","2/0"],
                ["0/1","1/1","2/1"],
                ["0/2","1/2","2/2"],
                ["0/0","0/1","0/2"],
                ["1,0","1/1","1/2"],
                ["2/0","2/1","2/2"],
                ["0/0","1/1","2/2"],
                ["0/2","1/1","2/0"]
            ]

        tk.Frame.__init__(self, self.master)
        self.create_widgets()
        self.grid()
        self.place()
        self.bind()      

    def create_widgets(self, event=""):
            self.zahlen = []
            for self.row in range(3):
                for self.column in range(3):
                    self.zahlen.append((self.column, self.row))

            for i in self.zahlen:
                self.Button =  tk.Button(self,font= 1, command=lambda i=i:self.handle(self.zahlen.index(i)), height=5, width=10)
                self.Button.grid(column=i[1], row=i[0])
                self.list_button_alle.append(self.Button)
                
    def win(self, args=str):
        for self.widget in self.winfo_children():
            self.widget.destroy()

        self.label = tk.Label(self, text=f"*{args}* hat gewonnen!!!", font=1)
        self.label.place(x = 100, y = 80)
        self.label1 = tk.Label(self, text="Nochmal?--Druck auf den Knopf")
        self.label1.place(x = 100, y = 180)

        self.button_neuanfang = tk.Button(self,command= self.new_start, height=2, width=4, text="^-^", font=1)
        self.button_neuanfang.place(x = 150, y = 280)

    def new_start(self, event=""):
        for self.widget in self.winfo_children():
            self.widget.destroy()
        del self.list_button_alle[:]
        del self.list_button_alle_schonveraendert[:]
        del self.list_x_alle_Positionen[:]
        del self.list_x_alle_moeglichkeiten[:]
        del self.list_o_alle_Positionen[:]
        del self.list_o_alle_moeglichkeiten[:]
        self.create_widgets()

    def handle(self,event):
        self.button = self.list_button_alle[event]
        #x
        if self.Anfang == True and self.button not in self.list_button_alle_schonveraendert:
            self.button.configure(text =  "X")
            #self.button.grid(ipadx=44, ipady=44)
            self.list_button_alle_schonveraendert.append(self.button)

            self.position_x = self.position[event]
            self.list_x_alle_Positionen.append(self.position_x)

            if len(self.list_x_alle_Positionen) >= 3:
                for self.a in self.list_x_alle_Positionen:
                    for self.b in self.list_x_alle_Positionen:
                        for self.c in self.list_x_alle_Positionen:
                            self.f = [self.a,self.b,self.c]
                            self.list_x_alle_moeglichkeiten.append(self.f)  
        
            if len(self.list_x_alle_Positionen) >= 3:
                for self.i in self.Moeglichkeit:
                    if self.i in self.list_x_alle_moeglichkeiten:
                        self.win("X")
                        self.gewonen = True

            self.Anfang = False
        #o
        elif self.Anfang == False and self.button not in self.list_button_alle_schonveraendert:
            self.button.configure(text = "O")
            #self.button.grid(ipadx=44, ipady=44)
            self.list_button_alle_schonveraendert.append(self.button)

            self.position_o = self.position[event]
            self.list_o_alle_Positionen.append(self.position_o)

            if len(self.list_o_alle_Positionen)>=3:
                for self.a in self.list_o_alle_Positionen:
                    for self.b in self.list_o_alle_Positionen:
                        for self.c in self.list_o_alle_Positionen:
                            self.d = [self.a,self.b,self.c]
                            self.list_o_alle_moeglichkeiten.append(self.d)
            
            if len(self.list_o_alle_Positionen) >= 3:
                for self.i in self.Moeglichkeit:
                    if self.i in self.list_o_alle_moeglichkeiten:
                        self.gewonen = True
                        self.win("O")
            
            self.Anfang = True
            
        self.a = len(self.list_x_alle_Positionen)
        self.b = len(self.list_o_alle_Positionen)  
        if self.a + self.b == 9:
            self.win("Keiner")
            
app = App()
app.mainloop()