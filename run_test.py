import os
import webbrowser


if __name__ == "__main__":
    command = "nosetests --with-coverage --cover-erase --cover-html --cover-package=project"
    os.system(command)

    cover_report_path = r"C:\Users\cumon\Desktop\Web Projects\noname\cover\index.html"
    #webbrowser.open(cover_report_path)
