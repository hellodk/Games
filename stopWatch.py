import SimpleGUICS2Pygame.simpleguics2pygame as simplegui;

# define global variables

millis=0;
wins=0;
attempts=0;

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format_time(t):
    mil=t%10;
    temp=int(t/10);
    sec=temp%60;
    mnt=int(temp/60);
    if(sec<10):
        sec_string="0"+str(sec);
    else:
        sec_string=str(sec);
    return str(mnt)+":"+sec_string+"."+str(mil);    

# define event handlers for buttons; "Start", "Stop", "Reset"

def start_timer():
    timer.start();

def stop_timer():
    timer.stop();
    global wins,attempts;
    if(millis%10==0):
        wins=wins+1;
    attempts=attempts+1;    
    

def reset_timer():
    global millis,wins,attempts
    timer.stop();
    millis=0;
    wins=0;
    attempts=0;

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global millis;
    millis +=1;
    
    
def draw_handler(canvas):
    canvas.draw_text(format_time(millis), (120,120), 50, "White");
    canvas.draw_text(str(wins)+"/"+str(attempts),(340,30),25,"Red");
# create frame
frame=simplegui.create_frame("stopwatch",400,200);

# register event handlers

frame.add_button("Start",start_timer,100);
frame.add_button("Stop",stop_timer,100);
frame.add_button("Reset",reset_timer,100);
timer = simplegui.create_timer(100, timer_handler);
frame.set_draw_handler(draw_handler);

# start timer and frame
frame.start();
