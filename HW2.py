# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 00:23:02 2021

@author: clu1

HW #2: Mattress POS Prototype
This program will calculate the cost of a mattress

I completed this work individually
"""
tax_rate = .0625
promo_discount = .1

print("Welcome to the mattress price simulator!")


#Gets the mattress brand and stores it as Sealy or Simmons
#Gets the size based on if brand is Sealy or Simmons
mattress_brand = input('Please select the mattress brand (1 - Sealy, 2 - Simmons): ')
while mattress_brand != "1" and mattress_brand != "2":
    mattress_brand = input("Please enter '1' or '2': ")  
if mattress_brand == "1":
    mattress_brand = 'Sealy'
    size = input("Please select the size (K = King, Q = Queen, T = Twin): ")
    #Makes string uppercase to accept both upper and lowercase
    size = size.capitalize()
    while size != "K" and size != "Q" and size != "T":
        size = input("Please enter 'K', 'Q', or 'T': ")
        size = size.capitalize()
if mattress_brand == "2":
    mattress_brand = 'Simmons'
    size = input("Please select the size (K = King, Q = Queen, F = Full): ")
    #Makes string uppercase to accept both upper and lowercase
    size = size.capitalize()
    while size != "K" and size != "Q" and size != "F":
        size = input("Please enter 'K', 'Q', or 'F': ")
        size = size.capitalize()
if size == "K":
    size = "King"
if size == "Q":
    size = "Queen"
if size == "T":
    size = "Twin"
if size == "F":
    size = "Full"


comfort_level = input("Please enter the comfort level (M - Medium, F - Firm, E - Extra Firm): ")
comfort_level = comfort_level.capitalize()
while comfort_level != "M" and comfort_level != "F" and comfort_level != "E":
    comfort_level = input("Please enter 'M', 'F', or 'E': ")
    comfort_level = comfort_level.capitalize()
if comfort_level == "M":
    comfort_level = "Medium"
if comfort_level == "F":
    comfort_level = "Firm"
if comfort_level == "E":
    comfort_level = "Extra Firm"
    
box_springs = input("Do you like to have box springs? (Y - Yes, N - No): ")
box_springs = box_springs.capitalize()
while box_springs != "Y" and box_springs != "N":
    box_springs = input("Please enter 'Y' or 'N': ")
    box_springs = box_springs.capitalize()

shipping = input("Which shipping mode do you like? (S - Standard, N - Next Day): ")
shipping = shipping.capitalize()
while shipping != "S" and shipping != "N":
    shipping = input("Please enter 'S' or 'N': ")
    shipping = shipping.capitalize()
if shipping == "S":
    shipping_price = 100
else:
    shipping_price = 300

promotion = input("Promotion code: ")
promotion = promotion.lower()

#symbolic constants for mattress each option
sealy_medium_king = 1800
sealy_medium_queen = 1400
sealy_medium_twin= 900
sealy_firm_king= 2200
sealy_firm_queen = 1800
sealy_firm_twin = 1300
sealy_extra_king = 2400
sealy_extra_queen = 2000
sealy_extra_twin = 1500
simmons_medium_king = 2000
simmons_medium_queen = 1400
simmons_medium_full = 1000
simmons_firm_king = 2500
simmons_firm_queen = 1900
simmons_firm_full = 1500
simmons_extra_king = 3000
simmons_extra_queen = 2400
simmons_extra_full = 2000

print("========== Order Summary ==========")
print(mattress_brand + ", " + size + ", " + comfort_level + ": ")

#prints the mattress price
if mattress_brand == "Sealy":
    if comfort_level == "Medium":
        if size == "King":
            print(f"Mattress:          $ {sealy_medium_king:,.2f}")
            mattress_price = sealy_medium_king
        if size == "Queen":
            print(f"Mattress:           $ {sealy_medium_queen:,.2f}")
            mattress_price = sealy_medium_queen
        if size == "Twin":
            print(f"Mattress:           $ {sealy_medium_twin:,.2f}")
            mattress_price = sealy_medium_twin
    if comfort_level == "Firm":
        if size == "King": 
            print(f"Mattress:           $ {sealy_firm_king:,.2f}")
            mattress_price = sealy_firm_king
        if size == "Queen":
            print(f"Mattress:           $ {sealy_firm_queen:,.2f}")
            mattress_price = sealy_firm_queen
        if size == "Twin":
            print(f"Mattress:           $ {sealy_firm_twin:,.2f}")
            mattress_price = sealy_firm_twin
    if comfort_level == "Extra Firm":
        if size == "King":
            print(f"Mattress:           $ {sealy_extra_king:,.2f}")
            mattress_price = sealy_extra_king
        if size == "Queen":
            print(f"Mattress:           $ {sealy_extra_queen:,.2f}")
            mattress_price = sealy_extra_queen
        if size == "Twin":
            print(f"Mattress:           $ {sealy_extra_twin:,.2f}") 
            mattress_price = sealy_extra_twin
if mattress_brand == "Simmons":
    if comfort_level == "Medium":
        if size == "King":
            print(f"Mattress:          $ {simmons_medium_king:,.2f}")
            mattress_price = simmons_medium_king
        if size == "Queen":
            print(f"Mattress:          $ {simmons_medium_queen:,.2f}")
            mattress_price = simmons_medium_queen
        if size == "Full":
            print(f"Mattress:          $ {simmons_medium_full:,.2f}")
            mattress_price = simmons_medium_full
    if comfort_level == "Firm":
        if size == "King":
            print(f"Mattress:          $ {simmons_firm_king:,.2f}")
            mattress_price = simmons_firm_king
        if size == "Queen":
            print(f"Mattress:          $ {simmons_firm_queen:,.2f}")
            mattress_price = simmons_firm_queen
        if size == "Full":
            print(f"Mattress:          $ {simmons_firm_full:,.2f}")
            mattress_price = simmons_firm_full
    if comfort_level == "Extra Firm":
        if size == "King":
            print(f"Mattress:          $ {simmons_extra_king:,.2f}")
            mattress_price = simmons_extra_king
        if size == "Queen":
            print(f"Mattress:          $ {simmons_extra_queen:,.2f}")
            mattress_price = simmons_extra_queen
        if size == "Full":
            print(f"Mattress:          $ {simmons_extra_full:,.2f}") 
            mattress_price = simmons_extra_full


#Prints box spring price
if box_springs == "Y":
    if size == "King":
        box_springs = 400
        print(f"Box springs:       $   {box_springs:,.2f}")
    if size == "Queen":
        box_springs = 300
        print(f"Box springs:       $   {box_springs:,.2f}")
    if size == "Full":
        box_springs = 200
        print(f"Box springs:       $   {box_springs:,.2f}")           
    if size == "Twin":
        box_springs = 100
        print(f"Box springs:       $   {box_springs:,.2f}")
else:
    box_springs = 0


if promotion == "sleep":
    discount = (mattress_price + box_springs)*promo_discount*-1
    print(f"Discount:          $  {discount:,.2f}")
else:
    discount = 0
    
subtotal = mattress_price + box_springs + discount
print(f"Subtotal:          $ {subtotal:,.2f}")

if shipping == 'N':
    print(f"Next day shipping: $   {shipping_price:,.2f}")
else:
    print(f"Standard shipping: $   {shipping_price:,.2f}")

tax = subtotal*tax_rate
print(f"Tax:               $   {tax:,.2f}")

print("-----------------------------------")
total = subtotal + shipping_price + tax
print(f"Total:             $ {total:,.2f}")


















