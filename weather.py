from tkinter import *
from PIL import ImageTk, Image
import requests
import configparser
import sv_ttk


config = configparser.ConfigParser()
config.read('config.ini')


url = 'http://api.openweathermap.org/data/2.5/weather'
api_key = config['weather']['api_key']
iconUrl = 'http://openweathermap.org/img/wn/{}@2x.png'

app = Tk()
app.geometry('300x450')
app.title('Weather App')


def getWeather(city):
    try:
        params = {'q':city,'appid':api_key,'lang':'en'}
        data = requests.get(url,params = params).json()
        if data:
            city = data ['name'].capitalize()
            country = data['sys']['country']
            temp = int(data['main']['temp'] -273.15)
            icon = data['weather'][0]['icon']
            condition = data['weather'][0]['description']
            return(city,country,temp,icon,condition)
    except:
        print("Incorrect place name. Please, correct it")
def main():
    city =cityEntry.get()
    weather = getWeather(city)
    if weather:
        locationLabel['text'] = '{},{}'.format(weather[0],weather[1])
        tempLabel['text']= '{}°C'.format(weather[2])
        conditionLabel['text']=weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(iconUrl.format(weather[3]),stream=True).raw))
        iconLabel.configure(image=icon)
        iconLabel.image= icon

#Dark & Light Mode Button function
is_on=False
def toggle():
    global is_on
    is_on = not is_on
    if is_on:
        button.config(text="Dark Mode")
        # Açma işlemleri burada yapılacak
        sv_ttk.set_theme("dark")

    else:
        button.config(text="Light Mode")
        # Kapama işlemleri burada yapılacak
        sv_ttk.set_theme("light")


cityEntry = Entry(app,justify='center')
cityEntry.pack(fill=BOTH,ipady=10,padx=18,pady=5)
cityEntry.focus()

searchButton = Button(app, text ='Search', font=('Arial',15),command=main)
searchButton.pack(fill=BOTH,ipady=10,padx=20)

button = Button(app, text="Light Mode", command=toggle)
button.pack(ipady=10,padx=18,pady=5)
button.focus()

iconLabel= Label(app)
iconLabel.pack()

locationLabel = Label(app,font=('Arial',30))
locationLabel.pack()

tempLabel = Label(app,font=('Arial',15,'bold'))
tempLabel.pack()

conditionLabel = Label(app,font=('Arial',20))
conditionLabel.pack()


mainloop()