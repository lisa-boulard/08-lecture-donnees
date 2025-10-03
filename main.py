import csv
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l=[]
    with open(filename, 'r', encoding='latin-1') as f:
        r=csv.reader(f,delimiter=';')
        for i in r:
            i_nums = [float(x) if '.' in x else int(x) for x in i]
            l.append(i_nums)
    return l

def get_list_k(data, k):
    if 0 <= k < len(data):
        return data[k]
    else:
        return None




def get_first(l):
    if len(l) > 0:
        return l[0]
    else:
        return None

def get_last(l):
    if len(l) > 0:
        return l[-1]
    else:
        return None

def get_max(l):
    if len(l) > 0:
        return max(l)
    else:
        return None

def get_min(l):
    if len(l) > 0:
        return min(l)
    else:
        return None

def get_sum(l):
    if len(l) > 0:
        return sum(l)
    else:
        return None



#### Fonction principale


def main():
    data = read_data(FILENAME)
    for i, l in enumerate(data):
         print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
