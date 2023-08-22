'''
  Guess the Number Game

  ---------------------
  入力した範囲内で出題される、
  ランダムな数字を当てるゲーム
  ---------------------

  Usage:
  1. 最小値と、最大値を入力する
  2. プログラムが最小値と最大値の範囲でランダムな数値を生成。
  3. ユーザーはプログラムが生成した数値が何かを当てる

'''

import random

def minAndMaxValueInput():
  '''
  プレイヤーに最小値を最大値を入力してもらう関数
  '''
  minValue = input("最小値を入力してください : ")
  while not minValue.isdigit() : minValue = playerInput()
  maxValue = input("最大値を入力してください : ")
  while not maxValue.isdigit() : maxValue = playerInput() 
  return int(minValue), int(maxValue)

def playerInitializeInput():
  '''
  最大値、最小値が適正な範囲かを判定する
  '''
  n, m = minAndMaxValueInput()
  while not n <= m: 
    print("最大値は最小値以上の値にして下さい。")
    n, m = minAndMaxValueInput()
  return n, m

def generateAnswer(n, m) :
  '''
  答えを乱数により生成
  '''
  answer = random.randint(n, m)
  return answer

def gameInitialize() :
  '''
  ゲームの準備として、答えの数字を準備する
  '''
  n, m = playerInitializeInput()
  answer = generateAnswer(n, m)
  return answer


def playerInput():
  '''
  プレイヤーからのインプットを受け付ける
  必ず数字であることを保証
  '''
  inpt = input("数字を入力してください : ")
  while not inpt.isdigit():
    inpt = input("数字を入力してください : ")
  return int(inpt)


def gameLoop(answer) :
  '''
  ゲームのメインループ
  '''
  print()
  print("さあ、答えの数字を当てて見て下さい。")
  print()

  # ユーザーの入力を判定する
  while True:
    if playerInput() == answer:
      print("正解!")
      return
    print("残念！ハズレ！")

def gameShutdown() :
  '''
  ゲームの終了処理
  '''
  print("Game Over!")

if __name__ == '__main__' :
	answer = gameInitialize()
	gameLoop(answer)
	gameShutdown()




