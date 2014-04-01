import simplegui
import random

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

ball_pos = [WIDTH / 2, HEIGHT / 2] 
ball_vel = [((-1) ** random.randrange(2)) * random.randrange(1,4), -1 * random.randrange(1,3)]

paddle1_pos = [4, 40]
paddle1_vel = [0, 0]
paddle2_pos = [596 , 40]
paddle2_vel = [0, 0]

score1 = 0
score2 = 0


# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if right == True:
        ball_vel = [random.randrange(1, 4), -1 * random.randrange(1,3)]
    elif right == False:	
        ball_vel = [ -1 * random.randrange(1,4), -1 * random.randrange(1,3)]
  
# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  
    global score1, score2  
    score1 = 0
    score2 = 0
    pass

def update_paddle1(): 
    global paddle1_pos 
     
    if (paddle1_pos[1] - (PAD_HEIGHT / 2)) - paddle1_vel[1] >= 0: 
    
        paddle1_vel[1] 
    else:  
        paddle1_pos[1] = PAD_HEIGHT / 2 
        paddle1_vel[1] = 0

def update_paddle2(): 
    global paddle2_pos 
     
    if (paddle2_pos[1] - (PAD_HEIGHT / 2)) - paddle2_vel[1] >= 0: 
    
        paddle2_vel[1] 
    else: 
     
        paddle2_pos[1] = PAD_HEIGHT / 2 
        paddle2_vel[1] = 0        

def update_paddle3(): 
    global paddle1_pos 
    if (paddle1_pos[1] + (PAD_HEIGHT / 2)) + paddle1_vel[1] <= 400: 
            paddle1_vel[1] 
    else:  
        paddle1_pos[1] = 400 - PAD_HEIGHT / 2 
        paddle1_vel[1] = 0        

def update_paddle4(): 
    global paddle2_pos 
     
    if (paddle2_pos[1] + (PAD_HEIGHT / 2)) + paddle2_vel[1] <= 400: 
    
        paddle2_vel[1] 
    else: 
     
        paddle2_pos[1] = 400 - PAD_HEIGHT / 2 
        paddle2_vel[1] = 0                
        
        
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    #draw score card
    canvas.draw_text(str(score1), [40, 30], 24, 'white')
    canvas.draw_text(str(score2), [550, 30], 24, 'white')

    
    # left paddle position & velocity
    paddle1_pos[1] += paddle1_vel[1]   
    canvas.draw_line([paddle1_pos[0],paddle1_pos[1]-HALF_PAD_HEIGHT],[paddle1_pos[0],paddle1_pos[1]+HALF_PAD_HEIGHT], PAD_WIDTH, "white")
    
    # right paddle position & velocity
    paddle2_pos[1] += paddle2_vel[1]
    canvas.draw_line([paddle2_pos[0],paddle2_pos[1]-HALF_PAD_HEIGHT],[paddle2_pos[0],paddle2_pos[1]+HALF_PAD_HEIGHT], PAD_WIDTH, "white")
    
    # update ball

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # update paddle's vertical position, keep paddle on the screen
    update_paddle1()
    update_paddle2()
    update_paddle3()
    update_paddle4()
    
    #this code will  tests whether the ball touches/collides 
    #with the left and right screen
    if ball_pos[0] < PAD_WIDTH + BALL_RADIUS: #this touches left
        if ball_pos[1] >= paddle1_pos[1]- HALF_PAD_HEIGHT and ball_pos[1] <= paddle1_pos[1] + HALF_PAD_HEIGHT:
            ball_vel[0] = - 1.1 * ball_vel[0]
        else:
            ball_init(True)
            score2 += 1
        
    if ball_pos[0] > (WIDTH - PAD_WIDTH - 1) - BALL_RADIUS: #this touches right
        if ball_pos[1] >= paddle2_pos[1]- HALF_PAD_HEIGHT and ball_pos[1] <= paddle2_pos[1] + HALF_PAD_HEIGHT:
            ball_vel[0] = - 1.1 * ball_vel[0]
        else:
            ball_init(False)
            score1 += 1
        
    #this code will bounce ball off the top & bottom of the screen
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]    
    
    # draw ball and scores
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 5
    #moves left paddle up and down
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = acc
    if key==simplegui.KEY_MAP["w"] and paddle1_pos[1] > 40:
        paddle1_vel[1] -= acc      
        
    #moves right paddle up and down    
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] -= acc

    
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    acc = 0
    #moves left paddle up and down
    if key!=simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0
    elif key!=simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = 0
    
    #moves right paddle up and down    
    if key!=simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0
    elif key!=simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0

def restart():
    global ball_pos, ball_vel, score1, score2
    score1 = 0
    score2 = 0
    ball_pos = [WIDTH / 2, HEIGHT / 2] 
    ball_vel = [((-1) ** random.randrange(2)) * random.randrange(1,4), -1 * random.randrange(1,3)]

        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 100)


# start frame
init()
frame.start()
restart()