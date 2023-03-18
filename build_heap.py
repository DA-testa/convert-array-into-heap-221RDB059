# python3
from math import log2, ceil, floor


def swap(data, node_one_index, node_two_index):
    temp = data[node_one_index]
    data[node_one_index] = data[node_two_index]
    data[node_two_index] = temp

    return data


# This is the way I came up with to find the last non-leaf node
def find_last_nonleaf_node(n):
    full_row_amount = floor(log2(n+1))
    last_row_node_amount = n - (2**full_row_amount - 1)
    used_parent_nodes = ceil(last_row_node_amount / 2)
    last_full_row_node_index = 2**(full_row_amount-1)-2
    index = last_full_row_node_index + used_parent_nodes

    return index


def heapify(parent_index: int, data: list, swaps: list):
    children_one_index = parent_index*2 + 1

    # Check if a children node exist
    if children_one_index >= len(data):
        # If children nodes do not exist, then return
        return data

    children_two_index = parent_index*2 + 2
    smaller_child_index = children_one_index

    if children_two_index < len(data):
        # If both children nodes exist, choose the smaller one
        if data[children_two_index] < data[children_one_index]:
            smaller_child_index = children_two_index

    if data[smaller_child_index] < data[parent_index]:
        swap(data, parent_index, smaller_child_index)
        swaps.append([parent_index, smaller_child_index])

        # Follows the parent node lower
        heapify(smaller_child_index, data, swaps)

    return data


def build_heap(data, n):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    last_nonleaf_node_index = find_last_nonleaf_node(n)
    for i in range(last_nonleaf_node_index, -1, -1):
        heapify(i, data, swaps)

    return swaps


def main():

    # TODO : add input and corresponding checks
    # add another input for I or F
    # first two tests are from keyboard, third test is from a file
    test_type = input("Choose a test type (I or F): ").lower()

    if test_type.find("i") != -1:
        # input from keyboard
        n = int(input("Node amount: "))
        data = list(map(int, input("Nodes: ").split()))
    elif test_type.find("f") != -1:
        filename = input("Enter file name: ")
        with open(filename, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    else:
        raise Exception("Unknown command")

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data
    # and give back all swaps
    swaps = build_heap(data, n)

    # TODO: output how many swaps were made,
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
