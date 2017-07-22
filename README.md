# result_analysis
College Semester Result analysis software using pandas. Generates a PDF report of the data(data visualization).

Requirements:
    Python 3.x
        modules:
            Numpy
            Scipy
            csv 
            matplotlib
            seaborn
            Tkinter
            tkMessageBox
            pandas
            
User Inputs:
    Path of the datafile (type: textbox)
    Department (type: radio button)
    Name for the pdf report or the path(type: textbox)
    
Output:
    PDF File
    
To freeze the code on windows:
    execute "py2exe setup.py" from cmd.
    paste "data.ico" in dist folder.