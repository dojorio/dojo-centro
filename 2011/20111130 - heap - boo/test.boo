import NUnit.Framework
import System


def pop(heap):
    if heap == []:
        return null
    
    x = heap[0]
    
    heap[0] = heap[-1]
    heap.Pop()
    
    def swap(i, j):
        temp = heap[i -1]
        heap[i -1] = heap[j -1]
        heap[j -1] = temp
      
    def isGreater(i, j):
        return heap.Count >= j and heap[i -1] > heap[j -1]
        
    def left(parent):
        return heap[parent * 2 - 1]
    
    def right(parent):
        return heap[parent * 2]
    
    def bubbleDown(parent, left, right):
        
        if isGreater(parent, right) and isGreater(left, right):
            swap(parent, right)
        elif isGreater(parent, left):
            swap(parent, left)
    
    bubbleDown(1, 2, 3)
    bubbleDown(2, 4, 5)
    
    return x
    
class HeapPopTests:
    [Test]
    def pop_heap_vazia():
        heap = []
        Assert.AreEqual(null, pop(heap))
        Assert.AreEqual([], heap)
    
    [Test]
    def pop_heap_com_1_elemento():
        heap = [1]
        Assert.AreEqual(1, pop(heap))
        Assert.AreEqual([], heap)

    [Test]
    def pop_heap_com_2_elementos_crescentes():
        heap = [1, 2]
        Assert.AreEqual(1, pop(heap))
        Assert.AreEqual([2], heap)

    [Test]
    def pop_heap_com_3_elementos_crescentes():
        heap = [1, 2, 3]
        Assert.AreEqual(1, pop(heap))
        Assert.AreEqual([2, 3], heap)
    
    [Test]
    def pop_heap_com_3_elementos_nao_crescentes():
        heap = [1, 3, 2]
        Assert.AreEqual(1, pop(heap))
        Assert.AreEqual([2, 3], heap)
    
    [Test]
    def pop_heap_com_4_elementos_crescentes():
        heap = [1, 2, 3, 4]
        Assert.AreEqual(1, pop(heap))
        Assert.AreEqual([2, 4, 3], heap)
        
    [Test]
    def pop_heap_com_4_elementos_nao_crescentes():
        heap = [1, 3, 2, 4]
        Assert.AreEqual(1, pop(heap))
        Assert.AreEqual([2, 3, 4], heap)
        
    [Test]
    def pop_heap_com_4_elementos_nao_crescentes_no_final():
        heap = [1, 2, 4, 3]
        Assert.AreEqual(1, pop(heap))
        Assert.AreEqual([2, 3, 4], heap)
        
    [Test]
    def pop_heap_com_5_elementos_crescentes():
        heap = [1, 2, 3, 4, 5]
        Assert.AreEqual(1, pop(heap))
        Assert.AreEqual([2, 4, 3, 5], heap)