import txtopp as tp

def main():
    rawl = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Physics Equator/files/raw_formula.txt'
    forml = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Physics Equator/files/formula_database.txt'

    raw_formula = tp.read_list(rawl, '\n')
    tp.add_list(file=forml, separator='\n', list=raw_formula)



    def DivCon(eq):
        x = eq.index('/')
        print(x)
        print(eq)
        if len(eq) == x+2:
            print(eq)
            var = eq[x+1]
            eq.remove(var)
            eq.remove('/')
            print(eq)
            y = eq.index('=')
            if y-1 == 0:
                eq.insert(0, '(')
                eq.insert(2, ')*'+var)
                equation = ''
                for item in eq:
                    equation = equation+item
                tp.add_object(forml, '\n', equation)
                
                
    def MultCon(eq):
        x = eq.index('*')
        print(x)
        print(eq)
        if len(eq) == x+2:
            print(eq)
            var = eq[x+1]
            eq.remove(var)
            eq.remove('*')
            print(eq)
            y = eq.index('=')
            if y-1 == 0:
                eq.insert(0, '(')
                eq.insert(2, ')/'+var)
                equation = ''
                for item in eq:
                    equation = equation+item
                tp.add_object(forml, '\n', equation)




    for item in raw_formula:
        item = [x for x in item]
        if '/' in item:
            DivCon(item)
        if '*' in item:
            MultCon(item)


    all_form = tp.read_list(forml, '\n')
    clean_form = []

    for item in all_form:
        if item in clean_form: pass
        else: clean_form.append(item)
        
    tp.delete_list(forml, '\n', all_form)
    tp.add_list(forml, '\n', clean_form)