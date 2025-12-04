
zakupy= { 
    "Piekarnia" : "chleb, bulka, pączek",
    "Warzywniak": "marchew, seler, rukola"
}
suma =0

for key, value in zakupy.items():
    key_duze= key.title()
    value_duze=value.title()
    print("Idę do ", key_duze,"kupić nastepujące rzeczy",value_duze)
for i in zakupy.values():
    produkty=[a.strip() for a in value.split(",")] # odzielam produkty tak, żeby dla pythona to były odzielne wyrazy a nie całość 
    suma+= len(produkty)
print (" Łączna suma produktów: ", suma)



    


