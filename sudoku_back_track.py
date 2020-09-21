'''
>>> y axis represents row no.
>>> x axis represents col no.
>>> rs represents total no. of rows in a cell
>>> cs represents total no. of columns in a cell
>>>cell represents the matrix with smallest value of (rows+cols) consisting all the no.s (i.e. 3x3 in a 9x9 matrix)
'''

dict_an, alpha_numeric,cell_rows,cell_columns,none = {str(i):chr(i+55) for i in range(10,36)}, True, 3, 3, 0
inv_dict_an = {chr(i+55):str(i) for i in range(10,36)}


def inter(n):
    return inv_dict_an.get(n,n)

def purify(s):
    while '' in s: s.remove('')
    return s

class Sudoku(list):
    
    def __init__(self,cell_rows,cell_columns,matrix = None):
        self.rs,self.cs = cell_rows,cell_columns
        if matrix == None:
            for i in range(cell_rows*cell_columns):
                self.append(purify(list(map(inter,input().split())))) #needs modification for UI
        else: self.extend(matrix)
            
    def __str__(self):
        cs,rs = self.cs,self.rs
        n0 = cs*rs
        ls = len(str(n0))
        s1 = ('+'+((('-' * (ls+2)+'+')*cs)+'+') * (rs-1)+('-' * (ls+2)+'+') * cs)+'\n'
        s = s1
        for j in range(n0):
            s+='|'
            for i in range(n0):
                n = ' '
                if self[j][i] != '0':
                    n = self[j][i]
                    if alpha_numeric:
                        n = dict_an.get(n,n)
                s+=(' '*(ls-len(n)+1)+n+[' ||',' |'][bool((i+1) % cs or i == n0-1)])
            divider = ['=','-'][bool((j+1)%rs or j == n0-1)]
            s+=('\n+'+(((divider * (ls+2)+'+') * cs)+'+') * (rs-1)+(divider * (ls+2)+'+') * cs+'\n')
        return s

    def possible(self,y,x,n):
        for i in range(self.cs*self.rs):
            if (self[y][i] == n) or (self[i][x] == n): return False
        x0,y0 = x//self.cs*self.cs,y//self.rs*self.rs
        for i in range(x0,x0+self.cs):
            for j in range(y0,y0+self.rs):
                if self[j][i] == n: return False
        return True

    def solve(self,sample = False):
        global i
        for y in range(self.rs*self.cs):
            for x in range(self.rs*self.cs):
                if self[y][x] == '0':
                    for n in range(1,self.rs*self.cs+1):
                        if i != '1': break
                        if self.possible(y,x,str(n)):
                            self[y][x] = str(n)
                            self.solve(sample)
                            self[y][x] = '0'
                    return
        print(self)
        i = '' if sample else input("need more solutions of the same problem?\n(enter 1 if Yes, any other key if no) : ") 




def create_sudoku():
    inp = 0
    while inp!='1':
        sudoku = Sudoku(cell_rows,cell_columns)
        print('\nCheck Your Input:')
        print(sudoku)
        inp = input('verify your input (enter 1 to confirm your input, any other key to re-enter the input) : ')
    return sudoku

    



while True:
    print('\nPlease choose(enter the corresponding no.):\n=========================================\n1) Solve Sudoku    2) set or change values    anything else) quit\n')
    sc = input('\nenter corresponding number >>> ')
    
    if sc == '1':
        print('\nSolve Sudoku:\n============\n')
        while True:
            print('RULES:\n(1) Please place the digits at their right places and replace the unknowns with',none,'\n(2) Fill up one row at a time with space separated inputs')
            print('\n[N.B.: The number of spaces between any two units are not case sensitive, but there sequence is.]\nrow no.s and column no.s are given just to guide while placing the input values, u may or may not follow them :)\n')
            i = '1'
            create_sudoku().solve()
            if i == '1': print("No other solutions possible\n")
            if not input('\nDo you want more?\n(enter 1 if Yes, any other key to go to the main menu) :') == '1': break
            print('\n')
            

    elif sc == '2':
        print('\n\nSet or change values:\n====================')
        while True:
            print("\nWhat do u want to set or change? :\n[You can change multiple of them one after another]\n1) Sudoku type or size [ now >>> '",cell_rows*cell_columns,'x',cell_rows*cell_columns,"' with ('total cell rows','total cell columns') =",(cell_rows,cell_columns),"]\n2) digit types [ now >>>",['only neumeric', 'alpha-neumeric'][alpha_numeric],"]\n3) blank filler [ now >>>",none,"]\nanything else) go back to the main menu\n")
            Inp = input('\nchoose the corresponding number >>> ')
            
            if Inp == '1':
                print('N.B. : cell represents the matrix with total rows > 1 and total columns >1 that consists all the possible numbers (e.g. 3x3 in a 9x9 matrix)')
                cell_rows,cell_columns = int(input('enter total ROWS in a CELL : ')),int(input('enter total COLUMNS in a CELL : '))
                i = input('\nDo you want to see how the choosen sudoku table would look like?\n(enter 1 to see a sample of a solved sudoku, enter 0 to see only the empty table, any other key to save change and go back) : ')
                if i == '0': print(Sudoku(cell_rows,cell_columns,[['0' for i in range(cell_rows*cell_columns)] for j in range(cell_rows*cell_columns)]))
                elif i == '1':Sudoku(cell_rows,cell_columns,[['0' for i in range(cell_rows*cell_columns)] for j in range(cell_rows*cell_columns)]).solve(1)
                    
            elif Inp == '2':
                if input('\nDo you want to change the digit type to'+['alpha-numeric','only numeric'][alpha_numeric]+'/n(enter 1 to confirm, any other key to cancel) : ') == '1': alpha_numeric = not alpha_numeric
                
            elif Inp == '3':
                while True:
                    New = input("\nenter a valid value for the blank filler (by default 0):\n[Case Sensitive: this value must not be a block letter or a number other than 0]\nenter the new value >>> ")
                    if New != ' ' and New not in '123456789' and check2(New):
                        none = New
                        break
                    print('can not assign blank filler to',New,'\n')

            else: break


    else: break