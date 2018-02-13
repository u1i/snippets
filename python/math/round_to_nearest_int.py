def myround(x, base=50):
    return int(base * round(float(x)/base))
    
print myround([221,29,187])
