
def selectionSort(array):
    num_sorted = 0
    while num_sorted < len(array) - 1:
      smallest_ind = num_sorted
      for i in range(num_sorted + 1, len(array)):
        if array[i] < array[smallest_ind]:
          smallest_ind = i
      swap(num_sorted, smallest_ind, array)
      num_sorted += 1
    return array

def swap(i, j, array):
  	array[i], array[j] = array[j], array[i]
