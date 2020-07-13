import tkinter as tk
from tkinter import *
import requests
import json

window = tk.Tk()
window.title("Weather App")
window.iconbitmap("icon1.ico")
window.geometry("700x100")
#window.resizable(0,0)





def query():
    zip = str(zipentry.get())
    api_request = requests.get("http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=" + zip +"&date=2020-07-11&distance=25&API_KEY=939879E3-89E1-4AE5-A552-0649B0174BB0")
    data = json.loads(api_request.content)
    area = data[0]['ReportingArea']
    quality = str(data[0]['AQI'])
    category = data[0]['Category']['Name']
    if category == "Good":
        weather_color = "green"
    elif category == "Moderate":
        weather_color = "yellow"
    elif category == "Unhealty":
        weather_color = "orange"
    elif category == "Unhealthy for Sensitive Groups":
        weather_color = "red"
    elif category == "Very Unhealthy":
        weather_color = "blue"
    elif category == "Hazardous":
        weather_color = "black"
    window.configure(background= weather_color)
    label = tk.Label(window, text="City :" + area + "  " + "AQI: " + quality + "    Category: " + category, width=55, height=2, bg=weather_color, fg="white", font=('Arial', 14))
    label.grid(row=1, column=0, columnspan=3,padx=10, pady=10)



zipbutton = tk.Button(window, text="Show Air Quality", command=query)
zipbutton.grid(row=0, column=1, padx=1,pady=1)

zipentry= tk.Entry(window)
zipentry.grid(row=0, column=0, padx=10, pady=10)


#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89121&distance=25&API_KEY=939879E3-89E1-4AE5-A552-0649B0174BB0



window.mainloop()