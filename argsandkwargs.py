def printargs(*args,**kwargs):
    print(f'these are the arguments that are passed and are interpreted as tuple:{args}')
    print(f'these are the keyword arguments that are passed and are interpreted as dictionary:{kwargs}')

printargs(23,24,78,56,234,123.90,namre="Vivek",classr="24MCC101-A")