def rebase(input_base, digits, output_base):

    if input_base < 2 or output_base < 2:
        raise ValueError("Bases must be at least 2")
    
    if not all(0 <= i < input_base for i in digits):
        raise ValueError("Invalid digit")
    
    decimal = sum( input_base**index*binary for index,binary in enumerate(digits[::-1]))
    if decimal==0:
        return [0]

    result = []
    while decimal>0:
        decimal,digit = divmod(decimal,output_base)
        result.append(digit)    
    
    return  result[::-1]