import customtkinter
from PIL import ImageTk, Image
import requests
import configparser


config = configparser.ConfigParser()
config.read('config.ini')


url = 'http://api.openweathermap.org/data/2.5/weather'
api_key = config['weather']['api_key']
iconUrl = 'http://openweathermap.org/img/wn/{}@2x.png'

app = customtkinter.CTk()
app.geometry('300x450')
app.title('Weather App')


def getWeather(city):
    try:
        params = {'q':city,'appid':api_key,'lang':'en'}
        data = requests.get(url,params = params).json()
        if data:
            city = str(data['name']).title()
            country = data['sys']['country']
            temp = int(data['main']['temp'] -273.15)
            icon = data['weather'][0]['icon']
            condition = data['weather'][0]['description']
            return(city,country,temp,icon,condition)
    except:
        print(f"No data available on {city}")

def main():
    city =cityEntry.get()
    weather = getWeather(city)
    if weather:
        locationLabel.configure(text = '{},{}'.format(weather[0],weather[1]) )
        tempLabel.configure( text = '{}°C'.format(weather[2]) )
        conditionLabel.configure( text = weather[4] )
        icon = customtkinter.CTkImage(Image.open(requests.get(iconUrl.format(weather[3]),stream=True).raw), size=(100, 100))
        iconLabel.configure(image=icon)
        iconLabel.image= icon

#Dark & Light Mode Button function
is_on=False
def toggle():
    global is_on
    is_on = not is_on
    if is_on:
        button.configure(text="Dark Mode")
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("dark-blue")

    else:
        button.configure(text="Light Mode")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")


cityEntry = customtkinter.CTkEntry(app,justify='center', placeholder_text="Enter City Name")
cityEntry.pack(fill=customtkinter.BOTH,ipady=10,padx=18,pady=5)
cityEntry.focus()

# add enter key event
cityEntry.bind('<Return>', lambda event: main())

searchButton = customtkinter.CTkButton(app, text ='Search', font=('Arial',15),command=main)
searchButton.pack(fill=customtkinter.BOTH,ipady=10,padx=20)

button = customtkinter.CTkButton(app, text="Dark Mode", command=toggle)
button.pack(ipady=10,padx=18,pady=5)
button.focus()

iconLabel= customtkinter.CTkLabel(app, text="", width=80,height=80)
iconLabel.pack()

locationLabel = customtkinter.CTkLabel(app,font=('Arial',30), text="")
locationLabel.pack()

tempLabel = customtkinter.CTkLabel(app,font=('Arial',15,'bold'), text="")
tempLabel.pack()

conditionLabel = customtkinter.CTkLabel(app,font=('Arial',20), text="")
conditionLabel.pack()


app.mainloop()
