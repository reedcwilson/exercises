def slices(series, length):
    if not length or length > len(series):
        raise ValueError("invalid length: {}".format(length))
    return [list(map(int, list(series[i:i+length])))
            for i in range(len(series) - length + 1)]
