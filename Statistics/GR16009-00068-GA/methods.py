import numpy as np
import csv
import collections
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.pyplot import figure

def build_dict_from_csv():
    fabricante = []
    general_dict = {}
    with open("VendaCarros.csv",  newline='',encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for val,row in enumerate(csv_reader):
            if val ==0:
                for i in row:
                    general_dict[i]= [] 
            general_dict["Fabricante"].append(row[0])
            general_dict["Estado"].append(row[1])
            general_dict["ValorVenda"].append(row[2])
            general_dict["ValorCusto"].append(row[3])
            general_dict["TotalDesconto"].append(row[4])
            general_dict["CustoEntrega"].append(row[5])
            general_dict["CustoMaoDeObra"].append(row[6])
            general_dict["Ano"].append(row[7])
            general_dict["Lucro"].append(row[8])

        for k,v in general_dict.items():
            del general_dict[k][0]
    return general_dict

def check_both(data: dict, x:tuple, y:tuple):
    """
    checks two classes and return occurences of x and y between them.
    data: dict. dict with csv data in lists
    x: tuple. First value: the dict key, second value: item to be searched
    y: tuple. First value: the dict key, second value: item to be searched
    returns: the ocurrence of the items on x and y simultaneously
    """
    occurence = 0
    assert len(data[x[0]]) == len(data[y[0]]), "categories have different sizes."
    for i in range(len(data[x[0]])):
        if (data[x[0]][i]==x[1]) and (data[y[0]][i]==y[1]):
            occurence+=1
    return occurence

def check_occurence(data: dict, search_for:str , sub_classes:list):
    x = []
    for i in range(len(data[search_for])):
        current_row = [elem[i] for elem in data.values()]
        if set(sub_classes).issubset(current_row):
            x.append(data[search_for][i])
    return x

def histograms(main_key: str, sort_by: str, val_range:tuple=None, _dict:dict=None):
    # plot histograms for the main key sorted by something
    # example: plot histograms of CustoEntrega for each "estado"
    # so main_key = CustoEntrega, sort_by = Estado
    # TODO: val_range can be improved, but I dont know the best way to group values to show best distribuition
    general_dict = _dict
    figure(figsize=(7,7), dpi=100)
    maoDeObra = sorted([int(x) for x in general_dict[main_key]])
    if val_range is None: 
        bin = np.arange(0,1500,200)
    else:
        bin = np.arange(val_range[0], val_range[1] + ((val_range[1]/7.5)/2) ,val_range[1] / 7.5)
    
    plt.hist(maoDeObra, bins=bin)
    plt.grid()
    plt.title(f"{main_key} - Geral")
    plt.show()

    # Per state
    cost_per_state = {}
    for state in list(set(general_dict[sort_by])):
        cost_per_state[state] = np.array(check_occurence(data=general_dict, search_for= main_key, sub_classes=[state]))
        print(f"{main_key} - {state} mean: R$ {np.mean(np.array(cost_per_state[state]).astype(np.int64))}")

    print(f"\nHistogramas {main_key} por {sort_by}:")
    for state in list(set(general_dict[sort_by])):
        figure(figsize=(7, 7), dpi=100)
        plt.hist(sorted([int(x) for x in cost_per_state[state]]), bins=bin)
        plt.grid()
        plt.title(f"{main_key} - {state}")
        plt.show()
