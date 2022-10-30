from itertools import product
from game import Game

class AI():

    game = ''
    whoI = ''
    whoE = ''

    def __init__(this, game, whoI):
        a = ['X', '0']
        this.game = game
        this.whoI = whoI
        a.pop(a.index(whoI))
        this.whoE = a[0]


    def generationVariant(this):
        p = this.game.p
        variants = []

        # Находим местоположение ноликов и крестиков
        index0, indexX = [], []
        res = [i for j in p for i in j]
        while '0' in res:
            index = res.index('0')
            index0.append(index)
            res[index] = '#'

        while 'X' in res:
            index = res.index('X')
            indexX.append(index)
            res[index] = '#'



        for i in product('X0 ', repeat=9):

            isFit = True
            for j in index0:
                if i[j] != '0':
                    isFit = False
                    break
            for j in indexX:
                if i[j] != 'X' and isFit:
                    isFit = False
                    break

            if isFit:
                a = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
                a[0] = list(i)[:3]
                a[1] = list(i)[3:6]
                a[2] = list(i)[6:]
                variants.append(a)
        return variants


    def analis(this, variants):

        # Находим победные варианты
        if len(variants) == 3**9 or this.game.p[1][1] == ' ':
            return(1, 1)
        else:

            # Ищем не закрытые лини соперника

            # Проверка не закрытой диагонали с лева направо
            line = []
            for y in range(len(this.game.p)):
                for x in range(len(this.game.p[y])):
                    if y == x:
                        line.append(this.game.p[y][x])
            if line.count(this.whoE) == 2 and line.count(' ') == 1:
                return line.index(' '), line.index(' ')

            # Проверка не закрытой диагонали с права на лево
            line = []
            for y in range(len(this.game.p)):
                for x in range(len(this.game.p[y])):
                    if y == 2 - x:
                        line.append(this.game.p[y][x])
            if line.count(this.whoE) == 2 and line.count(' ') == 1:
                x = line.index(' ')
                y = 2 - x
                return x, y

            # Проверка не закрытой горизонтальной линии
            for y in range(len(this.game.p)):
                if line.count(this.whoE) == 2 and line.count(' ') == 1:
                    return this.game.p[y].index(' '), y

            # Проверка не закрытой вертикальной линии
            line = []
            for x in range(len(this.game.p)):
                for y in range(len(this.game.p[x])):
                    line.append(this.game.p[y][x])
                if line.count(this.whoE) == 2 and line.count(' ') == 1:
                    return x, line.index(' ')



            # Если не нашли не закрытые линии противника, то выбираем лучший ход для себя
            goodV = []
            for i in variants:
                game = Game()
                game.p = i
                if game.chekWin() == this.whoI:
                    goodV.append(i)

            dictV = {}
            for i in goodV:
                counS = [k for j in i for k in j].count(this.whoI) - [i for j in this.game.p for i in j].count(this.whoI)
                dictV[counS] = i

            minCountS = 1000
            for i in dictV.keys():
                minCountS = min(i, minCountS)

            if minCountS != 1000:
                winV = dictV[minCountS]

                for y in range(len(winV)):
                    for x in range(len(winV[y])):
                        if winV[y][x] == this.whoI and this.game.p[y][x] == ' ':
                            return x, y
            else:
                for y in range(len(this.game.p)):
                    for x in range(len(this.game.p[y])):
                        if this.game.p[y][x] == ' ':
                            return x, y