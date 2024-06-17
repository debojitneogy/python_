import pygame

pygame.init();
#display set up
screen = pygame.display.set_mode((610,610));
pygame.display.set_caption("tic-tac-toe");
icon = pygame.image.load("./icon.png");
pygame.display.set_icon(icon);
screen.fill((255, 130, 28));

board_record = ["","","","","","","","",""];
won = False;

#drawing grid
cells_ = [];
def draw_grid():
    for y in range(0,615,205):
        for x in range(0,615,205):
            grid_cell = pygame.Rect(x,y,200,200);
            cells_.append(grid_cell);
            pygame.draw.rect(screen,(0,0,0),grid_cell,1,5);
draw_grid();
#print(cell_cods);

#display
def display():
    x_ = pygame.image.load("./close.png");
    x_ = pygame.transform.scale(x_,(150,150));
    o_ = pygame.image.load("./o.png");
    o_ = pygame.transform.scale(o_,(150,150));
    for i in range(9):
        if board_record[i] == "X":
            cell_:pygame.Rect = cells_[i]
            screen.blit(x_,(cell_.x+25,cell_.y+25));
        elif board_record[i] == "O":
            cell_:pygame.Rect = cells_[i]
            screen.blit(o_,(cell_.x+25,cell_.y+25),);
        
#gameplay
turn = "O";
def place_move(i_rect):#places the move
    global turn;
    if board_record[i_rect] == "":
        if turn == "O":#on o's turn
            board_record[i_rect] = "O";
            turn = "X";# on x's turn
        elif turn == "X":
            board_record[i_rect] = "X";
            turn = "O";
        display();
        win_check()
            
#if win
def draw_win(condition):
    #win line
    l = [
        [cells_[0], cells_[1], cells_[2]],
        [cells_[3], cells_[4], cells_[5]],
        [cells_[6], cells_[7], cells_[8]],
        [cells_[0], cells_[3], cells_[6]],
        [cells_[1], cells_[4], cells_[7]],
        [cells_[2], cells_[5], cells_[8]],
        [cells_[0], cells_[4], cells_[8]],
        [cells_[2], cells_[4], cells_[6]]];
    
    a = l[condition][0];
    b = l[condition][2];
    
    pygame.draw.line(screen,(0,0,0),(a.x+100,a.y+100),(b.x+100,b.y+100),20);
    
    #win text
    c = "";
    if turn == "X":
        c = "O";
    elif turn == "O":
        c = "X"

    txt = pygame.font.Font('freesansbold.ttf',30);
    win_txt = txt.render(f"{c} Wins!!",True,(255,255,255));
    screen.blit(win_txt,(245,290));

#win check
def win_check():
    global board_record;
    global won;
    l = [
        [board_record[0], board_record[1], board_record[2]],
        [board_record[3], board_record[4], board_record[5]],
        [board_record[6], board_record[7], board_record[8]],
        [board_record[0], board_record[3], board_record[6]],
        [board_record[1], board_record[4], board_record[7]],
        [board_record[2], board_record[5], board_record[8]],
        [board_record[0], board_record[4], board_record[8]],
        [board_record[2], board_record[4], board_record[6]]];
    
    for condition in l:
        if condition[0] == condition[1] == condition[2]!= '':
            draw_win(l.index(condition));
            won = True
            return True
    return False

    
#game loop
running = True;
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
        if event.type == pygame.MOUSEBUTTONDOWN:#on click
            mouse_pos = pygame.mouse.get_pos()
            for rect_i in range(len(cells_)):#on click which cell
                _rect:pygame.Rect = cells_[rect_i];
                if _rect.collidepoint(mouse_pos[0],mouse_pos[1]):
                    if won == False:
                        place_move(rect_i);
                    
    pygame.display.update();