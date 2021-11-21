import txtopp as tp

def main():
    novar = int(input('Enter no.of known figures: '))
    var = {}
    symbols = []

    for i in range(1, novar+1):
        r = str(i)
        symbol = input('Enter known variable symbol: ')
        symbols.append(symbol)
        var[symbol] = float(input(f'Enter Value of {symbol}: '))
    symbol = input('Enter symbol of unknown figure: ')
    symbols.append(symbol)

    var[symbol] = ''

    fdl = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Physics Equator/files/formula_database.txt'
    odl = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Physics Equator/files/operator_database.txt'
    raw_formulae = tp.read_list(fdl, '\n')
    operators = tp.read_list(odl, ',')

    new_formulae = []

    for item in raw_formulae:
        if symbols[novar] in item:
            new_formulae.append(item)
            
    print(new_formulae)

    new_formula = []

    for item in new_formulae:
        if novar == 1: 
            if symbols[0] in item: new_formula.append(item)
        if novar == 2: 
            if symbols[0] and symbols[1] in item: new_formula.append(item)
        if novar == 3: 
            if symbols[0] and symbols[1] and symbols[2] in item: new_formula.append(item)
        if novar == 4: 
            if symbols[0] and symbols[1] and symbols[2] and symbols[3] in item: new_formula.append(item)
        if novar == 5: 
            if symbols[0] and symbols[1] and symbols[2] and symbols[3] and symbols[4] in item: new_formula.append(item)
            
            
    print(new_formula)


    def equate():
        formulae = []
        for item in new_formula:
            item = [x for x in item]
            if item.index(symbols[novar]) == len(item)-1 or item.index(symbols[novar]) == 0:
                f = ''
                for i in item:
                    f = f+str(i)
                formulae.append(f)
                
                

        formula = formulae[0] 
        formula = formula.strip(symbols[novar])
        formula = formula.strip('=')
        formula = [x for x in formula]
        
        print(formula)
        
        for item in formula:
            if item in symbols:
                i = formula.index(item)
                formula.remove(item)
                formula.insert(i, var[item])
        
        function = ''
        for item in formula:
            function = function+str(item)
        print(eval(function))


    equate()