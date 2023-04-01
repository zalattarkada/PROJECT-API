
def recommend_diet(df, vegetarian=False, vegan=False, dairyfree=False, glutenfree=False, 
                   time_range=None, kcal_range=None, protein_range=None):
    '''creamos un filtro de restricciones dietarias'''

    if vegetarian:
        df = df[~df['vegetarian']]
    if vegan:
        df = df[~df['vegan']]
    if dairyfree:
        df = df[~df['dairyfree']]
    if glutenfree:
        df = df[~df['glutenfree']]
        
    if time_range:
        if time_range == '0-15':
            df = df[df['minutes'] <= 15]
        elif time_range == '15-30':
            df = df[(df['minutes'] > 15) & (df['minutes'] <= 30)]
        elif time_range == '30-45':
            df = df[(df['minutes'] > 30) & (df['minutes'] <= 45)]
        elif time_range == '45-60':
            df = df[(df['minutes'] > 45) & (df['minutes'] <= 60)]
        elif time_range == '60+':
            df = df[df['minutes'] > 60]
    
    if kcal_range:
        if kcal_range == '0-150':
            df = df[df['calories'] <= 150]
        elif kcal_range == '150-300':
            df = df[(df['calories'] > 150) & (df['calories'] <= 300)]
        elif kcal_range == '300-450':
            df = df[(df['calories'] > 300) & (df['calories'] <= 450)]
        elif kcal_range == '450-600':
            df = df[(df['calories'] > 450) & (df['calories'] <= 600)]
        elif kcal_range == '600-750':
            df = df[(df['calories'] > 600) & (df['calories'] <= 750)]
        elif kcal_range == '750+':
            df = df[df['calories'] > 750]
    
    if protein_range:
        if protein_range == '0-10':
            df = df[df['protein_g'] <= 10]
        elif protein_range == '10-20':
            df = df[(df['protein_g'] > 10) & (df['protein_g'] <= 20)]
        elif protein_range == '20-30':
            df = df[(df['protein_g'] > 20) & (df['protein_g'] <= 30)]
        elif protein_range == '30-40':
            df = df[(df['protein_g'] > 30) & (df['protein_g'] <= 40)]
    
    return df