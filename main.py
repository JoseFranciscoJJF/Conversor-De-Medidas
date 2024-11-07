import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from decimal import *


class System(ctk.CTk):

    def submit(self):
        left = self.left_value.get()
        right = self.right_value.get()
        was = self.left_combobox.get()
        will = self.right_combobox.get()
        if was == will:
            messagebox.showwarning('Atenção','Selecione unidades difeentes.')
        elif str(self.left_value).count(',')!=0:
            messagebox.showwarning('Atenção','Precisa digitar ponto ´.´ ao invés da vírgula ´,´.')
        elif str(self.left_value).strip()=='':
            messagebox.showwarning('Atenção','Digite um número real.')
        else:
            print(f' Left = {left}  |  right = {right}')
            print(f'\n de = {was}  |  para = {will}')
        
            if self.button==1:
                self.converting_area(was, will)
            elif self.button==2:
                self.converting_longitude(was, will)
            elif self.button==3:
                self.converting_density(was, will)
            elif self.button==4:
                self.converting_energy(was, will)
            elif self.button==5:
                self.converting_weight(was, will)
            elif self.button==6:
                self.converting_prection(was, will)
            elif self.button==7:
                self.converting_temperatura(was, will)
            elif self.button==8:
                self.converting_time(was, will)
            elif self.button==9:
                self.converting_volume(was, will)
            
            #del self.category[:]
            #self.category.append('Homem')
            #self.category.append('Mulher')
            #self.left_combobox.set(self.category[0])
            #self.right_combobox.set(self.category[0])
            #self.left_combobox.configure(values=self.category)
            #self.right_combobox.configure(values=self.category)
        pass
    
    def help(self):
        messagebox.showinfo('Sobre nós','Este produto de software é o resultado de análises e investigações acerca das Unidades De Medida mais sonantes no SI.\nServe para agregar soluções rápidas e aprendizado com relação à temática.\n\tSistema  De Conversão De Medidas\n\n\t@coppyright J2F AllRightsReserved')
    
    def clear(self):
        self.left_value.set('')
        self.right_value.set('')
    
    def area(self):
        self.title.configure(text='Área')
        del self.category[:]
        self.category.append('Quilometros Quadrados')
        self.category.append('Hectares')
        self.category.append('Acres')
        self.category.append('Metros Quadrados')
        self.category.append('Jardas Quadradas')
        self.category.append('Pés Quadrados')
        self.category.append('Centimetros Quadrados')
        self.category.append('Milimetros Quadrados')
        self.button = 1
        self.click(self.button)
        pass
    
    def density(self):
        self.title.configure(text='Densidade')
        del self.category[:]
        self.category.append('Quilograma Por Metro Cúbico')
        self.category.append('Quilograma Por Litros')
        self.category.append('Quilograma Por Centimetro Cúbico')
        self.category.append('Grama Por Metro Cúbico')
        self.category.append('Grama Por Litros')
        self.category.append('Grama Por Centimetro Cúbico')
        self.button = 3
        self.click(self.button)
        pass
    def energy(self):
        self.title.configure(text='Energia')
        del self.category[:]
        self.category.append('QuiloWatt-Hora')
        self.category.append('Caloria')
        self.category.append('Joule')
        self.button = 4
        self.click(self.button)
        pass
        
    def longitude(self):
        self.title.configure(text='Comprimento')
        del self.category[:]
        self.category.append('Milhas Náuticas')
        self.category.append('Milhas')
        self.category.append('Quilometros')
        self.category.append('Furlong')
        self.category.append('Metros')
        self.category.append('Jardas')
        self.category.append('Varas')
        self.category.append('Pés')
        self.category.append('Palmos')
        self.category.append('Polegadas')
        self.category.append('Centímetros')
        self.category.append('Milimetros')
        self.button = 2
        self.click(self.button)
        pass
    
    def prection(self):
        self.title.configure(text='Pressão')
        del self.category[:]
        self.category.append('Pascal')
        self.category.append('Atmosfera')
        self.category.append('Milímetro de Mercúrio')
        self.category.append('Bar')
        self.button = 6
        self.click(self.button)
        pass

    def time(self):
        self.title.configure(text='Tempo')
        del self.category[:]
#        self.category.append('Milénio')
        self.category.append('Século')
        self.category.append('Década')
        self.category.append('Ano')
        self.category.append('Mês')
        self.category.append('Semana')
        self.category.append('Dia')
        self.category.append('Hora')
        self.category.append('Minuto')
        self.category.append('Segundo')
        self.button = 8
        self.click(self.button)
        pass

    def weight(self):
        self.title.configure(text='Massa')
        del self.category[:]
        self.category.append('Toneladas')
        self.category.append('Stone')
        self.category.append('Quilogramas')
        self.category.append('Libras')
        self.category.append('Onças')
        self.category.append('Gramas')
        self.category.append('Mililitros')
        self.category.append('Miligramas')
        self.button = 5
        self.click(self.button)
        pass
    
    def verify(self):
        if str(self.btn_submit)=='Salvar Dados'.upper():
            print('Eu não existo!')
        else:
            print('Assim está bom?')
        pass

    def volume(self):
        self.title.configure(text='Volume')
        del self.category[:]
        self.category.append('Metros Cúbicos')
        self.category.append('Jardas Cúbicas')
        self.category.append('Pés Cúbicos')
        self.category.append('Litros')
        self.category.append('Galões')
        self.category.append('Mililitros')
        self.category.append('Quart')
        self.category.append('Pint')
        self.category.append('Onça Líquida')
        self.button = 9
        self.click(self.button)
        pass
    
    
    def temperature(self):
        self.title.configure(text='Temperatura')
        del self.category[:]
        self.category.append('Celsius')
        self.category.append('Fahrenheit')
        self.category.append('Kelvin')
        self.button = 7
        self.click(self.button)
        pass
    
    def button_default(self):
        self.btn_opcao_1.configure(fg_color='blue')
        self.btn_opcao_2.configure(fg_color='blue')
        self.btn_opcao_3.configure(fg_color='blue')
        self.btn_opcao_4.configure(fg_color='blue')
        self.btn_opcao_5.configure(fg_color='blue')
        self.btn_opcao_6.configure(fg_color='blue')
        self.btn_opcao_7.configure(fg_color='blue')
        self.btn_opcao_8.configure(fg_color='blue')
        self.btn_opcao_9.configure(fg_color='blue')
        self.btn_help.configure(fg_color='blue')
    
    global button
    def click(self, button):
        self.left_combobox.set(self.category[0])
        self.right_combobox.set(self.category[0])
        self.left_combobox.configure(values=self.category)
        self.right_combobox.configure(values=self.category)
        self.button_default()
        if button==1:
           self.btn_opcao_1.configure(fg_color='darkblue')
        elif (button==2):
           self.btn_opcao_2.configure(fg_color='darkblue')
        elif (button==3):
           self.btn_opcao_3.configure(fg_color='darkblue')
        elif (button==4):
           self.btn_opcao_4.configure(fg_color='darkblue')
        elif (button==5):
           self.btn_opcao_5.configure(fg_color='darkblue')
        elif (button==6):
           self.btn_opcao_6.configure(fg_color='darkblue')
        elif (button==7):
           self.btn_opcao_7.configure(fg_color='darkblue')
        elif (button==8):
           self.btn_opcao_8.configure(fg_color='darkblue')
        elif (button==9):
           self.btn_opcao_9.configure(fg_color='darkblue')
            
        pass

    # Função De Estilizão do BackGround
    def appearance(self):
        self.lb_apm = ctk.CTkLabel(self, text='Tema', bg_color='transparent', text_color=['#000','#fff']).place(x=650, y=430)
        self.opt_apm = ctk.CTkOptionMenu(self, values=['Dark', 'Light', 'System'], bg_color='transparent', command=self.change_apm).place(x=650, y=460)

    def change_apm(self, nova_aparencia):
        ctk.set_appearance_mode(nova_aparencia)
    
    # Função De Estruturação Dos Principais Componetes Do sISTEMA
    def components(self):
        # Menu
        self.frame = ctk.CTkFrame(self, width=160, height=500, corner_radius=0, bg_color='#00A2E8', fg_color='#00A2E8').place(x=10, y=0)
        self.frame_title = ctk.CTkFrame(self, width=608, height=50, corner_radius=0, bg_color='#00A2E8', fg_color='#00A2E8').place(x=180, y=0)
        self.title = ctk.CTkLabel(self.frame_title, text='Medidas', font=('Century Gothic bold', 24), bg_color='#00A2E8', text_color='#fff')
        self.title.place(x=420, y=10)
        
        self.btn_opcao_1 = ctk.CTkButton(self, width=150, text='Área'.upper(), command=self.area, fg_color='darkblue', hover_color='lightblue')
        self.btn_opcao_1.place(x=15, y=100)
        self.btn_opcao_2 = ctk.CTkButton(self, width=150, text='Comprimento'.upper(), command=self.longitude, fg_color='darkblue', hover_color='lightblue')
        self.btn_opcao_2.place(x=15, y=130)
        self.btn_opcao_3 = ctk.CTkButton(self, width=150, text='Densidade'.upper(), command=self.density, fg_color='darkblue', hover_color='lightblue')
        self.btn_opcao_3.place(x=15, y=160)
        self.btn_opcao_4 = ctk.CTkButton(self, width=150, text='Energia'.upper(), command=self.energy, fg_color='darkblue', hover_color='lightblue')
        self.btn_opcao_4.place(x=15, y=190)
        self.btn_opcao_5 = ctk.CTkButton(self, width=150, text='Massa'.upper(), command=self.weight, fg_color='darkblue', hover_color='lightblue')
        self.btn_opcao_5.place(x=15, y=220)
        self.btn_opcao_6 = ctk.CTkButton(self, width=150, text='Pressão'.upper(), command=self.prection, fg_color='darkblue', hover_color='lightblue')
        self.btn_opcao_6.place(x=15, y=250)
        self.btn_opcao_7 = ctk.CTkButton(self, width=150, text='Temperatura'.upper(), command=self.temperature, fg_color='darkblue', hover_color='lightblue')
        self.btn_opcao_7.place(x=15, y=280)
        self.btn_opcao_8 = ctk.CTkButton(self, width=150, text='Tempo'.upper(), command=self.time, fg_color='darkblue', hover_color='lightblue')
        self.btn_opcao_8.place(x=15, y=310)
        self.btn_opcao_9 = ctk.CTkButton(self, width=150, text='Volume'.upper(), command=self.volume, fg_color='darkblue', hover_color='lightblue')
        self.btn_opcao_9.place(x=15, y=340)
        #
        self.btn_help = ctk.CTkButton(self, width=150, text='Ajuda'.upper(), command=self.help, fg_color='darkblue', hover_color='lightblue')
        self.btn_help.place(x=15, y=460)
        
        # ComboBox
        self.left_combobox = ctk.CTkComboBox(self, values=self.category, font=('Century Gothic bold', 14), width=200)
        self.left_combobox.place(x=200, y=100)
        #left_combobox.pack_configure(side='left')
        self.left_combobox.configure(justify='right')
        #self.left_combobox.pack_configure(padx=100,pady=125)
        
        self.right_combobox = ctk.CTkComboBox(self, values=self.category, font=('Century Gothic bold', 14), width=200)
        self.right_combobox.place(x=590, y=100)
        
        
        # Entrys
        self.entry_left = ctk.CTkEntry(self, width=80, textvariable=self.left_value, font=('Century Gothic bold', 12), fg_color='transparent')
        self.entry_left.place(x=410, y=100)
        self.entry_right = ctk.CTkEntry(self, state='readonly', width=80, textvariable=self.right_value, font=('Century Gothic bold', 12), fg_color='transparent')
        self.entry_right.place(x=500, y=100)
        
        # Buttons
        self.btn_submit = ctk.CTkButton(self, width=150, text='Converter'.upper(), command=self.submit, fg_color='#00A2E8', hover_color='blue')
        self.btn_submit.place(x=420, y=150)
        self.btn_clear = ctk.CTkButton(self, width=150, text='Limpar'.upper(), command=self.clear, fg_color='#999999', hover_color='#787878')
        self.btn_clear.place(x=420, y=185)
        #btn_clear = ctk.CTkButton(main_window, text='Limpar Campos'.upper(), command=clear, fg_color='#555', hover_color='#333')
        #btn_clear.place(x=590, y=150)
        
        self.area() # Iniciando com a primeira opção!
    
    
    def converting_area(self, was, will):
        if was.upper()=='METROS QUADRADOS':
            if will.upper()=='METROS QUADRADOS':
                pass
            elif will.lower() =='centimetros quadrados':
                self.right_value.set('')
                self.right_value.set(str(float(self.left_value.get())*10000))
                print(f'\n Left = {self.right_value.get()}')
            elif will.upper()=='MILiMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*1000000))
            elif will.upper()=='QUILOMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())/1000000))
            elif will.upper()=='ACRES':
                self.right_value.set(str(float(self.left_value.get())/4046.86))
            elif will.upper()=='HECTARES':
                self.right_value.set(str(float(self.left_value.get())/10000))
            elif will.upper()=='PÉS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*10.7639))
            elif will.upper()=='JARDAS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*1.19599))
            else:
                print('\nRevisar Escrita!')
        elif was.upper()=='CENTIMETROS QUADRADOS':
            if will.upper()=='METROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())/10000))
            elif will.upper()=='CENTIMETROS QUADRADOS':
                pass
            elif will.upper()=='MILIMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*100))
            elif will.upper()=='QUILOMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())/10000000))
            elif will.upper()=='ACRES':
                self.right_value.set(str(float(self.left_value.get())/40468600))
            elif will.upper()=='HECTARES':
                self.right_value.set(str(float(self.left_value.get())/100000))
            elif will.upper()=='PÉS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())/929.0304))
            elif will.upper()=='JARDAS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())/8361.273))
        elif was.upper()=='MILIMETROS QUADRADOS':
            if will.upper()=='METROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())/1000000))
            elif will.upper()=='CENTIMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())/100))
            elif will.upper()=='MILIMETROS QUADRADOS':
                pass
            elif will.upper()=='QUILOMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())/1000000000))
            elif will.upper()=='ACRES':
                self.right_value.set(str(float(self.left_value.get())/4046860000))
            elif will.upper()=='HECTARES':
                self.right_value.set(str(float(self.left_value.get())/100000000))
            elif will.upper()=='PÉS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())/9290304))
            elif will.upper()=='JARDAS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())/83612736))
        elif was.upper()=='QUILOMETROS QUADRADOS':
            if will.upper()=='METROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*1000000))
            elif will.upper()=='CENTIMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*10000000))
            elif will.upper()=='MILIMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*1000000000))
            elif will.upper()=='QUILOMETROS QUADRADOS':
                pass
            elif will.upper()=='ACRES':
                self.right_value.set(str(float(self.left_value.get())*247.105))
            elif will.upper()=='HECTARES':
                self.right_value.set(str(float(self.left_value.get())*100))
            elif will.upper()=='PÉS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*10763910.4))
            elif will.upper()=='JARDAS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*1195990))
        elif was.upper()=='ACRES':
            if will.upper()=='METROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*4046.86))
            elif will.upper()=='CENTIMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*40458600))
            elif will.upper()=='MILIMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*4045860000))
            elif will.upper()=='QUILOMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())/247.105))
            elif will.upper()=='ACRES':
                pass
            elif will.upper()=='HECTARES':
                self.right_value.set(str(float(self.left_value.get())/2.471))
            elif will.upper()=='PÉS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*43.560))
            elif will.upper()=='JARDAS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*4840))
        elif was.upper()=='HECTARES':
            if will.upper()=='METROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*10000))
            elif will.upper()=='CENTIMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*10000000))
            elif will.upper()=='MILIMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*10000000000))
            elif will.upper()=='QUILOMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())/100))
            elif will.upper()=='ACRES':
                self.right_value.set(str(float(self.left_value.get())*2.471))
            elif will.upper()=='HECTARES':
                pass
            elif will.upper()=='PÉS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*107639))
            elif will.upper()=='JARDAS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*11959.9))
        elif was.upper()=='PÉS QUADRADOS':
            if will.upper()=='METROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())/10.7639))
            elif will.upper()=='CENTIMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*929.0304))
            elif will.upper()=='MILIMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*9290304))
            elif will.upper()=='QUILOMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())/10763910.4))
            elif will.upper()=='ACRES':
                self.right_value.set(str(float(self.left_value.get())/43.560))
            elif will.upper()=='HECTARES':
                self.right_value.set(str(float(self.left_value.get())/107639))
            elif will.upper()=='PÉS QUADRADOS':
                pass
            elif will.upper()=='JARDAS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*0.111114311196997))
        elif was.upper()=='JARDAS QUADRADOS':
            if will.upper()=='METROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())/1.19599))
            elif will.upper()=='CENTIMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*8361.273))
            elif will.upper()=='MILIMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())*83612736))
            elif will.upper()=='QUILOMETROS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())/1195900))
            elif will.upper()=='ACRES':
                self.right_value.set(str(float(self.left_value.get())/4840))
            elif will.upper()=='HECTARES':
                self.right_value.set(str(float(self.left_value.get())/11959.9))
            elif will.upper()=='PÉS QUADRADOS':
                self.right_value.set(str(float(self.left_value.get())/12.873516761))
            elif will.upper()=='JARDAS QUADRADOS':
                pass
        pass
    def converting_longitude(self, was, will):
        if  was.upper()=='METROS':
            if will.upper()=='METROS':
                pass
            elif will =='Centímetros':
                self.right_value.set(str(float(self.left_value.get())*100))
            elif will.upper()=='MILIMETROS':
                self.right_value.set(str(float(self.left_value.get())*1000))
            elif will.upper()=='QUILOMETROS':
                self.right_value.set(str(float(self.left_value.get())/1000))
            elif will.upper()=='POLEGADAS':
                self.right_value.set(str(float(self.left_value.get())/0.0254))
            elif will.upper()=='PÉS':
                self.right_value.set(str(float(self.left_value.get())/0.3048))
            elif will.upper()=='JARDAS':
                self.right_value.set(str(float(self.left_value.get())/0.9144))
            elif will.upper()=='MILHAS':
                self.right_value.set(str(float(self.left_value.get())/1609.34))
            elif will =='Milhas Náuticas':
                self.right_value.set(str(float(self.left_value.get())/1852))
            elif will.upper()=='PALMOS':
                self.right_value.set(str(float(self.left_value.get())/0.2))
            elif will.upper()=='VARAS':
                self.right_value.set(str(float(self.left_value.get())*0.839))
            elif will.upper()=='FURLONG':
                self.right_value.set(str(float(self.left_value.get())/201.168))
            else:
               print('\nRevise a Escrita!')
        if  was =='Centímetros':
            if will.upper()=='METROS':
                self.right_value.set(str(float(self.left_value.get())/100))
            elif will =='Centímetros':
                pass
            elif will.upper()=='MILIMETROS':
                self.right_value.set(str(float(self.left_value.get())*10))
            elif will.upper()=='QUILOMETROS':
                self.right_value.set(str(float(self.left_value.get())/100000))
            elif will.upper()=='POLEGADAS':
                self.right_value.set(str(float(self.left_value.get())/2.54))
            elif will.upper()=='PÉS':
                self.right_value.set(str(float(self.left_value.get())/30.48))
            elif will.upper()=='JARDAS':
                self.right_value.set(str(float(self.left_value.get())/91.44))
            elif will.upper()=='MILHAS':
                self.right_value.set(str(float(self.left_value.get())/160934))
            elif will =='Milhas Náuticas':
                self.right_value.set(str(float(self.left_value.get())/185200))
            elif will.upper()=='PALMOS':
                self.right_value.set(str(float(self.left_value.get())/20))
            elif will.upper()=='VARAS':
                self.right_value.set(str(float(self.left_value.get())/83.9))
            elif will.upper()=='FURLONG':
                self.right_value.set(str(float(self.left_value.get())/20116.8))
            else:
               print('\nRevise a Escrita!')
        if  was =='Milimetros':
            if will.upper()=='METROS':
                self.right_value.set(str(float(self.left_value.get())/1000))
            elif will =='Centímetros':
                self.right_value.set(str(float(self.left_value.get())/10))
            elif will.upper()=='MILIMETROS':
                pass
            elif will.upper()=='QUILOMETROS':
                self.right_value.set(str(float(self.left_value.get())/1000000))
            elif will.upper()=='POLEGADAS':
                self.right_value.set(str(float(self.left_value.get())/25.4))
            elif will.upper()=='PÉS':
                self.right_value.set(str(float(self.left_value.get())/304.8))
            elif will.upper()=='JARDAS':
                self.right_value.set(str(float(self.left_value.get())/914.4))
            elif will.upper()=='MILHAS':
                self.right_value.set(str(float(self.left_value.get())/1609344))
            elif will.upper()=='MILHAS NÁUTICAS':
                self.right_value.set(str(float(self.left_value.get())/1852000))
            elif will.upper()=='PALMOS':
                self.right_value.set(str(float(self.left_value.get())/200))
            elif will.upper()=='VARAS':
                self.right_value.set(str(float(self.left_value.get())/839))
            elif will.upper()=='FURLONG':
                self.right_value.set(str(float(self.left_value.get())/201168))
            else:
               print('\nRevise a Escrita!')
        if  was =='Quilometros':
            if will.upper()=='METROS':
                self.right_value.set(str(float(self.left_value.get())*1000))
            elif will =='Centímetros':
                self.right_value.set(str(float(self.left_value.get())*100000))
            elif will.upper()=='MILIMETROS':
                self.right_value.set(str(float(self.left_value.get())*1000000))
            elif will.upper()=='QUILOMETROS':
                pass
            elif will.upper()=='POLEGADAS':
                self.right_value.set(str(float(self.left_value.get())*39370.1))
            elif will.upper()=='PÉS':
                self.right_value.set(str(float(self.left_value.get())*3280.84))
            elif will.upper()=='JARDAS':
                self.right_value.set(str(float(self.left_value.get())*1093.61))
            elif will.upper()=='MILHAS':
                self.right_value.set(str(float(self.left_value.get())/1.60934))
            elif will.upper()=='MILHAS NÁUTICAS':
                self.right_value.set(str(float(self.left_value.get())/1.852000))
            elif will.upper()=='PALMOS':
                self.right_value.set(str(float(self.left_value.get())/0.0002))
            elif will.upper()=='VARAS':
                self.right_value.set(str(float(self.left_value.get())*1191.89511323))
            elif will.upper()=='FURLONG':
                self.right_value.set(str(float(self.left_value.get())/0.201168))
            else:
               print('\nRevise a Escrita!')
        if  was =='Polegadas':
            if will.upper()=='METROS':
                self.right_value.set(str(float(self.left_value.get())*0.0254))
            elif will =='Centímetros':
                self.right_value.set(str(float(self.left_value.get())*2.54))
            elif will.upper()=='MILIMETROS':
                self.right_value.set(str(float(self.left_value.get())*25.4))
            elif will.upper()=='QUILOMETROS':
                self.right_value.set(str(float(self.left_value.get())/39370.1))
            elif will.upper()=='POLEGADAS':
                pass
            elif will.upper()=='PÉS':
                self.right_value.set(str(float(self.left_value.get())/12))
            elif will.upper()=='JARDAS':
                self.right_value.set(str(float(self.left_value.get())/36))
            elif will.upper()=='MILHAS':
                self.right_value.set(str(float(self.left_value.get())/63360))
            elif will.upper()=='MILHAS NÁUTICAS':
                self.right_value.set(str(float(self.left_value.get())/72913.3858267))
            elif will.upper()=='PALMOS':
                self.right_value.set(str(float(self.left_value.get())/8))
            elif will.upper()=='VARAS':
                self.right_value.set(str(float(self.left_value.get())/33.031496))
            elif will.upper()=='FURLONG':
                self.right_value.set(str(float(self.left_value.get())/7920))
            else:
               print('\nRevise a Escrita!')
        if  was =='Pés':
            if will.upper()=='METROS':
                self.right_value.set(str(float(self.left_value.get())*0.3048))
            elif will =='Centímetros':
                self.right_value.set(str(float(self.left_value.get())*30.48))
            elif will.upper()=='MILIMETROS':
                self.right_value.set(str(float(self.left_value.get())*304.8))
            elif will.upper()=='QUILOMETROS':
                self.right_value.set(str(float(self.left_value.get())/3280.84))
            elif will.upper()=='POLEGADAS':
                self.right_value.set(str(float(self.left_value.get())*12))
            elif will.upper()=='PÉS':
                pass
            elif will.upper()=='JARDAS':
                self.right_value.set(str(float(self.left_value.get())/3))
            elif will.upper()=='MILHAS':
                self.right_value.set(str(float(self.left_value.get())/5280))
            elif will.upper()=='MILHAS NÁUTICAS':
                self.right_value.set(str(float(self.left_value.get())/6076.115485))
            elif will.upper()=='PALMOS':
                self.right_value.set(str(float(self.left_value.get())/0.656167979))
            elif will.upper()=='VARAS':
                self.right_value.set(str(float(self.left_value.get())/2.752624671))
            elif will.upper()=='FURLONG':
                self.right_value.set(str(float(self.left_value.get())/660))
            else:
               print('\nRevise a Escrita!')
        if  was =='Jardas':
            if will.upper()=='METROS':
                self.right_value.set(str(float(self.left_value.get())*0.9144))
            elif will =='Centímetros':
                self.right_value.set(str(float(self.left_value.get())*91.44))
            elif will.upper()=='MILIMETROS':
                self.right_value.set(str(float(self.left_value.get())*914.4))
            elif will.upper()=='QUILOMETROS':
                self.right_value.set(str(float(self.left_value.get())/1093.61))
            elif will.upper()=='POLEGADAS':
                self.right_value.set(str(float(self.left_value.get())*36))
            elif will.upper()=='PÉS':
                self.right_value.set(str(float(self.left_value.get())*3))
            elif will.upper()=='JARDAS':
                pass
            elif will.upper()=='MILHAS':
                self.right_value.set(str(float(self.left_value.get())/1760))
            elif will.upper()=='MILHAS NÁUTICAS':
                self.right_value.set(str(float(self.left_value.get())/2025.3718285))
            elif will.upper()=='PALMOS':
                self.right_value.set(str(float(self.left_value.get())*6))
            elif will.upper()=='VARAS':
                self.right_value.set(str(float(self.left_value.get())/0.9175415573))
            elif will.upper()=='FURLONG':
                self.right_value.set(str(float(self.left_value.get())/220))
            else:
               print('\nRevise a Escrita!')
        if  was =='Milhas':
            if will.upper()=='METROS':
                self.right_value.set(str(float(self.left_value.get())*1609.34))
            elif will =='Centímetros':
                self.right_value.set(str(float(self.left_value.get())*160934))
            elif will.upper()=='MILIMETROS':
                self.right_value.set(str(float(self.left_value.get())*1609344))
            elif will.upper()=='QUILOMETROS':
                self.right_value.set(str(float(self.left_value.get())*1.6034))
            elif will.upper()=='POLEGADAS':
                self.right_value.set(str(float(self.left_value.get())*63360))
            elif will.upper()=='PÉS':
                self.right_value.set(str(float(self.left_value.get())*5280))
            elif will.upper()=='JARDAS':
                self.right_value.set(str(float(self.left_value.get())*1760))
            elif will.upper()=='MILHAS':
                pass
            elif will.upper()=='MILHAS NÁUTICAS':
                self.right_value.set(str(float(self.left_value.get())*0.8689163))
            elif will.upper()=='PALMOS':
                self.right_value.set(str(float(self.left_value.get())*8046.32))
            elif will.upper()=='VARAS':
                self.right_value.set(str(float(self.left_value.get())*1918.1692491))
            elif will.upper()=='FURLONG':
                self.right_value.set(str(float(self.left_value.get())*8))
            else:
               print('\nRevise a Escrita!')
        if  was =='Palmos':
            if will.upper()=='METROS':
                self.right_value.set(str(float(self.left_value.get())*0.20))
            elif will =='Centímetros':
                self.right_value.set(str(float(self.left_value.get())*20))
            elif will.upper()=='MILIMETROS':
                self.right_value.set(str(float(self.left_value.get())*200))
            elif will.upper()=='QUILOMETROS':
                self.right_value.set(str(float(self.left_value.get())*0.0002))
            elif will.upper()=='POLEGADAS':
                self.right_value.set(str(float(self.left_value.get())*7.874))
            elif will.upper()=='PÉS':
                self.right_value.set(str(float(self.left_value.get())*0.166667))
            elif will.upper()=='JARDAS':
                self.right_value.set(str(float(self.left_value.get())*0.0555556))
            elif will.upper()=='MILHAS':
                self.right_value.set(str(float(self.left_value.get())*0.000124274384))
            elif will.upper()=='MILHAS NÁUTICAS':
                self.right_value.set(str(float(self.left_value.get())*0.00010799136))
            elif will.upper()=='PALMOS':
                pass
            elif will.upper()=='VARAS':
                self.right_value.set(str(float(self.left_value.get())*0.238379))
            elif will.upper()=='FURLONG':
                self.right_value.set(str(float(self.left_value.get())*0.00099341939))
            elif will.upper()=='ANO-LUZ':
                self.right_value.set(str(float(self.left_value.get())/9461000000000000000))
            else:
               print('\nRevise a Escrita!')
        if  was =='Milhas Náuticas':
            if will.upper()=='METROS':
                self.right_value.set(str(float(self.left_value.get())*1852))
            elif will =='Centímetros':
                self.right_value.set(str(float(self.left_value.get())*185200))
            elif will.upper()=='MILIMETROS':
                self.right_value.set(str(float(self.left_value.get())*1852000))
            elif will.upper()=='QUILOMETROS':
                self.right_value.set(str(float(self.left_value.get())*1.852))
            elif will.upper()=='POLEGADAS':
                self.right_value.set(str(float(self.left_value.get())*72913.3858267))
            elif will.upper()=='PÉS':
                self.right_value.set(str(float(self.left_value.get())*6076.1154485))
            elif will.upper()=='JARDAS':
                self.right_value.set(str(float(self.left_value.get())*2025.371828521))
            elif will.upper()=='MILHAS':
                self.right_value.set(str(float(self.left_value.get())*1.150779448))
            elif will.upper()=='MILHAS NÁUTICAS':
                pass
            elif will.upper()=='PALMOS':
                self.right_value.set(str(float(self.left_value.get())*9260))
            elif will.upper()=='VARAS':
                self.right_value.set(str(float(self.left_value.get())*2027.38977497))
            elif will.upper()=='FURLONG':
                self.right_value.set(str(float(self.left_value.get())*9.206235))
            else:
               print('\nRevise a Escrita!')
        if  was =='Varas':
            if will.upper()=='METROS':
                self.right_value.set(str(float(self.left_value.get())*0.839))
            elif will =='Centímetros':
                self.right_value.set(str(float(self.left_value.get())*83.90))
            elif will.upper()=='MILIMETROS':
                self.right_value.set(str(float(self.left_value.get())*839))
            elif will.upper()=='QUILOMETROS':
                self.right_value.set(str(float(self.left_value.get())*0.000839))
            elif will.upper()=='POLEGADAS':
                self.right_value.set(str(float(self.left_value.get())*33.031496))
            elif will.upper()=='PÉS':
                self.right_value.set(str(float(self.left_value.get())*2.752824671916))
            elif will.upper()=='JARDAS':
                self.right_value.set(str(float(self.left_value.get())*0.9175415573))
            elif will.upper()=='MILHAS':
                self.right_value.set(str(float(self.left_value.get())*0.00052133043))
            elif will.upper()=='MILHAS NÁUTICAS':
                self.right_value.set(str(float(self.left_value.get())*0.000453023758))
            elif will.upper()=='PALMOS':
                self.right_value.set(str(float(self.left_value.get())*4.195))
            elif will.upper()=='VARAS':
                pass
            elif will.upper()=='FURLONG':
                self.right_value.set(str(float(self.left_value.get())*0.0041706434))
            else:
               print('\nRevise a Escrita!')
        if  was =='Furlong':
            if will.upper()=='METROS':
                self.right_value.set(str(float(self.left_value.get())*201.168))
            elif will =='Centímetros':
                self.right_value.set(str(float(self.left_value.get())*20116.8))
            elif will.upper()=='MILIMETROS':
                self.right_value.set(str(float(self.left_value.get())*201168))
            elif will.upper()=='QUILOMETROS':
                self.right_value.set(str(float(self.left_value.get())*0.201168))
            elif will.upper()=='POLEGADAS':
                self.right_value.set(str(float(self.left_value.get())*7920))
            elif will.upper()=='PÉS':
                self.right_value.set(str(float(self.left_value.get())*660))
            elif will.upper()=='JARDAS':
                self.right_value.set(str(float(self.left_value.get())*220))
            elif will.upper()=='MILHAS':
                self.right_value.set(str(float(self.left_value.get())*0.125))
            elif will.upper()=='MILHAS NÁUTICAS':
                self.right_value.set(str(float(self.left_value.get())*0.10862203))
            elif will.upper()=='PALMOS':
                self.right_value.set(str(float(self.left_value.get())*1005.84))
            elif will.upper()=='VARAS':
                self.right_value.set(str(float(self.left_value.get())*239.771156138))
            elif will.upper()=='FURLONG':
                pass
            else:
               print('\nRevise a Escrita!')

    def converting_density(self, was, will):
        value = float(self.left_value.get())
        
        if was == 'Quilograma Por Metro Cúbico':
            if will == 'Quilograma Por Metro Cúbico':
                self.right_value.set(str(value))
            elif will == 'Quilograma Por Centimetro Cúbico':
                self.right_value.set(str(value * 1000000))
            elif will == 'Quilograma Por Litros':
                self.right_value.set(str(value * 1000))
            elif will == 'Grama Por Metro Cúbico':
                self.right_value.set(str(value * 1000))
            elif will == 'Grama Por Centimetro Cúbico':
                self.right_value.set(str(value * 1000000))
            elif will == 'Grama Por Litros':
                self.right_value.set(str(value * 1e6))
            else:
                print('\nRevise a Escrita!')

        elif was == 'Quilograma Por Centimetro Cúbico':
            if will == 'Quilograma Por Metro Cúbico':
                self.right_value.set(str(value / 1000000))
            elif will == 'Quilograma Por Centimetro Cúbico':
                self.right_value.set(str(value))
            elif will == 'Quilograma Por Litros':
                self.right_value.set(str(value * 1000))
            elif will == 'Grama Por Metro Cúbico':
                self.right_value.set(str(value * 1000))
            elif will == 'Grama Por Centimetro Cúbico':
                self.right_value.set(str(value * 1e6))
            elif will == 'Grama Por Litros':
                self.right_value.set(str(value * 1e3))
            else:
                print('\nRevise a Escrita!')

        elif was == 'Quilograma Por Litros':
            if will == 'Quilograma Por Metro Cúbico':
                self.right_value.set(str(value / 1000))
            elif will == 'Quilograma Por Centimetro Cúbico':
                self.right_value.set(str(value * 1000))
            elif will == 'Quilograma Por Litros':
                self.right_value.set(str(value))
            elif will == 'Grama Por Metro Cúbico':
                self.right_value.set(str(value * 1000))
            elif will == 'Grama Por Centimetro Cúbico':
                self.right_value.set(str(value * 1e6))
            elif will == 'Grama Por Litros':
                self.right_value.set(str(value * 1000))
            else:
                print('\nRevise a Escrita!')

        elif was == 'Grama Por Metro Cúbico':
            if will == 'Quilograma Por Metro Cúbico':
                self.right_value.set(str(value / 1000))
            elif will == 'Quilograma Por Centimetro Cúbico':
                self.right_value.set(str(value / 1000))
            elif will == 'Quilograma Por Litros':
                self.right_value.set(str(value / 1000))
            elif will == 'Grama Por Metro Cúbico':
                self.right_value.set(str(value))
            elif will == 'Grama Por Centimetro Cúbico':
                self.right_value.set(str(value * 1000))
            elif will == 'Grama Por Litros':
                self.right_value.set(str(value / 1000))
            else:
                print('\nRevise a Escrita!')

        elif was == 'Grama Por Centimetro Cúbico':
            if will == 'Quilograma Por Metro Cúbico':
                self.right_value.set(str(value / 1e6))
            elif will == 'Quilograma Por Centimetro Cúbico':
                self.right_value.set(str(value / 1000))
            elif will == 'Quilograma Por Litros':
                self.right_value.set(str(value / 1e3))
            elif will == 'Grama Por Metro Cúbico':
                self.right_value.set(str(value * 1000))
            elif will == 'Grama Por Centimetro Cúbico':
                self.right_value.set(str(value))
            elif will == 'Grama Por Litros':
                self.right_value.set(str(value / 1000))
            else:
                print('\nRevise a Escrita!')

        elif was == 'Grama Por Litros':
            if will == 'Quilograma Por Metro Cúbico':
                self.right_value.set(str(value / 1e3))
            elif will == 'Quilograma Por Centimetro Cúbico':
                self.right_value.set(str(value / 1e6))
            elif will == 'Quilograma Por Litros':
                self.right_value.set(str(value))
            elif will == 'Grama Por Metro Cúbico':
                self.right_value.set(str(value * 1000))
            elif will == 'Grama Por Centimetro Cúbico':
                self.right_value.set(str(value * 1e3))
            elif will == 'Grama Por Litros':
                self.right_value.set(str(value))
            else:
                print('\nRevise a Escrita!')

        else:
            print('\nRevise a Escrita!')

    def converting_energy(self, was, will):
        if was.upper() == 'QUILOWATT-HORA':
            if will.upper() == 'QUILOWATT-HORA':
                pass
            elif will.upper() == 'CALORIA':
                self.right_value.set(str(float(self.left_value.get()) * 860.421))
            elif will.upper() == 'JOULE':
                self.right_value.set(str(float(self.left_value.get()) * 3.6e6))
            elif will.upper() == 'KILOCALORIA':
                self.right_value.set(str(float(self.left_value.get()) * 860.421 / 1000))
        elif was.upper() == 'CALORIA':
            if will.upper() == 'QUILOWATT-HORA':
                self.right_value.set(str(float(self.left_value.get()) / 860.421))
            elif will.upper() == 'CALORIA':
                pass
            elif will.upper() == 'JOULE':
                self.right_value.set(str(float(self.left_value.get()) * 4.184))
            elif will.upper() == 'KILOCALORIA':
                self.right_value.set(str(float(self.left_value.get()) / 1000))
        elif was.upper() == 'JOULE':
            if will.upper() == 'QUILOWATT-HORA':
                self.right_value.set(str(float(self.left_value.get()) / 3.6e6))
            elif will.upper() == 'CALORIA':
                self.right_value.set(str(float(self.left_value.get()) / 4.184))
            elif will.upper() == 'JOULE':
                pass
            elif will.upper() == 'KILOCALORIA':
                self.right_value.set(str(float(self.left_value.get()) / 4184))
        elif was.upper() == 'KILOCALORIA':
            if will.upper() == 'QUILOWATT-HORA':
                self.right_value.set(str(float(self.left_value.get()) * 1.162222e-3))
            elif will.upper() == 'CALORIA':
                self.right_value.set(str(float(self.left_value.get()) * 1000))
            elif will.upper() == 'JOULE':
                self.right_value.set(str(float(self.left_value.get()) * 4184))
            elif will.upper() == 'KILOCALORIA':
                pass
        else:
            pass
        pass
    def converting_weight(self, was, will):
        if was.upper() == 'TONELADAS':
            if will.upper() == 'TONELADAS':
                pass
            elif will.upper() == 'STONE':
                self.right_value.set(str(float(self.left_value.get()) * 157.473))
            elif will.upper() == 'QUILOGRAMAS':
                self.right_value.set(str(float(self.left_value.get()) * 1000))
            elif will.upper() == 'LIBRAS':
                self.right_value.set(str(float(self.left_value.get()) * 2204.62))
            elif will.upper() == 'ONÇAS':
                self.right_value.set(str(float(self.left_value.get()) * 35273.96))
            elif will.upper() == 'GRAMAS':
                self.right_value.set(str(float(self.left_value.get()) * 1000000))
            elif will.upper() == 'MILIGRAMAS':
                self.right_value.set(str(float(self.left_value.get()) * 1000000000))
        elif was.upper() == 'STONE':
            if will.upper() == 'TONELADAS':
                self.right_value.set(str(float(self.left_value.get()) / 157.473))
            elif will.upper() == 'STONE':
                pass
            elif will.upper() == 'QUILOGRAMAS':
                self.right_value.set(str(float(self.left_value.get()) * 6.35029))
            elif will.upper() == 'LIBRAS':
                self.right_value.set(str(float(self.left_value.get()) * 14));
            elif will.upper() == 'ONÇAS':
                self.right_value.set(str(float(self.left_value.get()) * 224));
            elif will.upper() == 'GRAMAS':
                self.right_value.set(str(float(self.left_value.get()) * 6350.29))
            elif will.upper() == 'MILIGRAMAS':
                self.right_value.set(str(float(self.left_value.get()) * 6350290));
        elif was.upper() == 'QUILOGRAMAS':
            if will.upper() == 'TONELADAS':
                self.right_value.set(str(float(self.left_value.get()) / 1000))
            elif will.upper() == 'STONE':
                self.right_value.set(str(float(self.left_value.get()) / 6.35029))
            elif will.upper() == 'QUILOGRAMAS':
                pass
            elif will.upper() == 'LIBRAS':
                self.right_value.set(str(float(self.left_value.get()) * 2.20462))
            elif will.upper() == 'ONÇAS':
                self.right_value.set(str(float(self.left_value.get()) * 35.274))
            elif will.upper() == 'GRAMAS':
                self.right_value.set(str(float(self.left_value.get()) * 1000))
            elif will.upper() == 'MILIGRAMAS':
                self.right_value.set(str(float(self.left_value.get()) * 1000000))
        elif was.upper() == 'LIBRAS':
            if will.upper() == 'TONELADAS':
                self.right_value.set(str(float(self.left_value.get()) / 2204.62))
            elif will.upper() == 'STONE':
                self.right_value.set(str(float(self.left_value.get()) / 14));
            elif will.upper() == 'QUILOGRAMAS':
                self.right_value.set(str(float(self.left_value.get()) / 2.20462))
            elif will.upper() == 'LIBRAS':
                pass
            elif will.upper() == 'ONÇAS':
                self.right_value.set(str(float(self.left_value.get()) * 16));
            elif will.upper() == 'GRAMAS':
                self.right_value.set(str(float(self.left_value.get()) * 453.592));
            elif will.upper() == 'MILIGRAMAS':
                self.right_value.set(str(float(self.left_value.get()) * 453592));
        elif was.upper() == 'ONÇAS':
            if will.upper() == 'TONELADAS':
                self.right_value.set(str(float(self.left_value.get()) / 35273.96))
            elif will.upper() == 'STONE':
                self.right_value.set(str(float(self.left_value.get()) / 224));
            elif will.upper() == 'QUILOGRAMAS':
                self.right_value.set(str(float(self.left_value.get()) / 35.274))
            elif will.upper() == 'LIBRAS':
                self.right_value.set(str(float(self.left_value.get()) / 16));
            elif will.upper() == 'ONÇAS':
                pass
            elif will.upper() == 'GRAMAS':
                self.right_value.set(str(float(self.left_value.get()) * 28.3495));
            elif will.upper() == 'MILIGRAMAS':
                self.right_value.set(str(float(self.left_value.get()) * 28349.5));
        elif was.upper() == 'GRAMAS':
            if will.upper() == 'TONELADAS':
                self.right_value.set(str(float(self.left_value.get()) / 1000000))
            elif will.upper() == 'STONE':
                self.right_value.set(str(float(self.left_value.get()) / 6350.29))
            elif will.upper() == 'QUILOGRAMAS':
                self.right_value.set(str(float(self.left_value.get()) / 1000))
            elif will.upper() == 'LIBRAS':
                self.right_value.set(str(float(self.left_value.get()) / 453.592))
            elif will.upper() == 'ONÇAS':
                self.right_value.set(str(float(self.left_value.get()) / 28.3495))
            elif will.upper() == 'GRAMAS':
                pass
            elif will.upper() == 'MILIGRAMAS':
                self.right_value.set(str(float(self.left_value.get()) * 1000));
        elif was.upper() == 'MILIGRAMAS':
            if will.upper() == 'TONELADAS':
                self.right_value.set(str(float(self.left_value.get()) / 1000000000))
            elif will.upper() == 'STONE':
                self.right_value.set(str(float(self.left_value.get()) / 6350290))
            elif will.upper() == 'QUILOGRAMAS':
                self.right_value.set(str(float(self.left_value.get()) / 1000000))
            elif will.upper() == 'LIBRAS':
                self.right_value.set(str(float(self.left_value.get()) / 453592));
            elif will.upper() == 'ONÇAS':
                self.right_value.set(str(float(self.left_value.get()) / 28349.5));
            elif will.upper() == 'GRAMAS':
                self.right_value.set(str(float(self.left_value.get()) / 1000));
            elif will.upper() == 'MILIGRAMAS':
                pass
        pass
    def converting_prection(self, was, will):
        if was.upper() == 'PASCAL':
            if will.upper() == 'PASCAL':
                pass
            elif will.upper() == 'ATMOSFERA':
                self.right_value.set(str(float(self.left_value.get()) * 0.000009869))
            elif will.upper() == 'MILÍMETRO DE MERCÚRIO':
                self.right_value.set(str(float(self.left_value.get()) * 0.00750062))
            elif will.upper() == 'BAR':
                self.right_value.set(str(float(self.left_value.get()) * 0.00001))
            pass
        elif was.upper() == 'ATMOSFERA':
            if will.upper() == 'PASCAL':
                self.right_value.set(str(float(self.left_value.get()) * 101325))
            elif will.upper() == 'ATMOSFERA':
                pass
            elif will.upper() == 'MILÍMETRO DE MERCÚRIO':
                self.right_value.set(str(float(self.left_value.get()) * 760))
            elif will.upper() == 'BAR':
                self.right_value.set(str(float(self.left_value.get()) * 1.01325))
            pass
        elif was.upper() == 'MiLÍMETRO DE MERCÚRIO':
            if will.upper() == 'PASCAL':
                self.right_value.set(str(float(self.left_value.get()) * 133.322))
            elif will.upper() == 'ATMOSFERA':
                self.right_value.set(str(float(self.left_value.get()) * 0.00131579))
            elif will.upper() == 'MILÍMETRO DE MERCÚRIO':
                pass
            elif will.upper() == 'BAR':
                self.right_value.set(str(float(self.left_value.get()) * 0.00133322))
            pass
        elif was.upper() == 'BAR':
            if will.upper() == 'PASCAL':
                self.right_value.set(str(float(self.left_value.get()) * 100000))
            elif will.upper() == 'ATMOSFERA':
                self.right_value.set(str(float(self.left_value.get()) * 0.980665))
            elif will.upper() == 'MILÍMETRO DE MERCÚRIO':
                self.right_value.set(str(float(self.left_value.get()) * 750.062))
            elif will.upper() == 'BAR':
                pass
            pass
        else:
            print('\n')
        pass
    def converting_temperatura(self, was, will):
        if was.upper() == 'CELSIUS':
            if will.upper() == 'CELSIUS':
                pass
            elif will.upper() == 'FAHRENHEIT':
                self.right_value.set(str(float(self.left_value.get()) * (9/5) + 32))
            elif will.upper() == 'KELVIN':
                self.right_value.set(str(float(self.left_value.get()) + 273.15))
        elif was.upper() == 'FAHRENHEIT':
            if will.upper() == 'CELSIUS':
                self.right_value.set(str(5*(float(self.left_value.get()) - 32)/9))
            elif will.upper() == 'FAHRENHEIT':
                pass
            elif will.upper() == 'KELVIN':
                self.right_value.set(str(273.15+(5/9)*(float(self.left_value.get()) - 32)))
        elif was.upper() == 'KELVIN':
            if will.upper() == 'CELSIUS':
                self.right_value.set(str(float(self.left_value.get()) - 273.15))
            elif will.upper() == 'FAHRENHEIT':
                self.right_value.set(str(32+(9/5)*(float(self.left_value.get()) - 273.15)))
            elif will.upper() == 'KELVIN':
                pass
        else:
            pass
        pass
    def converting_time(self, was, will):
        if was.upper() == 'SEGUNDO':
            if will.upper() == 'SEGUNDO':
                pass
            elif will.upper() == 'MINUTO':
                self.right_value.set(str(float(self.left_value.get()) / 60))
            elif will.upper() == 'HORA':
                self.right_value.set(str(float(self.left_value.get()) / 3600))
            elif will.upper() == 'DIA':
                self.right_value.set(str(float(self.left_value.get()) / 86400))
            elif will.upper() == 'SEMANA':
                self.right_value.set(str(float(self.left_value.get()) / 604800))
            elif will.upper() == 'MÊS':
                self.right_value.set(str(float(self.left_value.get()) / 2629746))
            elif will.upper() == 'ANO':
                self.right_value.set(str(float(self.left_value.get()) / 31556952))
            elif will.upper() == 'DÉCADA':
                self.right_value.set(str(float(self.left_value.get()) / 315569520))
            elif will.upper() == 'SÉCULO':
                self.right_value.set(str(float(self.left_value.get()) / 3155695200))
        elif was.upper() == 'MINUTO':
            if will.upper() == 'SEGUNDO':
                self.right_value.set(str(float(self.left_value.get()) * 60))
            elif will.upper() == 'MINUTO':
                pass
            elif will.upper() == 'HORA':
                self.right_value.set(str(float(self.left_value.get()) / 60))
            elif will.upper() == 'DIA':
                self.right_value.set(str(float(self.left_value.get()) / 1440))
            elif will.upper() == 'SEMANA':
                self.right_value.set(str(float(self.left_value.get()) / 10080))
            elif will.upper() == 'MÊS':
                self.right_value.set(str(float(self.left_value.get()) / 43800))
            elif will.upper() == 'ANO':
                self.right_value.set(str(float(self.left_value.get()) / 525600))
            elif will.upper() == 'DÉCADA':
                self.right_value.set(str(float(self.left_value.get()) / 5256000))
            elif will.upper() == 'SÉCULO':
                self.right_value.set(str(float(self.left_value.get()) / 52560000))
        elif was.upper() == 'HORA':
            if will.upper() == 'SEGUNDO':
                self.right_value.set(str(float(self.left_value.get()) * 3600))
            elif will.upper() == 'MINUTO':
                self.right_value.set(str(float(self.left_value.get()) * 60))
            elif will.upper() == 'HORA':
                pass
            elif will.upper() == 'DIA':
                self.right_value.set(str(float(self.left_value.get()) / 24))
            elif will.upper() == 'SEMANA':
                self.right_value.set(str(float(self.left_value.get()) / 168))
            elif will.upper() == 'MÊS':
                self.right_value.set(str(float(self.left_value.get()) / 730))
            elif will.upper() == 'ANO':
                self.right_value.set(str(float(self.left_value.get()) / 8760))
            elif will.upper() == 'DÉCADA':
                self.right_value.set(str(float(self.left_value.get()) / 87600))
            elif will.upper() == 'SÉCULO':
                self.right_value.set(str(float(self.left_value.get()) / 876000))
        elif was.upper() == 'DIA':
            if will.upper() == 'SEGUNDO':
                self.right_value.set(str(float(self.left_value.get()) * 86400))
            elif will.upper() == 'MINUTO':
                self.right_value.set(str(float(self.left_value.get()) * 1440))
            elif will.upper() == 'HORA':
                self.right_value.set(str(float(self.left_value.get()) * 24))
            elif will.upper() == 'DIA':
                pass
            elif will.upper() == 'SEMANA':
                self.right_value.set(str(float(self.left_value.get()) / 7))
            elif will.upper() == 'MÊS':
                self.right_value.set(str(float(self.left_value.get()) / 30.44))
            elif will.upper() == 'ANO':
                self.right_value.set(str(float(self.left_value.get()) / 365))
            elif will.upper() == 'DÉCADA':
                self.right_value.set(str(float(self.left_value.get()) / 3650))
            elif will.upper() == 'SÉCULO':
                self.right_value.set(str(float(self.left_value.get()) / 36500))
        elif was.upper() == 'SEMANA':
            if will.upper() == 'SEGUNDO':
                self.right_value.set(str(float(self.left_value.get()) * 604800))
            elif will.upper() == 'MINUTO':
                self.right_value.set(str(float(self.left_value.get()) * 10080))
            elif will.upper() == 'HORA':
                self.right_value.set(str(float(self.left_value.get()) * 168))
            elif will.upper() == 'DIA':
                self.right_value.set(str(float(self.left_value.get()) * 7))
            elif will.upper() == 'SEMANA':
                pass
            elif will.upper() == 'MÊS':
                self.right_value.set(str(float(self.left_value.get()) * 4.34524))
            elif will.upper() == 'ANO':
                self.right_value.set(str(float(self.left_value.get()) / 52.1429))
            elif will.upper() == 'DÉCADA':
                self.right_value.set(str(float(self.left_value.get()) / 521.429))
            elif will.upper() == 'SÉCULO':
                self.right_value.set(str(float(self.left_value.get()) / 5214.29))
        elif was.upper() == 'MÊS':
            if will.upper() == 'SEGUNDO':
                self.right_value.set(str(float(self.left_value.get()) * 2629746))
            elif will.upper() == 'MINUTO':
                self.right_value.set(str(float(self.left_value.get()) * 43800))
            elif will.upper() == 'HORA':
                self.right_value.set(str(float(self.left_value.get()) * 730))
            elif will.upper() == 'DIA':
                self.right_value.set(str(float(self.left_value.get()) * 30.44))
            elif will.upper() == 'SEMANA':
                self.right_value.set(str(float(self.left_value.get()) * 12))
            elif will.upper() == 'MÊS':
                pass
            elif will.upper() == 'ANO':
                self.right_value.set(str(float(self.left_value.get()) / 12))
            elif will.upper() == 'DÉCADA':
                self.right_value.set(str(float(self.left_value.get()) / 120));
            elif will.upper() == 'SÉCULO':
                self.right_value.set(str(float(self.left_value.get()) / 1200));
        elif was.upper() == 'ANO':
            if will.upper() == 'SEGUNDO':
                self.right_value.set(str(float(self.left_value.get()) * 31556952))
            elif will.upper() == 'MINUTO':
                self.right_value.set(str(float(self.left_value.get()) * 525600))
            elif will.upper() == 'HORA':
                self.right_value.set(str(float(self.left_value.get()) * 8760))
            elif will.upper() == 'DIA':
                self.right_value.set(str(float(self.left_value.get()) * 365))
            elif will.upper() == 'SEMANA':
                self.right_value.set(str(float(self.left_value.get()) * 52.1429))
            elif will.upper() == 'MÊS':
                self.right_value.set(str(float(self.left_value.get()) * 12));
            elif will.upper() == 'DÉCADA':
                self.right_value.set(str(float(self.left_value.get()) / 10));
            elif will.upper() == 'SÉCULO':
                self.right_value.set(str(float(self.left_value.get()) / 100));
        elif was.upper() == 'DÉCADA':
            if will.upper() == 'SEGUNDO':
                self.right_value.set(str(float(self.left_value.get()) * 315569520))
            elif will.upper() == 'MINUTO':
                self.right_value.set(str(float(self.left_value.get()) * 5256000))
            elif will.upper() == 'HORA':
                self.right_value.set(str(float(self.left_value.get()) * 87600))
            elif will.upper() == 'DIA':
                self.right_value.set(str(float(self.left_value.get()) * 3650))
            elif will.upper() == 'SEMANA':
                self.right_value.set(str(float(self.left_value.get()) * 521.429))
            elif will.upper() == 'MÊS':
                self.right_value.set(str(float(self.left_value.get()) * 120));
            elif will.upper() == 'ANO':
                self.right_value.set(str(float(self.left_value.get()) * 10));
            elif will.upper() == 'DÉCADA':
                pass
            elif will.upper() == 'SÉCULO':
                self.right_value.set(str(float(self.left_value.get()) / 10));
        elif was.upper() == 'SÉCULO':
            if will.upper() == 'SEGUNDO':
                self.right_value.set(str(float(self.left_value.get()) * 3155695200))
            elif will.upper() == 'MINUTO':
                self.right_value.set(str(float(self.left_value.get()) * 52560000))
            elif will.upper() == 'HORA':
                self.right_value.set(str(float(self.left_value.get()) * 876000))
            elif will.upper() == 'DIA':
                self.right_value.set(str(float(self.left_value.get()) * 36500))
            elif will.upper() == 'SEMANA':
                self.right_value.set(str(float(self.left_value.get()) * 5214.29))
            elif will.upper() == 'MÊS':
                self.right_value.set(str(float(self.left_value.get()) * 120));
            elif will.upper() == 'ANO':
                self.right_value.set(str(float(self.left_value.get()) * 100));
            elif will.upper() == 'DÉCADA':
                self.right_value.set(str(float(self.left_value.get()) * 10));
            elif will.upper() == 'SÉCULO':
                pass




#    def converting_volume(self, was, will):
#        pass
    
    

    def converting_volume(self, was, will):
        if was.upper() == 'METROS CÚBICOS':
            if will.upper() == 'METROS CÚBICOS':
                pass
            elif will.upper() == 'JARDAS CÚBICAS':
                self.right_value.set(str(float(self.left_value.get()) * 35.3147))
            elif will.upper() == 'PÉS CÚBICOS':
                self.right_value.set(str(float(self.left_value.get()) * 35.315))
            elif will.upper() == 'LITROS':
                self.right_value.set(str(float(self.left_value.get()) * 1000))
            elif will.upper() == 'GALÕES':
                self.right_value.set(str(float(self.left_value.get()) * 264.172))
            elif will.upper() == 'MILILITROS':
                self.right_value.set(str(float(self.left_value.get()) * 1000000))
            elif will.upper() == 'QUART':
                self.right_value.set(str(float(self.left_value.get()) * 1056.69))
            elif will.upper() == 'PINT':
                self.right_value.set(str(float(self.left_value.get()) * 2113.38))
            elif will.upper() == 'ONÇA LÍQUIDA':
                self.right_value.set(str(float(self.left_value.get()) * 33814))
        elif was.upper() == 'JARDAS CÚBICAS':
            if will.upper() == 'METROS CÚBICOS':
                self.right_value.set(str(float(self.left_value.get()) / 35.3147))
            elif will.upper() == 'JARDAS CÚBICAS':
                pass
            elif will.upper() == 'PÉS CÚBICOS':
                self.right_value.set(str(float(self.left_value.get()) * 27))
            elif will.upper() == 'LITROS':
                self.right_value.set(str(float(self.left_value.get()) * 764.555))
            elif will.upper() == 'GALÕES':
                self.right_value.set(str(float(self.left_value.get()) * 201.974))
            elif will.upper() == 'MILILITROS':
                self.right_value.set(str(float(self.left_value.get()) * 764555))
            elif will.upper() == 'QUART':
                self.right_value.set(str(float(self.left_value.get()) * 1000))
            elif will.upper() == 'PINT':
                self.right_value.set(str(float(self.left_value.get()) * 2000))
            elif will.upper() == 'ONÇA LÍQUIDA':
                self.right_value.set(str(float(self.left_value.get()) * 33814 / 27))
        elif was.upper() == 'PÉS CÚBICOS':
            if will.upper() == 'METROS CÚBICOS':
                self.right_value.set(str(float(self.left_value.get()) / 35.315))
            elif will.upper() == 'JARDAS CÚBICAS':
                self.right_value.set(str(float(self.left_value.get()) / 27))
            elif will.upper() == 'PÉS CÚBICOS':
                pass
            elif will.upper() == 'LITROS':
                self.right_value.set(str(float(self.left_value.get()) * 28.3168))
            elif will.upper() == 'GALÕES':
                self.right_value.set(str(float(self.left_value.get()) * 7.48052))
            elif will.upper() == 'MILILITROS':
                self.right_value.set(str(float(self.left_value.get()) * 28316.8))
            elif will.upper() == 'QUART':
                self.right_value.set(str(float(self.left_value.get()) * 33.814))
            elif will.upper() == 'PINT':
                self.right_value.set(str(float(self.left_value.get()) * 67.628))
            elif will.upper() == 'ONÇA LÍQUIDA':
                self.right_value.set(str(float(self.left_value.get()) * 33814 / 28.3168))
        elif was.upper() == 'LITROS':
            if will.upper() == 'METROS CÚBICOS':
                self.right_value.set(str(float(self.left_value.get()) / 1000))
            elif will.upper() == 'JARDAS CÚBICAS':
                self.right_value.set(str(float(self.left_value.get()) / 764.555))
            elif will.upper() == 'PÉS CÚBICOS':
                self.right_value.set(str(float(self.left_value.get()) / 28.3168))
            elif will.upper() == 'LITROS':
                pass
            elif will.upper() == 'GALÕES':
                self.right_value.set(str(float(self.left_value.get()) / 3.78541))
            elif will.upper() == 'MILILITROS':
                self.right_value.set(str(float(self.left_value.get()) * 1000))
            elif will.upper() == 'QUART':
                self.right_value.set(str(float(self.left_value.get()) * 1.05669))
            elif will.upper() == 'PINT':
                self.right_value.set(str(float(self.left_value.get()) * 2.11338))
            elif will.upper() == 'ONÇA LÍQUIDA':
                self.right_value.set(str(float(self.left_value.get()) * 33.814))
        elif was.upper() == 'GALÕES':
            if will.upper() == 'METROS CÚBICOS':
                self.right_value.set(str(float(self.left_value.get()) / 264.172))
            elif will.upper() == 'JARDAS CÚBICAS':
                self.right_value.set(str(float(self.left_value.get()) / 201.974))
            elif will.upper() == 'PÉS CÚBICOS':
                self.right_value.set(str(float(self.left_value.get()) / 7.48052))
            elif will.upper() == 'LITROS':
                self.right_value.set(str(float(self.left_value.get()) * 3.78541))
            elif will.upper() == 'GALÕES':
                pass
            elif will.upper() == 'MILILITROS':
                self.right_value.set(str(float(self.left_value.get()) * 3785.41))
            elif will.upper() == 'QUART':
                self.right_value.set(str(float(self.left_value.get()) * 4))
            elif will.upper() == 'PINT':
                self.right_value.set(str(float(self.left_value.get()) * 8));
            elif will.upper() == 'ONÇA LÍQUIDA':
                self.right_value.set(str(float(self.left_value.get()) * 128));
        elif was.upper() == 'MILILITROS':
            if will.upper() == 'METROS CÚBICOS':
                self.right_value.set(str(float(self.left_value.get()) / 1000000))
            elif will.upper() == 'JARDAS CÚBICAS':
                self.right_value.set(str(float(self.left_value.get()) / 764555))
            elif will.upper() == 'PÉS CÚBICOS':
                self.right_value.set(str(float(self.left_value.get()) / 28316.8))
            elif will.upper() == 'LITROS':
                self.right_value.set(str(float(self.left_value.get()) / 1000))
            elif will.upper() == 'GALÕES':
                self.right_value.set(str(float(self.left_value.get()) / 3785.41))
            elif will.upper() == 'MILILITROS':
                pass
            elif will.upper() == 'QUART':
                self.right_value.set(str(float(self.left_value.get()) / 946.353))
            elif will.upper() == 'PINT':
                self.right_value.set(str(float(self.left_value.get()) / 473.176));
            elif will.upper() == 'ONÇA LÍQUIDA':
                self.right_value.set(str(float(self.left_value.get()) / 29.5735));
        elif was.upper() == 'QUART':
            if will.upper() == 'METROS CÚBICOS':
                self.right_value.set(str(float(self.left_value.get()) / 1056.69))
            elif will.upper() == 'JARDAS CÚBICAS':
                self.right_value.set(str(float(self.left_value.get()) / 1000))
            elif will.upper() == 'PÉS CÚBICOS':
                self.right_value.set(str(float(self.left_value.get()) / 33.814))
            elif will.upper() == 'LITROS':
                self.right_value.set(str(float(self.left_value.get()) / 1.05669))
            elif will.upper() == 'GALÕES':
                self.right_value.set(str(float(self.left_value.get()) / 4));
            elif will.upper() == 'MILILITROS':
                self.right_value.set(str(float(self.left_value.get()) * 946.353));
            elif will.upper() == 'QUART':
                pass
            elif will.upper() == 'PINT':
                self.right_value.set(str(float(self.left_value.get()) * 2));
            elif will.upper() == 'ONÇA LÍQUIDA':
                self.right_value.set(str(float(self.left_value.get()) * 32));
        elif was.upper() == 'PINT':
            if will.upper() == 'METROS CÚBICOS':
                self.right_value.set(str(float(self.left_value.get()) / 2113.38))
            elif will.upper() == 'JARDAS CÚBICAS':
                self.right_value.set(str(float(self.left_value.get()) / 2000))
            elif will.upper() == 'PÉS CÚBICOS':
                self.right_value.set(str(float(self.left_value.get()) / 67.628))
            elif will.upper() == 'LITROS':
                self.right_value.set(str(float(self.left_value.get()) / 2.11338))
            elif will.upper() == 'GALÕES':
                self.right_value.set(str(float(self.left_value.get()) / 8));
            elif will.upper() == 'MILILITROS':
                self.right_value.set(str(float(self.left_value.get()) * 473.176));
            elif will.upper() == 'QUART':
                self.right_value.set(str(float(self.left_value.get()) / 2));
            elif will.upper() == 'PINT':
                pass
            elif will.upper() == 'ONÇA LÍQUIDA':
                self.right_value.set(str(float(self.left_value.get()) * 16));


    
    
    def __init__(self):
        super().__init__()
        self.title('Sistema De Conversão De Medidas')
        self.geometry('800x500')
        self.resizable(0,0)
        self.iconbitmap('Images/analysis-finance-graph.ico')

        self.category=[]
        self.left_value = StringVar()
        self.right_value = StringVar()
        
        self.appearance()
        self.components()
        #self.submit()
    
    
#if __name__==__'__main__':
#    main()


# Ponto de entrada principal
if __name__ == "__main__": 
    app = System()
    app.mainloop()