from js import document as doc

# Make the "Initializing Python" status disappear
doc.getElementById("status").innerHTML = ""

canvas = doc.getElementById("draw-here")

canvas.setAttribute("width", doc.body.clientWidth)
canvas.setAttribute("height", 300)
ctx = canvas.getContext("2d")
ctx.strokeStyle = "#F4908E"
ctx.lineJoin = "round"
ctx.lineWidth = 5

# Global variables
pen = False
lastPoint = (0, 0)


def onmousemove(e):
    global lastPoint

    if pen:
        newPoint = (e.offsetX, e.offsetY)
        ctx.beginPath()
        ctx.moveTo(lastPoint[0], lastPoint[1])
        ctx.lineTo(newPoint[0], newPoint[1])
        ctx.closePath()
        ctx.stroke()
        lastPoint = newPoint


def onmousedown(e):
    global pen, lastPoint
    pen = True
    lastPoint = (e.offsetX, e.offsetY)


def onmouseup(e):
    global pen
    pen = False


canvas.addEventListener("mousemove", onmousemove)
canvas.addEventListener("mousedown", onmousedown)
canvas.addEventListener("mouseup", onmouseup)

# Colors

div = doc.getElementById("colors")
colors = ["#F4908E", "#F2F097", "#88B0DC", "#F7B5D1", "#53C4AF", "#FDE38C"]

for c in colors:
    node = doc.createElement("div")
    node.setAttribute("class", "color")
    node.setAttribute("id", c)
    node.setAttribute("style", f"background-color: {c}")

    def setColor(e):
        ctx.strokeStyle = e.target.id

    node.addEventListener("click", setColor)
    div.appendChild(node)
