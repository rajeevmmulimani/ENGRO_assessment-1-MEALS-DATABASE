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
##app = Window(root)
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
#data2 = response_API_2.text
raw_data1 = data1
#raw_data2 = data2
parse_json1 = json.loads(raw_data1)
#parse_json2 = json.loads(raw_data2)
#search_meals=[]

#length_data1 = len(data1)
#meals = data1.get('strCategory')
#data2 = response_API_2.text
#raw_data2 = data2
#parse_json2 = json.loads(raw_data2)
#print(parse_json2)
copy_category=[]
copy_catg_list_title=[]
length_of_list_of_categories_of_meals=0
length_of_available_meals_in_category=0
button_name=[]
var_erg=0

for catg_list, meals in parse_json1.items():
    #print(catg)
    #category = meals['strCategory']+ " "
    category = catg_list
    copy_category.append(catg_list)
    length_of_list_of_categories_of_meals += 1
    #print(catg_list)
    for meal in meals:
        #print(meal)
        catg_list_title = meal
        #copy_catg_list_title.append(meal)
        #print(catg_list_title['strCategory'])
        temp = catg_list_title['strCategory']
        copy_catg_list_title.append(temp)
        #print(category)
        #print(temp)
        length_of_available_meals_in_category += 1

#response_API_2 = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?c='+search_meals2)

##for list_of_categories_of_meals in copy_category:
##    print(list_of_categories_of_meals[0:])
#for available_meals_in_category in copy_catg_list_title:
    #print(available_meals_in_category[0:length_of_available_meals_in_category])
#print("12345")

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
        #print(search_meals2)
                    #print(category1)
        #copy_category1.append(catg_list1)
        length_of_list_of_category1_of_meals += 1
        test_var=0
        for dish in meals1:
            catg_list1_title = dish
            temp_test = catg_list1_title['strMeal']
                        #copy_catg_dishes_title1.append(temp_test)
                        #copy_catg_dishes_title1.append(catg_list1_title['strMeal'])
            copy_catg_dishes_title1.insert(length_of_available_dishes_in_category, temp_test)
            length_of_available_dishes_in_category +=1
            #print(temp_test)
            test_var += 1
                        #print(copy_catg_dishes_title1)
                        #copy_catg_dishes_title1=temp_test
            #for m_desc in range(length_of_available_dishes_in_category):
                #print(m_desc)
        ind_length_of_available_dishes_in_category.insert(test_var, test_var)
        #print(test_var)
        #print(ind_length_of_available_dishes_in_category)
    

##button_name1=[]
##var_erg1=0

#print(copy_catg_list_title[1])


copy_desc=[]

##for m_desc in range(length_of_available_dishes_in_category):
##    #print(m_desc)
##    dishes_selection = copy_catg_dishes_title1[m_desc]
##    #print(dishes_selection)
##    search_dishes = dishes_selection
##    response_API_3 = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s='+search_dishes)
##    data3=response_API_3.text
##    raw_data3 = data3
##    parse_json3 = json.loads(raw_data3)
##    #print(parse_json3)
##    for dish_list, dish in parse_json3.items():
##        copy_desc = dish_list
##        for dish_list3 in dish:
##            list3_title = dish_list3
##            temp3_test = list3_title['strInstructions']
##            #print(temp3_test)
            
        
    
##main_window = tk.Tk()
##main_window.config(width=300, height=200)
##main_window.title("result")
##combo = ttk.Combobox(values=["Python", "C", "C++", "Java"])
###combo = ttk.Combobox(values={'meals': [{'strMeal': 'Beef and Mustard Pie', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/sytuqu1511553755.jpg', 'idMeal': '52874'}, {'strMeal': 'Beef and Oyster pie', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/wrssvt1511556563.jpg', 'idMeal': '52878'}, {'strMeal': 'Beef Banh Mi Bowls with Sriracha Mayo, Carrot & Pickled Cucumber', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/z0ageb1583189517.jpg', 'idMeal': '52997'}, {'strMeal': 'Beef Bourguignon', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/vtqxtu1511784197.jpg', 'idMeal': '52904'}, {'strMeal': 'Beef Brisket Pot Roast', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/ursuup1487348423.jpg', 'idMeal': '52812'}, {'strMeal': 'Beef Dumpling Stew', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/uyqrrv1511553350.jpg', 'idMeal': '52873'}, {'strMeal': 'Beef Lo Mein', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/1529444830.jpg', 'idMeal': '52952'}, {'strMeal': 'Beef Rendang', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/bc8v651619789840.jpg', 'idMeal': '53053'}, {'strMeal': 'Beef stroganoff', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/svprys1511176755.jpg', 'idMeal': '52834'}, {'strMeal': 'Beef Sunday Roast', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/ssrrrs1503664277.jpg', 'idMeal': '52824'}, {'strMeal': 'Beef Wellington', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/vvpprx1487325699.jpg', 'idMeal': '52803'}, {'strMeal': 'Big Mac', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/urzj1d1587670726.jpg', 'idMeal': '53013'}, {'strMeal': 'Bitterballen (Dutch meatballs)', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/lhqev81565090111.jpg', 'idMeal': '52979'}, {'strMeal': 'Braised Beef Chilli', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/uuqvwu1504629254.jpg', 'idMeal': '52826'}, {'strMeal': 'Cevapi Sausages', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/vc08jn1628769553.jpg', 'idMeal': '53055'}, {'strMeal': 'Chivito uruguayo', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/n7qnkb1630444129.jpg', 'idMeal': '53063'}, {'strMeal': 'Corned Beef and Cabbage', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/xb97a81583266727.jpg', 'idMeal': '52998'}, {'strMeal': 'Croatian Bean Stew', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/tnwy8m1628770384.jpg', 'idMeal': '53058'}, {'strMeal': 'Croatian lamb peka', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/pn59o51628769837.jpg', 'idMeal': '53056'}, {'strMeal': 'Egyptian Fatteh', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/rlwcc51598734603.jpg', 'idMeal': '53031'}, {'strMeal': 'Gołąbki (cabbage roll)', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/q8sp3j1593349686.jpg', 'idMeal': '53021'}, {'strMeal': 'Irish stew', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/sxxpst1468569714.jpg', 'idMeal': '52781'}, {'strMeal': 'Jamaican Beef Patties', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/wsqqsw1515364068.jpg', 'idMeal': '52938'}, {'strMeal': 'Ma Po Tofu', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/1525874812.jpg', 'idMeal': '52947'}, {'strMeal': 'Massaman Beef curry', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/tvttqv1504640475.jpg', 'idMeal': '52827'}, {'strMeal': 'Minced Beef Pie', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/xwutvy1511555540.jpg', 'idMeal': '52876'}, {'strMeal': 'Montreal Smoked Meat', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg', 'idMeal': '52927'}, {'strMeal': 'Moussaka', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/ctg8jd1585563097.jpg', 'idMeal': '53006'}, {'strMeal': 'Mulukhiyah', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/x372ug1598733932.jpg', 'idMeal': '53029'}, {'strMeal': 'Oxtail with broad beans', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/1520083578.jpg', 'idMeal': '52943'}, {'strMeal': 'Paszteciki (Polish Pasties)', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/c9a3l31593261890.jpg', 'idMeal': '53017'}, {'strMeal': 'Pate Chinois', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg', 'idMeal': '52930'}, {'strMeal': 'Portuguese prego with green piri-piri', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/ewcikl1614348364.jpg', 'idMeal': '53042'}, {'strMeal': 'Red Peas Soup', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/sqpqtp1515365614.jpg', 'idMeal': '52941'}, {'strMeal': 'Roti john', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/hx335q1619789561.jpg', 'idMeal': '53052'}, {'strMeal': 'Soy-Glazed Meatloaves with Wasabi Mashed Potatoes & Roasted Carrots', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/o2wb6p1581005243.jpg', 'idMeal': '52992'}, {'strMeal': 'Spaghetti Bolognese', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/sutysw1468247559.jpg', 'idMeal': '52770'}, {'strMeal': 'Steak and Kidney Pie', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/qysyss1511558054.jpg', 'idMeal': '52881'}, {'strMeal': 'Steak Diane', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/vussxq1511882648.jpg', 'idMeal': '52935'}, {'strMeal': 'Szechuan Beef', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/1529443236.jpg', 'idMeal': '52950'}, {'strMeal': 'Traditional Croatian Goulash', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/n1hcou1628770088.jpg', 'idMeal': '53057'}, {'strMeal': "Vegetable Shepherd's Pie", 'strMealThumb': 'https://www.themealdb.com/images/media/meals/w8umt11583268117.jpg', 'idMeal': '53000'}]})
##combo.bind("<<ComboboxSelected>>", selection_changed)
##combo.place(x=50, y=50)



class Window(Frame):
    #var1=0
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        #app = Window(root)
        #print(test)
        #main_window = tk.Tk()
        #main_window.config(width=300, height=200)
        #main_window.title("result")
        #combo = ttk.Combobox(values=["Python", "C", "C++", "Java"])
        #combo = ttk.Combobox(values={'meals': [{'strMeal': 'Beef and Mustard Pie', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/sytuqu1511553755.jpg', 'idMeal': '52874'}, {'strMeal': 'Beef and Oyster pie', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/wrssvt1511556563.jpg', 'idMeal': '52878'}, {'strMeal': 'Beef Banh Mi Bowls with Sriracha Mayo, Carrot & Pickled Cucumber', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/z0ageb1583189517.jpg', 'idMeal': '52997'}, {'strMeal': 'Beef Bourguignon', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/vtqxtu1511784197.jpg', 'idMeal': '52904'}, {'strMeal': 'Beef Brisket Pot Roast', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/ursuup1487348423.jpg', 'idMeal': '52812'}, {'strMeal': 'Beef Dumpling Stew', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/uyqrrv1511553350.jpg', 'idMeal': '52873'}, {'strMeal': 'Beef Lo Mein', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/1529444830.jpg', 'idMeal': '52952'}, {'strMeal': 'Beef Rendang', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/bc8v651619789840.jpg', 'idMeal': '53053'}, {'strMeal': 'Beef stroganoff', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/svprys1511176755.jpg', 'idMeal': '52834'}, {'strMeal': 'Beef Sunday Roast', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/ssrrrs1503664277.jpg', 'idMeal': '52824'}, {'strMeal': 'Beef Wellington', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/vvpprx1487325699.jpg', 'idMeal': '52803'}, {'strMeal': 'Big Mac', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/urzj1d1587670726.jpg', 'idMeal': '53013'}, {'strMeal': 'Bitterballen (Dutch meatballs)', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/lhqev81565090111.jpg', 'idMeal': '52979'}, {'strMeal': 'Braised Beef Chilli', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/uuqvwu1504629254.jpg', 'idMeal': '52826'}, {'strMeal': 'Cevapi Sausages', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/vc08jn1628769553.jpg', 'idMeal': '53055'}, {'strMeal': 'Chivito uruguayo', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/n7qnkb1630444129.jpg', 'idMeal': '53063'}, {'strMeal': 'Corned Beef and Cabbage', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/xb97a81583266727.jpg', 'idMeal': '52998'}, {'strMeal': 'Croatian Bean Stew', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/tnwy8m1628770384.jpg', 'idMeal': '53058'}, {'strMeal': 'Croatian lamb peka', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/pn59o51628769837.jpg', 'idMeal': '53056'}, {'strMeal': 'Egyptian Fatteh', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/rlwcc51598734603.jpg', 'idMeal': '53031'}, {'strMeal': 'Gołąbki (cabbage roll)', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/q8sp3j1593349686.jpg', 'idMeal': '53021'}, {'strMeal': 'Irish stew', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/sxxpst1468569714.jpg', 'idMeal': '52781'}, {'strMeal': 'Jamaican Beef Patties', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/wsqqsw1515364068.jpg', 'idMeal': '52938'}, {'strMeal': 'Ma Po Tofu', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/1525874812.jpg', 'idMeal': '52947'}, {'strMeal': 'Massaman Beef curry', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/tvttqv1504640475.jpg', 'idMeal': '52827'}, {'strMeal': 'Minced Beef Pie', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/xwutvy1511555540.jpg', 'idMeal': '52876'}, {'strMeal': 'Montreal Smoked Meat', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg', 'idMeal': '52927'}, {'strMeal': 'Moussaka', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/ctg8jd1585563097.jpg', 'idMeal': '53006'}, {'strMeal': 'Mulukhiyah', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/x372ug1598733932.jpg', 'idMeal': '53029'}, {'strMeal': 'Oxtail with broad beans', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/1520083578.jpg', 'idMeal': '52943'}, {'strMeal': 'Paszteciki (Polish Pasties)', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/c9a3l31593261890.jpg', 'idMeal': '53017'}, {'strMeal': 'Pate Chinois', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg', 'idMeal': '52930'}, {'strMeal': 'Portuguese prego with green piri-piri', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/ewcikl1614348364.jpg', 'idMeal': '53042'}, {'strMeal': 'Red Peas Soup', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/sqpqtp1515365614.jpg', 'idMeal': '52941'}, {'strMeal': 'Roti john', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/hx335q1619789561.jpg', 'idMeal': '53052'}, {'strMeal': 'Soy-Glazed Meatloaves with Wasabi Mashed Potatoes & Roasted Carrots', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/o2wb6p1581005243.jpg', 'idMeal': '52992'}, {'strMeal': 'Spaghetti Bolognese', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/sutysw1468247559.jpg', 'idMeal': '52770'}, {'strMeal': 'Steak and Kidney Pie', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/qysyss1511558054.jpg', 'idMeal': '52881'}, {'strMeal': 'Steak Diane', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/vussxq1511882648.jpg', 'idMeal': '52935'}, {'strMeal': 'Szechuan Beef', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/1529443236.jpg', 'idMeal': '52950'}, {'strMeal': 'Traditional Croatian Goulash', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/n1hcou1628770088.jpg', 'idMeal': '53057'}, {'strMeal': "Vegetable Shepherd's Pie", 'strMealThumb': 'https://www.themealdb.com/images/media/meals/w8umt11583268117.jpg', 'idMeal': '53000'}]})
        #combo.bind("<<ComboboxSelected>>", command=self.selection_changed)
        #combo.place(x=50, y=50)

        #exitButton = Button(self, text="stop", command=self.clickExitButton)

        #exitButton.place(x=600, y=290)
        #e1 = tk.Entry(window, show=None, font=('Arial', 14))
        #e1.pack()
        #canvas= Canvas (labelframe)
        #var1=0
        self.t1=Entry()
        self.t1.place(x=240, y=210)
        #self.tt1=
        self.b1=Button(self, text="view the description", command=self.part2)
        #self.b1.bind('<Button-2>',self.part2)
        self.b1.place(x=245, y=250)
        
        try:
            var1=0
            teststr1=[]
            teststr2=[]
            #mainLabel = Label(self, text="click on any of the meal category above to view the list of meals", fg='red', font={"Helvetica", 8})
            #mainLabel.place(x=180, y=90)
            for i in range(length_of_available_meals_in_category):
            #print(copy_catg_list_title[i])
            #print(length_of_available_meals_in_category)
            #print(len(length_of_available_meals_in_category))
            #for available_meals_in_category in copy_catg_list_title:
                #teststr1=available_meals_in_category[0:length_of_available_meals_in_category]
                teststr1=copy_catg_list_title[i]
                
                #print(copy_category[0])
                #print(teststr1)
                var1 += 1
                #var_arg.append(var1)
                #tkk = Button(self, text=str(i+1)+":"+teststr1)
                tkk1 = Button(self, text=str(i+1)+":"+teststr1, command=self.part1)
                tempxy = teststr1
                button_name.append(tempxy)
                #print(button_name)
            #print(copy_catg_list_title)
            #tkk.pack(side=RIGHT)
                tkk1.grid(row=1, column=i+3)
            #tkk2=Button(self, text=str(i+1)+":"+teststr1, command=self.part2)
            
            
            
##                combbox=ttk.Combobox(self, values=["Python", "C", "C++", "Java"])
##                combbox.bind("<<ComboboxSelected>>", selection_changed)
##                combbox.place(x=60,y=150)

            
            #@mainLabel = Label(self, text="click on any of the meal category above to view the list of meals", fg='red', font={"Helvetica", 8})
            #mainLabel.grid(row=i+8, column=1)
            #@mainLabel.place(x=180, y=90)
            #tkk.grid(row=i, column=0, columnspan=5)
            #print("i is :",i)
        
        #for j in range(length_of_available_meals_in_category):
##                category_selection = copy_catg_list_title[i]
##                search_meals2=category_selection
                #copy_meals_list.append(search_meals2)
            #print(search_meals2)

##                response_API_2 = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?c='+search_meals2)
##                data2 = response_API_2.text
##                raw_data2 = data2
##                parse_json2 = json.loads(raw_data2)
                #print(parse_json2)
                #print("test1")
                #print(search_meals2)
                #print(parse_json2)
                #test_var=0
##                for catg_list1, meals1 in parse_json2.items():
##                    category1=catg_list1
##                    print(search_meals2)
##                    #print(category1)
##                    copy_category1.append(catg_list1)
##                    #length_of_list_of_category1_of_meals += 1
##                    test_var=0
##                    for dish in meals1:
##                        catg_list1_title = dish
##                        temp_test = catg_list1_title['strMeal']
##                        #copy_catg_dishes_title1.append(temp_test)
##                        #copy_catg_dishes_title1.append(catg_list1_title['strMeal'])
##                        #copy_catg_dishes_title1.insert(temp_test)
##                        #length_of_available_dishes_in_category +=1
##                        print(temp_test)
##                        test_var += 1
##                        #print(copy_catg_dishes_title1)
##                        #copy_catg_dishes_title1=temp_test
##                        #print(test_var)
                    
                    
                
            
        except:
            print("check your internet/api socket link/contact administrator Rajeev @8790388055")
        finally:
            print("test for finally block exception completed")
            
##            main_window = tk.Tk()
##            main_window.config(width=300, height=200)
##            main_window.title("result")
##            combo = ttk.Combobox(values=["Python", "C", "C++", "Java"])
##            #combo = ttk.Combobox(values={'meals': [{'strMeal': 'Beef and Mustard Pie', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/sytuqu1511553755.jpg', 'idMeal': '52874'}, {'strMeal': 'Beef and Oyster pie', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/wrssvt1511556563.jpg', 'idMeal': '52878'}, {'strMeal': 'Beef Banh Mi Bowls with Sriracha Mayo, Carrot & Pickled Cucumber', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/z0ageb1583189517.jpg', 'idMeal': '52997'}, {'strMeal': 'Beef Bourguignon', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/vtqxtu1511784197.jpg', 'idMeal': '52904'}, {'strMeal': 'Beef Brisket Pot Roast', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/ursuup1487348423.jpg', 'idMeal': '52812'}, {'strMeal': 'Beef Dumpling Stew', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/uyqrrv1511553350.jpg', 'idMeal': '52873'}, {'strMeal': 'Beef Lo Mein', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/1529444830.jpg', 'idMeal': '52952'}, {'strMeal': 'Beef Rendang', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/bc8v651619789840.jpg', 'idMeal': '53053'}, {'strMeal': 'Beef stroganoff', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/svprys1511176755.jpg', 'idMeal': '52834'}, {'strMeal': 'Beef Sunday Roast', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/ssrrrs1503664277.jpg', 'idMeal': '52824'}, {'strMeal': 'Beef Wellington', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/vvpprx1487325699.jpg', 'idMeal': '52803'}, {'strMeal': 'Big Mac', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/urzj1d1587670726.jpg', 'idMeal': '53013'}, {'strMeal': 'Bitterballen (Dutch meatballs)', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/lhqev81565090111.jpg', 'idMeal': '52979'}, {'strMeal': 'Braised Beef Chilli', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/uuqvwu1504629254.jpg', 'idMeal': '52826'}, {'strMeal': 'Cevapi Sausages', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/vc08jn1628769553.jpg', 'idMeal': '53055'}, {'strMeal': 'Chivito uruguayo', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/n7qnkb1630444129.jpg', 'idMeal': '53063'}, {'strMeal': 'Corned Beef and Cabbage', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/xb97a81583266727.jpg', 'idMeal': '52998'}, {'strMeal': 'Croatian Bean Stew', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/tnwy8m1628770384.jpg', 'idMeal': '53058'}, {'strMeal': 'Croatian lamb peka', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/pn59o51628769837.jpg', 'idMeal': '53056'}, {'strMeal': 'Egyptian Fatteh', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/rlwcc51598734603.jpg', 'idMeal': '53031'}, {'strMeal': 'Gołąbki (cabbage roll)', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/q8sp3j1593349686.jpg', 'idMeal': '53021'}, {'strMeal': 'Irish stew', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/sxxpst1468569714.jpg', 'idMeal': '52781'}, {'strMeal': 'Jamaican Beef Patties', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/wsqqsw1515364068.jpg', 'idMeal': '52938'}, {'strMeal': 'Ma Po Tofu', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/1525874812.jpg', 'idMeal': '52947'}, {'strMeal': 'Massaman Beef curry', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/tvttqv1504640475.jpg', 'idMeal': '52827'}, {'strMeal': 'Minced Beef Pie', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/xwutvy1511555540.jpg', 'idMeal': '52876'}, {'strMeal': 'Montreal Smoked Meat', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg', 'idMeal': '52927'}, {'strMeal': 'Moussaka', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/ctg8jd1585563097.jpg', 'idMeal': '53006'}, {'strMeal': 'Mulukhiyah', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/x372ug1598733932.jpg', 'idMeal': '53029'}, {'strMeal': 'Oxtail with broad beans', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/1520083578.jpg', 'idMeal': '52943'}, {'strMeal': 'Paszteciki (Polish Pasties)', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/c9a3l31593261890.jpg', 'idMeal': '53017'}, {'strMeal': 'Pate Chinois', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg', 'idMeal': '52930'}, {'strMeal': 'Portuguese prego with green piri-piri', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/ewcikl1614348364.jpg', 'idMeal': '53042'}, {'strMeal': 'Red Peas Soup', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/sqpqtp1515365614.jpg', 'idMeal': '52941'}, {'strMeal': 'Roti john', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/hx335q1619789561.jpg', 'idMeal': '53052'}, {'strMeal': 'Soy-Glazed Meatloaves with Wasabi Mashed Potatoes & Roasted Carrots', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/o2wb6p1581005243.jpg', 'idMeal': '52992'}, {'strMeal': 'Spaghetti Bolognese', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/sutysw1468247559.jpg', 'idMeal': '52770'}, {'strMeal': 'Steak and Kidney Pie', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/qysyss1511558054.jpg', 'idMeal': '52881'}, {'strMeal': 'Steak Diane', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/vussxq1511882648.jpg', 'idMeal': '52935'}, {'strMeal': 'Szechuan Beef', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/1529443236.jpg', 'idMeal': '52950'}, {'strMeal': 'Traditional Croatian Goulash', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/n1hcou1628770088.jpg', 'idMeal': '53057'}, {'strMeal': "Vegetable Shepherd's Pie", 'strMealThumb': 'https://www.themealdb.com/images/media/meals/w8umt11583268117.jpg', 'idMeal': '53000'}]})
##            combo.bind("<<ComboboxSelected>>", selection_changed)
##            combo.place(x=50, y=50)
##            main_window.mainloop()
            #@var2=0 
            #@temp1=var1   
            #@for j in range(var1):
                #tkk1 = Button(self, text=teststr2+str(j+1), command=self.part1)
                #tkk1 = Button(self, text=teststr2+str(j+1))
                #@tkk1 = Button(self, text=button_name[j])
                #tempxyz=button_name[j]
                #print(button_name[j])
                #print(j)
                #print(temp1)
                #print(var2)
            #var2+= 1
                #tkk1.grid(row=j+temp1+1,column=j+var2+2)
            #tkk1.grid(row=j,column=var1)
                #@tkk1.place(x=350, y=190+var2)
            #print(var1)
            #tkk1.grid(row=var1+1,column=j+temp1)
                #@var2+= 30
            #temp1=var1
                #@temp1 -= 1
            #print("var1:",var1,"var2:",var2,"temp1:",temp1)
            #print()
            #print("j is :",j)
        
##    for list_of_categories_of_meals in copy_category:
##        print(list_of_categories_of_meals[0:])
##    for available_meals_in_category in copy_catg_list_title:
##        print(available_meals_in_category[0:length_of_available_meals_in_category])
        
                #def callback1(self):
    def clear():                #  print("test_callback1")
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
####        var = StringVar()
####        var=copy_catg_dishes_title1
####        combo = ttk.Combobox(self, textvariable=var)
####        combo['values']=copy_catg_dishes_title1
####        combo['state']='readonly'
####        combo.place(x=50, y=50)
####        var.trace('w', get_index)
####        button = Button(self, text="clear", command=clear)
####        button.pack()
        
        
        ##if button_name == "beef":
        #combbox=ttk.Combobox(self, values=copy_catg_dishes_title1, state = "readonly")
        var_temp = []
        dish_title=[]
        combo_numr=0
        combbox=Combobox(self, values=copy_catg_dishes_title1)
        test_str=combbox.get()
        for zi in range(length_of_available_dishes_in_category):
            #print(zi)
            #print(length_of_available_dishes_in_category)
            #for 
            var_temp=copy_catg_dishes_title1[zi]
            dish_title.insert(zi,var_temp)
            
            
        #print(dish_title)   
        #combbox=Combobox(self, values=dish_title, state="readonly")
            #combbox=Combobox(self, values=["Python", "C", "C++", "Java"])
            #combbox=ttk.Combobox(self, values=copy_catg_dishes_title1)
            combo_numr += 1
            combbox.place(x=60,y=150)
            combbox.set("pick a dish from menu")
            #combbox.set(dish_title[zi])
            #combbox=Button(self, text=zi)
            #combbox.grid(row=50,column=50)
            #combbox.set(dish_title[zi])
            
        
        
        
            
            #combbox.set(dish_title)
        
        
        
        
##        selection=combbox.get()
        #combbox.set("pick a dish from menu")
            

            self.tt=Entry()
            self.tt.insert(END, str(dish_title))
            #test_str=combbox.get()
            rrp=combbox.bind("<<ComboboxSelected>>", test_str)
            lb=Label(self,text='selection is:'+" "+str(combo_numr))
            lb.place(x=260, y=150)
##        messagebox.showinfo(
##            title="New Selection",
##            message=f"Selected option: {test_str}"
##            )
            #print(test_str)
            #print(rrp)
            
            #print(zi)
        #self.tt.delete(0, 'end')
        #self.tt.insert(END, str('test_read'))
        #self.tt.insert(END, str(dish_title))
            #combbox.bind('<Button-1>',command=self.tt)
        #test_str=str(self.tt.get())
        #test_str=str(combbox.get())
        #print(test_str)
##        
##  
##        
##        #combbox.set(selection)
##       
##        messagebox.showinfo(title="New Selection", message=f"Selected option: {selection}")
##        combbox.bind()
        
        
        
        ##combbox.pack(padx=50, pady=50)
        
        
        
        
        
##        var2=0 
##        ##temp1=var_arg   
##        ##for j in range(length_of_available_meals_in_category):
##        for j in range(ind_length_of_available_dishes_in_category[0]):
##            tkk1 = Button(self, text=j)
##            #tkk1 = Button(self, text=button_name[j], command=self.dishesAvailable)
##            tkk1.place(x=100, y=190+var2)
##            var2+= 30
##            #print("test1")
            
           
#print("main")        
##    def dishesAvailable(self):
##        category_selection = copy_catg_list_title[0]
##        search_meals2 = category_selection
##        #print(search_meals2)
##        response_API_2 = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?c='+search_meals2)
##        data2 = response_API_2.text
##        raw_data2 = data2
##        parse_json2 = json.loads(raw_data2)
##        #print(parse_json2)
##        print("test1")
#print("main")        

#print(length_of_list_of_categories_of_meals)
#print(length_of_available_meals_in_category)

#print(length_of_list_of_category1_of_meals)
#print(copy_catg_dishes_title1[0])
#print(ind_length_of_available_dishes_in_category)


#category_meals = parse_json1['meals']
#print(category_meals)
#no_of_list_in_category = len (category_meals)
#print(no_of_list_in_category)
#meals = category_meals[0:]
#print(meals)

#parse_json2 = json.loads(data2)

#print(copy_category1)
#print(copy_catg_dishes_title1)
#print(length_data1) 
#print(parse_json2)

##root=Tk()
##app = Window(root)
##root.wm_title("Assessment for meal database")
##root.geometry("720x400+650+50")

        
    def part2(self):
        num=int(self.t1.get())
        result=num
        #print(test)
        #print(num)
        #sttr="{'meals': [{'strCategory': 'Beef'}, {'strCategory': 'Breakfast'}, {'strCategory': 'Chicken'}, {'strCategory': 'Dessert'}, {'strCategory': 'Goat'}, {'strCategory': 'Lamb'}, {'strCategory': 'Miscellaneous'}, {'strCategory': 'Pasta'}, {'strCategory': 'Pork'}, {'strCategory': 'Seafood'}, {'strCategory': 'Side'}, {'strCategory': 'Starter'}, {'strCategory': 'Vegan'}, {'strCategory': 'Vegetarian'}]}"
        #messagebox.showinfo("description",sttr)
        #print(num)
        
##        for m_desc in range(length_of_available_dishes_in_category):
##            #print(m_desc)
        dishes_selection = copy_catg_dishes_title1[num-1]
            #print(dishes_selection)
        search_dishes = dishes_selection
        response_API_3 = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s='+search_dishes)
        data3=response_API_3.text
        raw_data3 = data3
        parse_json3 = json.loads(raw_data3)
            #print(parse_json3)
        for dish_list, dish in parse_json3.items():
            copy_desc = dish_list
            for dish_list3 in dish:
                list3_title = dish_list3
                temp3_test = list3_title['strInstructions']
                #print(temp3_test)
                sttr=temp3_test
                messagebox.showinfo("description",sttr)
                    
 
    

#print(test)
app = Window(root)
root.mainloop()
