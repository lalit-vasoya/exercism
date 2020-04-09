def slices(series, length):

    if len(series)==0 or length <= 0 or len(series)<length:
        raise ValueError('Not valid..!')

    length_str = len(series)+1
    return [series[i:i+length] for i in range(length_str-length)]
