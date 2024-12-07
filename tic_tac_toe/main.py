from guizero import App, Box, PushButton, Text

app = App("Tic Tac Toe")


def reset():
    startButton.show()
    resetButton.hide()
    

def start():
    startButton.hide()
    resetButton.show()
    



text = Text(app, text="Tic Tac Toe" , align="top")

startButton = PushButton(app, text="Start", command=start)
resetButton = PushButton(app, text="Reset", command=reset)
resetButton.hide()
boxes = []

box = Box(app, layout="grid", grid=[1, 0], width="100", height="100")

for i in range(3):
    for j in range(3):
        boxes.append(PushButton(box, text=" ", grid=[j, i], width="10", height="5"))








app.display()