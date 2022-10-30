from game import Game
from ai import AI

def main():
    game = Game()
    ai = AI(game, 'X')
    win = False
    zStep = True
    game.draw()
    while not win:

        # Ход игрока
        if zStep:
            print('\n\nХодит игрок: ', end='')
            x, y = [int(i) - 1 for i in input().split(' ')]
            ok = game.step((x, y), zStep)
            if ok:
                zStep = False
                game.draw()
            else:
                print('\n\nТы не можешь так сходить')
        else:
            print('\n\nХодит компьютер: ')
            x, y = ai.analis(ai.generationVariant())
            ok = game.step((x, y), zStep)
            if ok:
                zStep = True
                game.draw()
            else:
                print('\n\nТы не можешь так сходить')
        # Проверка победы
        whoWin = game.chekWin()
        if whoWin in {'X', '0', 'никто'}:
            print(f'Победил {whoWin}')
            win = True



if __name__ == '__main__':
    main()
