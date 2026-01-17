# Reeborg-maze-problem
I am sharing the solution to the Reeborg's World maze problem in Python. I have attached a README file so that you can read how I bypass getting stuck in a loop. 
The code might a bit complex and there are some simpler solutions out there particularly the one that Gemini gave me, however good thing I didn't blindly rely on 
that code as it also had to edited so that it doesn't get stuck in an infinite loop. In the maze, you can get my most times without running into the loop, except for 
if you start out somewhere that leads you out in the open without any wall nearby. In which case, the robot woll start to follow a square path in a loop with no end.
In order to solve that problem you can just give it the command to walk() until it is nearby another wall. Here, I have used a while loop with the condition that, if 
the loop runs more than five times in one go then Reeborg will walk() till there is a wall_in_front().
