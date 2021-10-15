# This game contains the state of the chess game and it is responsible to determine the valid moves at the current state. It will also keep a move log.

import numpy as np

class GameState():

    def __init__(self):

        # Board is an 8x8 two dimensional list. First character represents the color of the piece (black or white), while the second one represents the type of the piece (pawn, rook, knight, 
        # bishop, queen and king).

        # Remember to add castling rights and enpassant
        self.board = [

            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.WhiteToMove = True
        self.MoveLog = []
        self.WhitePiecesCaptured = []
        self.BlackPiecesCaptured = []
        self.CurrentMove = 0
        

    def makeMove(self, move):
        if move.isMoveLegal:

            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = move.pieceMoved
            self.MoveLog.append(move)
            
            self.WhiteToMove = not self.WhiteToMove
            self.CurrentMove += 1
            print(self.CurrentMove)

    def goBackMove(self):

        if self.CurrentMove > 0:

            BackMove = self.MoveLog[self.CurrentMove - 1]
            self.board[BackMove.endRow][BackMove.endCol] = BackMove.pieceCaptured
            self.board[BackMove.startRow][BackMove.startCol] = BackMove.pieceMoved

            self.WhiteToMove = not self.WhiteToMove
            self.CurrentMove -= 1


    def goForwardMove(self):
        pass

class Move:

    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v : k for  k, v in ranksToRows.items()}

    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board, WhiteToMove):

        self.isMoveLegal = True
        self.WhiteToMove = WhiteToMove
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]



        self.pieceMoved = board[self.startRow][self.startCol] 

        # Check if it's white turn to move

        if (self.pieceMoved[0] == "w" and self.WhiteToMove) or (self.pieceMoved[0] == "b" and (not self.WhiteToMove)):

            self.isMoveLegal = True

        else:

            self.isMoveLegal = False



        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        # make this real chess notation
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
    
    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]












