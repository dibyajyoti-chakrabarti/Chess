from tkinter import *
from PIL import Image, ImageTk
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

import mysql.connector as mc
from mysql.connector import Error

chess = customtkinter.CTk()
chess.geometry("200x200")
chess.title("Chess Window")

gameBG = ImageTk.PhotoImage(Image.open("C:\Debbo 12A\Chess\windowBG.jpg"))
BGLabel = Label(chess, image = gameBG)
BGLabel.image = gameBG
BGLabel.place(x=0,y=0)

Label(chess, padx=360,pady=425, bg = "black").place(x=50,y=20)

Label(chess,text = "Current Player", bg = "black", fg = "white", font = ("Times New Roman",25,"bold")).place(x=800,y=50)
Label(chess, bg = "green", padx=70,pady=30, font = ("Britannic Bold",40,"bold")).place(x=840,y=130)
Label(chess, bg = "white", padx=60,pady=20, font = ("Britannic Bold",40,"bold")).place(x=850,y=140)

Label(chess,text = "", bg = "black", fg = "white", font = ("Britannic Bold",40,"bold"),padx=130,pady=500).place(x=1110,y=0)


defaultBoard = '''r n b q k b q r
p p p p p p p p
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
P P P P P P P P
R N B Q K B N R'''

def startDefault():
    try:
        #Connecting variables for DBMS
        connectCredentials = {
            'user' : 'root',
            'password' : 'iCode69!',
            'database': 'chess',
            'raise_on_warnings': True,
            'autocommit': True
            }

        #Connecting to DBMS
        conn = mc.connect(**connectCredentials)

        #When connected
        if conn.is_connected():
            dbInfo = conn.get_server_info()
            print("The server details", dbInfo)

            cursor = conn.cursor()
                        
            command1 = "delete from game_board;"
            print(command1)
            cursor.execute(command1)

            command2 = "insert into game_board values (\""+defaultBoard+"\");"
            print(command2)
            cursor.execute(command2)
   
    #Closing connections 
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Done")
startDefault()

def get_board():
    try:
        #Connecting variables for DBMS
        connectCredentials = {
            'user' : 'root',
            'password' : 'iCode69!',
            'database': 'chess',
            'raise_on_warnings': True,
            'autocommit': True
            }

        #Connecting to DBMS
        conn = mc.connect(**connectCredentials)

        #When connected
        if conn.is_connected():
            dbInfo = conn.get_server_info()
            print("The server details", dbInfo)

            cursor = conn.cursor()
                        

            command1 = "select * from game_board;"
            print(command1)
            cursor.execute(command1)
            contentList = cursor.fetchall()

            current_board = (contentList[0])[0]
            
    #Closing connections 
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Done")
    
    return current_board


def update_promotion_piece(piece):
    try:
        #Connecting variables for DBMS
        connectCredentials = {
            'user' : 'root',
            'password' : 'iCode69!',
            'database': 'chess',
            'raise_on_warnings': True,
            'autocommit': True
            }

        #Connecting to DBMS
        conn = mc.connect(**connectCredentials)

        #When connected
        if conn.is_connected():
            dbInfo = conn.get_server_info()
            print("The server details", dbInfo)

            cursor = conn.cursor()
                        

            command1 = "delete from promotion_piece;"
            print(command1)
            cursor.execute(command1)

            command2 = "insert into promotion_piece values(\""+piece+"\");"
            print(command2)
            cursor.execute(command2)
            
    #Closing connections 
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Done")

def get_promotion_piece():
    try:
        #Connecting variables for DBMS
        connectCredentials = {
            'user' : 'root',
            'password' : 'iCode69!',
            'database': 'chess',
            'raise_on_warnings': True,
            'autocommit': True
            }

        #Connecting to DBMS
        conn = mc.connect(**connectCredentials)

        #When connected
        if conn.is_connected():
            dbInfo = conn.get_server_info()
            print("The server details", dbInfo)

            cursor = conn.cursor()
                        

            command1 = "select * from promotion_piece;"
            print(command1)
            cursor.execute(command1)
            contentList = cursor.fetchall()

            current_piece = (contentList[0])[0]
            
    #Closing connections 
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Done")

    return current_piece

def defaultCountTurn():
    try:
        #Connecting variables for DBMS
        connectCredentials = {
            'user' : 'root',
            'password' : 'iCode69!',
            'database': 'chess',
            'raise_on_warnings': True,
            'autocommit': True
            }

        #Connecting to DBMS
        conn = mc.connect(**connectCredentials)

        #When connected
        if conn.is_connected():
            dbInfo = conn.get_server_info()
            print("The server details", dbInfo)

            cursor = conn.cursor()
            
            command1 = "delete from count_turn;"
            print(command1)
            cursor.execute(command1)

            command2 = "insert into count_turn values (0);"
            print(command2)
            cursor.execute(command2)

            
    #Closing connections 
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Done")

    
defaultCountTurn()

def update_game_status_0():
    try:
        #Connecting variables for DBMS
        connectCredentials = {
            'user' : 'root',
            'password' : 'iCode69!',
            'database': 'chess',
            'raise_on_warnings': True,
            'autocommit': True
            }

        #Connecting to DBMS
        conn = mc.connect(**connectCredentials)

        #When connected
        if conn.is_connected():
            dbInfo = conn.get_server_info()
            print("The server details", dbInfo)

            cursor = conn.cursor()
                        
            command1 = "delete from game_status;"
            print(command1)
            cursor.execute(command1)
           
            command2 = "insert into game_status values (0);"
            print(command2)
            cursor.execute(command2)
    
    #Closing connections 
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Done")

def update_game_status_1():
    try:
        #Connecting variables for DBMS
        connectCredentials = {
            'user' : 'root',
            'password' : 'iCode69!',
            'database': 'chess',
            'raise_on_warnings': True,
            'autocommit': True
            }

        #Connecting to DBMS
        conn = mc.connect(**connectCredentials)

        #When connected
        if conn.is_connected():
            dbInfo = conn.get_server_info()
            print("The server details", dbInfo)

            cursor = conn.cursor()
                        
            command1 = "delete from game_status;"
            print(command1)
            cursor.execute(command1)
           
            command2 = "insert into game_status values (1);"
            print(command2)
            cursor.execute(command2)
    
    #Closing connections 
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Done")

def get_game_status():
    try:
        #Connecting variables for DBMS
        connectCredentials = {
            'user' : 'root',
            'password' : 'iCode69!',
            'database': 'chess',
            'raise_on_warnings': True,
            'autocommit': True
            }

        #Connecting to DBMS
        conn = mc.connect(**connectCredentials)

        #When connected
        if conn.is_connected():
            dbInfo = conn.get_server_info()
            print("The server details", dbInfo)

            cursor = conn.cursor()
                        
            command1 = "select * from game_status;"
            print(command1)
            cursor.execute(command1)
            contentList = cursor.fetchall()

            current_status = (contentList[0])[0]
        
    
    #Closing connections 
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Done")

    return current_status

def runStatus():
    update_game_status_0()

runStatus()

def boardGUI():

    content = get_board()

    l1=content.split('\n')
    l2=[]
    for i in l1:
        dummy = i.split(" ")
        l2.append(dummy)
    
    board = l2
    def buttonLayout():
        
        def decideSquareColour(i,j):
            if i%2!=0:
                if j%2!=0:
                    colour = "#99CCFF"
                else:
                    colour = "#006599"
            else:
                if j%2!=0:
                    colour = "#006599"
                else:
                    colour = "#99CCFF"
            return colour
        
        def decideSquareImage(i,j):
            

            imageInfo = ""
            if i%2!=0:
                if j%2!=0:
                    if board[i][j] == "P":
                        imageInfo = "C:\Debbo 12A\Chess\wsq_P.png"
                    elif board[i][j] == "B":
                        imageInfo = "C:\Debbo 12A\Chess\wsq_B.png"
                    elif board[i][j] == "N":
                        imageInfo = "C:\Debbo 12A\Chess\wsq_N.png"
                    elif board[i][j] == "R":
                        imageInfo = "C:\Debbo 12A\Chess\wsq_R.png"
                    elif board[i][j] == "Q":
                        imageInfo = "C:\Debbo 12A\Chess\wsq_Q.png"
                    elif board[i][j] == "K":
                        imageInfo = "C:\Debbo 12A\Chess\wsq_K.png"

                    
                    if board[i][j] == 'p':
                        imageInfo = "C:\Debbo 12A\Chess\white_sq_p.png"
                    elif board[i][j] == "b":
                        imageInfo = "C:\Debbo 12A\Chess\white_sq_b.png"
                    elif board[i][j] == "n":
                        imageInfo = "C:\Debbo 12A\Chess\white_sq_n.png"
                    elif board[i][j] == "r":
                        imageInfo = "C:\Debbo 12A\Chess\white_sq_r.png"
                    elif board[i][j] == "q":
                        imageInfo = "C:\Debbo 12A\Chess\white_sq_q.png"
                    elif board[i][j] == "k":
                        imageInfo = "C:\Debbo 12A\Chess\white_sq_k.png"

                    if board[i][j] == "-":
                        imageInfo = "C:\Debbo 12A\Chess\whiteSq.png"
                else:
                    if board[i][j] == "P":
                        imageInfo = "C:\Debbo 12A\Chess\dsq_P.png"
                    elif board[i][j] == "B":
                        imageInfo = "C:\Debbo 12A\Chess\dsq_B.png"
                    elif board[i][j] == "N":
                        imageInfo = "C:\Debbo 12A\Chess\dsq_N.png"
                    elif board[i][j] == "R":
                        imageInfo = "C:\Debbo 12A\Chess\dsq_R.png"
                    elif board[i][j] == "Q":
                        imageInfo = "C:\Debbo 12A\Chess\dsq_Q.png"
                    elif board[i][j] == "K":
                        imageInfo = "C:\Debbo 12A\Chess\dsq_K.png"

                    
                    if board[i][j] == 'p':
                        imageInfo = "C:\Debbo 12A\Chess\dark_sq_p.png"
                    elif board[i][j] == "b":
                        imageInfo = "C:\Debbo 12A\Chess\dark_sq_b.png"
                    elif board[i][j] == "n":
                        imageInfo = "C:\Debbo 12A\Chess\dark_sq_n.png"
                    elif board[i][j] == "r":
                        imageInfo = "C:\Debbo 12A\Chess\dark_sq_r.png"
                    elif board[i][j] == "q":
                        imageInfo = "C:\Debbo 12A\Chess\dark_sq_q.png"
                    elif board[i][j] == "k":
                        imageInfo = "C:\Debbo 12A\Chess\dark_sq_k.png"
                    
                    if board[i][j] == "-":
                        imageInfo = ("C:\Debbo 12A\Chess\darkSq.png")
            else:
                if j%2!=0:
                    if board[i][j] == "P":
                        imageInfo = "C:\Debbo 12A\Chess\dsq_P.png"
                    elif board[i][j] == "B":
                        imageInfo = "C:\Debbo 12A\Chess\dsq_B.png"
                    elif board[i][j] == "N":
                        imageInfo = "C:\Debbo 12A\Chess\dsq_N.png"
                    elif board[i][j] == "R":
                        imageInfo = "C:\Debbo 12A\Chess\dsq_R.png"
                    elif board[i][j] == "Q":
                        imageInfo = "C:\Debbo 12A\Chess\dsq_Q.png"
                    elif board[i][j] == "K":
                        imageInfo = "C:\Debbo 12A\Chess\dsq_K.png"

                    
                    if board[i][j] == 'p':
                        imageInfo = "C:\Debbo 12A\Chess\dark_sq_p.png"
                    elif board[i][j] == "b":
                        imageInfo = "C:\Debbo 12A\Chess\dark_sq_b.png"
                    elif board[i][j] == "n":
                        imageInfo = "C:\Debbo 12A\Chess\dark_sq_n.png"
                    elif board[i][j] == "r":
                        imageInfo = "C:\Debbo 12A\Chess\dark_sq_r.png"
                    elif board[i][j] == "q":
                        imageInfo = "C:\Debbo 12A\Chess\dark_sq_q.png"
                    elif board[i][j] == "k":
                        imageInfo = "C:\Debbo 12A\Chess\dark_sq_k.png"

                    if board[i][j] == "-":
                        imageInfo = ("C:\Debbo 12A\Chess\darkSq.png")
                else:
                    if board[i][j] == "P":
                        imageInfo = "C:\Debbo 12A\Chess\wsq_P.png"
                    elif board[i][j] == "B":
                        imageInfo = "C:\Debbo 12A\Chess\wsq_B.png"
                    elif board[i][j] == "N":
                        imageInfo = "C:\Debbo 12A\Chess\wsq_N.png"
                    elif board[i][j] == "R":
                        imageInfo = "C:\Debbo 12A\Chess\wsq_R.png"
                    elif board[i][j] == "Q":
                        imageInfo = "C:\Debbo 12A\Chess\wsq_Q.png"
                    elif board[i][j] == "K":
                        imageInfo = "C:\Debbo 12A\Chess\wsq_K.png"


                    if board[i][j] == 'p':
                        imageInfo = "C:\Debbo 12A\Chess\white_sq_p.png"
                    elif board[i][j] == "b":
                        imageInfo = "C:\Debbo 12A\Chess\white_sq_b.png"
                    elif board[i][j] == "n":
                        imageInfo = "C:\Debbo 12A\Chess\white_sq_n.png"
                    elif board[i][j] == "r":
                        imageInfo = "C:\Debbo 12A\Chess\white_sq_r.png"
                    elif board[i][j] == "q":
                        imageInfo = "C:\Debbo 12A\Chess\white_sq_q.png"
                    elif board[i][j] == "k":
                        imageInfo = "C:\Debbo 12A\Chess\white_sq_k.png"

                    if board[i][j] == "-":
                        imageInfo = "C:\Debbo 12A\Chess\whiteSq.png"
            return imageInfo
        
        def xCo(j):
            x_co =83 * (j+1)
            return x_co
        def yCo(i):
            y_co= 83 * (i+1)
            return y_co
        
        def possibleMoves(i,j):

            try:
                #Connecting variables for DBMS
                connectCredentials = {
                    'user' : 'root',
                    'password' : 'iCode69!',
                    'database': 'chess',
                    'raise_on_warnings': True,
                    'autocommit': True
                    }

                #Connecting to DBMS
                conn = mc.connect(**connectCredentials)

                #When connected
                if conn.is_connected():
                    dbInfo = conn.get_server_info()
                    print("The server details", dbInfo)

                    cursor = conn.cursor()
                    
                    command1 = "select max(count) from count_turn;"
                    print(command1)
                    cursor.execute(command1)
                    contentList = cursor.fetchall()
                   

            
            #Closing connections 
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
                print("Done")
          
           
            turn = contentList[0][0]
            
            piece = board[i][j]

            def turnBoard(board_list):
                    reversed_board = []
                    r1 = []
                    r2 = []
                    r3 = []
                    r4 = []
                    r5 = []
                    r6 = []
                    r7 = []
                    r8 = []
                    row1 = board_list[0]
                    for el in reversed(row1):
                        r1.append(el)
                    row2 = board_list[1]
                    for el in reversed(row2):
                        r2.append(el)
                    row3 = board_list[2]
                    for el in reversed(row3):
                        r3.append(el)
                    row4 = board_list[3]
                    for el in reversed(row4):
                        r4.append(el)
                    row5 = board_list[4]
                    for el in reversed(row5):
                        r5.append(el)
                    row6 = board_list[5]
                    for el in reversed(row6):
                        r6.append(el)
                    row7 = board_list[6]
                    for el in reversed(row7):
                        r7.append(el)
                    row8 = board_list[7]
                    for el in reversed(row8):
                        r8.append(el)

                    reversed_board.append(r8)
                    reversed_board.append(r7)
                    reversed_board.append(r6)
                    reversed_board.append(r5)
                    reversed_board.append(r4)
                    reversed_board.append(r3)
                    reversed_board.append(r2)
                    reversed_board.append(r1)
                    return reversed_board


            def displayMoves(x_list, y_list,piece):
                def check_possibility(x_current,y_current, x_list,y_list):
                    for index in range (0,len(y_list)):
                        y = y_list[index]
                        x = x_list[index]

                        if x == x_current and y == y_current:
                            return 1
                
                def update_board(i,j,y,x,piece):
                    def updated_turn_dbms():
                        try:
                            #Connecting variables for DBMS
                            connectCredentials = {
                                'user' : 'root',
                                'password' : 'iCode69!',
                                'database': 'chess',
                                'raise_on_warnings': True,
                                'autocommit': True
                                }

                            #Connecting to DBMS
                            conn = mc.connect(**connectCredentials)

                            #When connected
                            if conn.is_connected():
                                dbInfo = conn.get_server_info()
                                print("The server details", dbInfo)

                                cursor = conn.cursor()
                                                

                                command1 = "select max(count) from count_turn;"
                                print(command1)
                                cursor.execute(command1)
                                contentList = cursor.fetchall()

                                current_count = (contentList[0])[0]
                                updated_count = current_count + 1
                                print(updated_count)

                                command2 = "insert into count_turn(count) values ("+str(updated_count)+");"
                                print(command2)
                                cursor.execute(command2)

                                    
                        #Closing connections 
                        finally:
                            if conn.is_connected():
                                cursor.close()
                                conn.close()
                            print("Done")
                    
                    Label(chess,text = "", bg = "black", fg = "white", font = ("Britannic Bold",40,"bold"),padx=130,pady=500).place(x=1110,y=0)

                    def whiteWins():
                        #Basic Dimensions
                        whiteWinner = Tk()
                        whiteWinner.geometry('550x600')
                        whiteWinner.title('Winner!')
                        whiteWinner['bg']='black'

                        newMsg = '''
                        Congratulations!






                        has won the game!

                        BY KILLING THE
                        [Black King]
                        '''
                        def closeGame():
                            whiteWinner.destroy()
                            chess.destroy()
                            
                        Label(whiteWinner,text="We have a winner!", fg="white", font= ("Bernard MT Condensed", 25, 'bold'), bg="#58B11A",  anchor='n',padx=15,pady=5).place(x=130, y=50)
                        Label(whiteWinner, text=newMsg, bg="black", fg="white", font= ("Times New Roman",17, 'bold')).place(x=30,y=120)
                        Label(whiteWinner, text=" ", bg="green", fg="white", font= ("Times New Roman",25, 'bold'),padx=43,pady=28).place(x = 220,y = 200)
                        Label(whiteWinner, text=" ", bg="white", fg="white", font= ("Times New Roman",25, 'bold'),padx=33,pady=18).place(x = 230,y = 210)

                        endGame=Button(whiteWinner, text= "Alright", bg= '#58B11A', fg= '#FDEDEC', font= ("Old English Text MT", 22, 'bold'), cursor= 'hand2', command= closeGame, borderwidth= 10).place(x=210, y=480)

                    def blackWins():
                        #Basic Dimensions
                        blackWinner = Tk()
                        blackWinner.geometry('550x600')
                        blackWinner.title('Winner!')
                        blackWinner['bg']='#FBF5F5'

                        newMsg = '''
                        Congratulations!






                        has won the game!

                        BY KILLING THE
                        [White King]
                        '''
                        def closeGame():
                            blackWinner.destroy()
                            chess.destroy()
                            
                        Label(blackWinner,text="We have a winner!", fg="black", font= ("Bernard MT Condensed", 25, 'bold'), bg="#58B11A",  anchor='n',padx=15,pady=5).place(x=130, y=50)
                        Label(blackWinner, text=newMsg, bg="#FBF5F5", fg="black", font= ("Times New Roman",17, 'bold')).place(x=30,y=120)
                        Label(blackWinner, text=" ", bg="green", fg="black", font= ("Times New Roman",25, 'bold'),padx=43,pady=28).place(x = 220,y = 200)
                        Label(blackWinner, text=" ", bg="black", fg="black", font= ("Times New Roman",25, 'bold'),padx=33,pady=18).place(x = 230,y = 210)

                        endGame=Button(blackWinner, text= "Alright", bg= '#58B11A', fg= '#FDEDEC', font= ("Old English Text MT", 22, 'bold'), cursor= 'hand2', command= closeGame, borderwidth= 10).place(x=210, y=480)
                    
                    if board[y][x] == "k":
                        print("White has won")
                        whiteWins()

                        update_game_status_1()

                    if board[y][x] == "K":
                        print("Black has won")
                        blackWins()

                        update_game_status_1()
                    
                    if board[i][j] == "P" and i == 1:

                        _piece = get_promotion_piece()
                        piece = _piece
                        if _piece == "P":
                            
                            updated_turn_dbms()
                    
                    if board[i][j] == "p" and i == 1:
                        
                        _piece = get_promotion_piece()
                        piece = _piece
                        if _piece == "p":
                            
                            updated_turn_dbms()


                    if (piece == "P" or piece == "p") and i == 1:
                        print("Sheit")
                    else:
                        
                        board[y][x] = piece
                        board[i][j] = '-'
                    
                    
                    dummy = ""
                    dummyList=[]
                    for element in board:
                        dummy = str(element) 
                        dummyList.append(element)
                    #print(dummyList)
                    #print("---")

                    if (piece == "P" or piece == "p") and i == 1:
                        turned_board = dummyList
                    else:
                        turned_board = turnBoard(dummyList)
                    #print(turned_board)

                    s = ""
                    for element in turned_board:
                        if element == "[" or element =="\'" or element ==" ":
                            element = ""
                        if element == ",":
                            element = " "
                        if element == "]":
                            element = "\n"
                        s=s+str(element) 
                    s_=""
                    for element in s:
                        if element == "[" or element =="\'" or element ==" ":
                            element = ""
                        if element == ",":
                            element = " "
                        if element == "]":
                            element = "\n"
                        s_=s_+str(element) 
                    print(s_)

                    try:
                        #Connecting variables for DBMS
                        connectCredentials = {
                            'user' : 'root',
                            'password' : 'iCode69!',
                            'database': 'chess',
                            'raise_on_warnings': True,
                            'autocommit': True
                            }

                        #Connecting to DBMS
                        conn = mc.connect(**connectCredentials)

                        #When connected
                        if conn.is_connected():
                            dbInfo = conn.get_server_info()
                            print("The server details", dbInfo)

                            cursor = conn.cursor()
                                        
                            command1 = "delete from game_board;"
                            print(command1)
                            cursor.execute(command1)

                            command2 = "insert into game_board values (\""+s_+"\");"
                            print(command2)
                            cursor.execute(command2)
                
                    #Closing connections 
                    finally:
                        if conn.is_connected():
                            cursor.close()
                            conn.close()
                        print("Done")
                    
                    updated_turn_dbms()

                    try:
                        #Connecting variables for DBMS
                        connectCredentials = {
                            'user' : 'root',
                            'password' : 'iCode69!',
                            'database': 'chess',
                            'raise_on_warnings': True,
                            'autocommit': True
                            }

                        #Connecting to DBMS
                        conn = mc.connect(**connectCredentials)

                        #When connected
                        if conn.is_connected():
                            dbInfo = conn.get_server_info()
                            print("The server details", dbInfo)

                            cursor = conn.cursor()
                                        

                            command1 = "select max(count) from count_turn;"
                            print(command1)
                            cursor.execute(command1)
                            contentList = cursor.fetchall()

                            current_count = (contentList[0])[0]

                    #Closing connections 
                    finally:
                        if conn.is_connected():
                            cursor.close()
                            conn.close()
                        print("Done")
                    
                    counter = current_count

                    if counter % 2 == 0:
                        Label(chess, bg = "white", padx=60,pady=20, font = ("Britannic Bold",40,"bold")).place(x=850,y=140)
                    
                    if counter %2 != 0:
                        Label(chess, bg = "black", padx=60,pady=20, font = ("Britannic Bold",40,"bold")).place(x=850,y=140)

                    
                    
                    
                def possibleButtons():
                    
                    def column1():
                        x=0

                        y=0
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=0
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=1
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=1
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=2
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=2
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=3
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=3
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=4
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=4
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)

                        y=5
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=5
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=6
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=6
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=7
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=7
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                    
                    def column2():
                        x=1

                        y=0
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=0
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=1
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=1
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=2
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=2
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=3
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=3
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=4
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=4
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)

                        y=5
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=5
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=6
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=6
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=7
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=7
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)

                    def column3():
                        x=2

                        y=0
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=0
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=1
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=1
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=2
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=2
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=3
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=3
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=4
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=4
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)

                        y=5
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=5
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=6
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=6
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=7
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=7
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                    
                    def column4():
                        x=3

                        y=0
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=0
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=1
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=1
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=2
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=2
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=3
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=3
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=4
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=4
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)

                        y=5
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=5
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=6
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=6
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=7
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=7
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                    
                    def column5():
                        x=4

                        y=0
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=0
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=1
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=1
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=2
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=2
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=3
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=3
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=4
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=4
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)

                        y=5
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=5
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=6
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=6
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=7
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=7
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)

                    def column6():
                        x=5

                        y=0
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=0
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=1
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=1
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=2
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=2
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=3
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=3
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=4
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=4
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)

                        y=5
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=5
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=6
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=6
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=7
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=7
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)

                    def column7():
                        x=6

                        y=0
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=0
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=1
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=1
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=2
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=2
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=3
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=3
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=4
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=4
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)

                        y=5
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=5
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=6
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=6
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=7
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=7
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)

                    def column8():
                        x=7

                        y=0
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=0
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=1
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=1
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=2
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=2
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=3
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=3
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=4
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=4
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)

                        y=5
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=5
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=6
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=6
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)
                        
                        y=7
                        check = check_possibility(y,x,y_list,x_list)
                        if check == 1:
                            def displace_piece():
                                y=7
                                print(y,x)
                                update_board(i,j,y,x,piece)
                                boardGUI()

                            y_co = yCo(y) - 50
                            x_co = xCo(x)
                            imageInfo = decideSquareImage(y,x)
                            image = ImageTk.PhotoImage(Image.open(imageInfo))
                            sq = customtkinter.CTkButton(master = chess, text = "", image = image, width = 80, height = 80, compound = "left", command = displace_piece, fg_color = "#FE2828", hover_color = "#F08E8E")
                            sq.pack(pady=10, padx =10)
                            sq.place(x = x_co, y = y_co)


                    column1()
                    column2()
                    column3()
                    column4()
                    column5()
                    column6()
                    column7()
                    column8()
                possibleButtons()

            
            #Vacant Space
            if piece == '-':
                print("Vacant Space")
            
            def checkDangerPos(turn):
                all_x=[]
                all_y=[]

                if turn == 1:
                    #White
                    rev_board = turnBoard(board)
                    for i in rev_board:
                        print(i)
                    print("\n")

                    p_x = []
                    p_y = []

                    r_x = []
                    r_y = []

                    n_x = []
                    n_y = []

                    b_x = []
                    b_y = []

                    q_x = []
                    q_y = []
                    for c in range (0,8):
                        for r in range (0,8):
                            
                            if rev_board[c][r] == "p":
                                
                                p_x.append(r)
                                p_y.append(c)
                            
                            if rev_board[c][r] == "r":

                                r_x.append(r)
                                r_y.append(c)
                            
                            if rev_board[c][r] == "n":

                                n_x.append(r)
                                n_y.append(c) 
                            
                            if rev_board[c][r] == "b":

                                b_x.append(r)
                                b_y.append(c) 
                            
                            if rev_board[c][r] == "q":

                                q_x.append(r)
                                q_y.append(c) 
                    
                    
                    
                    #Pawn
                    for index in range (len(p_y)):
                        y = p_y[index]
                        x = p_x[index]

                        #Kill 1
                        x_co = x-1
                        y_co = y-1
                        if x_co > -1 and y_co >-1:
                            all_y.append(y_co)
                            all_x.append(x_co)

                        #Kill 2
                        x_co = x+1
                        y_co = y-1
                        if x_co < 8 and y_co >-1:
                            all_y.append(y_co)
                            all_x.append(x_co)

                    #Rook
                    for index in range (len(r_y)):
                        i = r_y[index]
                        j = r_x[index]
                        
                        pos_hor=[]
                        pos_ver=[]
                        
                        #Horizontal
                        for left_x in range (j-1,-1,-1):

                            if rev_board[i][left_x] == '-':
                                pos_hor.append(left_x)
                            elif rev_board[i][left_x].isupper()==True:
                                pos_hor.append(left_x)
                                pos_hor.append(left_x-1)
                                break
                            else:
                                pos_hor.append(left_x)
                                break
                        for right_x in range (j+1,8):
                            
                            if rev_board[i][right_x] == '-':
                                pos_hor.append(right_x)
                            elif rev_board[i][right_x].isupper()==True:
                                pos_hor.append(right_x)
                                pos_hor.append(right_x+1)
                                break
                            else:
                                pos_hor.append(right_x)
                                break
                            
                        
                        for x in pos_hor:
                            all_x.append(x)
                            all_y.append(i)
                        

                        #Vertical
                        for up_y in range (i-1,-1,-1):
                            if rev_board[up_y][j] == '-':
                                pos_ver.append(up_y)
                            elif rev_board[up_y][j].isupper()==True:
                                pos_ver.append(up_y)
                                pos_ver.append(up_y-1)
                                break
                            else:
                                pos_ver.append(up_y)
                                break
                        for down_y in range (i+1,8):
                            if rev_board[down_y][j] == '-':
                                pos_ver.append(down_y)
                            elif rev_board[down_y][j].isupper()==True:
                                pos_ver.append(down_y)
                                pos_ver.append(down_y+1)
                                break
                            else:
                                pos_ver.append(down_y)
                                break
                        
                        for y in pos_ver:
                            all_x.append(j)
                            all_y.append(y)
                     
                    #Knight
                    for index in range (len(n_y)):
                        y_co = n_y[index]
                        x_co = n_x[index]

                        i = y_co
                        j = x_co

                        #Possibility 1
                        y = i-2
                        x = j+1
                        if x<8 and y>-1 and (board[y][x].islower()==False):
                            all_x.append(x)
                            all_y.append(y) 

                        # possibility 2
                        x = j+2
                        y = i-1
                        if x<8 and y>-1  and (board[y][x].islower()==False):
                            all_x.append(x)
                            all_y.append(y) 

                        # possibility 3
                        x = j+2
                        y = i+1
                        if x<8 and y<8 and (board[y][x].islower()==False):
                            all_x.append(x)
                            all_y.append(y) 

                        # possibility 4
                        x = j+1
                        y = i+2
                        if x<8 and y<8 and (board[y][x].islower()==False):
                            all_x.append(x)
                            all_y.append(y) 

                        # possibility 5
                        x = j-1
                        y = i+2
                        if x>-1 and y<8 and (board[y][x].islower()==False):
                            all_x.append(x)
                            all_y.append(y) 

                        # possibility 6
                        x = j-2
                        y = i+1
                        if x>-1 and y<8 and (board[y][x].islower()==False):
                            all_x.append(x)
                            all_y.append(y) 

                        # possibility 7
                        x = j-2
                        y = i-1
                        if x>-1 and y>-1 and (board[y][x].islower()==False):
                            all_x.append(x)
                            all_y.append(y) 
                        
                        # possibility 8
                        x = j-1
                        y = i-2
                        if x>-1 and y>-1:
                            all_x.append(x)
                            all_y.append(y) 

                    #Bishop
                    for index in range (len(b_y)):
                        i = b_y[index]
                        j = b_x[index]

                        # 1st Quad
                        ref = i+j
                       
                        x_co = []
                        y_co = []
                        for y in range (0,i+1):
                            for x in range (j,8):
                                if x!= j and y!= i:
                                    if (x+y) == ref:
                                        if rev_board[y][x] == '-':
                                            y_co.append(y)
                                            x_co.append(x)
                                        elif rev_board[y][x].isupper() == True:
                                            y_co = []
                                            x_co = []
                                            y_co.append(y)
                                            x_co.append(x)
                                            y_co.append(y - 1)
                                            x_co.append(x + 1)
                                        elif rev_board[y][x].islower() == True:
                                            y_co = []
                                            x_co = []
                        

                        for items in x_co:
                            all_x.append(items)
                        for items in y_co:
                            all_y.append(items)

                        # 2nd Quad
                        
                        ref = i-j
                        x_co = []
                        y_co = []
                        for y in range (0,i+1):
                            for x in range (0,j+1):
                                if (y-x) == ref:
                                    if y != i and x != j:
                                        
                                        if rev_board[y][x] == '-':
                                            y_co.append(y)
                                            x_co.append(x)
                                        elif rev_board[y][x].isupper() == True:
                                            y_co = []
                                            x_co = []
                                            y_co.append(y)
                                            x_co.append(x)
                                            y_co.append(y - 1)
                                            x_co.append(x - 1)
                                        elif rev_board[y][x].islower() == True:
                                            y_co = []
                                            x_co = []
                        for items in x_co:
                            all_x.append(items)
                        for items in y_co:
                            all_y.append(items)   

                        
                    
                        # 3rd Quad
                        
                        ref = i+j
                        check =[]
                        for y in range (i,8):
                            for x in range (0,j+1):
                                if (x+y) == ref:
                                    if x != j and y != i:
                                        if rev_board[y][x] == '-':
                                            
                                            all_x.append(x)
                                            all_y.append(y)    
                                            
                                        elif rev_board[y][x].isupper() == True:
                                            
                                            all_x.append(x)
                                            all_y.append(y) 
                                            all_x.append(y + 1)
                                            all_y.append(x - 1)
                                            check.append(1)
                                            break
                                        elif rev_board[y][x].islower() == True:
                                            check.append(1)
                                            break
                            if (1 in check) == True:
                                break

                            
                        # 4th Quad
                        
                        ref = i-j
                        check =[]
                        for y in range (i,8):
                            for x in range (j,8):
                                if (y-x) == ref:
                                    if x != j and y != i:
                                        if rev_board[y][x] == '-':
                                            
                                            all_x.append(x)
                                            all_y.append(y) 
                                        elif rev_board[y][x].isupper() == True:
                                            
                                            all_x.append(x)
                                            all_y.append(y)
                                            all_y.append(y + 1)
                                            all_x.append(x + 1)
                                            check.append(1)
                                            break
                                        elif rev_board[y][x].islower() == True:
                                            check.append(1)
                                            break
                            if (1 in check) == True:
                                break
                        
                    #Queen
                    for index in range (len(q_y)):
                        i = q_y[index]
                        j = q_x[index]
                        
                        pos_hor=[]
                        pos_ver=[]
                        
                        #Horizontal
                        for left_x in range (j-1,-1,-1):

                            if rev_board[i][left_x] == '-':
                                pos_hor.append(left_x)
                            elif rev_board[i][left_x].isupper()==True:
                                pos_hor.append(left_x)
                                pos_hor.append(left_x-1)
                                break
                            else:
                                pos_hor.append(left_x)
                                break
                        for right_x in range (j+1,8):
                            
                            if rev_board[i][right_x] == '-':
                                pos_hor.append(right_x)
                            elif rev_board[i][right_x].isupper()==True:
                                pos_hor.append(right_x)
                                pos_hor.append(right_x+1)
                                break
                            else:
                                pos_hor.append(right_x)
                                break
                            
                        
                        for x in pos_hor:
                            all_x.append(x)
                            all_y.append(i)
                        

                        #Vertical
                        for up_y in range (i-1,-1,-1):
                            if rev_board[up_y][j] == '-':
                                pos_ver.append(up_y)
                            elif rev_board[up_y][j].isupper()==True:
                                pos_ver.append(up_y)
                                pos_ver.append(up_y-1)
                                break
                            else:
                                pos_ver.append(up_y)
                                break
                        for down_y in range (i+1,8):
                            if rev_board[down_y][j] == '-':
                                pos_ver.append(down_y)
                            elif rev_board[down_y][j].isupper()==True:
                                pos_ver.append(down_y)
                                pos_ver.append(down_y+1)
                                break
                            else:
                                pos_ver.append(down_y)
                                break
                        
                        for y in pos_ver:
                            all_x.append(j)
                            all_y.append(y)
                        
                        # 1st Quad
                        ref = i+j
                       
                        x_co = []
                        y_co = []
                        for y in range (0,i+1):
                            for x in range (j,8):
                                if x!= j and y!= i:
                                    if (x+y) == ref:
                                        if rev_board[y][x] == '-':
                                            y_co.append(y)
                                            x_co.append(x)
                                        elif rev_board[y][x].isupper() == True:
                                            y_co = []
                                            x_co = []
                                            y_co.append(y)
                                            x_co.append(x)
                                            y_co.append(y - 1)
                                            x_co.append(x + 1)
                                        elif rev_board[y][x].islower() == True:
                                            y_co = []
                                            x_co = []
                        

                        for items in x_co:
                            all_x.append(items)
                        for items in y_co:
                            all_y.append(items)

                        # 2nd Quad
                        
                        ref = i-j
                        x_co = []
                        y_co = []
                        for y in range (0,i+1):
                            for x in range (0,j+1):
                                if (y-x) == ref:
                                    if y != i and x != j:
                                        
                                        if rev_board[y][x] == '-':
                                            y_co.append(y)
                                            x_co.append(x)
                                        elif rev_board[y][x].isupper() == True:
                                            y_co = []
                                            x_co = []
                                            y_co.append(y)
                                            x_co.append(x)
                                            y_co.append(y - 1)
                                            x_co.append(x - 1)
                                        elif rev_board[y][x].islower() == True:
                                            y_co = []
                                            x_co = []
                        for items in x_co:
                            all_x.append(items)
                        for items in y_co:
                            all_y.append(items)   

                        
                    
                        # 3rd Quad
                        
                        ref = i+j
                        check =[]
                        for y in range (i,8):
                            for x in range (0,j+1):
                                if (x+y) == ref:
                                    if x != j and y != i:
                                        if rev_board[y][x] == '-':
                                            
                                            all_x.append(x)
                                            all_y.append(y)    
                                            
                                        elif rev_board[y][x].isupper() == True:
                                            
                                            all_x.append(x)
                                            all_y.append(y) 
                                            all_x.append(y + 1)
                                            all_y.append(x - 1)
                                            check.append(1)
                                            break
                                        elif rev_board[y][x].islower() == True:
                                            check.append(1)
                                            break
                            if (1 in check) == True:
                                break

                            
                        # 4th Quad
                        
                        ref = i-j
                        check =[]
                        for y in range (i,8):
                            for x in range (j,8):
                                if (y-x) == ref:
                                    if x != j and y != i:
                                        if rev_board[y][x] == '-':
                                            
                                            all_x.append(x)
                                            all_y.append(y) 
                                        elif rev_board[y][x].isupper() == True:
                                            
                                            all_x.append(x)
                                            all_y.append(y)
                                            all_y.append(y + 1)
                                            all_x.append(x + 1)
                                            check.append(1)
                                            break
                                        elif rev_board[y][x].islower() == True:
                                            check.append(1)
                                            break
                            if (1 in check) == True:
                                break

                                    
                if turn == 2:
                    #Black
                    rev_board = turnBoard(board)
                    for i in rev_board:
                        print(i)
                    print("\n")

                    P_x = []
                    P_y = []

                    R_x = []
                    R_y = []

                    N_x = []
                    N_y = []

                    B_x = []
                    B_y = []

                    Q_x = []
                    Q_y = []
                    for c in range (0,8):
                        for r in range (0,8):
                            
                            if rev_board[c][r] == "P":
                                
                                P_x.append(r)
                                P_y.append(c)
                            
                            if rev_board[c][r] == "R":

                                R_x.append(r)
                                R_y.append(c)
                            
                            if rev_board[c][r] == "N":

                                N_x.append(r)
                                N_y.append(c) 
                            
                            if rev_board[c][r] == "B":

                                B_x.append(r)
                                B_y.append(c) 
                            
                            if rev_board[c][r] == "Q":

                                Q_x.append(r)
                                Q_y.append(c) 
                    

                    #Pawn
                    for index in range (len(P_y)):
                        y = P_y[index]
                        x = P_x[index]

                        #Kill 1
                        x_co = x-1
                        y_co = y-1
                        if x_co > -1 and y_co >-1:
                            all_y.append(y_co)
                            all_x.append(x_co)

                        #Kill 2
                        x_co = x+1
                        y_co = y-1
                        if x_co < 8 and y_co >-1:
                            all_y.append(y_co)
                            all_x.append(x_co)
                
                    #Rook
                    for index in range (len(R_y)):
                        i = R_y[index]
                        j = R_x[index]
                        
                        pos_hor=[]
                        pos_ver=[]
                        
                        #Horizontal
                        for left_x in range (j-1,-1,-1):

                            if rev_board[i][left_x] == '-':
                                pos_hor.append(left_x)
                            elif rev_board[i][left_x].islower()==True:
                                pos_hor.append(left_x)
                                pos_hor.append(left_x-1)
                                break
                            else:
                                pos_hor.append(left_x)
                                break
                        for right_x in range (j+1,8):
                            
                            if rev_board[i][right_x] == '-':
                                pos_hor.append(right_x)
                            elif rev_board[i][right_x].islower()==True:
                                pos_hor.append(right_x)
                                pos_hor.append(right_x+1)
                                break
                            else:
                                pos_hor.append(right_x)
                                break
                            
                        
                        for x in pos_hor:
                            all_x.append(x)
                            all_y.append(i)
                        

                        #Vertical
                        for up_y in range (i-1,-1,-1):
                            if rev_board[up_y][j] == '-':
                                pos_ver.append(up_y)
                            elif rev_board[up_y][j].islower()==True:
                                pos_ver.append(up_y)
                                pos_ver.append(up_y-1)
                                break
                            else:
                                pos_ver.append(up_y)
                                break
                        for down_y in range (i+1,8):
                            if rev_board[down_y][j] == '-':
                                pos_ver.append(down_y)
                            elif rev_board[down_y][j].islower()==True:
                                pos_ver.append(down_y)
                                pos_ver.append(down_y+1)
                                break
                            else:
                                pos_ver.append(down_y)
                                break
                        
                        for y in pos_ver:
                            all_x.append(j)
                            all_y.append(y)

                    #Knight
                    for index in range (len(N_y)):
                        y_co = N_y[index]
                        x_co = N_x[index]

                        i = y_co
                        j = x_co

                        #Possibility 1
                        y = i-2
                        x = j+1
                        if x<8 and y>-1 and (board[y][x].isupper()==False):
                            all_x.append(x)
                            all_y.append(y) 

                        # possibility 2
                        x = j+2
                        y = i-1
                        if x<8 and y>-1  and (board[y][x].isupper()==False):
                            all_x.append(x)
                            all_y.append(y) 

                        # possibility 3
                        x = j+2
                        y = i+1
                        if x<8 and y<8 and (board[y][x].isupper()==False):
                            all_x.append(x)
                            all_y.append(y) 

                        # possibility 4
                        x = j+1
                        y = i+2
                        if x<8 and y<8 and (board[y][x].isupper()==False):
                            all_x.append(x)
                            all_y.append(y) 

                        # possibility 5
                        x = j-1
                        y = i+2
                        if x>-1 and y<8 and (board[y][x].isupper()==False):
                            all_x.append(x)
                            all_y.append(y) 

                        # possibility 6
                        x = j-2
                        y = i+1
                        if x>-1 and y<8 and (board[y][x].isupper()==False):
                            all_x.append(x)
                            all_y.append(y) 

                        # possibility 7
                        x = j-2
                        y = i-1
                        if x>-1 and y>-1 and (board[y][x].isupper()==False):
                            all_x.append(x)
                            all_y.append(y) 
                        
                        # possibility 8
                        x = j-1
                        y = i-2
                        if x>-1 and y>-1:
                            all_x.append(x)
                            all_y.append(y) 

                    #Bishop
                    for index in range (len(B_y)):
                        i = B_y[index]
                        j = B_x[index]

                        # 1st Quad
                        ref = i+j
                       
                        x_co = []
                        y_co = []
                        for y in range (0,i+1):
                            for x in range (j,8):
                                if x!= j and y!= i:
                                    if (x+y) == ref:
                                        if rev_board[y][x] == '-':
                                            y_co.append(y)
                                            x_co.append(x)
                                        elif rev_board[y][x].islower() == True:
                                            y_co = []
                                            x_co = []
                                            y_co.append(y)
                                            x_co.append(x)
                                            y_co.append(y - 1)
                                            x_co.append(x + 1)
                                        elif rev_board[y][x].isupper() == True:
                                        
                                            y_co = []
                                            x_co = []
                        

                        for items in x_co:
                            all_x.append(items)
                        for items in y_co:
                            all_y.append(items)

                        # 2nd Quad
                        
                        ref = i-j
                        x_co = []
                        y_co = []
                        for y in range (0,i+1):
                            for x in range (0,j+1):
                                if (y-x) == ref:
                                    if y != i and x != j:
                                        
                                        if rev_board[y][x] == '-':
                                            y_co.append(y)
                                            x_co.append(x)
                                        elif rev_board[y][x].islower() == True:
                                            y_co = []
                                            x_co = []
                                            y_co.append(y)
                                            x_co.append(x)
                                            y_co.append(y - 1)
                                            x_co.append(x - 1)
                                        elif rev_board[y][x].isupper() == True:
                                            y_co = []
                                            x_co = []
                        for items in x_co:
                            all_x.append(items)
                        for items in y_co:
                            all_y.append(items)   

                        
                    
                        # 3rd Quad
                        
                        ref = i+j
                        check =[]
                        for y in range (i,8):
                            for x in range (0,j+1):
                                if (x+y) == ref:
                                    if x != j and y != i:
                                        if rev_board[y][x] == '-':
                                            
                                            all_x.append(x)
                                            all_y.append(y)    
                                            
                                        elif rev_board[y][x].islower() == True:
                                            
                                            all_x.append(x)
                                            all_y.append(y) 
                                            all_x.append(y + 1)
                                            all_y.append(x - 1)
                                            check.append(1)
                                            break
                                        elif rev_board[y][x].isupper() == True:
                                            check.append(1)
                                            break
                            if (1 in check) == True:
                                break

                            
                        # 4th Quad
                        
                        ref = i-j
                        check =[]
                        for y in range (i,8):
                            for x in range (j,8):
                                if (y-x) == ref:
                                    if x != j and y != i:
                                        if rev_board[y][x] == '-':
                                            
                                            all_x.append(x)
                                            all_y.append(y) 
                                        elif rev_board[y][x].islower() == True:
                                            
                                            all_x.append(x)
                                            all_y.append(y)
                                            all_y.append(y + 1)
                                            all_x.append(x + 1)
                                            check.append(1)
                                            break
                                        elif rev_board[y][x].isupper() == True:
                                            check.append(1)
                                            break
                            if (1 in check) == True:
                                break

                    #Queen
                    for index in range (len(Q_y)):
                        i = Q_y[index]
                        j = Q_x[index]
                        
                        pos_hor=[]
                        pos_ver=[]
                        
                        #Horizontal
                        for left_x in range (j-1,-1,-1):

                            if rev_board[i][left_x] == '-':
                                pos_hor.append(left_x)
                            elif rev_board[i][left_x].islower()==True:
                                pos_hor.append(left_x)
                                pos_hor.append(left_x-1)
                                break
                            else:
                                pos_hor.append(left_x)
                                break
                        for right_x in range (j+1,8):
                            
                            if rev_board[i][right_x] == '-':
                                pos_hor.append(right_x)
                            elif rev_board[i][right_x].islower()==True:
                                pos_hor.append(right_x)
                                pos_hor.append(right_x+1)
                                break
                            else:
                                pos_hor.append(right_x)
                                break
                            
                        
                        for x in pos_hor:
                            all_x.append(x)
                            all_y.append(i)
                        

                        #Vertical
                        for up_y in range (i-1,-1,-1):
                            if rev_board[up_y][j] == '-':
                                pos_ver.append(up_y)
                            elif rev_board[up_y][j].islower()==True:
                                pos_ver.append(up_y)
                                pos_ver.append(up_y-1)
                                break
                            else:
                                pos_ver.append(up_y)
                                break
                        for down_y in range (i+1,8):
                            if rev_board[down_y][j] == '-':
                                pos_ver.append(down_y)
                            elif rev_board[down_y][j].islower()==True:
                                pos_ver.append(down_y)
                                pos_ver.append(down_y+1)
                                break
                            else:
                                pos_ver.append(down_y)
                                break
                        
                        for y in pos_ver:
                            all_x.append(j)
                            all_y.append(y)
                        
                        # 1st Quad
                        ref = i+j
                       
                        x_co = []
                        y_co = []
                        for y in range (0,i+1):
                            for x in range (j,8):
                                if x!= j and y!= i:
                                    if (x+y) == ref:
                                        if rev_board[y][x] == '-':
                                            y_co.append(y)
                                            x_co.append(x)
                                        elif rev_board[y][x].islower() == True:
                                            y_co = []
                                            x_co = []
                                            y_co.append(y)
                                            x_co.append(x)
                                            y_co.append(y - 1)
                                            x_co.append(x + 1)
                                        elif rev_board[y][x].isupper() == True:
                                            y_co = []
                                            x_co = []
                        

                        for items in x_co:
                            all_x.append(items)
                        for items in y_co:
                            all_y.append(items)

                        # 2nd Quad
                        
                        ref = i-j
                        x_co = []
                        y_co = []
                        for y in range (0,i+1):
                            for x in range (0,j+1):
                                if (y-x) == ref:
                                    if y != i and x != j:
                                        
                                        if rev_board[y][x] == '-':
                                            y_co.append(y)
                                            x_co.append(x)
                                        elif rev_board[y][x].islower() == True:
                                            y_co = []
                                            x_co = []
                                            y_co.append(y)
                                            x_co.append(x)
                                            y_co.append(y - 1)
                                            x_co.append(x - 1)
                                        elif rev_board[y][x].isupper() == True:
                                            y_co = []
                                            x_co = []
                        for items in x_co:
                            all_x.append(items)
                        for items in y_co:
                            all_y.append(items)   

                        
                    
                        # 3rd Quad
                        
                        ref = i+j
                        check =[]
                        for y in range (i,8):
                            for x in range (0,j+1):
                                if (x+y) == ref:
                                    if x != j and y != i:
                                        if rev_board[y][x] == '-':
                                            
                                            all_x.append(x)
                                            all_y.append(y)    
                                            
                                        elif rev_board[y][x].islower() == True:
                                            
                                            all_x.append(x)
                                            all_y.append(y) 
                                            all_x.append(y + 1)
                                            all_y.append(x - 1)
                                            check.append(1)
                                            break
                                        elif rev_board[y][x].isupper() == True:
                                            check.append(1)
                                            break
                            if (1 in check) == True:
                                break

                            
                        # 4th Quad
                        
                        ref = i-j
                        check =[]
                        for y in range (i,8):
                            for x in range (j,8):
                                if (y-x) == ref:
                                    if x != j and y != i:
                                        if rev_board[y][x] == '-':
                                            
                                            all_x.append(x)
                                            all_y.append(y) 
                                        elif rev_board[y][x].islower() == True:
                                            
                                            all_x.append(x)
                                            all_y.append(y)
                                            all_y.append(y + 1)
                                            all_x.append(x + 1)
                                            check.append(1)
                                            break
                                        elif rev_board[y][x].isupper() == True:
                                            check.append(1)
                                            break
                            if (1 in check) == True:
                                break
                
                for index in range (0,len(all_y)):
                    all_y[index] = 7 - all_y[index]
                    all_x[index] = 7 - all_x[index]

                return all_y, all_x
            
            def ch_whiteWins():
                #Basic Dimensions
                whiteWinner = Tk()
                whiteWinner.geometry('550x600')
                whiteWinner.title('Winner!')
                whiteWinner['bg']='black'

                newMsg = '''
                Congratulations!






                has won the game!
                BY CHECKMATING
                THE
                [Black King]
                '''
                def closeGame():
                    whiteWinner.destroy()
                    chess.destroy()
                            
                Label(whiteWinner,text="We have a winner!", fg="white", font= ("Bernard MT Condensed", 25, 'bold'), bg="#58B11A",  anchor='n',padx=15,pady=5).place(x=130, y=50)
                Label(whiteWinner, text=newMsg, bg="black", fg="white", font= ("Times New Roman",17, 'bold')).place(x=60,y=120)
                Label(whiteWinner, text=" ", bg="green", fg="white", font= ("Times New Roman",25, 'bold'),padx=43,pady=28).place(x = 220,y = 200)
                Label(whiteWinner, text=" ", bg="white", fg="white", font= ("Times New Roman",25, 'bold'),padx=33,pady=18).place(x = 230,y = 210)
                    
                endGame=Button(whiteWinner, text= "Alright", bg= '#58B11A', fg= '#FDEDEC', font= ("Old English Text MT", 22, 'bold'), cursor= 'hand2', command= closeGame, borderwidth= 10).place(x=200, y=480)
            
            def ch_blackWins():
                #Basic Dimensions
                blackWinner = Tk()
                blackWinner.geometry('550x600')
                blackWinner.title('Winner!')
                blackWinner['bg']='#FBF5F5'

                newMsg = '''
                Congratulations!






                has won the game!
                BY CHECKMATING
                THE
                [White King]
                '''
                def closeGame():
                    blackWinner.destroy()
                    chess.destroy()
                            
                Label(blackWinner,text="We have a winner!", fg="black", font= ("Bernard MT Condensed", 25, 'bold'), bg="#58B11A",  anchor='n',padx=15,pady=5).place(x=130, y=50)
                Label(blackWinner, text=newMsg, bg="#FBF5F5", fg="black", font= ("Times New Roman",17, 'bold')).place(x=60,y=120)
                Label(blackWinner, text=" ", bg="green", fg="black", font= ("Times New Roman",25, 'bold'),padx=43,pady=28).place(x = 220,y = 200)
                Label(blackWinner, text=" ", bg="black", fg="black", font= ("Times New Roman",25, 'bold'),padx=33,pady=18).place(x = 230,y = 210)
                    
                endGame=Button(blackWinner, text= "Alright", bg= '#58B11A', fg= '#FDEDEC', font= ("Old English Text MT", 22, 'bold'), cursor= 'hand2', command= closeGame, borderwidth= 10).place(x=200, y=480)

            current_status = get_game_status()

            status = current_status
            

            if (turn % 2 == 0) and (status != 1) :
                
                # White Side
                if piece == "P":
                    update_promotion_piece("P")

                    if i == 1:
                        def promote_bishop():

                            Label(chess,text = "", bg = "black", fg = "white", font = ("Times New Roman",20,"bold"),padx=150,pady=40).place(x=1110,y=10)

                            
                            Label(chess,text = "Selected:", bg = "black", fg = "white", font = ("Times New Roman",20,"bold")).place(x=1160,y=10)
                            Label(chess,text = "White Bishop", bg = "black", fg = "light green", font = ("Times New Roman",20,"bold")).place(x=1130,y=60)

                            update_promotion_piece("B")
                        def promote_knight():

                            Label(chess,text = "", bg = "black", fg = "white", font = ("Times New Roman",20,"bold"),padx=150,pady=40).place(x=1110,y=10)


                            Label(chess,text = "Selected:", bg = "black", fg = "white", font = ("Times New Roman",20,"bold")).place(x=1160,y=10)
                            Label(chess,text = "White Knight", bg = "black", fg = "light green", font = ("Times New Roman",20,"bold")).place(x=1130,y=60)

                            update_promotion_piece("N")
                        def promote_rook():

                            Label(chess,text = "", bg = "black", fg = "white", font = ("Times New Roman",20,"bold"),padx=150,pady=40).place(x=1110,y=10)

                            Label(chess,text = "Selected:", bg = "black", fg = "white", font = ("Times New Roman",20,"bold")).place(x=1160,y=10)
                            Label(chess,text = "White Rook", bg = "black", fg = "light green", font = ("Times New Roman",23,"bold")).place(x=1130,y=60)

                            update_promotion_piece("R")
                        def promote_queen():

                            Label(chess,text = "", bg = "black", fg = "white", font = ("Times New Roman",20,"bold"),padx=150,pady=40).place(x=1110,y=10)

                            Label(chess,text = "Selected:", bg = "black", fg = "white", font = ("Times New Roman",20,"bold")).place(x=1160,y=10)
                            Label(chess,text = "White Queen", bg = "black", fg = "light green", font = ("Times New Roman",23,"bold")).place(x=1120,y=60)

                            update_promotion_piece("Q")
                        
                        bishop = ImageTk.PhotoImage(Image.open("C:\Debbo 12A\Chess\wsq_B.png"))
                        bishopIcon = customtkinter.CTkButton(master = chess, text = "", image = bishop, width = 80, height = 80, compound = "left", command = promote_bishop, fg_color = "#99CCFF", hover_color = "#DAE9F8")
                        bishopIcon.pack(pady=10, padx =10)
                        bishopIcon.place(x = 1170, y = 130)
                                            
                        knight = ImageTk.PhotoImage(Image.open("C:\Debbo 12A\Chess\wsq_N.png"))
                        knightIcon = customtkinter.CTkButton(master = chess, text = "", image = knight, width = 80, height = 80, compound = "left", command = promote_knight, fg_color = "#99CCFF", hover_color = "#DAE9F8")
                        knightIcon.pack(pady=10, padx =10)
                        knightIcon.place(x = 1170, y = 280)
                                                
                        rook = ImageTk.PhotoImage(Image.open("C:\Debbo 12A\Chess\wsq_R.png"))
                        rookIcon = customtkinter.CTkButton(master = chess, text = "", image = rook, width = 80, height = 80, compound = "left", command = promote_rook, fg_color = "#99CCFF", hover_color = "#DAE9F8")
                        rookIcon.pack(pady=10, padx =10)
                        rookIcon.place(x = 1170, y = 430)
                                                
                        queen = ImageTk.PhotoImage(Image.open("C:\Debbo 12A\Chess\wsq_Q.png"))
                        queenIcon = customtkinter.CTkButton(master = chess, text = "", image = queen, width = 80, height = 80, compound = "left", command = promote_queen, fg_color = "#99CCFF", hover_color = "#DAE9F8")
                        queenIcon.pack(pady=10, padx =10)
                        queenIcon.place(x = 1170, y = 580)

                    wP_pos_x=[]
                    wP_pos_y=[]
                    print("White Pawn")
                    # Possibility 1
                    y = i-1
                    x = j-1
                    if y>-1 and x>-1 and (board[y][x].islower()==True):
                        wP_pos_x.append(x)
                        wP_pos_y.append(y)
                        
                    # Possibility 2
                    y = i-1
                    x = j
                    if y>-1 and (board[y][x]=='-'):
                        wP_pos_x.append(x)
                        wP_pos_y.append(y)
                    
                    # Possibility 3
                    y = i-1
                    x = j+1
                    if y>-1 and x<8 and (board[y][x].islower()==True):
                        wP_pos_x.append(x)
                        wP_pos_y.append(y)

                    # Bonus possibility
                    y = 4
                    x = j
                    if i == 6 and board[y][x] == '-' and board[y+1][x] == '-':
                        wP_pos_x.append(x)
                        wP_pos_y.append(y)

                    '''for index in range (0,len(wP_pos_y)):
                        print(wP_pos_y[index],wP_pos_x[index])'''
                    buttonLayout()
                    displayMoves(wP_pos_x,wP_pos_y,"P")
                        
                if piece == "R":
                    print("White Rook")
                    pos_hor=[]
                    pos_ver=[]
                    wR_pos_x=[]
                    wR_pos_y=[]
                    #Horizontal
                    for left_x in range (j-1,-1,-1):
                        if board[i][left_x] == '-':
                            pos_hor.append(left_x)
                        elif board[i][left_x].islower()==True:
                            pos_hor.append(left_x)
                            break
                        else:
                            break
                    for right_x in range (j+1,8):
                        if board[i][right_x] == '-':
                            pos_hor.append(right_x)
                        elif board[i][right_x].islower()==True:
                            pos_hor.append(right_x)
                            break
                        else:
                            break
                    
                    for x in pos_hor:
                        wR_pos_x.append(x)
                        wR_pos_y.append(i)

                    #Vertical
                    for up_y in range (i-1,-1,-1):
                        if board[up_y][j] == '-':
                            pos_ver.append(up_y)
                        elif board[up_y][j].islower()==True:
                            pos_ver.append(up_y)
                            break
                        else:
                            break
                    for down_y in range (i+1,8):
                        if board[down_y][j] == '-':
                            pos_ver.append(down_y)
                        elif board[down_y][j].islower()==True:
                            pos_ver.append(down_y)
                            break
                        else:
                            break
                    
                    for y in pos_ver:
                        wR_pos_x.append(j)
                        wR_pos_y.append(y)
                    
                    '''for index in range (0,len(wR_pos_y)):
                        print(wR_pos_y[index],wR_pos_x[index])'''
                    buttonLayout()
                    displayMoves(wR_pos_x,wR_pos_y,"R")
                        
                if piece == "N":
                    print("White horse")
                    
                    wN_pos_x=[]
                    wN_pos_y=[]
                    #Possibility 1
                    y = i-2
                    x = j+1
                    if x<8 and y>-1 and (board[y][x].isupper()==False):
                        wN_pos_x.append(x)
                        wN_pos_y.append(y) 

                    # possibility 2
                    x = j+2
                    y = i-1
                    if x<8 and y>-1  and (board[y][x].isupper()==False):
                        wN_pos_x.append(x)
                        wN_pos_y.append(y) 

                    # possibility 3
                    x = j+2
                    y = i+1
                    if x<8 and y<8 and (board[y][x].isupper()==False):
                        wN_pos_x.append(x)
                        wN_pos_y.append(y)  

                    # possibility 4
                    x = j+1
                    y = i+2
                    if x<8 and y<8 and (board[y][x].isupper()==False):
                        wN_pos_x.append(x)
                        wN_pos_y.append(y) 

                    # possibility 5
                    x = j-1
                    y = i+2
                    if x>-1 and y<8 and (board[y][x].isupper()==False):
                        wN_pos_x.append(x)
                        wN_pos_y.append(y)  

                    # possibility 6
                    x = j-2
                    y = i+1
                    if x>-1 and y<8 and (board[y][x].isupper()==False):
                        wN_pos_x.append(x)
                        wN_pos_y.append(y) 

                    # possibility 7
                    x = j-2
                    y = i-1
                    if x>-1 and y>-1 and (board[y][x].isupper()==False):
                        wN_pos_x.append(x)
                        wN_pos_y.append(y) 
                    
                    # possibility 8
                    x = j-1
                    y = i-2
                    if x>-1 and y>-1:
                        wN_pos_x.append(x)
                        wN_pos_y.append(y) 
                    
                    '''for index in range (0,len(wN_pos_y)):
                        print(wN_pos_y[index],wN_pos_x[index])'''
                    buttonLayout()
                    displayMoves(wN_pos_x,wN_pos_y,"N")

                if piece == "B":
                    print("WHite Bishop")
                    # 1st Quad
                    
                    ref = i+j
                    
                    wB_pos_x = []
                    wB_pos_y = []

                    x_co = []
                    y_co = []
                    for y in range (0,i+1):
                        for x in range (j,8):
                            if x!= j and y!= i:
                                if (x+y) == ref:
                                    if board[y][x] == '-':
                                        y_co.append(y)
                                        x_co.append(x)
                                    elif board[y][x].islower() == True:
                                        y_co = []
                                        x_co = []
                                        y_co.append(y)
                                        x_co.append(x)
                                    elif board[y][x].isupper() == True:
                                        y_co = []
                                        x_co = []

                    for items in x_co:
                        wB_pos_x.append(items)
                    for items in y_co:
                        wB_pos_y.append(items)                      
                    
                        
                    # 2nd Quad
                    
                    ref = i-j
                    x_co = []
                    y_co = []
                    for y in range (0,i+1):
                        for x in range (0,j+1):
                            if (y-x) == ref:
                                if y != i and x != j:
                                    
                                    if board[y][x] == '-':
                                        y_co.append(y)
                                        x_co.append(x)
                                    elif board[y][x].islower() == True:
                                        y_co = []
                                        x_co = []
                                        y_co.append(y)
                                        x_co.append(x)
                                    elif board[y][x].isupper() == True:
                                        y_co = []
                                        x_co = []
                    for items in x_co:
                        wB_pos_x.append(items)
                    for items in y_co:
                        wB_pos_y.append(items)    
                
                    # 3rd Quad
                    
                    ref = i+j
                    check =[]
                    for y in range (i,8):
                        for x in range (0,j+1):
                            if (x+y) == ref:
                                if x != j and y != i:
                                    if board[y][x] == '-':
                                        
                                        wB_pos_x.append(x)
                                        wB_pos_y.append(y)    
                                    elif board[y][x].islower() == True:
                                        
                                        wB_pos_x.append(x)
                                        wB_pos_y.append(y) 
                                        check.append(1)
                                        break
                                    elif board[y][x].isupper() == True:
                                        check.append(1)
                                        break
                        if (1 in check) == True:
                            break
                    # 4th Quad
                    
                    ref = i-j
                    check =[]
                    for y in range (i,8):
                        for x in range (j,8):
                            if (y-x) == ref:
                                if x != j and y != i:
                                    if board[y][x] == '-':
                                        
                                        wB_pos_x.append(x)
                                        wB_pos_y.append(y) 
                                    elif board[y][x].islower() == True:
                                        
                                        wB_pos_x.append(x)
                                        wB_pos_y.append(y) 
                                        check.append(1)
                                        break
                                    elif board[y][x].isupper() == True:
                                        check.append(1)
                                        break
                        if (1 in check) == True:
                            break
                
                    '''for index in range (0,len(wB_pos_y)):
                        print(wB_pos_y[index],wB_pos_x[index])'''
                    buttonLayout()
                    displayMoves(wB_pos_x,wB_pos_y,"B")

                if piece == "Q":
                    print("White Queen")
                    pos_hor=[]
                    pos_ver=[]
                    wQ_pos_x=[]
                    wQ_pos_y=[]
                    #Horizontal
                    for left_x in range (j-1,-1,-1):
                        if board[i][left_x] == '-':
                            pos_hor.append(left_x)
                        elif board[i][left_x].islower()==True:
                            pos_hor.append(left_x)
                            break
                        else:
                            break
                    for right_x in range (j+1,8):
                        if board[i][right_x] == '-':
                            pos_hor.append(right_x)
                        elif board[i][right_x].islower()==True:
                            pos_hor.append(right_x)
                            break
                        else:
                            break
                    
                    for x in pos_hor:
                        wQ_pos_x.append(x)
                        wQ_pos_y.append(i)

                    #Vertical
                    for up_y in range (i-1,-1,-1):
                        if board[up_y][j] == '-':
                            pos_ver.append(up_y)
                        elif board[up_y][j].islower()==True:
                            pos_ver.append(up_y)
                            break
                        else:
                            break
                    for down_y in range (i+1,8):
                        if board[down_y][j] == '-':
                            pos_ver.append(down_y)
                        elif board[down_y][j].islower()==True:
                            pos_ver.append(down_y)
                            break
                        else:
                            break
                    
                    for y in pos_ver:
                        wQ_pos_x.append(j)
                        wQ_pos_y.append(y)
                    
                    
                    # 1st Quad
                    
                    ref = i+j
                    
                    
                    x_co = []
                    y_co = []
                    for y in range (0,i+1):
                        for x in range (j,8):
                            if x!= j and y!= i:
                                if (x+y) == ref:
                                    if board[y][x] == '-':
                                        y_co.append(y)
                                        x_co.append(x)
                                    elif board[y][x].islower() == True:
                                        y_co = []
                                        x_co = []
                                        y_co.append(y)
                                        x_co.append(x)
                                    elif board[y][x].isupper() == True:
                                        y_co = []
                                        x_co = []

                    for items in x_co:
                        wQ_pos_x.append(items)
                    for items in y_co:
                        wQ_pos_y.append(items)                      
                        
                        
                    # 2nd Quad
                    
                    ref = i-j
                    x_co = []
                    y_co = []
                    for y in range (0,i+1):
                        for x in range (0,j+1):
                            if (y-x) == ref:
                                if y != i and x != j:
                                    
                                    if board[y][x] == '-':
                                        y_co.append(y)
                                        x_co.append(x)
                                    elif board[y][x].islower() == True:
                                        y_co = []
                                        x_co = []
                                        y_co.append(y)
                                        x_co.append(x)
                                    elif board[y][x].isupper() == True:
                                        y_co = []
                                        x_co = []
                    for items in x_co:
                        wQ_pos_x.append(items)
                    for items in y_co:
                        wQ_pos_y.append(items)    
                    
                    # 3rd Quad
                    
                    ref = i+j
                    check =[]
                    for y in range (i,8):
                        for x in range (0,j+1):
                            if (x+y) == ref:
                                if x != j and y != i:
                                    if board[y][x] == '-':
                                        
                                        wQ_pos_x.append(x)
                                        wQ_pos_y.append(y)    
                                    elif board[y][x].islower() == True:
                                        
                                        wQ_pos_x.append(x)
                                        wQ_pos_y.append(y) 
                                        check.append(1)
                                        break
                                    elif board[y][x].isupper() == True:
                                        check.append(1)
                                        break
                        if (1 in check) == True:
                            break
                    # 4th Quad
                    
                    ref = i-j
                    check =[]
                    for y in range (i,8):
                        for x in range (j,8):
                            if (y-x) == ref:
                                if x != j and y != i:
                                    if board[y][x] == '-':
                                        
                                        wQ_pos_x.append(x)
                                        wQ_pos_y.append(y) 
                                    elif board[y][x].islower() == True:
                                        
                                        wQ_pos_x.append(x)
                                        wQ_pos_y.append(y) 
                                        check.append(1)
                                        break
                                    elif board[y][x].isupper() == True:
                                        check.append(1)
                                        break
                        if (1 in check) == True:
                            break
                
                    '''for index in range (0,len(wQ_pos_y)):
                        print(wQ_pos_y[index],wQ_pos_x[index])'''
                    buttonLayout()
                    displayMoves(wQ_pos_x,wQ_pos_y,"Q")

                if piece == "K":
                    print("White King")

                    wK_pos_x=[]
                    wK_pos_y=[]
                    # Possibility 1
                    y = i-1
                    x = j
                    if y>-1 and (board[y][x].isupper()==False):
                        
                        wK_pos_x.append(x)
                        wK_pos_y.append(y)

                    # Possibility 2
                    y = i-1
                    x = j+1
                    if y>-1 and x<8 and (board[y][x].isupper()==False):
                        
                        wK_pos_x.append(x)
                        wK_pos_y.append(y)

                    # Possibility 3
                    y = i
                    x = j+1
                    if x<8 and (board[y][x].isupper()==False):
                        
                        wK_pos_x.append(x)
                        wK_pos_y.append(y)

                    # Possibility 4
                    y = i+1
                    x = j+1
                    if y<8 and x<8 and (board[y][x].isupper()==False):
                        
                        wK_pos_x.append(x)
                        wK_pos_y.append(y)

                    # Possibility 5
                    y = i+1
                    x = j
                    if y<8 and (board[y][x].isupper()==False):
                    
                        wK_pos_x.append(x)
                        wK_pos_y.append(y)

                    # Possibility 6
                    y = i+1
                    x = j-1
                    if x>-1 and y<8 and (board[y][x].isupper()==False):
                        
                        wK_pos_x.append(x)
                        wK_pos_y.append(y)

                    # Possibility 7
                    y = i
                    x = j-1
                    if x>-1 and (board[y][x].isupper()==False):
                        
                        wK_pos_x.append(x)
                        wK_pos_y.append(y)

                    # Possibility 8
                    y = i-1
                    x = j-1
                    if y>-1 and x>-1 and (board[y][x].isupper()==False):
                        
                        wK_pos_x.append(x)
                        wK_pos_y.append(y)

                    check = []
                    if len(wK_pos_y) == 0:
                        check.append(1)
                    
                    all_y,all_x = checkDangerPos(1)
                    
                    #print(all_y,all_x)
                    #print("---")
                    #print(wK_pos_y,wK_pos_x)

                    for index_1 in range (len(all_y)):
                        for index_2 in range (len(wK_pos_y)):
                            if wK_pos_y[index_2] == all_y[index_1]:
                                if wK_pos_x[index_2] == all_x[index_1]:
                                    wK_pos_y[index_2] = " "
                                    wK_pos_x[index_2] = " "
                    while wK_pos_y.count(" ")>0:
                        wK_pos_y.remove(" ")
                        wK_pos_x.remove(" ")
                    
                    #print(1 in check)
                    #print( len(wK_pos_y))

                    if (1 in check) == False:
                        if len(wK_pos_y) == 0:
                            print("Checkmate; Win for Black")
                            ch_blackWins()

                            update_game_status_1()
                    #print(wK_pos_y)
                    #print(wK_pos_x)

                    '''for index in range (0,len(wK_pos_y)):
                        print(wK_pos_y[index],wK_pos_x[index])'''
                    buttonLayout()
                    displayMoves(wK_pos_x,wK_pos_y,"K")
                    
            
            if (turn % 2 != 0) and (status != 1):
                
                # Black Side               
                if piece == "p":
                    print("Black Pawn")

                    update_promotion_piece("p")

                    if i == 1:
                        def promote_bishop():

                            Label(chess,text = "", bg = "black", fg = "white", font = ("Times New Roman",20,"bold"),padx=150,pady=40).place(x=1110,y=10)

                            Label(chess,text = "Selected:", bg = "black", fg = "white", font = ("Times New Roman",20,"bold")).place(x=1160,y=10)
                            Label(chess,text = "Black Bishop", bg = "black", fg = "light blue", font = ("Times New Roman",20,"bold")).place(x=1130,y=60)

                            update_promotion_piece("b")
                        def promote_knight():

                            Label(chess,text = "", bg = "black", fg = "white", font = ("Times New Roman",20,"bold"),padx=150,pady=40).place(x=1110,y=10)

                            Label(chess,text = "Selected:", bg = "black", fg = "white", font = ("Times New Roman",20,"bold")).place(x=1160,y=10)
                            Label(chess,text = "Black Knight", bg = "black", fg = "light blue", font = ("Times New Roman",20,"bold")).place(x=1130,y=60)

                            update_promotion_piece("n")
                        def promote_rook():

                            Label(chess,text = "", bg = "black", fg = "white", font = ("Times New Roman",20,"bold"),padx=150,pady=40).place(x=1110,y=10)

                            Label(chess,text = "Selected:", bg = "black", fg = "white", font = ("Times New Roman",20,"bold")).place(x=1160,y=10)
                            Label(chess,text = "Black Rook", bg = "black", fg = "light blue", font = ("Times New Roman",23,"bold")).place(x=1130,y=60)

                            update_promotion_piece("r")
                        def promote_queen():

                            Label(chess,text = "", bg = "black", fg = "white", font = ("Times New Roman",20,"bold"),padx=150,pady=40).place(x=1110,y=10)

                            Label(chess,text = "Selected:", bg = "black", fg = "white", font = ("Times New Roman",20,"bold")).place(x=1160,y=10)
                            Label(chess,text = "Black Queen", bg = "black", fg = "light blue", font = ("Times New Roman",23,"bold")).place(x=1120,y=60)

                            update_promotion_piece("q")
                        
                        bishop = ImageTk.PhotoImage(Image.open("C:\Debbo 12A\Chess\dark_sq_b.png"))
                        bishopIcon = customtkinter.CTkButton(master = chess, text = "", image = bishop, width = 80, height = 80, compound = "left", command = promote_bishop, fg_color = "#006599", hover_color = "#DAE9F8")
                        bishopIcon.pack(pady=10, padx =10)
                        bishopIcon.place(x = 1170, y = 130)
                                            
                        knight = ImageTk.PhotoImage(Image.open("C:\Debbo 12A\Chess\dark_sq_n.png"))
                        knightIcon = customtkinter.CTkButton(master = chess, text = "", image = knight, width = 80, height = 80, compound = "left", command = promote_knight, fg_color = "#006599", hover_color = "#DAE9F8")
                        knightIcon.pack(pady=10, padx =10)
                        knightIcon.place(x = 1170, y = 280)
                                                
                        rook = ImageTk.PhotoImage(Image.open("C:\Debbo 12A\Chess\dark_sq_r.png"))
                        rookIcon = customtkinter.CTkButton(master = chess, text = "", image = rook, width = 80, height = 80, compound = "left", command = promote_rook, fg_color = "#006599", hover_color = "#DAE9F8")
                        rookIcon.pack(pady=10, padx =10)
                        rookIcon.place(x = 1170, y = 430)
                                                
                        queen = ImageTk.PhotoImage(Image.open("C:\Debbo 12A\Chess\dark_sq_q.png"))
                        queenIcon = customtkinter.CTkButton(master = chess, text = "", image = queen, width = 80, height = 80, compound = "left", command = promote_queen, fg_color = "#006599", hover_color = "#DAE9F8")
                        queenIcon.pack(pady=10, padx =10)
                        queenIcon.place(x = 1170, y = 580)

                    dP_pos_x=[]
                    dP_pos_y=[]
                    print("White Pawn")
                    # Possibility 1
                    y = i-1
                    x = j-1
                    if y>-1 and x>-1 and (board[y][x].isupper()==True):
                        dP_pos_x.append(x)
                        dP_pos_y.append(y)
                        
                    # Possibility 2
                    y = i-1
                    x = j
                    if y>-1 and (board[y][x]=='-'):
                        dP_pos_x.append(x)
                        dP_pos_y.append(y)
                    
                    # Possibility 3
                    y = i-1
                    x = j+1
                    if y>-1 and x<8 and (board[y][x].isupper()==True):
                        dP_pos_x.append(x)
                        dP_pos_y.append(y)
                    # Bonus possibility
                    y = 4
                    x = j
                    if i == 6 and board[y][x] == '-' and board[y+1][x] == '-':
                        dP_pos_x.append(x)
                        dP_pos_y.append(y)
                    '''for index in range (0,len(dP_pos_y)):
                        print(dP_pos_y[index],dP_pos_x[index])'''
                    buttonLayout()
                    displayMoves(dP_pos_x,dP_pos_y,"p")

                if piece == "r":
                    print("Black Rook")
                    pos_hor=[]
                    pos_ver=[]
                    dR_pos_x=[]
                    dR_pos_y=[]
                    #Horizontal
                    for left_x in range (j-1,-1,-1):
                        if board[i][left_x] == '-':
                            pos_hor.append(left_x)
                        elif board[i][left_x].isupper()==True:
                            pos_hor.append(left_x)
                            break
                        else:
                            break
                    for right_x in range (j+1,8):
                        if board[i][right_x] == '-':
                            pos_hor.append(right_x)
                        elif board[i][right_x].isupper()==True:
                            pos_hor.append(right_x)
                            break
                        else:
                            break
                    
                    for x in pos_hor:
                        dR_pos_x.append(x)
                        dR_pos_y.append(i)

                    #Vertical
                    for up_y in range (i-1,-1,-1):
                        if board[up_y][j] == '-':
                            pos_ver.append(up_y)
                        elif board[up_y][j].isupper()==True:
                            pos_ver.append(up_y)
                            break
                        else:
                            break
                    for down_y in range (i+1,8):
                        if board[down_y][j] == '-':
                            pos_ver.append(down_y)
                        elif board[down_y][j].isupper()==True:
                            pos_ver.append(down_y)
                            break
                        else:
                            break
                    
                    for y in pos_ver:
                        dR_pos_x.append(j)
                        dR_pos_y.append(y)
                    
                    '''for index in range (0,len(dR_pos_y)):
                        print(dR_pos_y[index],dR_pos_x[index])'''
                    buttonLayout()
                    displayMoves(dR_pos_x,dR_pos_y,"r")
                
                if piece == "n":
                    print("Black horse")

                    dN_pos_x=[]
                    dN_pos_y=[]
                    #Possibility 1
                    y = i-2
                    x = j+1
                    if x<8 and y>-1 and (board[y][x].islower()==False):
                        dN_pos_x.append(x)
                        dN_pos_y.append(y) 

                    # possibility 2
                    x = j+2
                    y = i-1
                    if x<8 and y>-1  and (board[y][x].islower()==False):
                        dN_pos_x.append(x)
                        dN_pos_y.append(y) 

                    # possibility 3
                    x = j+2
                    y = i+1
                    if x<8 and y<8 and (board[y][x].islower()==False):
                        dN_pos_x.append(x)
                        dN_pos_y.append(y)  

                    # possibility 4
                    x = j+1
                    y = i+2
                    if x<8 and y<8 and (board[y][x].islower()==False):
                        dN_pos_x.append(x)
                        dN_pos_y.append(y) 

                    # possibility 5
                    x = j-1
                    y = i+2
                    if x>-1 and y<8 and (board[y][x].islower()==False):
                        dN_pos_x.append(x)
                        dN_pos_y.append(y)  

                    # possibility 6
                    x = j-2
                    y = i+1
                    if x>-1 and y<8 and (board[y][x].islower()==False):
                        dN_pos_x.append(x)
                        dN_pos_y.append(y) 

                    # possibility 7
                    x = j-2
                    y = i-1
                    if x>-1 and y>-1 and (board[y][x].islower()==False):
                        dN_pos_x.append(x)
                        dN_pos_y.append(y) 
                    
                    # possibility 8
                    x = j-1
                    y = i-2
                    if x>-1 and y>-1:
                        dN_pos_x.append(x)
                        dN_pos_y.append(y) 
                    
                    '''for index in range (0,len(dN_pos_y)):
                        print(dN_pos_y[index],dN_pos_x[index])'''
                    buttonLayout()
                    displayMoves(dN_pos_x,dN_pos_y,"n")
                
                if piece == "b":
                    print("Black Bishop")

                    # 1st Quad
                    
                    ref = i+j
                    
                    dB_pos_x = []
                    dB_pos_y = []

                    x_co = []
                    y_co = []
                    for y in range (0,i+1):
                        for x in range (j,8):
                            if x!= j and y!= i:
                                if (x+y) == ref:
                                    if board[y][x] == '-':
                                        y_co.append(y)
                                        x_co.append(x)
                                    elif board[y][x].isupper() == True:
                                        y_co = []
                                        x_co = []
                                        y_co.append(y)
                                        x_co.append(x)
                                    elif board[y][x].islower() == True:
                                        y_co = []
                                        x_co = []

                    for items in x_co:
                        dB_pos_x.append(items)
                    for items in y_co:
                        dB_pos_y.append(items)                      
                    
                        
                    # 2nd Quad
                    
                    ref = i-j
                    x_co = []
                    y_co = []
                    for y in range (0,i+1):
                        for x in range (0,j+1):
                            if (y-x) == ref:
                                if y != i and x != j:
                                    
                                    if board[y][x] == '-':
                                        y_co.append(y)
                                        x_co.append(x)
                                    elif board[y][x].isupper() == True:
                                        y_co = []
                                        x_co = []
                                        y_co.append(y)
                                        x_co.append(x)
                                    elif board[y][x].islower() == True:
                                        y_co = []
                                        x_co = []
                    for items in x_co:
                        dB_pos_x.append(items)
                    for items in y_co:
                        dB_pos_y.append(items)    
                
                    # 3rd Quad
                    
                    ref = i+j
                    check =[]
                    for y in range (i,8):
                        for x in range (0,j+1):
                            if (x+y) == ref:
                                if x != j and y != i:
                                    if board[y][x] == '-':
                                        
                                        dB_pos_x.append(x)
                                        dB_pos_y.append(y)    
                                    elif board[y][x].isupper() == True:
                                        
                                        dB_pos_x.append(x)
                                        dB_pos_y.append(y) 
                                        check.append(1)
                                        break
                                    elif board[y][x].islower() == True:
                                        check.append(1)
                                        break
                        if (1 in check) == True:
                            break
                    # 4th Quad
                    
                    ref = i-j
                    check =[]
                    for y in range (i,8):
                        for x in range (j,8):
                            if (y-x) == ref:
                                if x != j and y != i:
                                    if board[y][x] == '-':
                                        
                                        dB_pos_x.append(x)
                                        dB_pos_y.append(y) 
                                    elif board[y][x].isupper() == True:
                                        
                                        dB_pos_x.append(x)
                                        dB_pos_y.append(y) 
                                        check.append(1)
                                        break
                                    elif board[y][x].islower() == True:
                                        check.append(1)
                                        break
                        if (1 in check) == True:
                            break
                
                    '''for index in range (0,len(dB_pos_y)):
                        print(dB_pos_y[index],dB_pos_x[index])'''
                    buttonLayout()
                    displayMoves(dB_pos_x,dB_pos_y,"b")
                
                if piece == "q":
                    print("Black Queen")
                    pos_hor=[]
                    pos_ver=[]
                    dQ_pos_x=[]
                    dQ_pos_y=[]
                    #Horizontal
                    for left_x in range (j-1,-1,-1):
                        if board[i][left_x] == '-':
                            pos_hor.append(left_x)
                        elif board[i][left_x].isupper()==True:
                            pos_hor.append(left_x)
                            break
                        else:
                            break
                    for right_x in range (j+1,8):
                        if board[i][right_x] == '-':
                            pos_hor.append(right_x)
                        elif board[i][right_x].isupper()==True:
                            pos_hor.append(right_x)
                            break
                        else:
                            break
                    
                    for x in pos_hor:
                        dQ_pos_x.append(x)
                        dQ_pos_y.append(i)

                    #Vertical
                    for up_y in range (i-1,-1,-1):
                        if board[up_y][j] == '-':
                            pos_ver.append(up_y)
                        elif board[up_y][j].isupper()==True:
                            pos_ver.append(up_y)
                            break
                        else:
                            break
                    for down_y in range (i+1,8):
                        if board[down_y][j] == '-':
                            pos_ver.append(down_y)
                        elif board[down_y][j].isupper()==True:
                            pos_ver.append(down_y)
                            break
                        else:
                            break
                    
                    for y in pos_ver:
                        dQ_pos_x.append(j)
                        dQ_pos_y.append(y)
                    
                    
                    # 1st Quad
                    
                    ref = i+j
                    
                    
                    x_co = []
                    y_co = []
                    for y in range (0,i+1):
                        for x in range (j,8):
                            if x!= j and y!= i:
                                if (x+y) == ref:
                                    if board[y][x] == '-':
                                        y_co.append(y)
                                        x_co.append(x)
                                    elif board[y][x].isupper() == True:
                                        y_co = []
                                        x_co = []
                                        y_co.append(y)
                                        x_co.append(x)
                                    elif board[y][x].islower() == True:
                                        y_co = []
                                        x_co = []

                    for items in x_co:
                        dQ_pos_x.append(items)
                    for items in y_co:
                        dQ_pos_y.append(items)                      
                        
                        
                    # 2nd Quad
                    
                    ref = i-j
                    x_co = []
                    y_co = []
                    for y in range (0,i+1):
                        for x in range (0,j+1):
                            if (y-x) == ref:
                                if y != i and x != j:
                                    
                                    if board[y][x] == '-':
                                        y_co.append(y)
                                        x_co.append(x)
                                    elif board[y][x].isupper() == True:
                                        y_co = []
                                        x_co = []
                                        y_co.append(y)
                                        x_co.append(x)
                                    elif board[y][x].islower() == True:
                                        y_co = []
                                        x_co = []
                    for items in x_co:
                        dQ_pos_x.append(items)
                    for items in y_co:
                        dQ_pos_y.append(items)    
                    
                    # 3rd Quad
                    
                    ref = i+j
                    check =[]
                    for y in range (i,8):
                        for x in range (0,j+1):
                            if (x+y) == ref:
                                if x != j and y != i:
                                    if board[y][x] == '-':
                                        
                                        dQ_pos_x.append(x)
                                        dQ_pos_y.append(y)    
                                    elif board[y][x].isupper() == True:
                                        
                                        dQ_pos_x.append(x)
                                        dQ_pos_y.append(y) 
                                        check.append(1)
                                        break
                                    elif board[y][x].islower() == True:
                                        check.append(1)
                                        break
                        if (1 in check) == True:
                            break
                    # 4th Quad
                    
                    ref = i-j
                    check =[]
                    for y in range (i,8):
                        for x in range (j,8):
                            if (y-x) == ref:
                                if x != j and y != i:
                                    if board[y][x] == '-':
                                        
                                        dQ_pos_x.append(x)
                                        dQ_pos_y.append(y) 
                                    elif board[y][x].isupper() == True:
                                        
                                        dQ_pos_x.append(x)
                                        dQ_pos_y.append(y) 
                                        check.append(1)
                                        break
                                    elif board[y][x].islower() == True:
                                        check.append(1)
                                        break
                        if (1 in check) == True:
                            break
                
                    '''for index in range (0,len(dQ_pos_y)):
                        print(dQ_pos_y[index],dQ_pos_x[index])'''
                    buttonLayout()
                    displayMoves(dQ_pos_x,dQ_pos_y,"q")
                
                if piece == "k":
                    print("Black King")

                    dK_pos_x=[]
                    dK_pos_y=[]
                    # Possibility 1
                    y = i-1
                    x = j
                    if y>-1 and (board[y][x].islower()==False):
                        
                        dK_pos_x.append(x)
                        dK_pos_y.append(y)

                    # Possibility 2
                    y = i-1
                    x = j+1
                    if y>-1 and x<8 and (board[y][x].islower()==False):
                        
                        dK_pos_x.append(x)
                        dK_pos_y.append(y)

                    # Possibility 3
                    y = i
                    x = j+1
                    if x<8 and (board[y][x].islower()==False):
                        
                        dK_pos_x.append(x)
                        dK_pos_y.append(y)

                    # Possibility 4
                    y = i+1
                    x = j+1
                    if y<8 and x<8 and (board[y][x].islower()==False):
                        
                        dK_pos_x.append(x)
                        dK_pos_y.append(y)

                    # Possibility 5
                    y = i+1
                    x = j
                    if y<8 and (board[y][x].islower()==False):
                    
                        dK_pos_x.append(x)
                        dK_pos_y.append(y)

                    # Possibility 6
                    y = i+1
                    x = j-1
                    if x>-1 and y<8 and (board[y][x].islower()==False):
                        
                        dK_pos_x.append(x)
                        dK_pos_y.append(y)

                    # Possibility 7
                    y = i
                    x = j-1
                    if x>-1 and (board[y][x].islower()==False):
                        
                        dK_pos_x.append(x)
                        dK_pos_y.append(y)

                    # Possibility 8
                    y = i-1
                    x = j-1
                    if y>-1 and x>-1 and (board[y][x].islower()==False):
                        
                        dK_pos_x.append(x)
                        dK_pos_y.append(y)
                    
                    check = []
                    if len(dK_pos_y) == 0:
                        check.append(1)
                    
                    all_y,all_x = checkDangerPos(2)
                    
                    #print(all_y,all_x)
                    #print("---")
                    #print(wK_pos_y,wK_pos_x)

                    for index_1 in range (len(all_y)):
                        for index_2 in range (len(dK_pos_y)):
                            if dK_pos_y[index_2] == all_y[index_1]:
                                if dK_pos_x[index_2] == all_x[index_1]:
                                    dK_pos_y[index_2] = " "
                                    dK_pos_x[index_2] = " "
                    while dK_pos_y.count(" ")>0:
                        dK_pos_y.remove(" ")
                        dK_pos_x.remove(" ")
                    
                    #print(dK_pos_y)
                    #print(dK_pos_x)

                    if (1 in check) == False:
                        if len(dK_pos_y) == 0:
                            print("Checkmate; Win for White")
                            ch_whiteWins()

                            update_game_status_1()
                    
                    '''for index in range (0,len(dK_pos_y)):
                        print(dK_pos_y[index],dK_pos_x[index])'''
                    buttonLayout()
                    displayMoves(dK_pos_x,dK_pos_y,"k")
                 

        def display_complete_board():
            def column1():
                # Column 1
                j=0

                i=0
                def movePiece():
                    i=0
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=1
                def movePiece():
                    i=1
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=2
                def movePiece():
                    i=2
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=3
                def movePiece():
                    i=3
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=4
                def movePiece():
                    i=4
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=5
                def movePiece():
                    i=5
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=6
                def movePiece():
                    i=6
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=7
                def movePiece():
                    i=7
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)
                
            def column2():
                # Column 2
                j=1

                i=0
                def movePiece():
                    i=0
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=1
                def movePiece():
                    i=1
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=2
                def movePiece():
                    i=2
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=3
                def movePiece():
                    i=3
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=4
                def movePiece():
                    i=4
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=5
                def movePiece():
                    i=5
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=6
                def movePiece():
                    i=6
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=7
                def movePiece():
                    i=7
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)
            
            def column3():
                # Column 3
                j=2

                i=0
                def movePiece():
                    i=0
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=1
                def movePiece():
                    i=1
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=2
                def movePiece():
                    i=2
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=3
                def movePiece():
                    i=3
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=4
                def movePiece():
                    i=4
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=5
                def movePiece():
                    i=5
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=6
                def movePiece():
                    i=6
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=7
                def movePiece():
                    i=7
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)
            
            def column4():
                # Column 4
                j=3

                i=0
                def movePiece():
                    i=0
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=1
                def movePiece():
                    i=1
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=2
                def movePiece():
                    i=2
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=3
                def movePiece():
                    i=3
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=4
                def movePiece():
                    i=4
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=5
                def movePiece():
                    i=5
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=6
                def movePiece():
                    i=6
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=7
                def movePiece():
                    i=7
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)
            
            def column5():
                # Column 5
                j=4

                i=0
                def movePiece():
                    i=0
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=1
                def movePiece():
                    i=1
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=2
                def movePiece():
                    i=2
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=3
                def movePiece():
                    i=3
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=4
                def movePiece():
                    i=4
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=5
                def movePiece():
                    i=5
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=6
                def movePiece():
                    i=6
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=7
                def movePiece():
                    i=7
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)
            
            def column6():
                # Column 6
                j=5

                i=0
                def movePiece():
                    i=0
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=1
                def movePiece():
                    i=1
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=2
                def movePiece():
                    i=2
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=3
                def movePiece():
                    i=3
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=4
                def movePiece():
                    i=4
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=5
                def movePiece():
                    i=5
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=6
                def movePiece():
                    i=6
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=7
                def movePiece():
                    i=7
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)
            
            def column7():
                # Column 7
                j=6

                i=0
                def movePiece():
                    i=0
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=1
                def movePiece():
                    i=1
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=2
                def movePiece():
                    i=2
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=3
                def movePiece():
                    i=3
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=4
                def movePiece():
                    i=4
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=5
                def movePiece():
                    i=5
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=6
                def movePiece():
                    i=6
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=7
                def movePiece():
                    i=7
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)
                
            def column8():
                # Column 8
                j=7

                i=0
                def movePiece():
                    i=0
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=1
                def movePiece():
                    i=1
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=2
                def movePiece():
                    i=2
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=3
                def movePiece():
                    i=3
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=4
                def movePiece():
                    i=4
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=5
                def movePiece():
                    i=5
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=6
                def movePiece():
                    i=6
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)

                i=7
                def movePiece():
                    i=7
                    print(i,j)
                    print("---")
                    possibleMoves(i,j)
                sqColour = decideSquareColour(i,j)
                x_co = xCo(j)
                y_co = yCo(i)-50

                imageInfo = decideSquareImage(i,j)
                image_00 = ImageTk.PhotoImage(Image.open(imageInfo))
                sq_00 = customtkinter.CTkButton(master = chess, text = "", image = image_00, width = 80, height = 80, compound = "left", command = movePiece, fg_color = sqColour, hover_color = "#DAE9F8")
                sq_00.pack(pady=10, padx =10)
                sq_00.place(x = x_co, y = y_co)
            column1()
            column2()
            column3()
            column4()
            column5()
            column6()
            column7()
            column8()
        display_complete_board()
    buttonLayout()

boardGUI()

chess.mainloop()
