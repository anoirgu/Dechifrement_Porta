#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Med Anoir Guesmi

#defenition du tableaudu porta
matrice_porta=[
              [("a","n"),("b","o"),("c","p"),("d","q"),("e","r"),("f","s"),("g","t"),("h","u"),("i","v"),("j","w"),("k","x"),("l","y"),("m","z")],
              [("a","z"),("b","n"),("c","o"),("d","p"),("e","q"),("f","r"),("g","s"),("h","t"),("i","u"),("j","v"),("k","w"),("l","x"),("m","y")],
              [("a","y"),("b","z"),("c","n"),("d","o"),("e","p"),("f","q"),("g","r"),("h","s"),("i","t"),("j","u"),("k","v"),("l","w"),("m","x")],
              [("a","x"),("b","y"),("c","z"),("d","n"),("e","o"),("f","p"),("g","q"),("h","r"),("i","s"),("j","t"),("k","u"),("l","v"),("m","w")],
              [("a","w"),("b","x"),("c","y"),("d","z"),("e","n"),("f","o"),("g","p"),("h","q"),("i","r"),("j","s"),("k","t"),("l","u"),("m","v")],
              [("a","v"),("b","w"),("c","x"),("d","y"),("e","z"),("f","n"),("g","o"),("h","p"),("i","q"),("j","r"),("k","s"),("l","t"),("m","u")],
              [("a","u"),("b","v"),("c","w"),("d","x"),("e","y"),("f","z"),("g","n"),("h","o"),("i","p"),("j","q"),("k","r"),("l","s"),("m","t")],
              [("a","t"),("b","u"),("c","v"),("d","w"),("e","x"),("f","y"),("g","z"),("h","n"),("i","o"),("j","p"),("k","q"),("l","r"),("m","s")],
              [("a","s"),("b","t"),("c","u"),("d","v"),("e","w"),("f","x"),("g","y"),("h","z"),("i","n"),("j","o"),("k","p"),("l","q"),("m","r")],
              [("a","r"),("b","s"),("c","t"),("d","u"),("e","v"),("f","w"),("g","x"),("h","y"),("i","z"),("j","n"),("k","o"),("l","p"),("m","q")],
              [("a","q"),("b","r"),("c","s"),("d","t"),("e","u"),("f","v"),("g","w"),("h","x"),("i","y"),("j","z"),("k","n"),("l","o"),("m","p")],
              [("a","p"),("b","q"),("c","r"),("d","s"),("e","t"),("f","u"),("g","v"),("h","w"),("i","x"),("j","y"),("k","z"),("l","n"),("m","o")],
              [("a","o"),("b","p"),("c","q"),("d","r"),("e","s"),("f","t"),("g","u"),("h","v"),("i","w"),("j","x"),("k","y"),("l","z"),("m","n")]]
#dictionnaire qui lie les matrice avec les cle AB ,CD, EF, ....
dict_porta ={0:"AB",1:"CD",2:"EF" ,3:"GH",4:"IJ" ,5:"Kl",6:"MN",7:"OP",8:"QR",9:"ST",10:"UV",11:"WX",12:"YZ" }
#Liste qui contient les letre du premiere rang dans Le tableau du PORTA
List_First = ["a","b","c","d","e","f","g","h","i","j","k","l","m" ]
# List qui contient les lettre du deuxieme rang dans le tableau du PORTA
List_second =["n","o","p","q","r","s","t","u","v","w","x","y","z"]


print '''          *********************************************************************
          *                                                                   *
          *                                                                   *
          *           Dechiffrement Du Porta Avec Mot Probable                *
          *                Guesmi Mohamed Anoir                               *
          *                                                                   *
          *********************************************************************
          '''






while True :
    chiffre_porta = raw_input("Ecrire le texte chiffré  : \n")
    if chiffre_porta != "" and chiffre_porta!=" " :
        break
while True :
    mot_probable = raw_input("Ecrire le mot probable  : \n").lower()
    #il  faut que le mot probable soit <=  à la tialle du message
    if mot_probable != "" and mot_probable!=" " and len(mot_probable) <= len(chiffre_porta) :
        break

# metre le hash dans une liste en supremant les espaces
chifre_porta_list =[x.lower() for x in chiffre_porta if x!=" " ]
#construction d'une liste de nombre 1, 2 du  hach donneé
chifre_Porta_number =[ 1  if l in List_First  else 2 for l in chifre_porta_list]
mot_porbable_number =[1 if l in List_First else 2 for l in mot_probable]
# les 1 et 2 sont inverser car l'image chifrer d'une lettre qui appartient à la 1 ere moitie de l'alphabet  ,appartient à la deuxième moitie de l'alphabet et vice virca

mot_probable_number_complement = [2 if l in List_First else 1 for l in mot_probable]

#comparaison de deux list
def compar_list(list1,list2) :
    for i in range(len(list1)) :
        if list1[i]!=list2[i] :
            return False
    return True
#rechcerche d'indice de debut du chaine
def find_index_of_intersection() :
    for i in range(len(chifre_Porta_number)-len(mot_probable_number_complement)+1) :
        if compar_list(chifre_Porta_number[i:i+len(mot_probable_number_complement)],mot_probable_number_complement)==True :
             return i
#recherche de hach correspond au mot probable
def get_mot_in_hach():
    start = find_index_of_intersection()
    return chifre_porta_list[start:start+len(mot_probable_number_complement)]

mot_in_hash = get_mot_in_hach()


#fonction qui retourne l'index d'une tuple dans le dictionnaire du porta
def get_index(s):
    for i in range(13) :
        for j in range(13) :
            if matrice_porta[i][j]==s :
                return i,j

#variable pour stoker les number de ligne du key dans le dictionnaire
key_numb = list()

def get_Key() :
    key= []
    for i in range(len(mot_probable)) :
        #test si le chifre est dans le premier moitier ou non , pour
        #voir si on va utiliser son index ou l'index du hach
        if mot_probable[i] in List_First :
            x,y = get_index((mot_probable[i],mot_in_hash[i]))
        else :
            x,y = get_index((mot_in_hash[i],mot_probable[i]))
        key.append(dict_porta[x])
        key_numb.append(x)

    return key
key_word = get_Key()

#elémination des redondances
#le variable key contenule key sans redandonce
key = list()
for i in key_word  :
    if i[0] not in key :
        key.append(i[0])
#le variable key_number contient le numero du ligne dans le matrice de porta
key_number = list()
for i in key_numb :
    if i not in key_number :
        key_number.append(i)

#reputationdu key sous le hash
def constrcut_key_ender_hash() :
    repeat_key = []
    x=find_index_of_intersection()
    li= key_number*(len(chifre_porta_list)/len(key_number)+len(chifre_porta_list)%len(key_number))
    c=0
    for i in  range(x,len(chifre_porta_list)) :
        repeat_key.append(li[c])
        c+=1
    repeat_key2=[]
    t=[]
    if x != 0  :
        test=key_number
        test.reverse()
        li2=test*(len(chifre_porta_list)/len(key_number)+len(chifre_porta_list)%len(key_number))
        a=0
        for k in range(x) :
            repeat_key2.append(li2[a])
            a += 1
        t = repeat_key2
        t.reverse()
    return t+repeat_key

#la variable key_under_hash contient le key repeter
key_under_hash =  constrcut_key_ender_hash()

#fonction qui retourne le 1 ere carecter  d'un tuple dans le matrice de Porta
def get_caracter(i,c):
    for l in range(13):
        if matrice_porta[i][l][1]==c :
            return matrice_porta[i][l][0]
def get_clair_text() :
    text_clair = []
    for i in range(len(chifre_porta_list)) :
        if chifre_porta_list[i] in List_First :
            text_clair.append(matrice_porta[key_under_hash[i]][List_First.index(chifre_porta_list[i])][1])
        else:

            text_clair.append(get_caracter(key_under_hash[i],chifre_porta_list[i]))
    return  text_clair

text_claire = get_clair_text()
print  "La Cle est  : ","".join(key)
print  "Le Texte Claire est  : " , "".join(text_claire)























