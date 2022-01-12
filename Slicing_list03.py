def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    a=list1
    b=list1[::-1]
    return a+b
print(main([1,2,3,4,5,6,7,8,9]))