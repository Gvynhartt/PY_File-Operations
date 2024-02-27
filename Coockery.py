as_list = []  # весь файл в виде списка
as_dict = {}  # словарь, куда будет добавляться отформатированная инфа по блюдам

with open('recipes.txt', 'r', encoding='utf-8') as source:
    for line in source:
        filt_line = line.replace("\n", "")
        as_list.append(filt_line)

    if (as_list[len(as_list) - 1] != ''):
        as_list.append('')
    # да, это костыль, но мне очень лень думать
    # таким образом в конце списка добавляется дополнительный перенос,
    # \и не надо будет делать мозги при разбиении списка на подсписки


def make_dict_for_dish(dish):  # принимает на вход подсписок блюда
    dish_entry = {}
    dish_key = dish[0]
    dish_value = []

    for idx in range(2, len(dish)):
        ingr_dict = {}
        ingr_line = dish[idx]

        sep_str = ' | '
        sep1 = ingr_line.find(sep_str, 0, )  # индекс первого разделителя
        ingr_line2 = ingr_line[sep1 + len(sep_str)::]
        sep2 = ingr_line2.find(sep_str, 0, )  # индекс второго разделителя

        name = ingr_line[0:sep1:]
        quant = ingr_line2[0:sep2:]
        measr = ingr_line2[sep2 + len(sep_str)::]

        # пишем всё это в словарь
        ingr_dict['ingredient_name'] = name
        ingr_dict['quantity'] = quant
        ingr_dict['measure'] = measr
        # пушим словарь в список
        dish_value.append(ingr_dict)
        # список присваиваем блюду
        dish_entry[dish_key] = dish_value
    return dish_entry


def sep_list_by_dishes(list):  # создаёт подсписок для каждого ингредиента
    idx_start = 0
    idx_end = 0
    list_ingred = []
    for pos, elem in enumerate(list):
        if elem == '':
            idx_end = pos
            list_ingred = list[idx_start:idx_end]
            idx_start = idx_end + 1
            # форматируем подсписок блюда до вида словаря
            new_dish = make_dict_for_dish(list_ingred)
            # добавляем отформатированное блюдо в словарь со всеми блюдами
            as_dict.update(new_dish)


sep_list_by_dishes(as_list)
# print(as_dict)


def make_shop_list_for_dishes(dish_list, nmb_persons):
    outp_dict = {}
    # сюда записывается выходной словарь с подчсётами
    for dish in dish_list:
        if dish in as_dict.keys():
            ingr_list = as_dict[dish]
            for ingr in ingr_list:
                if ingr['ingredient_name'] not in outp_dict.keys():
                    ingr_name = ingr['ingredient_name']
                    ingr_measr = ingr['measure']
                    ingr_quant = int(ingr['quantity']) * nmb_persons
                    # подсловарь для ингр-та, куда записываются ед. изм. и кол-во
                    ingr_vals = {}
                    ingr_vals['measure'] = ingr_measr
                    ingr_vals['quantity'] = ingr_quant
                    # пуш в конечный словарь
                    outp_dict[ingr_name] = ingr_vals
                else: # вариант, если ингр-нт уже добавлен в конечный словарь
                    # получаем уже имеющееся кол-во ингр-та
                    ingr_name0 = ingr['ingredient_name']
                    ingr_quant0 = int(outp_dict[ingr_name0]['quantity'])
                    ingr_name = ingr['ingredient_name']
                    ingr_measr = ingr['measure']
                    # суммируем с уже имеющимся в конеч. сл-ре кол-вом инг-та
                    ingr_quant = int(ingr['quantity']) * nmb_persons + ingr_quant0
                    # подсловарь для ингр-та, куда записываются ед. изм. и кол-во
                    ingr_vals = {}
                    ingr_vals['measure'] = ingr_measr
                    ingr_vals['quantity'] = ingr_quant
                    # пуш в конечный словарь
                    outp_dict[ingr_name] = ingr_vals
    return outp_dict

print(make_shop_list_for_dishes(['Омлет', 'Фахитос', "Шарлотка"], 3))