def main(list1):
    """A list of several elements is given. Return all items from the beginning in three steps.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    a=list1[::3]
    return a
print(main([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))