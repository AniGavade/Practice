# num1 = [1, 2, 3, 4]
# num2 = [4, 3, 2, 1]
# result = map(lambda x,y : x*y, num1, num2)
# print(list(result)) 

# x1 = [1, 2, 3, 4, 5]
# y1 = [5, 4, 3, 2, 1]
# result = map(lambda x, y : x+y, x1, y1)
# print(list(result))

# result2 = map(lambda x, y : x*y, x1, y1)
# print(list(result2))

# result2 = map(lambda x, y : x/y, x1, y1)
# print(list(result2))

# result = lambda x, y : x+y
# print(result(2, 4))

# result2 = lambda x, y : x-y
# print(result2(2, 4))
#================================================================================

# def fun(variable):
    # letters = ['a', 'e', 'i', 'o', 'u']
#     if (variable in letters):
#         return True
#     else:
# #         return False
  
  
# # sequence
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
# letters = ['a', 'e', 'i', 'o', 'u']

# # using filter function
# # filtered = filter(fun, sequence)
# filtered= map(lambda a : True if a in letters else False, sequence)
  
# print('The filtered letters are:')
# for s in filtered:
#     print(s)

# game.py
# import the draw module
import draw

def play_game():
    ...

def main():
    result = play_game()
    draw.draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()