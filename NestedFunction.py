def deviationCal(a,b,c):
    def avgCalculator(a,b,c):
        avg=float((a+b+c)/3)
        print(f'this is the average calculator funcntion. {avg}')
        return avg
    avg=avgCalculator(a,b,c)
    print(f'the deviation of {a} from avg is :{a-avg}')
    print(f'the deviation of {b} from avg is :{b-avg}')
    print(f'the deviation of {c} from avg is :{c-avg}')

a=12.4
b=46.9
c=29.50
deviationCal(a,b,c)