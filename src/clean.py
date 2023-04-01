import re
def extract_minutes(summary):
    '''crea una nueva columna de minutos extrayendolas de la columna summary'''
    
    minutes_match = re.search(r'<b>(\d+?)\s+minutes?</b>', summary)
    if minutes_match:
        return int(minutes_match.group(1))
    else:
        return None
    
def extract_calories(summary):
    '''crea una nueva columna de calorias extrayendolas de la columna summary'''

    calories_match = re.search(r'<b>(\d+?)\s+calories?</b>', summary)
    if calories_match:
        return int(calories_match.group(1))
    else:
        return None
    
def extract_protein(summary):
    '''crea una nueva columna de proteinas extrayendolas de la columna summary'''

    protein_match = re.search(r'<b>(\d+?)g(?:\sof)?\s+protein</b>', summary)
    if protein_match:
        return int(protein_match.group(1))
    else:
        return None
