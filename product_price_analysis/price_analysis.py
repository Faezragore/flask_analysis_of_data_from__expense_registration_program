#!/usr/bin/python3
# -*- coding: utf-8 -*-

from locale import resetlocale
import sqlite3
from sqlite3 import Error
import re
import datetime
import sys
import os
import math
import time
from jinja2 import Template

#position = ["Еда", "Хлеб (батон)", "Овощи", "Крупы,макароны", "Печенье(конфеты и другое сладкое)", "Молочка(молоко,кефир,творог)", "Мясо(кура,гов,свинина,индейка)", "Пюре,йогурт детям.", "Ветчина(колбаса,сосиски)", "Вкусности детям", "Работа_еда", "Школа_питание", "Фрукты", "Рыба"]
 
class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()


    def amount_for_year(self, choosing_year):
#        sql = f"""SELECT round(sum(-1*(Value))) FROM expenses_for_year_all_time
#             WHERE Category IN ('Еда', 'Хлеб (батон)', 'Фрукты', 'Овощи', 'Крупы,макароны', 'Печенье(конфеты и другое сладкое)', 'Молочка(молоко,кефир,творог)', 'Мясо(кура,гов,свинина,индейка)', 'Пюре,йогурт детям.', 'Ветчина(колбаса,сосиски)', 'Вкусности детям', 'Работа_еда', 'Школа_питание', 'Рыба') 
#            AND DateTime LIKE '{choosing_year}-%';"""
        try:
            sql = f"""SELECT round(sum(-1*(Value))) FROM expenses_for_year_all_time
                 WHERE Category IN ('Еда', 'Хлеб (батон)', 'Фрукты', 'Овощи', 'Крупы,макароны', 'Печенье(конфеты и другое сладкое)', 'Молочка(молоко,кефир,творог)', 'Мясо(кура,гов,свинина,индейка)', 'Пюре,йогурт детям.', 'Ветчина(колбаса,сосиски)', 'Вкусности детям', 'Работа_еда', 'Школа_питание', 'Рыба') 
                 AND DateTime LIKE '{choosing_year}-%';"""
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            #print(choosing_year)
            for summa in res:
                print(summa[0])
                if summa: return summa[0]
            #result_str = str(res[0])
            #result_str = re.sub(r'\(|\)', '', result_str)
            #result_str = result_str.replace(",", "")
            #result_str = int(float(result_str))
            #table.add_row(result_str)
            #console = Console()
            #console.print(table)
            #return result_str
#                if i: return i
            print(result_str)
            return summa
        except:
            print("Ошибка чтения из БД")
#        except sqlite3.Error as error:
#            print("Ошибка чтения из БД", error)
        #return []


    def monthly_amount(self, choosing_year, choosing_month, position):
        #print(position)
#        total_amount = 0
#        for i in position:
#            print(i)
#            user = (selected_year, choosing_month, i)
#            print(len(i))
        #try:
            total_amount = 0
            position_dict = {}
            #position_list = []
            for one_position in position:
                position_list = []
                #print(i)
                user = (choosing_year, choosing_month, one_position)
                sql = f"""SELECT coalesce(sum(-1*(Value)), 0) FROM expenses_for_year_all_time WHERE DateTime LIKE "{choosing_year}-{choosing_month}%" AND Category = "{one_position}";"""
                #coalesce(sum(-1*(Value)), 0)
                #print(sql)
                self.__cur.execute(sql)
                #res = self.__cur.fetchall()
                res = self.__cur.fetchone()
                #for result in self.__cur:
                #print(res['Value'])
                result_str = res[0]
                #print(i, result_str)
                position_list.append(int(round(result_str)))
                #position_dict[one_position] = int(round(result_str))
                position_dict[one_position] = round(result_str)
                total_amount += result_str
            price = round(total_amount)
            #print("price", price)
            for key, value in position_dict.items():
                print(key, value)
            #print(position_dict)
            #if price: return price
            #print(position_list)
            #return price
            return position_dict


    def monthly_amount2(self, choosing_year, choosing_month, position):
        #print(position)
#        total_amount = 0
#        for i in position:
#            print(i)
#            user = (selected_year, choosing_month, i)
#            print(len(i))
        #try:
            total_amount = 0
            position_dict = {}
            #position_list = []
            for one_position in position:
                position_list = []
                #print(i)
                user = (choosing_year, choosing_month, one_position)
                #print(user)
                #sql = f"""SELECT round(sum(-1*(Value))) FROM expenses_for_year_all_time WHERE DateTime LIKE "{choosing_year}-{choosing_month}%" AND Category = "{i}";""" 
                #sql = f"""SELECT sum(-1*(cast(Value AS INT))) FROM expenses_for_year_all_time WHERE DateTime LIKE "{choosing_year}-{choosing_month}%" AND Category = "{i}";"""
                sql = f"""SELECT coalesce(sum(-1*(Value)), 0) FROM expenses_for_year_all_time WHERE DateTime LIKE "{choosing_year}-{choosing_month}%" AND Category = "{one_position}";"""
                #coalesce(sum(-1*(Value)), 0)
                #print(sql)
                self.__cur.execute(sql)
                #res = self.__cur.fetchall()
                res = self.__cur.fetchone()
                #for result in self.__cur:
                #print(res['Value'])
                result_str = res[0]
                #print(i, result_str)
                position_list.append(int(round(result_str)))
                #position_dict[one_position] = int(round(result_str))
                position_dict[one_position] = round(result_str)
                #show_product_statistics(self, one_position, result_st)
                #position_list.extend([i, int(round(result_str))])
                #result_str = sum
                #total_amount += (round(float(res)))
                #print("знать сумму", round(float(res)))
                #print("res с нулем", res[0])
#                if res[0] == 'None':
#                    res[0] = 0.0
#                    print("res", res[0])    
                #for summa in res:
                    #if res[0] is None:
#                   if (res[0]):
                        #res[0] = 0.0
                        #print("res", res[0])
                    #else:
                        #print("none", None)   
                    #print("summa", summa[0])
                    #print(type(summa[0]))
                    #print("total_amount", total_amount)
                total_amount += result_str
            #print(total_amount)
            #print(type(total_amount))
                #if summa: return summa[0]
            price = round(total_amount)
            posit = one_position
            print(posit)
            #print("price", price)
            for key, value in position_dict.items():
                print(key, value)
            #print(position_dict)
            #if price: return price
            #print(position_list)
            return price
            #return position_dict
            #result_str = str(res[0])
            #result_str = re.sub(r'\(|\)', '', result_str)
            #result_str = result_str.replace(",", "")
            #result_str = int(float(result_str))
            #table.add_row(result_str)
            #console = Console()
            #console.print(table)
            #return result_str
#                if i: return i
            #print(result_str)
            #return res
#        except:
#            print("Ошибка чтения из БД")  
#            
    def show_product_statistics(self, one_position, result_str):
        position_dict = {}
        position_dict[one_position] = int(round(result_str))
        return position_dict
        #for key, value in position_dict.items():
        #    return key, value
        








