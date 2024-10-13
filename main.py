import time 
import keyboard
from multiprocessing import Process
class project:
    def __init__(self, project_name,t) -> None:
        self.project_name = project_name
        self.elapsed_time = 0
        self.initial_start_time = 0
        self.timer_length = t
        self.start_time = 0

    def start_timer(self):
        start_time = time.time() - self.elapsed_time
        while time.time()-start_time<self.timer_length:
            try:
                self.elapsed_time = time.time() - start_time
                self.start_time = time.time() - self.elapsed_time
                # if self.elapsed_time % 5 == 0:    
                    # print('Hello, bkl! 5 seconds have passed and you have {} seconds remaining.'.format(self.timer_length-self.elapsed_time))
            except KeyboardInterrupt:
                a = input("""
                      1. press enter to continue:
                      2. type exit to exit: 
                      """)
                if a == "exit":
                    break

                
    def randi(self):
        
        print(self.elapsed_time)
        process = Process(target=self.start_timer, args=process)
        
        process.start()
        while process.is_alive():
            if keyboard.is_pressed('q'):
                process.terminate()
                break
            
    def start(self):
        self.initial_start_time = time.time()
        self.randi()

    def unpause(self):
        self.randi()



def main():
    saved_data = []
    while True:
        ans = take_input()
        if ans == 1:
            t = int(input("enter hours required"))
            project_name = input("enter your project name")
            project1 = project(project_name,t)
            saved_data.append(project1)
            project1.start()
        elif ans == 3:
            print("which project to continue")
            for i in range(len(saved_data)):
                print(f"{i}. {saved_data[i].project_name}")
            project_selected = int(input(""))
            if project_selected < len(saved_data):
                saved_data[project_selected].unpause()
        else:
            print("haha clown")
            exit(130)

        
        

def take_input():
    print("""
    1.Day-Scheduler
    2.Timer
    """)
    main_input = int(input("enter your choice: "))
    if main_input == 2:
        print(""" 
        1.Start Project
        2.Exit Project   
        3.Continue Project
        """)
        try:
            ans = int(input("enter your choice: "))
            
        except ValueError:
            print("only integer accepted motherfucker")
            exit(1)
        return ans 
    else:
        print("enter your time slot:")
if __name__ == "__main__": ## magic constant 
    main()