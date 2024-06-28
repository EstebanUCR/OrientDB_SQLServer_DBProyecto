import pandas as pd
import random

# Leer el archivo CSV original
input_file = 'UserWithData.csv'
df = pd.read_csv(input_file)

# Extraer la columna de IDs
ids = df['id'].tolist()

# Generar relaciones únicas
num_relations = 1_000_000
relations = set()

while len(relations) < num_relations:
    idMe = random.choice(ids)
    idFriend = random.choice(ids)
    if idMe != idFriend:
        relations.add((idMe, idFriend))

# Convertir el conjunto de relaciones a un DataFrame
relations_df = pd.DataFrame(list(relations), columns=['idMe', 'idFriend'])

# Guardar el nuevo DataFrame en un archivo CSV
output_file = 'UserRelations2.csv'
relations_df.to_csv(output_file, index=False)

print(f'Nuevo archivo CSV con relaciones guardado en: {output_file}')