class Game():

    p = []

    def __init__(this):
        this.p = [ [' ']*3 for i in range(0, 3)]


    def draw(this):
        '''
        Функиция отображения поля
        p: list<list<str>>
        '''
        for i in this.p:
            print(f'|{i[0]}|{i[1]}|{i[2]}|')


    def step(this, k, isZero):
        '''
        Функция хода игрока
        k: typle(x, y)
        isZero: bool. If true, zero
        return: bool
        '''
        try:
            y, x = k
            if this.p[x][y] not in {'X', '0'}:
                if isZero:
                    this.p[x][y] = '0'
                else:
                    this.p[x][y] = 'X'
                return True
            else:
                return False
        except:
            return False


    def chekWin(this):

        p = this.p
        # Проверка диагоналей
        if p[0][0] == p[1][1] == p[2][2]:
            return p[0][0]
        elif p[0][2] == p[1][1] == p[2][0]:
            return p[0][2]
        # Конец проверки диагонаей

        else:
            # Проверка горизонтальных линий
            for y in p:
                if len(set(y)) == 1 and y[0] in {'X', '0'}:
                    return y[0]
            # Проверка вертикальных линий
            for x in range(len(p)):
                if p[0][x] == p[1][x] == p[2][x] and p[0][x] in {'X', '0'}:
                    return p[0][x]

        # Проверка на возможность победы
        canWin = False
        for y in p:
            if ' ' in y:
                canWin = True
                break
        if canWin:
            return ' '
        else:
            return 'никто'