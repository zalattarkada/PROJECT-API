
def recommend_diet(df, vegetarian=True, vegan=True, dairyfree=True, glutenfree=True, 
                   time_range=None, kcal_range=None, protein_range=None):
    '''creamos un filtro de restricciones dietarias'''

    if vegetarian:
        df = df[df['vegetarian'] == True]
    if vegan:
        df = df[df['vegan'] == True]
    if dairyfree:
        df = df[df['dairyfree'] == True]
    if glutenfree:
        df = df[df['glutenfree'] == True]
        
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


def widget_recipes(df):
    # creamos checkdowns para las alergias
    vegetarian = widgets.Checkbox(value=True, description='Vegetarian')
    vegan = widgets.Checkbox(value=True, description='Vegan')
    dairyfree = widgets.Checkbox(value=True, description='Dairy Free')
    glutenfree = widgets.Checkbox(value=True, description='Gluten Free')

    # creamos dropdowns para los rangos de valores nutricionales
    time_range = widgets.Dropdown(options=['0-15', '15-30', '30-45', '45-60', '60+'], 
                                  description='Time Range')
    kcal_range = widgets.Dropdown(options=['0-150', '150-300', '300-450', '450-600', '600-750', '750+'], 
                                  description='Calories Range')
    protein_range = widgets.Dropdown(options=['0-10', '10-20', '20-30', '30-40'], 
                                     description='Protein Range')

    # creamos botón para filtrar las recetas
    filter_button = widgets.Button(description='Filter Recipes')

    # creamos el output
    output = widgets.Output()

    # define function to handle filter button click
    def filter_recipes(button):
        # función para limpiar el output previo
        output.clear_output() 
        with output:
            # aplicar los filtros a las recetas
            filtered_df = recommend_diet(df, vegetarian=vegetarian.value, vegan=vegan.value, 
                                      dairyfree=dairyfree.value, glutenfree=glutenfree.value, 
                                      time_range=time_range.value, kcal_range=kcal_range.value, 
                                      protein_range=protein_range.value)

            # seleccionar solo las columnas que queremos para el output
            filtered_df = filtered_df[['title', 'image', 'spoonacularsourceurl']]

            # mostrar mensaje si no hay recetas que se ajusten a la selección
            if filtered_df.empty:
                print('No recipes found. Please adjust your search criteria.')
            else:
                # mostrar las recetas
                for _, row in filtered_df.iterrows():
                    display(widgets.HTML(f'<h3>{row["title"]}</h3><img src="{row["image"]}" /><br><a href="{row["spoonacularsourceurl"]}">{row["spoonacularsourceurl"]}</a>'))

            # limpiar el mensaje en caso de no encontrarse recetas
            if filtered_df.empty and len(output.outputs) > 0:
                output.clear_output()

    # añadir botón
    filter_button.on_click(filter_recipes)

    # display widgets
    display(widgets.VBox([widgets.HBox([vegetarian, vegan, dairyfree, glutenfree]),
                          widgets.HBox([time_range, kcal_range, protein_range]),
                          filter_button,
                          output]))
