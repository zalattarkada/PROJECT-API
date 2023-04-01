
def get_recipes(api_key, num_results=100):
    '''esta función hace una request de la api de spoonacular'''
    url = f'https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}&number={num_results}&addRecipeInformation=true'
    api_key = '13dc080d47f14e8a9a759ac836d36aaf'
    # hacemos la request
    res = requests.get(url)

    # convertimos a json
    recipes = res.json()['results']

    # convertimos a df
    df = pd.DataFrame(recipes)

    return df