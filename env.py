import subprocess
import os

if __name__ == "__main__":
    command1 = "Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass"
    subprocess.run(["powershell", command1], shell=True)
    
    # "./env/scripts/activate"
    # env_path = r"C:\Users\cumon\Desktop\Web Projects\noname\env"
    # activate_script = os.path.join(env_path, "Scripts", "activate")
    # command2 = f'cmd /k "{activate_script}"'
    # os.system(command2)