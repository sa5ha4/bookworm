import tkinter
import sqlite3

rows = 25
cols = 25
tile_size = 25

window_wigth = tile_size * cols
window_height = tile_size * rows

class Tile:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

window = tkinter.Tk()
window.title("bookworm")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg= "grey", width= window_wigth, height= window_height)
canvas.pack()
window.update()

worm = Tile(2*tile_size, 10*tile_size)
box1 = Tile(7*tile_size, 5*tile_size)
box2 = Tile(7*tile_size, 7*tile_size)
box3 = Tile(7*tile_size, 9*tile_size)
box4 = Tile(7*tile_size, 11*tile_size)
box5 = Tile(7*tile_size, 13*tile_size)
box6 = Tile(7*tile_size, 15*tile_size)
box7 = Tile(7*tile_size, 17*tile_size)
velocityX = 0
velocityY = 0

#db funkcijas

def savienot():
    conn = sqlite3.connect('biblioteka.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gramatas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nosaukums TEXT,
            autors TEXT,
            gads INTEGER
        )
    ''')
    conn.commit()
    return conn, cursor

def pievienot(cursor, conn, nosaukums, autors, gads):
    cursor.execute('INSERT INTO gramatas (nosaukums, autors, gads) VALUES (?, ?, ?)',
                    (nosaukums, autors, gads))
    conn.commit()
    canvas.create_text(window_wigth/2, window_height/4, f"{nosaukums} pievienots!")

#tk funkcijas

def change_direction(e): 

    global velocityX, velocityY
    
    if (e.keysym == "Up" and velocityY != 1):
        velocityX = 0
        velocityY = -1
    elif (e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1
    elif (e.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0
    elif (e.keysym == "Right" and velocityX != -1):
        velocityX = 1
        velocityY = 0

def move():
    global worm, box1, box2
    
    if (worm.x < 0 or worm.x >= window_wigth or worm.y < 0 or worm.y >= window_height):
        return

    if (worm.x == box1.x and worm.y == box1.y):
        canvas.delete("all")
        canvas.create_text(window_wigth/2, window_height/3, font= ("ComicNeue", 20), text= 'Nosaukums: ')
        global entry1, entry2, entry3
        entry1 = tkinter.Entry(window, font= ("ComicNeue", 18))
        canvas.create_window(window_wigth/2, window_height/3+20, window= entry1)

        canvas.create_text(window_wigth/2, window_height/3*2, font= ("ComicNeue", 20), text= 'Autors: ')
        entry2 = tkinter.Entry(window, font= ("ComicNeue", 18))
        canvas.create_window(window_wigth/2, window_height/3+40, window= entry2)
                
        canvas.create_text(window_wigth/2, window_height/3*2.5, font= ("ComicNeue", 20), text= 'Gads: ')
        entry3 = tkinter.Entry(window, font= ("ComicNeue", 18))
        canvas.create_window(window_wigth/2, window_height/3+40, window= entry3)
        
        ok_button = tkinter.Button(window, text="OK", command=pievienot)
        canvas.create_window(window_wigth/4, window_height/3, window=ok_button)

    worm.x += velocityX*tile_size
    worm.y += velocityY*tile_size

def draw():
    global worm, box1, box2, box3, box4, box5, box6, box7
    move()

    canvas.delete("all")

    canvas.create_rectangle(box1.x, box1.y, box1.x + tile_size, box1.y + tile_size, fill = "#b659a3")
    canvas.create_text(14*tile_size, 5.5*tile_size, font= ("ComicNeue", 20), text= "1. Pievienot gramātu", fill= "#fff8f0")

    canvas.create_rectangle(box2.x, box2.y, box2.x + tile_size, box2.y + tile_size, fill = "#c77a31")
    canvas.create_text(13*tile_size, 7.5*tile_size, font= ("ComicNeue", 20), text= "2. Apskatīt visus", fill= "#fff8f0")

    canvas.create_rectangle(box3.x, box3.y, box3.x + tile_size, box3.y + tile_size, fill = "#dee044")
    canvas.create_text(11*tile_size, 9.5*tile_size, font= ("ComicNeue", 20), text= "3. Dzest", fill= "#fff8f0")

    canvas.create_rectangle(box4.x, box4.y, box4.x + tile_size, box4.y + tile_size, fill = "#2f9340")
    canvas.create_text(11*tile_size, 11.5*tile_size, font= ("ComicNeue", 20), text= "4. Atrast", fill= "#fff8f0")

    canvas.create_rectangle(box5.x, box5.y, box5.x + tile_size, box5.y + tile_size, fill = "#48bac2")
    canvas.create_text(14*tile_size, 13.5*tile_size, font= ("ComicNeue", 20), text= "5. Izkārtots saraksts", fill= "#fff8f0")

    canvas.create_rectangle(box6.x, box6.y, box6.x + tile_size, box6.y + tile_size, fill = "#274fa4")
    canvas.create_text(15.3*tile_size, 15.5*tile_size, font= ("ComicNeue", 20), text= "6. Izdotas pēc 2000. gada", fill= "#fff8f0")

    canvas.create_rectangle(box7.x, box7.y, box7.x + tile_size, box7.y + tile_size, fill = "#614bab")
    canvas.create_text(10.5*tile_size, 17.5*tile_size, font= ("ComicNeue", 20), text= "7. Iziet", fill= "#fff8f0")

    canvas.create_rectangle(worm.x, worm.y, worm.x + tile_size, worm.y + tile_size, fill= "#393939")

    window.after(160, draw)
draw()

window.bind("<KeyRelease>", change_direction)

window.mainloop()
