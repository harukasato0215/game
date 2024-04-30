#ウィンドウ作成用のモジュールを読み込み
import tkinter
 
#ウィンドウ生成
root = tkinter.Tk()
 
#サイズ
WIDTH = 480
HEIGHT = 320
 
#円を含む四角の一辺
circleWidth = 20
 
#座標保存用変数
PointOneX = 135
PointOneY = 155
PointTwoX = PointOneX + circleWidth
PointTwoY = PointOneY + circleWidth
 
#移動差分
dx = -10
dy = -10
 
#ウィンドウのタイトルを設定
root.title("サンプルゲーム")
root.minsize(WIDTH, HEIGHT)
 
#キャンバスの作成
canvas = tkinter.Canvas(bg="white", width=WIDTH, height=HEIGHT)
canvas.place(x=-3, y=-3)
 
 
#ボール描写を関数化
def drawBall():
    global PointTwoX, PointTwoY
    PointTwoX = PointOneX + circleWidth
    PointTwoY = PointOneY + circleWidth
    canvas.create_oval(
        PointOneX, PointOneY, PointTwoX, PointTwoY, fill="#4286f4", outline="")
 
 
#繰り返し処理の定義
def game_loop():
 
    #グローバル変数を利用することを明記
    global PointOneX, PointOneY
    global dx, dy
 
    #中点を求める
    centerX = PointOneX + (circleWidth / 2)
    centerY = PointOneY + (circleWidth / 2)
 
    #右にボールが抜けそうな場合反射させる
    print(PointTwoX)
    if PointTwoX > WIDTH:
        dx = -dx
 
    #左にボールが抜けそうな場合反射させる
    #if centerX + dx < 0:
    if PointOneX < 0:
        dx = -dx
 
    #下にボールが抜けそうな場合反射させる
    if PointTwoY > HEIGHT:
 
        dy = -dy
 
    #上にボールが抜けそうな場合反射させる
    if PointOneY < 0:
        dy = -dy
 
    PointOneX = PointOneX + dx
    PointOneY = PointOneY + dy
 
    #canvasを全て消す
    canvas.delete("all")
    #canvasの内容を再描写
    drawBall()
 
    root.after(50, game_loop)
 
 
game_loop()
 
#ウィンドウの表示とメインループ
root.mainloop()
