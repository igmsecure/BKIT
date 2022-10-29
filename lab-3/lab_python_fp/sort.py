def sort(arr):
    return sorted(arr, reverse=True, key = abs)

def sort_lambda(arr):
    return sorted(arr, reverse=True, key=lambda x: abs(x))