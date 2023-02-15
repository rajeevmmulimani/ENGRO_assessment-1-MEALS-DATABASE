# -*- coding: utf-8 -*-
"""
Created on Mon, Feb 07, 2023, 12:38 PM

@author: RajeevMulimani
"""
import requests
import json
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox

root=Tk()

root.wm_title("Assessment for meal database")
root.geometry("720x720+650+50")
test={1,2,3,4}

#search = 'a'
#response_API = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?f='+search)
#response_API = requests.get('https://www.themealdb.com/api/json/v1/1/lookup.php?i=52772')
#response_API = requests.get('https://www.themealdb.com/api/json/v1/1/lookup.php?i=52772')
#response_API = requests.get('https://github.com/HackerNews/API')
response_API_1 = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?c=list')
#response_API_2 = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?c='+search_meals2)
#temp_size1 = 
#search_meals1 = 'Arrabiata'
#response_API = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s='+search_meals)
#search_meals2 = 'Seafood'
#response_API_2 = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?c='+search_meals2)

data1 = response_API_1.text

raw_data1 = data1

parse_json1 = json.loads(raw_data1)



copy_category=[]
copy_catg_list_title=[]
length_of_list_of_categories_of_meals=0
length_of_available_meals_in_category=0
button_name=[]
var_erg=0

for catg_list, meals in parse_json1.items():
    
    category = catg_list
    copy_category.append(catg_list)
    length_of_list_of_categories_of_meals += 1
    
    for meal in meals:
        
        catg_list_title = meal
        
        temp = catg_list_title['strCategory']
        copy_catg_list_title.append(temp)
        
        length_of_available_meals_in_category += 1



copy_category1=[]
copy_catg_dishes_title1=[]
length_of_list_of_category1_of_meals=0
length_of_available_dishes_in_category=0
ind_length_of_available_dishes_in_category=[]


for m_num in range(length_of_available_meals_in_category):
    category_selection = copy_catg_list_title[m_num]
    search_meals2=category_selection
    response_API_2 = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?c='+search_meals2)
    data2 = response_API_2.text
    raw_data2 = data2
    parse_json2 = json.loads(raw_data2)
    for catg_list1, meals1 in parse_json2.items():
        category1=catg_list1
        
        length_of_list_of_category1_of_meals += 1
        test_var=0
        for dish in meals1:
            catg_list1_title = dish
            temp_test = catg_list1_title['strMeal']
                        
            copy_catg_dishes_title1.insert(length_of_available_dishes_in_category, temp_test)
            length_of_available_dishes_in_category +=1
            
            test_var += 1
                        
        ind_length_of_available_dishes_in_category.insert(test_var, test_var)
      

copy_desc=[]      
          
class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        
        self.t1=Entry()
        self.t1.place(x=240, y=210)
       
        self.b1=Button(self, text="view the description", command=self.part2)
        
        self.b1.place(x=245, y=250)
        
        try:
            var1=0
            teststr1=[]
            teststr2=[]
            
            for i in range(length_of_available_meals_in_category):
            
                teststr1=copy_catg_list_title[i]
                
                
                var1 += 1
                
                tkk1 = Button(self, text=str(i+1)+":"+teststr1, command=self.part1)
                tempxy = teststr1
                button_name.append(tempxy)
                
                tkk1.grid(row=1, column=i+3)             
                 
             
            
        except:
            print("check your internet/api socket link/contact administrator Rajeev @8790388055")
        finally:
            print("test for finally block exception completed")
            

    def clear():               
        combo.set('')

    def get_index(*arg):
        Label(self, text="the value at index"+str(combo.current())+"is"+" "+str(var.get()),font=('Helvetica 12')).pack()
    def selection_changed(event):
        selection = combbox.get()
        messagebox.showinfo(
            title="New Selection",
            message=f"Selected option: {selection}"
        )
    
    def part1(self):

        var_temp = []
        dish_title=[]
        combo_numr=0
        combbox=Combobox(self, values=copy_catg_dishes_title1)
        test_str=combbox.get()
        for zi in range(length_of_available_dishes_in_category):           
            var_temp=copy_catg_dishes_title1[zi]
            dish_title.insert(zi,var_temp)
            
            
        
            combo_numr += 1
            combbox.place(x=60,y=150)
            combbox.set("pick a dish from menu")                  
                                 
                   
            self.tt=Entry()
            self.tt.insert(END, str(dish_title))
            
            rrp=combbox.bind("<<ComboboxSelected>>", test_str)
            lb=Label(self,text='selection is:'+" "+str(combo_numr))
            lb.place(x=260, y=150)


        
    def part2(self):
        num=int(self.t1.get())
        result=num

        dishes_selection = copy_catg_dishes_title1[num-1]
            
        search_dishes = dishes_selection
        response_API_3 = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s='+search_dishes)
        data3=response_API_3.text
        raw_data3 = data3
        parse_json3 = json.loads(raw_data3)
            
        for dish_list, dish in parse_json3.items():
            copy_desc = dish_list
            for dish_list3 in dish:
                list3_title = dish_list3
                temp3_test = list3_title['strInstructions']
                
                sttr=temp3_test
                messagebox.showinfo("description",sttr)
                    
 
    


app = Window(root)
root.mainloop()
