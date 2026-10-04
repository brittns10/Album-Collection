
from flask import Flask, render_template, request
import sqlite3
import random
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/artists")
def artists():
    connection = sqlite3.connect("album_review.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    print("DATABASE:", os.path.abspath("album_review.db"))
    cursor.execute("SELECT name FROM artist")
    artist_list = cursor.fetchall()


    
    return render_template("artists.html", artists_name=artist_list)

@app.route("/register", methods=["get", "post"])
def register():
    connection = sqlite3.connect("album_review.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    if request.method == "POST":
        username = request.form["username"]
        pass_word = request.form["password"]
        email_add = request.form["email"]
        us_id = True
        while us_id:
            new_id = random.randint(1,100)
            cursor.execute("SELECT id FROM users WHERE id =?", (new_id,))
            in_id = cursor.fetchone()
            if in_id is None:        
                cursor.execute("INSERT or IGNORE into users (id, username, email, password) VALUES (?,?,?,?)",(new_id, username, email_add, pass_word))
                connection.commit()
                us_id = False
    return render_template("register.html")

@app.route("/albums")
def albums():
    connection = sqlite3.connect("album_review.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * from album")
    album_list = cursor.fetchall()
    return render_template("albums.html", album_list=album_list)

@app.route("/album/<int:id>")
def artist_page(id):
    connection = sqlite3.connect("album_review.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * from album WHERE id =?",(id,))
    album = cursor.fetchone()
    return render_template("album.html", album_list=album)

#@app.route("/artist/<int:artist_id>")
#def artist_page(artist_id):
  #  cursor.execute(
    #    "SELECT * FROM artist WHERE id = ?",
   #     (artist_id,)
  #  )
   # artist = cursor.fetchone()

    #return render_template("artist.html", artist=artist)

connection = sqlite3.connect("album_review.db")
cursor = connection.cursor()
#create table
command_one = """CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT, email TEXT, password TEXT)"""
cursor.execute(command_one)

command_two = """CREATE TABLE IF NOT EXISTS artist(id INTEGER PRIMARY KEY, name TEXT)"""
cursor.execute(command_two)

command_three = """CREATE TABLE IF NOT EXISTS album(id INTEGER PRIMARY KEY, title TEXT, year INTEGER, artist TEXT, FOREIGN KEY(artist) REFERENCES artist(id))"""
cursor.execute(command_three)

command_four = """CREATE TABLE IF NOT EXISTS reviews(id INTEGER, username TEXT, stars INTEGER, comment TEXT, date TEXT, FOREIGN KEY(username) REFERENCES users(id))"""
cursor.execute(command_four)

#adding to tables
#add artist
cursor.execute("INSERT or IGNORE into artist VALUES(1, 'Anita Baker')")
cursor.execute("INSERT or IGNORE into artist VALUES(2, 'Alicia Keys')")
cursor.execute("INSERT or IGNORE into artist VALUES(3, 'Aretha Franklin')")
cursor.execute("INSERT or IGNORE into artist VALUES(4, 'Barry White')")
cursor.execute("INSERT or IGNORE into artist VALUES(5, 'Brandy')")
cursor.execute("INSERT or IGNORE into artist VALUES(6, 'Al Green')")
cursor.execute("INSERT or IGNORE into artist VALUES(7, 'Bobby Brown')")
cursor.execute("INSERT or IGNORE into artist VALUES(8, 'Earth, Wind, and Fire')")
cursor.execute("INSERT or IGNORE into artist VALUES(9, 'DeBarge')")
cursor.execute("INSERT or IGNORE into artist VALUES(10, 'Deniece Williams')")
cursor.execute("INSERT or IGNORE into artist VALUES(11, 'Donny Hathaway')")
cursor.execute("INSERT or IGNORE into artist VALUES(12, 'En Vogue')")
cursor.execute("INSERT or IGNORE into artist VALUES(13, 'Erykah Badu')")
cursor.execute("INSERT or IGNORE into artist VALUES(14, 'Jill Scott')")
cursor.execute("INSERT or IGNORE into artist VALUES(15, 'Jodeci')")
cursor.execute("INSERT or IGNORE into artist VALUES(16, 'Keith Sweat')")
cursor.execute("INSERT or IGNORE into artist VALUES(17, 'Luther Vandross')")
cursor.execute("INSERT or IGNORE into artist VALUES(18, 'Marvin Gaye')")
cursor.execute("INSERT or IGNORE into artist VALUES(19, 'Maze')")
cursor.execute("INSERT or IGNORE into artist VALUES(20, 'Michael Jackson')")
cursor.execute("INSERT or IGNORE into artist VALUES(21, 'Minnie Ripperton')")
cursor.execute("INSERT or IGNORE into artist VALUES(22, 'New Edition')")
cursor.execute("INSERT or IGNORE into artist VALUES(23, 'Ohio Players')")
cursor.execute("INSERT or IGNORE into artist VALUES(24, 'Parliament')")
cursor.execute("INSERT or IGNORE into artist VALUES(25, 'Patti Labelle')")
cursor.execute("INSERT or IGNORE into artist VALUES(26, 'Patrice Rushen')")
cursor.execute("INSERT or IGNORE into artist VALUES(27, 'Peabo Bryson')")
cursor.execute("INSERT or IGNORE into artist VALUES(28, 'Prince')")
cursor.execute("INSERT or IGNORE into artist VALUES(29, 'Rufus')")
cursor.execute("INSERT or IGNORE into artist VALUES(30, 'Stevie Wonder')")
cursor.execute("INSERT or IGNORE into artist VALUES(31, 'Teena Marie')")
cursor.execute("INSERT or IGNORE into artist VALUES(32, 'The Isley Brothers')")
cursor.execute("INSERT or IGNORE into artist VALUES(33, 'The OJays')")
cursor.execute("INSERT or IGNORE into artist VALUES(34, 'Whitney Houston')")
connection.commit()



#add albums
cursor.execute("INSERT or IGNORE into album VALUES(1, 'The Songstress', 1983, 'Anita Baker')")
cursor.execute("INSERT or IGNORE into album VALUES(2, 'Rapture', 1986,'Anita Baker')")
cursor.execute("INSERT or IGNORE into album VALUES(3, 'Giving You the Best That I Got', 1988, 'Anita Baker')")
cursor.execute("INSERT or IGNORE into album VALUES(4, 'Compositions', 1990, 'Anita Baker')")
cursor.execute("INSERT or IGNORE into album VALUES(5, 'Rhythm of Love', 1994, 'Anita Baker')")
cursor.execute("INSERT or IGNORE into album VALUES(6, 'Songs In A Minor', 2001, 'Alicia Keys')")
cursor.execute("INSERT or IGNORE into album VALUES(7, 'The Diary of Alicia Keys', 2003, 'Alicia Keys')")
cursor.execute("INSERT or IGNORE into album VALUES(8, 'As I Am', 2007, 'Alicia Keys')")
cursor.execute("INSERT or IGNORE into album VALUES(9, 'The Element or Freedom', 2009, 'Alicia Keys')")
cursor.execute("INSERT or IGNORE into album VALUES(10, 'I Never Loved a Man the Way I Love You', 1967, 'Aretha Franklin')")
cursor.execute("INSERT or IGNORE into album VALUES(11, 'Lady Soul', 1968, 'Aretha Franklin')")
cursor.execute("INSERT or IGNORE into album VALUES(12, 'Aretha Now', 1968, 'Aretha Franklin')")
cursor.execute("INSERT or IGNORE into album VALUES(13, 'This Girls in Love With You', 1970, 'Aretha Franklin')")
cursor.execute("INSERT or IGNORE into album VALUES(14, 'Young, Gifted and Black', 1972, 'Aretha Franklin')")
cursor.execute("INSERT or IGNORE into album VALUES(15, 'Let Me In Your Life', 1974, 'Aretha Franklin')")
cursor.execute("INSERT or IGNORE into album VALUES(16, 'Head to the Sky', 1973, 'Earth, Wind & Fire')")
cursor.execute("INSERT or IGNORE into album VALUES(17, 'Thats the Way of the World', 1975, 'Earth, Wind & Fire')")
cursor.execute("INSERT or IGNORE into album VALUES(18, 'Spirit', 1976, 'Earth, Wind & Fire')")
cursor.execute("INSERT or IGNORE into album VALUES(19, 'All n All', 1977, 'Earth, Wind & Fire')")
cursor.execute("INSERT or IGNORE into album VALUES(20, 'I Am', 1979, 'Earth, Wind & Fire')")
cursor.execute("INSERT or IGNORE into album VALUES(21, 'Raise', 1981, 'Earth, Wind & Fire')")
cursor.execute("INSERT or IGNORE into album VALUES(22, 'Open Our Eyes', 1974, 'Earth, Wind & Fire')")
cursor.execute("INSERT or IGNORE into album VALUES(23, 'Funky Divas', 1992, 'En Vogue')")
cursor.execute("INSERT or IGNORE into album VALUES(24, 'Baduizm', 1997, 'Erykah Badu')")
cursor.execute("INSERT or IGNORE into album VALUES(25, 'Mamas Gun', 2000, 'Erykah Badu')")
cursor.execute("INSERT or IGNORE into album VALUES(26, 'Who Is Jill Scott?: Words and Sounds, Vol. 1', 2000, 'Jill Scott')")
cursor.execute("INSERT or IGNORE into album VALUES(27, 'Beautifully Human: Words and Sounds, Vol. 2', 2004, 'Jill Scott')")
cursor.execute("INSERT or IGNORE into album VALUES(28, 'The Real Thing: Words and Sounds, Vol. 3', 2007, 'Jill Scott')")
cursor.execute("INSERT or IGNORE into album VALUES(29, 'Forever My Lady', 1991, 'Jodeci')")
cursor.execute("INSERT or IGNORE into album VALUES(30, 'Diary of a Mad Band', 1993, 'Jodeci')")
cursor.execute("INSERT or IGNORE into album VALUES(31, 'The Show, The After Party, The Hotel', 1995, 'Jodeci')")
cursor.execute("INSERT or IGNORE into album VALUES(32, 'Never Too Much', 1981, 'Luther Vandross')")
cursor.execute("INSERT or IGNORE into album VALUES(33, 'Forever, For Always, For Love', 1982, 'Luther Vandross')")
cursor.execute("INSERT or IGNORE into album VALUES(34, 'Busy Body', 1983, 'Luther Vandross')")
cursor.execute("INSERT or IGNORE into album VALUES(35, 'The Night I Fell In Love', 1985, 'Luther Vandross')")
cursor.execute("INSERT or IGNORE into album VALUES(36, 'Give Me The Reason', 1986, 'Luther Vandross')")
cursor.execute("INSERT or IGNORE into album VALUES(37, 'Any Love', 1988, 'Luther Vandross')")
cursor.execute("INSERT or IGNORE into album VALUES(38, 'Whats Going On', 1971, 'Marvin Gaye')")
cursor.execute("INSERT or IGNORE into album VALUES(39, 'Lets Get It On', 1973, 'Marvin Gaye')")
cursor.execute("INSERT or IGNORE into album VALUES(40, 'I Want You', 1976, 'Marvin Gaye')")
cursor.execute("INSERT or IGNORE into album VALUES(41, 'Maze Featuring Frankie Beverly', 1977, 'Maze')")
cursor.execute("INSERT or IGNORE into album VALUES(42, 'Golden Time of Day', 1978, 'Maze')")
cursor.execute("INSERT or IGNORE into album VALUES(43, 'Inspiration', 1979, 'Maze')")
cursor.execute("INSERT or IGNORE into album VALUES(44, 'Joy and Pain', 1980, 'Maze')")
cursor.execute("INSERT or IGNORE into album VALUES(45, 'We Are One', 1983, 'Maze')")
cursor.execute("INSERT or IGNORE into album VALUES(47, 'Off the Wall', 1979, 'Michael Jackson')")
cursor.execute("INSERT or IGNORE into album VALUES(48, 'Thriller', 1982, 'Michael Jackson')")
cursor.execute("INSERT or IGNORE into album VALUES(49, 'Bad', 1987, 'Michael Jackson')")
cursor.execute("INSERT or IGNORE into album VALUES(50, 'Dangerous', 1991, 'Michael Jackson')")
cursor.execute("INSERT or IGNORE into album VALUES(51, 'Invicible', 2001, 'Michael Jackson')")
cursor.execute("INSERT or IGNORE into album VALUES(52, 'Mothership Connection', 1975, 'Parliament')")
cursor.execute("INSERT or IGNORE into album VALUES(53, 'Funkentelechy vs. The Placebo Syndrome', 1977, 'Parliament')")
cursor.execute("INSERT or IGNORE into album VALUES(54, 'Im in Love Again', 1983, 'Patti Labelle')")
cursor.execute("INSERT or IGNORE into album VALUES(55, 'Before the Dawn', 1975, 'Patrice Rushen')")
cursor.execute("INSERT or IGNORE into album VALUES(56, 'Pizzazz', 1979, 'Patrice Rushen')")
cursor.execute("INSERT or IGNORE into album VALUES(57, 'Straight from the Heart', 1982, 'Patrice Rushen')")
cursor.execute("INSERT or IGNORE into album VALUES(58, 'Reaching For The Sky', 1977, 'Peabo Bryson')")
cursor.execute("INSERT or IGNORE into album VALUES(59, 'Crosswinds', 1978, 'Peabo Bryson')")
cursor.execute("INSERT or IGNORE into album VALUES(60, 'For You', 1978, 'Prince')")
cursor.execute("INSERT or IGNORE into album VALUES(61, 'Prince', 1979, 'Prince')")
cursor.execute("INSERT or IGNORE into album VALUES(62, 'Controversy', 1981, 'Prince')")
cursor.execute("INSERT or IGNORE into album VALUES(63, '1999', 1982, 'Prince')")
cursor.execute("INSERT or IGNORE into album VALUES(64, 'Purple Rain', 1984, 'Prince')")
cursor.execute("INSERT or IGNORE into album VALUES(65, 'Around The World In a Day', 1985, 'Prince')")
cursor.execute("INSERT or IGNORE into album VALUES(66, 'Parade', 1986, 'Prince')")
cursor.execute("INSERT or IGNORE into album VALUES(67, 'Sign O The Times', 1987, 'Prince')")
cursor.execute("INSERT or IGNORE into album VALUES(68, 'Diamonds and Pearls', 1991, 'Prince')")
cursor.execute("INSERT or IGNORE into album VALUES(69, 'The Rainbow Children', 2001, 'Prince')")
cursor.execute("INSERT or IGNORE into album VALUES(70, 'Musicology', 2004, 'Prince')")
cursor.execute("INSERT or IGNORE into album VALUES(71, 'Xpectation', 2003, 'Prince')")
cursor.execute("INSERT or IGNORE into album VALUES(72, '3121', 2006, 'Prince')")
cursor.execute("INSERT or IGNORE into album VALUES(73, 'All This Love', 1982, 'DeBarge')")
cursor.execute("INSERT or IGNORE into album VALUES(74, 'In A Special Way', 1983, 'DeBarge')")
cursor.execute("INSERT or IGNORE into album VALUES(75, 'Rhythm of the Night', 1985, 'DeBarge')")
cursor.execute("INSERT or IGNORE into album VALUES(76, 'This is Niecy', 1976, 'Deniece Williams')")
cursor.execute("INSERT or IGNORE into album VALUES(77, 'Donny Hathaway', 1971, 'Donny Hathaway')")
cursor.execute("INSERT or IGNORE into album VALUES(78, 'Extension of a Man', 1973, 'Donny Hathaway')")
cursor.execute("INSERT or IGNORE into album VALUES(79, 'Rags to Rufus', 1974, 'Rufus')")
cursor.execute("INSERT or IGNORE into album VALUES(80, 'Rufus featuring Chaka Khan', 1975, 'Rufus')")
cursor.execute("INSERT or IGNORE into album VALUES(81, 'Ask Rufus', 1977, 'Rufus')")
cursor.execute("INSERT or IGNORE into album VALUES(82, 'Street Player', 1978, 'Rufus')")
cursor.execute("INSERT or IGNORE into album VALUES(83, 'Masterjam', 1979, 'Rufus')")
cursor.execute("INSERT or IGNORE into album VALUES(84, 'Where Im Coming From', 1971, 'Stevie Wonder')")
cursor.execute("INSERT or IGNORE into album VALUES(85, 'Music of My Mind', 1972, 'Stevie Wonder')")
cursor.execute("INSERT or IGNORE into album VALUES(86, 'Talking Book', 1972, 'Stevie Wonder')")
cursor.execute("INSERT or IGNORE into album VALUES(87, 'Innervisions', 1973, 'Stevie Wonder')")
cursor.execute("INSERT or IGNORE into album VALUES(88, 'Fulfillingness First Finale', 1974, 'Stevie Wonder')")
cursor.execute("INSERT or IGNORE into album VALUES(89, 'Songs in the Key of Life', 1976, 'Stevie Wonder')")
cursor.execute("INSERT or IGNORE into album VALUES(90, 'Journey Through the Secret Life of Plants', 1979, 'Stevie Wonder')")
cursor.execute("INSERT or IGNORE into album VALUES(91, 'Hotter Than July', 1980, 'Stevie Wonder')")
cursor.execute("INSERT or IGNORE into album VALUES(92, 'The Woman in Red', 1984, 'Stevie Wonder')")
cursor.execute("INSERT or IGNORE into album VALUES(93, 'In Square Circle', 1985, 'Stevie Wonder')")
cursor.execute("INSERT or IGNORE into album VALUES(94, 'Jungle Fever', 1991, 'Stevie Wonder')")
cursor.execute("INSERT or IGNORE into album VALUES(95, 'Harvest for World', 1976, 'The Isley Brothers')")
cursor.execute("INSERT or IGNORE into album VALUES(96, 'Go For Your Guns', 1977, 'The Isley Brothers')")
cursor.execute("INSERT or IGNORE into album VALUES(97, 'Showdown', 1978, 'The Isley Brothers')")
cursor.execute("INSERT or IGNORE into album VALUES(98, 'Whitney Houston', 1985, 'Whitney Houston')")
cursor.execute("INSERT or IGNORE into album VALUES(99, 'Whitney', 1987, 'Whitney Houston')")
cursor.execute("INSERT or IGNORE into album VALUES(100, 'The Bodyguard', 1992, 'Whitney Houston')")
cursor.execute("INSERT or IGNORE into album VALUES(101, 'Im Your Baby Tonight', 1990, 'Whitney Houston')")
cursor.execute("INSERT or IGNORE into album VALUES(102, 'The Preachers Wife', 1996, 'Whitney Houston')")
connection.commit()

#add to users
cursor.execute("INSERT or IGNORE into users VALUES(1, 'brittns', 'bsims3888@gmail.com', 'password')")
connection.commit()


app.run(host="0.0.0.0", port=80)
if __name__ == "__main__":
   app.run(debug=True)
