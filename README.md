# FLASKY CHAT

![Flasky Chat Python GIF Demonstration](https://github.com/smhussain5/Flask-SocketIO-Chat-Python/blob/main/FLASKY_CHAT_PYTHON.gif?raw=true)

## Problem 🤔

Real-time communication is a neccessity in a globally connected world. Such can be achieved via Flask, Python, and WebSockets.

## Solution 💡

This chat application utilizes simultaneous two-way communication channels over a single TCP connection via WebSockets to provide fast, real-time communication between users. Users must input their name and randomly-generated room code to join a session that is deleted after all users leave. Front-end utilizes Bootstrap and JavaScript to populate the message area with received/sent messages. Back-end utilizes Flask web-framework powered by Python and SocketIO to provide WebSocket capabilities.

## Technologies Used ⚙

- Flask
- Gunicorn
- Heroku
- PyCharm
- Python
- SocketIO

## Challenges 💢

This application was challenging to say the least! I originally wanted to deploy on PythonAnywhere but realized, after deployment, that it was not functioning as intended. After some research on their forums, I learned that they do NOT yet have support for WebSockets. After some further research, I decided to deploy to Heroku using Gunicorn, which was the exact solution I needed to restore proper functionality for the application!

## Insights 💭

This project demonstrated the power of WebSockets as a way to enable simultaneous communication between users. Flask allowed me to develop the back-end with few lines of code. Opportunities to refactor could include database persistence and limiting chat rooms to a specified number of users.

## Contact 📲

[![Static Badge](https://img.shields.io/badge/Send%20me%20an%20email-212121?style=flat-square&logo=gmail&logoColor=EA4335)](mailto:shababhussain525@gmail.com?)<br>
[![Static Badge](https://img.shields.io/badge/Connect_with_me_on_LinkedIn-212121?style=flat-square&logo=linkedin&logoColor=0A66C2)](https://www.linkedin.com/in/shabab-h)<br>
[![Static Badge](https://img.shields.io/badge/Follow_me_on_Twitter-212121?style=flat-square&logo=twitter&logoColor=1D9BF0)](https://twitter.com/shussain_5)<br>
[![Static Badge](https://img.shields.io/badge/Follow_me_on_GitHub-212121?style=flat-square&logo=github&logoColor=FAFAFA)](https://github.com/smhussain5)<br>
