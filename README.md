# Weather App

This Weather app is building python using the Libraries and a API provided by openweathermap for more information about this api visit [here]("https://openweathermap.org/api").

## Features

-  Enter the Specific city name which you want to look up and get weather details in fraction of seconds.
-  Just Search with the city name no need of using latitudes and longitudes
-  It also shows icons according to the weather, and temperature in celsius, with respective message like "clear sky", "cloudy" etc.
-  Available in both Light and Dark modes.

## Libraries and Use.

This Weatherapp basically utilizes 3 major libraries, they are.

-  **Pillow** - Python Imaging Library that support for opening, manipulating, and saving many different image file formats.

-  **Tkinter** - Tkinter is a Python used for developing GUI applications. Graphical components like buttons, input fields , dropdowns can be added using this.

-  **Requests** - As we are using the openweathermap API we need a HTTP library to send and make requests. Requests is a HTTP library we can make HTTP requests simpler and more human-friendly.

## Installation

This Project uses Python 3 as the main programming language, you need to clone the repository first inorder to use it. All the libraries used are added to the requirements.txt file you can install the project using the commands shown bellow.

Cloning the Repo

```sh
git clone "repository Link"
```

Installing the requirements using the requirements.txt file

```sh
cd weatherapp
pip install -r requirements.txt
```

-  Before running the weatherapp you need to add your openweathermap api key in the config.ini file, then run the following command.

Running the application.

```sh
python weather.py
```

### Output

As you can see the GUI is available in both Dark and Light Modes, it can be toggeled using the button. You need to enter the City name and search for it.

The output with the processed icon will be displayed below. In this project the temperature is displayed in Celsius, with a message about the weather.

&nbsp;

<p float="left">
<img src="/images/dark_output.jpg"  width="40%">
&nbsp; &nbsp; &nbsp; &nbsp;
<img src="/images/light_output.jpg"  width="40%">
</p>

### Contribution and Usage.

-  This is free to use software. And we are open to any contributions to it.

-  If you want to contribute to the Project make a Pull-request our members will look into it.
