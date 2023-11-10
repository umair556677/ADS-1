# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 07:13:43 2023

@author: umair
"""

# importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# reading a data
raw_waste = pd.read_csv("Singa-waste/2003_2017_waste.csv")
print(raw_waste)

# filtering a data by waste_types
food = raw_waste[raw_waste["waste_type"]== "Food"]
print(food)
glass = raw_waste[raw_waste["waste_type"]== "Glass"]
print(glass)
others = raw_waste[raw_waste["waste_type"]== "Others"]
print(others)
paper = raw_waste[raw_waste["waste_type"]== "Paper/Cardboard"]
print(paper)
plastics = raw_waste[raw_waste["waste_type"]== "Plastics"]
print(plastics)
textile = raw_waste[raw_waste["waste_type"]== "Textile/Leather"]
print(textile)
wood = raw_waste[raw_waste["waste_type"]== "Wood"]
print(wood)


def graph1():
    '''
    This function makes a lineplot of 6 wastages  from year 2003-2017
    '''
    # lineplot
    plt.figure()
    plt.plot(food['year'], food['waste_disposed_of_tonne'], label= "food")
    plt.plot(others['year'], others['waste_disposed_of_tonne'], label="others")
    plt.plot(plastics['year'], plastics['waste_disposed_of_tonne'], 
             label= "plastics")
    plt.plot(paper['year'], paper['waste_disposed_of_tonne'], label= "paper")
    plt.plot(textile['year'], textile['waste_disposed_of_tonne'], label= "textile")
    plt.legend(loc= "best", ncols= 3)
    plt.title("Lineplot of Singapore wastage from 2003-2017")
    plt.xlabel("Years")
    plt.ylabel("Disposed wastage (metric tonnes)")
    plt.show()
    plt.savefig("lineplot.png")


# filtering a data by year
food_2016 = food[food["year"] == 2016]
others_2016 = others[others["year"] == 2016]
plastics_2016 = plastics[plastics["year"] == 2016]
paper_2016 = paper[paper["year"] == 2016]
textile_2016 = textile[textile["year"] == 2016]


def graph2():
    '''
    This function shows a piechart of waste disposed in 2016
    '''
    # piechart
    plt.figure(figsize=(6,10))
    names =  np.array([food_2016["waste_type"], others_2016["waste_type"],
              plastics_2016["waste_type"], paper_2016["waste_type"],
              textile_2016["waste_type"]]).flatten()
    
    total = np.array([food_2016["waste_disposed_of_tonne"],
              others_2016["waste_disposed_of_tonne"],
              plastics_2016["waste_disposed_of_tonne"], 
              paper_2016["waste_disposed_of_tonne"],
              textile_2016["waste_disposed_of_tonne"]]).flatten()
     
    plt.pie(total, labels= names)
    plt.title("pie chart of wastes in 2016")
    plt.show()
    plt.savefig("piechart.png")



def graph3():
    '''
    This funtion indicates barchart of waste disposed in 2016
    '''
# barchart

    waste = ("food", "others", "paper", "plastics", "textile")
    year = np.array([food_2016["waste_disposed_of_tonne"],
              others_2016["waste_disposed_of_tonne"],
              plastics_2016["waste_disposed_of_tonne"], 
              paper_2016["waste_disposed_of_tonne"],
              textile_2016["waste_disposed_of_tonne"]]).flatten()
    
    plt.figure(figsize=(9,5))
    plt.bar(waste, year)
    plt.title("Waste disposed in 2016")
    plt.xlabel("Wastages")
    plt.ylabel("Disposed wastage in metric tonnes")
    plt.show()
    plt.savefig("barchart.png")



graph1()
graph2()
graph3()

