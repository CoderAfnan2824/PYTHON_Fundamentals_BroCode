#api: 

import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.text_label = QLabel("Enter the City: ", self)
        self.lineText = QLineEdit(self)
        self.button = QPushButton("Submit", self)

        self.temperature_label = QLabel("70°F", self)
        self.emoji_label = QLabel("☀️", self)
        self.description_label = QLabel("Sunny", self)

        self.initUI()

        
    
    def initUI(self):
        
        self.setWindowTitle("Weather App")
        self.setGeometry(500,250,250,350)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.text_label)
        vbox.addWidget(self.lineText)
        vbox.addWidget(self.button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)



        self.setLayout(vbox)
        self.text_label.setAlignment(Qt.AlignCenter)
        self.lineText.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.text_label.setObjectName("text")
        self.lineText.setObjectName("input")
        self.button.setObjectName("button")
        self.temperature_label.setObjectName("temp")
        self.emoji_label.setObjectName("emoji")
        self.description_label.setObjectName("Desc")

        self.setStyleSheet('''

                    QLabel, QPushButton{
                           font-family: Arial;
                           }
                    QLabel#text{
                           font-size: 40px;
                           font-style: italic;
                           }
                    QLineEdit#input{
                           font-size: 20px;
                           min-height: 20px;
                           }
                    QPushButton#button{
                           font-size: 20px;
                           font-weight: bold;
                           }
                    QLabel#temp{
                           font-size: 75px;
                           }
                    QLabel#emoji{
                           font-size: 100px;
                           font-family: Segoe UI emoji;
                           }
                    QLabel#desc{
                           font-size: 80px;
                           }
                           ''')
        
        self.button.clicked.connect(self.get_weather)

    
    def get_weather(self):
        
        print("Button clicked")
        try:
            api_key = "7a14395d4197bde0d669627d7f67aae4"
            city = self.lineText.text()
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request.\nCheck your input")
                case 401:
                    self.display_error("Unauthorized.\nInvalid API key")
                case 403:
                    self.display_error("Forbidden.\nAcess is deined")
                case 404:
                    self.display_error("Not found.\nCheck your input")
                case 500:
                    self.display_error("Internal server error.\nTry again later")
                case 502:
                    self.display_error("Bad gateaway.\nInvalid response from the server.")
                case 503:
                    self.display_error("Service unavailable.\nService is down")
                case 504:
                    self.display_error("Gateway Timeout.\nNo response from the server")
                case _:
                    self.display_error(f"Http error occured: {http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error.\nCheck your network connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout error.\n The request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many requests.\nCheck your URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")


    def display_error(self, message):
        self.temperature_label.setStyleSheet(" font-size: 30px")
        self.temperature_label.setText(message)

        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.15
        temp_f = (temp_k * 9/5) -459.67
        self.temperature_label.setStyleSheet(" font-size: 70px")
        self.temperature_label.setText(f"{temp_c:.0f}°C")

        weather_data = data["weather"][0]["description"]
        self.description_label.setText(weather_data)

        weather_id = data["weather"][0]["id"]

        self.emoji_label.setText(self.get_weather_emoji(weather_id))

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:      # Thunderstorm
            return "⛈️"
        elif 300 <= weather_id <= 321:    # Drizzle
            return "🌦️"
        elif 500 <= weather_id <= 531:    # Rain
            return "🌧️"
        elif 600 <= weather_id <= 622:    # Snow
            return "❄️"
        elif 701 <= weather_id <= 741:    # Fog, mist, haze
            return "🌫️"
        elif weather_id == 762:           # Volcanic ash
            return "🌋"
        elif weather_id == 771:           # Squalls
            return "💨"
        elif weather_id == 781:           # Tornado
            return "🌪️"
        elif weather_id == 800:           # Clear sky
            return "☀️"
        elif 801 <= weather_id <= 804:    # Clouds
            return "☁️"
        else:
            return "❓"
        


def main():
    app = QApplication(sys.argv)

    weatherApp = WeatherApp()

    weatherApp.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()