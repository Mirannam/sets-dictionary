
menu = {'lagman': 120, 'plov': 120, "borsh": 100}
menu.update(besh_barmak = 130)
print(menu)
print("лагман слишком дешевый")
menu.update(lagman = 130)
print(menu)
print("Ваш повар отвратительно готовит удалите борщ")
menu.pop('borsh', 100)
print(menu)
