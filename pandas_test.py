import pandas as pd

random_dict = {
    "pog": [8, 6, 5, 4, 3],
    "nog": [1, 2, 3, 4, 5],
    "namesies": ["Henrieta", "Tiffany", "George", "Billy-Jean", "Meagan"]
}

df = pd.DataFrame(random_dict)

print(df.loc[[0, 1], ['namesies', 'pog']])