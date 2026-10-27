import turtle
import math
import time

# -----------------------------
# SCREEN SETUP
# -----------------------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("For Palak ❤️")
screen.setup(width=900, height=700)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

# -----------------------------
# HELPER FUNCTION
# -----------------------------
def write_text(text, y, size, color="#ffb6c1"):
    t.goto(0, y)
    t.color(color)
    t.write(
        text,
        align="center",
        font=("Arial", size, "bold")
    )


# -----------------------------
# INTRO
# -----------------------------
write_text("Hey Palak... ❤️", 80, 28)

time.sleep(2)

write_text("I made something for you :)", 25, 18, "white")

time.sleep(3)

# Clear intro
t.clear()

# -----------------------------
# LITTLE COUNTDOWN
# -----------------------------
for text in ["Ready? 👀", "3", "2", "1", "❤️"]:
    t.clear()

    write_text(text, 0, 30)

    time.sleep(0.7)

t.clear()

# -----------------------------
# DRAW HEART
# -----------------------------
colors = [
    "#ffb6c1",
    "#ff85a2",
    "#ff69b4",
    "#ff4d88"
]

# Using multiple layers creates
# the text-filled heart effect
for scale in range(11, 17):

    for i in range(120):

        angle = i * (math.pi * 2) / 120

        x = 16 * (math.sin(angle) ** 3) * scale

        y = (
            13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle)
        ) * scale

        # Move heart slightly upward
        y += 40

        t.goto(x, y)

        t.color(colors[i % len(colors)])

        t.write(
            "I LOVE YOU!",
            align="center",
            font=("Arial", 7, "bold")
        )

# -----------------------------
# FINAL MESSAGE
# -----------------------------
time.sleep(1)

write_text(
    "I LOVE YOU PALAK! ❤️",
    -220,
    25,
    "white"
)

time.sleep(1)

write_text(
    "You are my favourite person <3",
    -260,
    15,
    "#ffb6c1"
)

# -----------------------------
# SMALL FINAL SURPRISE
# -----------------------------
time.sleep(2)

write_text(
    "Always. ❤️",
    -300,
    11,
    "#ff69b4"
)

turtle.done()