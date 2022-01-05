def fibonnacci_sequence (num):
    if num == 0 or num == 1:
        result = 1
        return result

    result = fibonnacci_sequence(num - 1) + fibonnacci_sequence(num - 2)

    return result 

print(fibonnacci_sequence(10))