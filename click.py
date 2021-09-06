import pyautogui
import appJar

def buttonPress(button):
    if (button == "Start"):
        amount = int(app.getEntry("amount"))
        button = app.radioButton("click")
        if (button == "Right Click"):
            button = "right"
        else:
            button = "left"
        for _ in range(amount):
            pyautogui.click(button=button)


app = appJar.gui("Pax Clicker")
app.icon = 'pmz.ico'
app.setSize("300x250")
app.setSticky("new")
app.setFont(size=16, family="Arial", underline=False, weight="bold")
app.setButtonFont(size=16, family="Arial", underline=False, weight="bold")
app.addLabel("         Pax Clicker\n\nEnter Amount of Clicks", row=0)
app.addEntry("amount", row=1)
app.addButton("Start", buttonPress, row=3)
app.setButtonBg("Start", "grey")
app.setSticky("e")
app.radioButton("click", "Right Click", row=2)
app.setSticky("w")
app.addLabel("by pax", row=5)
app.setLabelFont("bold")
app.radioButton("click", "Left Click", row=2)
app.setTransparency(percentage=0.85)
app.go()
