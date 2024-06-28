import csv
import re
import random

# Conjunto para almacenar todos los user_id
all_user_ids = set()

# Comprueba que los valores de las columnas estén bien hechas evitando problemas con listas
def combine_list_values(row):
    combined_row = []
    inside_list = False
    combined_value = ""

    for value in row:
        if "[" in value and "]" not in value:
            inside_list = True
            combined_value = value
        elif inside_list:
            combined_value += "," + value
            if "]" in value:
                inside_list = False
                combined_row.append(combined_value)
        else:
            combined_row.append(value)

    return combined_row

# Combina valores de listas en una sola cadena y lo escribe en un documento para solo agarrar los valores que nos intersan del dataset
def transform(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            combined_row = combine_list_values(row)
            
            user_id = combined_row[0]
            user_screen_name = combined_row[1]
            follower_count = combined_row[4]
            friend_count = combined_row[5]
            
            writer.writerow([user_id, user_screen_name, follower_count, friend_count])



# Nombre de los archivos rutas 
input_file = 'data.csv'
output_file = 'UserWithData.csv'

# Llamar a la función
transform(input_file, output_file)