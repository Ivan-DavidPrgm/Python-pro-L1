meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL" : "una respuesta a una broma",
            "SHEESH" : "ligera desaprobación",
            "CREEPY" : "aterrador, siniestro",
            "AGGRO" : "ponerse agresivo/enojado",
            "AURA" : "algo con mucha impresion" ,
            "67" : "un numero meme",
            "OUTSEVEN" : "algo fuera de lugar",
            "LARP" : "fingir algo por moda"      
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
     print(word,": ",meme_dict[word])
else:
    print("Escriba otra o escribela bien")
