import numpy as np
import pygame
import sys
import math

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board(): #     6          7
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return board

def is_valid_location(board, col):
	return board[ROW_COUNT-1][col] == 0
def get_next_open_row(board, col):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r

def drop_piece(board, row, col, piece):
	board[row][col] = piece
def minimax(board, depth, maximizing_player):
	valid_locations = get_valid_locations(board)
	terminal = is_terminal_node(board)

	if depth == 0 or terminal:
		if terminal:
			if winning_move(board, 2):
				return (None, 10000000)
			elif winning_move(board, 1):
				return (None, -10000000)
			else:
				return (None, 0)
		else:
			return (None, 0)

	if maximizing_player:
		value = -math.inf
		column = np.random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(board, col)
			b_copy = board.copy()
			drop_piece(b_copy, row, col, 2)
			new_score = minimax(b_copy, depth-1, False)[1] #recursion
			if new_score > value:
				value = new_score
				column = col
		return column, value
	else:
		value = math.inf
		column = np.random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(board, col)
			b_copy = board.copy()
			drop_piece(b_copy, row, col, 1)
			new_score = minimax(b_copy, depth-1, True)[1]
			if new_score < value:
				value = new_score
				column = col
		return column, value
