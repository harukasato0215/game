import tkinter 


#ウィンドウの作成
root =  tkinter.Tk()

# ウィンドウタイトル
root.title("ブロック崩し")

# 関数
# 画面のサイズ
width_size=800
height_size=500

# 円を含む四角の一辺
circleWidth = 20

# 座標
pointx=235
pointy=155
point2x =pointx+circleWidth/2
point2y =pointy+circleWidth/2

# 移動
dx=5
dy=5

#パドル
paddle_height=10
paddle_width=75
paddleY = height_size - paddle_height
paddleX = (width_size - paddle_width) / 2

#パドル操作
rightPress = False #右
leftPress = False #左
paddleSpeed = 10

#キャンバスの作成
root.minsize(width_size,height_size)
canvas = tkinter.Canvas(bg="pink", width=width_size, height=height_size)
canvas.place(x=-3, y=-3)

#ball
def ball():
    global point2x ,point2y
    point2x =pointx+circleWidth/2
    point2y =pointy+circleWidth/2
    canvas.create_oval(
        pointx,pointy,point2x,point2y,fill="#4286f4", outline="")
    
#パドル
def paddle():
    paddle1x=paddleX + paddle_width
    paddle1y=paddleY + paddle_height
    canvas.create_rectangle(
        paddleX, paddleY,paddle1x,paddle1y,fill='#4286f4',outline=""
    )

#パドルボタン操作

#右キー（押したとき）
def rightKey(event):
    global rightPress
    rightPress=True

#右キー（離したとき）
def rightKeyRelease(event):
    global rightPress
    rightPress= False

#左キー（押したとき）
def leftKey(event):
    global leftPress
    leftPress=True
    # print("左が押されました")

#左キー（離したとき）
def leftKeyRelease(event):
    global leftPress
    leftPress= False
    # print("左が離されました")

#a,dでも動くように追加
root.bind("<Right>",rightKey)
root.bind("<d>",rightKey)
root.bind("<KeyRelease-Right>",rightKeyRelease)
root.bind("<KeyRelease-d>",rightKeyRelease)
root.bind("<Left>",leftKey)
root.bind("<a>",leftKey)
root.bind("<KeyRelease-Left>",leftKeyRelease)
root.bind("<KeyRelease-a>",leftKeyRelease)


def game_loop():
    global pointx , pointy
    global point2x , point2y
    global dx, dy
    global paddleX
    
    #パドルの動き制御
    if rightPress:
     if paddleX+paddle_width+paddleSpeed < width_size:
        paddleX = paddleX + paddleSpeed
              
    if leftPress:
     if paddleX - paddleSpeed > 0:
        paddleX = paddleX - paddleSpeed



    centerX =pointx+(circleWidth/2)
    centerY =pointy+(circleWidth/2)

    # 右反射
    if point2x > width_size:
        dx=-dx
    # 左反射
    if pointx<0:
        dx=-dx
    # 上反射
    if point2y>height_size:
        dy=-dy
    # 下反射
    if pointy<0:
        #パドルの上に乗ったとき
        if centerX + dx >paddleX and centerX + dx < paddleX :
           dy=-dy
         #そのまま下に行ってしまったとき
        else:
           canvas.delete("all")
           
           

    pointx= pointx+dx
    pointy= pointy+dy
    canvas.delete("all")
    ball()
    paddle()
    root.after(50,game_loop)


game_loop()
root.mainloop()
