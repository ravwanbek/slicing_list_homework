def main(list1,n):
    """
    A list of several elements is given. Return all items from end n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    a=list1[::-n]
    return a
print(main([1,2,3,4,5,6,7,8,9,5,6,8,5,6,8,8],2))