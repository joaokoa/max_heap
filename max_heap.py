def max_heapify(A, n, i):
    """Mantém a propriedade de heap máximo"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and A[left] > A[largest]:
        largest = left
        
    if right < n and A[right] > A[largest]:
        largest = right
        
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)

def build_max_heap(A):
    """Constrói um heap máximo a partir de um array"""
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(A, n, i)

# Exemplo de uso
if __name__ == "__main__":
    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print("Array original:", arr)
    build_max_heap(arr)
    print("Heap máximo:", arr)
    # Saída esperada: [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
