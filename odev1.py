# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:
# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# output: [1,'a','cat',2,3,'dog',4,5]
#
# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
# Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:
# input: [[1, 2], [3, 4], [5, 6, 7]]
# output: [[[7, 6, 5], [4, 3], [2, 1]]


def flatten(list0):
    """
          Eğer list0 'ın elemanı bir liste değilse bu elemanı yeni listeye ekler.
          Eğer list0 'ın elemanıda bir liste ise fonksiyon kedisini çağırır(recursion). Böylece eleman liste olmayana kadar fonksiton kendini çağırır ve
          sonunda eleman bir liste değilse onu yeni listeye ekler.
    """
    new_list = []
    for idx in list0:
        if isinstance(idx, list):
            new_list += flatten(idx)
        else:
            new_list.append(idx)

    return new_list


# example for flatten function
l = [[1, 'a', ['cat'], 2], [[[[[[[10, 20, ['x']]]]]]]], [[[3]], 'dog'], 4, 5]

print(flatten(l))


def reversed_elements(list0):
    """
          Önce listenin elemanlarını slacing yöntemi kullanarak sondan başlayacak şekilde modifiye eder.
          Sonra listenin elemanlarıda bir liste mi diye kontrol edip eğer listeyse aynı işlem yine yapılır.
    """
    """
        Önce listenin elemanlarını slacing yöntemi kullanarak sondan başlayacak şekilde modifiye eder.
        Sonra listenin elemanlarıda bir liste mi diye kontrol edip eğer listeyse aynı işlem yine yapılır.
    """
    list0 = list0[-1::-1]
    for idx in list0:
        if isinstance(idx, list):
            index = list0.index(idx)  # düzenleyeceğimiz elemanın list0 içindeki indexsini bulma
            new_idx = idx[-1::-1]
            list0[index] = new_idx  # düzenlediğimiz elemanı listenin ilgili kısmına koyuyoruz
    return list0

# example for reserved_elements function
print(reversed_elements([[1, 2], [3, 4], [5, 6, 7]]))
