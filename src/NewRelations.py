import csv
import re
import random
# Conjunto para almacenar todos los user_id
all_user_ids = set()
friends_list = set()

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

def init_list_all_user_ids():
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        
        for row in reader:
            combined_row = combine_list_values(row)
            all_user_ids.add(combined_row[0])

def transform(input_file, output_file2):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file2, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        init_list_all_user_ids()
        for row in reader:
            combined_row = combine_list_values(row)
            
            user_id = combined_row[0]
            friend_count = combined_row[5]
            
            try:
                friend_count = int(friend_count)
                if(friend_count != 0):
                    all_user_ids_list = list(all_user_ids)  # Convertir el conjunto a lista
                    # Generate a list of unique random numbers within a specified range
                    unique_list_friend = random.sample(range(1, 40000), friend_count)  # Example range
                    for i in range(friend_count):
                        writer.writerow([user_id, all_user_ids_list[unique_list_friend[i]]])
                    
            except ValueError:
                # handle the exception here, e.g. print an error message or take appropriate action
                pass

# Nombre de los archivos rutas 
input_file = 'data.csv'
output_file = 'UserWithRelations.csv'

# Llamar a la función
transform(input_file, output_file)