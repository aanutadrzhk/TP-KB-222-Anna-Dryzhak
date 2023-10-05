def findMinElemWithIndex(listForSearch:list):
    min_id = 0
    min_elem = listForSearch[0]

    for i, elem in enumerate(listForSearch):
        if elem < min_elem:
            min_elem = elem
            min_id = i

    return min_id, min_elem

def findMaxElemWithIndex(listForSearch:list):
    max_id = 0
    max_elem = listForSearch[0]

    for i, elem in enumerate(listForSearch):
        if elem > max_elem:
            max_elem = elem
            max_idem = i

    return max_id, max_elem

def main():
    listOfData = [11, 14, 22, 33, 7, 88, 123, 345, 64, 10, 5, 55, 66, 44, 20]
    
    result = findMinElemWithIndex(listOfData)
    print(f"Min id: {result[0]}, Min value: {result[1]}")

    result = findMaxElemWithIndex(listOfData)
    print(f"Max id: {result[0]}, Max value: {result[1]}")

if __name__ == "__main__":
    main()