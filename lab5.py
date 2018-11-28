#Isaiah Hernandez
#Lab 5
#11/27/18
#cs2302
class Heap:

    def __init__(self):
        self.heap_array = []
        
    def percolate_up(self, node_index):
        while node_index > 0:
            # compute the parent node's index
            parent_index = (node_index - 1) // 2
            
            # check for a violation of the min heap property
            if self.heap_array[node_index] >= self.heap_array[parent_index]:
                # no violation, so percolate up is done.
                return
            else:
                # swap heap_array[node_index] and heap_array[parent_index]
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = temp
                
                # continue the loop from the parent node
                node_index = parent_index

    def percolate_down(self, node_index):
        child_index = 2 * node_index + 1
        value = self.heap_array[node_index]

        while child_index < len(self.heap_array):
            # Find the min among the node and all the node's children
            min_value = value
            min_index = -1
            i = 0
            while i < 2 and i + child_index < len(self.heap_array):
                if self.heap_array[i + child_index] < min_value:
                    min_value = self.heap_array[i + child_index]
                    min_index = i + child_index
                i = i + 1

            # check for a violation of the min heap property
            if min_value == value:
                return
            else:
                # swap heap_array[node_index] and heap_array[min_index]
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[min_index]
                self.heap_array[min_index] = temp
                
                # continue loop from the min index node
                node_index = min_index
                child_index = 2 * node_index + 1

    def insert(self, k):
        # add the new value to the end of the array.
        
        self.heap_array.append(k)
        
        # percolate up from the last index to restore heap property.
        self.percolate_up(len(self.heap_array) - 1)
        
    def extract_min(self):
        # save the min value from the root of the heap.
        min_value = self.heap_array[0]
        
        # move the last item in the array into index 0.
        replace_value = self.heap_array.pop()
        if len(self.heap_array) > 0:
            self.heap_array[0] = replace_value
            
            # percolate down to restore min heap property.
            self.percolate_down(0)
                
        # return the min value
        return min_value



def min_heap_percolate_down(node_index, heap_list, list_size):
    child_index = 2 * node_index + 1
    value = heap_list[node_index]

    while child_index < list_size:
        # Find the min among the node and all the node's children
        min_value = value
        min_index = -1
        i = 0
        while i < 2 and i + child_index < list_size:
            if heap_list[i + child_index] > min_value:
                min_value = heap_list[i + child_index]
                min_index = i + child_index
            i = i + 1
                                    
        if min_value == value:
            return

        # Swap heap_list[node_index] and heap_list[min_index]
        temp = heap_list[node_index]
        heap_list[node_index] = heap_list[min_index]
        heap_list[min_index] = temp
        
        node_index = min_index
        child_index = 2 * node_index + 1


# Sorts the list of numbers using the heap sort algorithm
def heap_sort(numbers):
    # Heapify numbers list
    i = len(numbers) // 2 - 1
    while i >= 0:
        min_heap_percolate_down(i, numbers, len(numbers))
        i = i - 1
                
    i = len(numbers) - 1
    while i > 0:
        # Swap numbers[0] and numbers[i]
        temp = numbers[0]
        numbers[0] = numbers[i]
        numbers[i] = temp

        min_heap_percolate_down(0, numbers, i)
        i = i - 1

tree = Heap()
otherTree = Heap()
nums = [12, 3, 45, 16, 56, 100, 9]
hardNumlist = [4, 56, 78, 12, 81, 46, 1]

print("Hard list of numbers")
print(hardNumlist)
for i in hardNumlist:
    n = i
    print("inserting " + str(n))
    tree.insert(i)
print(' heap array before heap sort: %s\n' % tree.heap_array)
heap_sort(tree.heap_array)
print("heap array after heap sort:")
print(tree.heap_array)
for i in hardNumlist:
    tree.insert(i)
print("Extracting min from  heap tree")
while i < len(tree.heap_array):
    print("min is  " + str(tree.extract_min()))
        
        