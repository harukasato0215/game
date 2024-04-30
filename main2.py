import tkinter,math,random
from tkinter import Canvas, PhotoImage


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

#半径
radius = math.sqrt( 2*((circleWidth/2)**2))

#スコア
score = 0

#パドル
paddle_height=10
paddle_width=75
paddleY = height_size - paddle_height
paddleX = (width_size - paddle_width) / 2

#パドル操作
rightPress = False #右
leftPress = False #左
paddleSpeed = 10

#ブロック
blockstartX = 20
blockstrtY = 30
blockRowCount = 10
blockColumnCount = 15
blockWidh = 45
blockHeight = 10
blockPadding = 10
blockOffsetTop = 10
blockOffsetLeft = 5
arrBlock = []

#リスト作成
for r in range(blockRowCount):
    tmpBlock = []
    for c in range(blockColumnCount):
        tmpBlock.append({"x1": 0, "y1": 0, "x2": 0, "y2": 0,"status":1})
    arrBlock.append(tmpBlock)

#キャンバスの作成
root.minsize(width_size,height_size)
canvas = tkinter.Canvas(bg="pink", width=width_size, height=height_size)
canvas.place(x=-3, y=-3)

#スコア
def scorenum():
    textScore =tkinter.Label(text="score:"+ str(score))
    textScore.place(x=0,y=0)
#GAMEオーバーの時のイメージ(dekitara)
gameover_image = PhotoImage(file="2311654.png")

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

#ブロック
def drawBlock():
       for r in range(blockRowCount):
        for c in range(blockColumnCount):
            leftXposition = blockstartX + (c * blockWidh) + (
                c * blockOffsetLeft)
            leftYposition = blockstrtY + (r * blockHeight) + (
                r * blockOffsetTop)
            rightXposition = leftXposition + blockWidh
            rightYposition = leftYposition + blockHeight
            arrBlock[r][c]["x1"] = leftXposition
            arrBlock[r][c]["y1"] = leftYposition
            arrBlock[r][c]["x2"] = rightXposition
            arrBlock[r][c]["y2"] = rightYposition

            if arrBlock[r][c]["status"] == 1:
                canvas.create_rectangle(
                    leftXposition,
                    leftYposition,
                    rightXposition,
                    rightYposition,
                    fill='#4286f4',
                    outline="")
                
            #CLEARしたとき
            # count_0 =arrBlock.count(0)
            # if count_0 > 0:
            #      canvas.delete("all")
            #       # Canvas上に画像を描画する
            #     canvas.create_text(width_size/2,height_size/2,font=("",25), fill="black",text="ゲームクリア")
            #      return


#ブロックと当たったとき
def detection(x,y):
    global dx,dy,score
    for r in range(blockRowCount):
        for c in range(blockColumnCount):
            b = arrBlock[r][c]
            if ((x + radius + dx > b["x1"] and x - radius -dx < b["x2"]) \
            and (y + radius + dy < b["y1"] or y - radius + dy < b["y2"]) \
            and b["status"]==1
            ):
                print("ブロックにあたった")
                dy = -dy
                b["status"] = 0
                score = score + 10

def game_loop():
    global pointx , pointy
    global point2x , point2y
    global dx, dy
    global paddleX
    global score
    
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
    if centerX + radius + dx > width_size:
        dx = -dx

    # 左反射
    if centerX + dx < radius:
        dx = -dx
    
    # 上反射
    if centerY  + dy < radius:
       dy = -dy

    # 下反射
    if centerY + radius + dy > height_size:
 
        #ボールの移動先がパドルの場合は跳ね返す
        if centerX + dx > paddleX and centerX + dx < paddleX + paddle_width:
            dy = -dy
        #ボールの移動先にパドルがない場合はゲームオーバー
        else:
            result = "score:"+ str(score)
            canvas.delete("all")
            # Canvas上に画像を描画する
            canvas.create_text(width_size/2,height_size/2,font=("",25), fill="black",text="ゲームオーバー")
            canvas.create_text(width_size/2,300,font=("",10), fill="black",text=result)
            return
    

           

    pointx= pointx+dx
    pointy= pointy+dy
    canvas.delete("all")
    ball()
    paddle()
    drawBlock()
    scorenum()
    detection(centerX, centerY)
    root.after(50,game_loop)


game_loop()
root.mainloop()
