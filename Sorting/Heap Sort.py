from heapq import heappush, heappop
def heapSort(tab):
    heap = []
    for value in tab:
        heappush(heap, value)
    return [heappop(heap) for i in range(len(heap))]
tab = [5, 4, 12, 2234, 331, 7, 136]
tab = heapSort(tab)
print(tab)
