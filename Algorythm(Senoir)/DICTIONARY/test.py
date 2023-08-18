# Practice
# studentRecord = [
#     {"studentName":"Seyla","class":"wep-a","algorithm":98,"html":90},
#     {"studentName":"seyha","class":"wep-b","algorithm":80,"html":90},
#     {"studentName":"Villa","class":"wep-a","algorithm":96,"html":92},
#     {"studentName":"mengheang","class":"wep-a","algorithm":66,"html":54},
# ]
# htmlScore=0
# algoScore=0
# nbOfstu=0
# for dic in studentRecord:
#     algoScore+=dic["algorithm"]
#     htmlScore+=dic["html"]
#     nbOfstu+=1
# print("Average of algorithm:", round(algoScore/nbOfstu))     
# print("Average of html:", round(htmlScore/nbOfstu))     
# round use for convert from float to integer  



# Practice1
# def quantity(dict):
#     count=0
#     for key in dict:
#         count+=dict[key]
#     return count
        
# listOfFruites=eval(input())
# result = quantity(listOfFruites)
# print(result)



# Practice2
# def quantity(array):
#     count=0
#     for dict in array:
#         count+=dict["quantity"]
#     return count
# fruitsList=[{"name":"Banana", "quantity":16},
#             {"name":"Orange", "quantity":4}]
# result=quantity(fruitsList)
# print(result)




# Practice3
        # <---------Function--------------->
# def nameOfFruits(fruit):
#     if fruit["quantity"] > 0:
#         return fruit["name"]
             
#         # <-------------Main Program--------------> 
# array=[{"name":"Banana","quantity":10},
#         {"name":"Orange","quantity":0},
#         {"name":"apple","quantity":7}]
# for dict in array:
#     result = nameOfFruits(dict)
#     if result != None:
#         print(result)




# # Practice4
#         <------------Function---------------->
# def nameOfFruits(fruit, dict):
#     return fruit[dict]["quantity"]*fruit[dict]["price"]
    
#         <---------------Main Program--------------->
# array=[{"name":"Banana","quantity":3,"price":10},
#        {"name":"Orange","quantity":4,"price":14}]
# price=0
# for index in range(len(array)):
#     price+=nameOfFruits(array,index)
# print(price)




# Practice 5



    
                    
                
    
