
class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.capacity = capacity
        self.heap = [0]
        self.size = 0

    def parent(self, index):
        return index // 2

    def left_child(self, index):
        return 2 * index

    def right_child(self, index):
        return (2 * index) + 1


    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        if self.is_full():
            return False

        self.heap.append(item)
        self.size += 1
        self.perc_up(self.size)
        return True

    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
                at that location to its proper place in the heap rearranging elements as it goes.'''
        while self.parent(i) > 0:
            if self.heap[i] > self.heap[self.parent(i)]:
                self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)



    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.is_empty():
            return None
        else:
            return self.heap[1]


    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        # Should call perc_down
        if self.is_empty():
            return None
        max = self.peek()
        iter = 1
        self.heap[iter] = self.heap[self.size]
        self.size -= iter
        self.heap.pop()
        self.perc_down(iter)
        return max


    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while self.left_child(i) <= self.size:
            if self.right_child(i) > self.size:
                maximo = self.left_child(i)
            elif self.heap[self.left_child(i)] > self.heap[self.right_child(i)]:
                maximo = self.left_child(i)
            else:
                maximo = self.right_child(i)

            if self.heap[i] < self.heap[maximo]:
                self.heap[i], self.heap[maximo] = self.heap[maximo], self.heap[i]
            i = maximo


    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        return self.heap[1:]


    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate 
        exactly the number of items in alist'''
        # Bottom-Up construction.  Do NOT call enqueue
        if self.capacity < len(alist):
            self.capacity = len(alist)
        i = self.parent(len(alist))
        self.size = len(alist)
        alist.insert(0, 0)
        self.heap = alist

        while i > 0:
            self.perc_down(i)
            i -= 1

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return self.size == 0


    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.size >= self.capacity

        
    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.capacity
    
    
    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.size


    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.heap = [0]
        for i in alist:
            self.enqueue(i)
        for i in range(len(alist) - 1, -1, -1):
            alist[i] = self.dequeue()



















