# Module Imports: The first thing that needs to be done in any program is to import any additional modules that are going
# to be used. In this example, tkinter and pillow have been imported so that the design for the buttons and logo can be 
# imported. Once I have a concrete algorithm for the calculations, pygame will be implemented so I can show the car moving
# around the track. 

from tkinter import *
import pandas as pd
import os
from PIL import Image, ImageTk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Font Definitions: In order to get the text to a format similiar to that set out by the inital designs, I had to implement
# these two variables that I would refer back to when specifying what sort of text I would like in my widget. If I were to
# implement some form of accessability in future, it would be best to have the size of the font, the type of font and it's boldness
# specified in seperate variables; because I am not doing this, I can reduce the workload by defining the fonts seperately.

defaultFont = ("Arial", 10 ,"bold")
defaultFont2 = ("Arial", 15 ,"bold")

# Preset Value Initialisation: These values are the initial states for the conditions before the program is run. This means that
# they will always be reset when the program is restarted, and can be referenced in future subroutines. 

dryPreset = False
wetPreset = False
AMPreset = False
McLarenPreset = False
MercedesPreset = False

DefaultWindow = True
WeatherWindow = False
PresetWindow = False

# Weather Window: This function will be bound to the Weather Button and when activated, while create the interface for the user
# to input their chosen conditions through. When the calcultions themselves are programmed, I will be able to use the weather
# buttons as inputs. These buttons have to be declared as global variables so that they can be destroyed in other sections of the
# program. Before these buttons are defined, you can see that the frame has the config function run on it. This is changing the
# background colour of the program, using the hex code taken from my design tools.

def openWeather():

    global dryButton, wetButton, weatherSubFrame

    functionFrame.config(bg='black')
    weatherSubFrame = Frame(functionFrame, bg="white", relief='solid', borderwidth=3, height=730, width=1080)
    weatherSubFrame.grid_propagate(False)
    weatherSubFrame.grid(row=0, column=0, columnspan=3, padx=0, pady=0, sticky="nsew")
    weatherSubFrame.columnconfigure(0, weight=0)
    weatherSubFrame.columnconfigure(1, weight=1)
    weatherSubFrame.columnconfigure(2, weight=0)
    weatherSubFrame.config(bg='#1c4587')
    

    dryButton = Button(weatherSubFrame, text="Dry and Warm", height=27, width=40, bg="white", relief="raised", font=defaultFont2, command=lambda:addDryWeather())
    dryButton.grid(row=1, column=1, rowspan=1, columnspan=1, padx=10, pady=(20,10), sticky=W+E)

    wetButton = Button(weatherSubFrame, text="Wet and Cold", height=27, width=40, bg="white", relief="raised", font=defaultFont2, command=lambda:addWetWeather())
    wetButton.grid(row=1, column=3, rowspan=1, columnspan=1, padx=10, pady=(20,10), sticky=W+E)

    WeatherWindow = True

    return WeatherWindow

def addDryWeather():
    global dryPreset, wetPreset
    dryPreset = True
    wetPreset = False
    return dryPreset, wetPreset

def addWetWeather():
    global wetPreset, dryPreset
    wetPreset = True
    dryPreset = False
    return wetPreset, dryPreset

# Reset Function: This function will reset the window to it's default state, that being the track display. When a track is not
# selected, the frame will be blank with a green background, meant to be representative of grass. Using the destroy function
# on the buttons created in other functions will mean that they are removed once this function is run, leaving the blank background
# that was there to begin with. The colour for this background is adjusted using the configure function again.

def resetToDefaults():

    global functionFrame

    DefaultWindow = True
    dryPreset = False
    wetPreset = False
    AMPreset = False
    McLarenPreset = False
    MercedesPreset = False

    DefaultWindow = True
    WeatherWindow = False
    PresetWindow = False

    functionFrame.destroy()

    functionFrame = Frame(widgetFrame, bg="white", relief='solid', borderwidth=3, height=720, width=1080)
    functionFrame.grid_propagate(False)
    functionFrame.grid(row=1, column=1, columnspan=3, padx=0, pady=5, sticky="nsew")

    functionFrame.columnconfigure(0, weight=1)
    functionFrame.columnconfigure(1, weight=1)
    functionFrame.columnconfigure(2, weight=1)
    functionFrame.config(bg='#00eb92')


    return DefaultWindow, dryPreset, wetPreset, AMPreset, McLarenPreset, MercedesPreset, WeatherWindow, PresetWindow

# Presets Function: This function will open the presets for the track and the car selected by the user. At the beginning of the
# function, global variables are defined just as before, and the background colour is promptly changed. The column weights have to
# be altered so that the widgets fit into the frame correctly; the same logic must be applied to the rows of the grid too. 

def openPresets():

    global AstonMartinImageData, MclarenImageData, MercedesImageData, carOptionsFrame, carImageFrame, carImageFramePlaceholder, dryButton, wetButton, presetsSubFrame

    functionFrame.config(bg='black')
    presetsSubFrame = Frame(functionFrame, bg="white", relief='solid', borderwidth=3, height=730, width=1080)
    presetsSubFrame.grid_propagate(False)
    presetsSubFrame.grid(row=0, column=0, columnspan=3, padx=0, pady=0, sticky="nsew")
    presetsSubFrame.config(bg='#1c4587')

    presetsSubFrame.columnconfigure(0, weight=1)
    presetsSubFrame.columnconfigure(1, weight=1)
    presetsSubFrame.columnconfigure(2, weight=1)
    presetsSubFrame.columnconfigure(3, weight=1)

    presetsSubFrame.rowconfigure(0, weight=0)
    presetsSubFrame.rowconfigure(1, weight=1)
    presetsSubFrame.rowconfigure(2, weight=1)
    presetsSubFrame.rowconfigure(3, weight=1)

    carOptionsFrame = Frame(presetsSubFrame, height=200, width=900)
    carOptionsFrame.grid(row=1, column=1, rowspan=1, columnspan=2, padx=(15,0), sticky=E+W)

    selectAston = Button(carOptionsFrame, text="Aston Martin Vantage", height=5, width=26, bg="red", relief="raised", borderwidth=2, font=defaultFont2, command=lambda:addAstonMartin())
    selectAston.grid(row=0, column=1, padx=(20,5), pady=5, sticky="nsew")

    selectMclaren = Button(carOptionsFrame, text="Mclaren Senna", height=5, width=26, bg="red", relief="raised", borderwidth=2, font=defaultFont2, command=lambda:addMclaren())
    selectMclaren.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

    selectMercedes = Button(carOptionsFrame, text="Mercedes AMG One", height=5, width=26, bg="red", relief="raised", borderwidth=2, font=defaultFont2, command=lambda:addMercedes())
    selectMercedes.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

    carImageFramePlaceholder = Frame(presetsSubFrame, height=300, width=500)
    carImageFramePlaceholder.grid(row=2, column=2, rowspan=1, columnspan=1, padx=(15,0), sticky=W)

    PresetWindow = True
    
    return PresetWindow, WeatherWindow


# Image Calling Functions: The six functions that you can see below all call the images from their respective file locations to
# display them to the user once they have selected their chosen track or vehicle. When continuing development, these functions
# should save the new preset to the calculator in addition to calling the image. This is done by destroying the placeholder widget
# and building a new one in it's place . The image data is called and then output into an image widget. This has to be labelled as an
# output image otherwise the cell resizes for the image, but does not show it to the user. 

def addAstonMartin():

    global carImageFrame, carImageOutput, AMPreset, McLarenPreset, MercedesPreset, presetsSubFrame

    carImageFramePlaceholder.destroy()

    AMPreset = True
    McLarenPreset = False
    MercedesPreset = False

    AstonMartinWidget = ImageTk.PhotoImage(AstonMartinImageData)

    carImageFrame = Frame(presetsSubFrame, height=300, width=500)
    carImageFrame.grid(row=2, column=2, rowspan=1, columnspan=1, padx=(15,0), sticky=W)

    carImageOutput = Label(carImageFrame, image=AstonMartinWidget)
    carImageOutput.image = AstonMartinWidget 
    carImageOutput.pack(anchor="center")

    return AMPreset, McLarenPreset, MercedesPreset


def addMclaren():

    global carImageFrame, carImageOutput,  AMPreset, McLarenPreset, MercedesPreset, presetsSubFrame

    AMPreset = False
    McLarenPreset = True
    MercedesPreset = False

    carImageFramePlaceholder.destroy()

    MclarenWidget = ImageTk.PhotoImage(MclarenImageData)

    carImageFrame = Frame(presetsSubFrame, height=400, width=500)
    carImageFrame.grid(row=2, column=2, rowspan=1, columnspan=1, padx=(15,0), sticky=W)

    carImageOutput = Label(carImageFrame, image=MclarenWidget)
    carImageOutput.image = MclarenWidget 
    carImageOutput.pack(anchor="center")

    return AMPreset, McLarenPreset, MercedesPreset

def addMercedes():

    global carImageFrame, carImageOutput,  AMPreset, McLarenPreset, MercedesPreset, presetsSubFrame

    carImageFramePlaceholder.destroy()

    AMPreset = False
    McLarenPreset = False
    MercedesPreset = True

    MercedesWidget = ImageTk.PhotoImage(MercedesImageData)

    carImageFrame = Frame(presetsSubFrame, height=400, width=500)
    carImageFrame.grid(row=2, column=2, rowspan=1, columnspan=1, padx=(15,0), sticky=W)

    carImageOutput = Label(carImageFrame, image=MercedesWidget)
    carImageOutput.image = MercedesWidget 
    carImageOutput.pack(anchor="center")

    return AMPreset, McLarenPreset, MercedesPreset

def calculateLaptime():

    global figure
    
    for widgets in GraphOuterFrame.winfo_children():
        widgets.destroy()
    print(dryPreset, wetPreset, AMPreset, McLarenPreset, MercedesPreset)

    TextPlaceholder.config(text="0. Please Input Car and Conditions")
    functionFrame.config(bg='black')

    xLabels = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000]
    yLabels = [0, 20, 50, 60, 70, 80, 90, 100]

    if dryPreset == True and McLarenPreset == True:

        fileForLaptime = pd.read_excel((r"SilverstoneMcLarenSennaDry.xlsx"), header=195)
        rowRequired = str(fileForLaptime.keys())
        lapTime = rowRequired[341:352]
        TextPlaceholder.config(text=lapTime)

        fileForGraph = pd.read_excel((r"SilverstoneMcLarenSennaDry.xlsx"), header=3)
        xValues = fileForGraph['x(distance)'] 
        yValues = fileForGraph['Final Velocity']

        figure = Figure(figsize=(60,60), dpi=10)

        subPlot = figure.add_subplot(111)
        subPlot.plot(xValues, yValues, linewidth =8, color='red')
        subPlot.set_xlabel('Distance Covered (m)', fontsize=100, labelpad=100)
        subPlot.set_ylabel('Top Speed (mph)', fontsize=100, labelpad=100)
        subPlot.set_xticklabels(xLabels,fontsize=50)
        subPlot.set_yticklabels(yLabels,fontsize=50)
        subPlot.set_title('Mclaren Senna In The Dry', fontsize=150, pad=100)

        canvas = FigureCanvasTkAgg(figure, master=GraphOuterFrame)
        canvas.draw()
        canvas.get_tk_widget().pack() 
       
    elif wetPreset == True and McLarenPreset == True:
              
        fileForLaptime = pd.read_excel((r"SilverstoneMcLarenSennaWet.xlsx"), header=195)
        rowRequired = str(fileForLaptime.keys())
        lapTime = rowRequired[341:352]
        TextPlaceholder.config(text=lapTime)
                
        fileForGraph = pd.read_excel((r"SilverstoneMcLarenSennaWet.xlsx"), header=3)
        xValues = fileForGraph['x(distance)'] 
        yValues = fileForGraph['Final Velocity']

        figure = Figure(figsize=(60,60), dpi=10)

        subPlot = figure.add_subplot(111)
        subPlot.plot(xValues, yValues, linewidth =8, color='blue')
        subPlot.set_xlabel('Distance Covered (m)', fontsize=100, labelpad=100)
        subPlot.set_ylabel('Top Speed (mph)', fontsize=100, labelpad=100)
        subPlot.set_xticklabels(xLabels,fontsize=50)
        subPlot.set_yticklabels(yLabels,fontsize=50)
        subPlot.set_title('Mclaren Senna In The Wet', fontsize=150, pad=100)

        canvas = FigureCanvasTkAgg(figure, master=GraphOuterFrame)
        canvas.draw()
        canvas.get_tk_widget().pack() 

    elif dryPreset == True and MercedesPreset == True:
        
        fileForLaptime = pd.read_excel((r"SilverstoneMercedesAMGOneDry.xlsx"), header=195)
        rowRequired = str(fileForLaptime.keys())
        lapTime = rowRequired[341:352]
        TextPlaceholder.config(text=lapTime)
        
        fileForGraph = pd.read_excel((r"SilverstoneMercedesAMGOneDry.xlsx"), header=3)
        xValues = fileForGraph['x(distance)'] 
        yValues = fileForGraph['Final Velocity']

        figure = Figure(figsize=(60,60), dpi=10)

        subPlot = figure.add_subplot(111)
        subPlot.plot(xValues, yValues, linewidth =8, color='red')
        subPlot.set_xlabel('Distance Covered (m)', fontsize=100, labelpad=100)
        subPlot.set_ylabel('Top Speed (mph)', fontsize=100, labelpad=100)
        subPlot.set_xticklabels(xLabels,fontsize=50)
        subPlot.set_yticklabels(yLabels,fontsize=50)
        subPlot.set_title('Mercedes AMG One In The Dry', fontsize=150, pad=100)

        canvas = FigureCanvasTkAgg(figure, master=GraphOuterFrame)
        canvas.draw()
        canvas.get_tk_widget().pack() 

    elif wetPreset == True and MercedesPreset == True:
        
        fileForLaptime = pd.read_excel((r"SilverstoneMercedesAMGOneWet.xlsx"), header=195)
        rowRequired = str(fileForLaptime.keys())
        lapTime = rowRequired[341:352]
        TextPlaceholder.config(text=lapTime)
        
        fileForGraph = pd.read_excel((r"SilverstoneMercedesAMGOneWet.xlsx"), header=3)
        xValues = fileForGraph['x(distance)'] 
        yValues = fileForGraph['Final Velocity']

        figure = Figure(figsize=(60,60), dpi=10)

        subPlot = figure.add_subplot(111)
        subPlot.plot(xValues, yValues, linewidth =8, color='blue')
        subPlot.set_xlabel('Distance Covered (m)', fontsize=100, labelpad=100)
        subPlot.set_ylabel('Top Speed (mph)', fontsize=100, labelpad=100)
        subPlot.set_xticklabels(xLabels,fontsize=50)
        subPlot.set_yticklabels(yLabels,fontsize=50)
        subPlot.set_title('Mercedes AMG One In The Wet', fontsize=150, pad=100)

        canvas = FigureCanvasTkAgg(figure, master=GraphOuterFrame)
        canvas.draw()
        canvas.get_tk_widget().pack() 


    elif dryPreset == True and AMPreset == True:

        fileForLaptime = pd.read_excel((r"SilverstoneAMVantageDry.xlsx"), header=195)
        rowRequired = str(fileForLaptime.keys())
        lapTime = rowRequired[341:352]
        TextPlaceholder.config(text=lapTime)
        
        fileForGraph = pd.read_excel((r"SilverstoneAMVantageDry.xlsx"), header=3)
        xValues = fileForGraph['x(distance)'] 
        yValues = fileForGraph['Final Velocity']
        
        figure = Figure(figsize=(60,60), dpi=10)

        subPlot = figure.add_subplot(111)
        subPlot.plot(xValues, yValues, linewidth =8, color='red')
        subPlot.set_xlabel('Distance Covered (m)', fontsize=100, labelpad=100)
        subPlot.set_ylabel('Top Speed (mph)', fontsize=100, labelpad=100)
        subPlot.set_xticklabels(xLabels,fontsize=50)
        subPlot.set_yticklabels(yLabels,fontsize=50)
        subPlot.set_title('Aston Martin Vantage In The Dry', fontsize=150, pad=100)

        canvas = FigureCanvasTkAgg(figure, master=GraphOuterFrame)
        canvas.draw()
        canvas.get_tk_widget().pack() 

    elif wetPreset == True and AMPreset == True:

        fileForLaptime = pd.read_excel((r"SilverstoneAMVantageWet.xlsx"), header=195)
        rowRequired = str(fileForLaptime.keys())
        lapTime = rowRequired[341:352]
        TextPlaceholder.config(text=lapTime)

        fileForGraph = pd.read_excel((r"SilverstoneAMVantageWet.xlsx"), header=3)
        xValues = fileForGraph['x(distance)'] 
        yValues = fileForGraph['Final Velocity']

        figure = Figure(figsize=(60,60), dpi=10)

        subPlot = figure.add_subplot(111)
        subPlot.plot(xValues, yValues, linewidth =8, color='blue')
        subPlot.set_xlabel('Distance Covered (m)', fontsize=100, labelpad=100)
        subPlot.set_ylabel('Top Speed (mph)', fontsize=100, labelpad=100)
        subPlot.set_xticklabels(xLabels,fontsize=50)
        subPlot.set_yticklabels(yLabels,fontsize=50)
        subPlot.set_title('Aston Martin Vantage In The Wet', fontsize=150, pad=100)

        canvas = FigureCanvasTkAgg(figure, master=GraphOuterFrame)
        canvas.draw()
        canvas.get_tk_widget().pack() 




# Images To Call: Seen below are the six images that are going to be called when their respective functions are called. Rather
# than referencing the address directly, packaging it as a variable makes referencing it continually easier as a result. 

AstonMartinImageData = Image.open(r"AMVantagePNG.png")

MclarenImageData = Image.open(r"McLarenSennaPNG.png")

MercedesImageData = Image.open(r"MercedesAMGOnePNG.png")

logoData = Image.open(r"CircuitChronicleLogo.png")

width = 200
height = 200
resizedLogo = logoData.resize((width, height))

# Main Window Definitions

mainWindow =Tk()
mainWindow.title("The Circuit Chronicle")
mainWindow.geometry("1920x1080")
mainWindow.resizable(True, True)
mainWindow.configure(background="grey12")
mainWindow.minsize(width=960, height=540)

# Frame Configurations - Main Window

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=0)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(4, weight=1)
mainWindow.columnconfigure(5, weight=1)
mainWindow.columnconfigure(6, weight=1)

mainWindow.rowconfigure(0, weight=0)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)

# Top Frame Definition

topbarFrame = Frame(mainWindow, bg='#0094ff', relief="solid")
topbarFrame.grid(row=0, column=0, columnspan=7, sticky=W+E)

# Frame Configurations - Top Frame

topbarFrame.columnconfigure(0, weight=0)
topbarFrame.columnconfigure(1, weight=1)
topbarFrame.columnconfigure(2, weight=1)
topbarFrame.columnconfigure(3, weight=1)
topbarFrame.columnconfigure(4, weight=1)


# Frame Widget Definitions

logoInfo = ImageTk.PhotoImage(resizedLogo)
finalLogo = Label(topbarFrame, image=logoInfo, relief="solid", borderwidth=0, highlightcolor='#0094ff')
finalLogo.grid(row = 0, column = 0, padx=10, pady=5, sticky=N+S+E)

TitleButton = Button(topbarFrame, text="Reset The Circuit Chronicle", height=5, width=20, bg="white", relief="raised", font=defaultFont2, command=lambda:resetToDefaults())
TitleButton.grid(row = 0, column = 1, padx=(10,20), pady=5, sticky=W+E)

PresetButton = Button(topbarFrame, text="Select Presets", height=5, width=20, bg="white", relief="raised", font=defaultFont2, command=lambda:openPresets())
PresetButton.grid(row = 0, column = 2, padx=20, pady=5, sticky=W+E)

WeatherButton = Button(topbarFrame, text="Select Weather", height=5, width=20, bg="white", relief="raised", font=defaultFont2, command=lambda:openWeather())
WeatherButton.grid(row = 0, column = 3, padx=20, pady=5, sticky=W+E)

LapTimeButton = Button(topbarFrame, text="Calculate Lap Time", height=5, width=20, bg="white", relief="raised", font=defaultFont2, command=lambda:calculateLaptime())
LapTimeButton.grid(row=0, column=4, padx=(20,30), pady=5, sticky=W+E)

# Function Frames

widgetFrame = Frame(mainWindow, bg="grey12")
widgetFrame.grid(row=1, column=1, rowspan=2, columnspan=5, sticky="nsew")

functionFrame = Frame(widgetFrame, bg="white", relief='solid', borderwidth=3, height=720, width=1080)
functionFrame.grid_propagate(False)
functionFrame.grid(row=1, column=1, columnspan=3, padx=0, pady=5, sticky="nsew")

functionFrame.columnconfigure(0, weight=1)
functionFrame.columnconfigure(1, weight=1)
functionFrame.columnconfigure(2, weight=1)

functionFrame.config(bg='#00eb92')


clipboardFrame = Frame(widgetFrame, bg='white', relief='solid', borderwidth=3, height=720, width=600)
clipboardFrame.grid(row=1, column=6, padx=5, pady=5, sticky="nsew")

clipboardFrame.columnconfigure(0, weight=1)
clipboardFrame.columnconfigure(1, weight=1)


# Output Laptime Textbox

LapTimeOuterFrame = Frame(clipboardFrame, height=100, width=600, bg='white', relief="solid", borderwidth=2)
LapTimeOuterFrame.grid(row=3,column=2, rowspan=1, columnspan=3, sticky=N, padx=10, pady=10)
LapTimeOuterFrame.grid_propagate(False)

LapTimeOuterFrame.columnconfigure(0, weight=0)
LapTimeOuterFrame.columnconfigure(1, weight=1)
LapTimeOuterFrame.columnconfigure(2, weight=1)
LapTimeOuterFrame.columnconfigure(3, weight=1)
LapTimeOuterFrame.columnconfigure(4, weight=0)

LapTimeOuterFrame.rowconfigure(0, weight=1)
LapTimeOuterFrame.rowconfigure(1, weight=1)
LapTimeOuterFrame.rowconfigure(2, weight=1)


LapTimeLabel = Label(LapTimeOuterFrame, bg='white', fg="black", font=defaultFont2, text="Your Laptime is:")
LapTimeLabel.grid(row=1, column=1, rowspan=2, padx=10, pady=5, sticky=N+S+W)

LapTimeInnerFrame = Frame(LapTimeOuterFrame, bg='white', width=30, bd=5, highlightcolor='black')
LapTimeInnerFrame.grid(row=1, column=2, rowspan=2, columnspan=3, padx=(0, 25), pady=5, sticky="nsew")

LapTimeInnerFrame.rowconfigure(0, weight=0)
LapTimeInnerFrame.rowconfigure(1, weight=1)
LapTimeInnerFrame.rowconfigure(2, weight=1)

LapTimeInnerFrame.columnconfigure(0, weight=1)
LapTimeInnerFrame.columnconfigure(1, weight=1)

TextPlaceholder = Label(LapTimeInnerFrame, bg='ghost white', width=28, text="Example Text", fg="black", font=defaultFont2)
TextPlaceholder.grid(row=1, column=1, rowspan=2, columnspan=2, sticky="nsew")

# Output Graph Box

GraphOuterFrame = Frame(clipboardFrame, height=600, width=600, bg='white', relief="solid", borderwidth=2)
GraphOuterFrame.grid(row=4,column=2, rowspan=1, columnspan=3, sticky=S, padx=10, pady=(0,10))

mainWindow.mainloop()

# Print current working directory
print("Current working directory:", os.getcwd())

# Test printing absolute paths formed by the relative paths
print("Absolute path for AMVantagePNG.png:", os.path.abspath("AMVantagePNG.png"))
print("Absolute path for McLarenSennaPNG.png:", os.path.abspath("McLarenSennaPNG.png"))
print("Absolute path for MercedesAMGOnePNG.png:", os.path.abspath("MercedesAMGOnePNG.png"))
print("Absolute path for CircuitChronicleLogo.png:", os.path.abspath("CircuitChronicleLogo.png"))