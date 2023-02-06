import json


with open('Ayon_ssp.json', 'r') as f:
    data = json.load(f)

name = data['name']
userName = data['login']
profileLink = data['html_url']
repoLink = data['repos_url']

htmlTamplet = '<!DOCTYPE html> <html> <head> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"> <style> .card { box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); max-width: 300px; margin: auto; text-align: center; font-family: arial; } .title { color: grey; font-size: 18px; } button { border: none; outline: 0; display: inline-block; padding: 8px; color: white; background-color: #000; text-align: center; cursor: pointer; width: 100%; font-size: 18px; } a { text-decoration: none; font-size: 22px; color: black; } button:hover, a:hover { opacity: 0.7; } </style> </head> <body> <h2 style="text-align:center">🙍‍♂️Profile</h2> <div class="card"> <img src="https://avatars.githubusercontent.com/u/80549753?s=400&u=74659f0d3a599612e461950bd720e16345ebf4c8&v=4" alt="John" style="width:100%"> <h1>{name}</h1> <p class="title">CEO & Founder, {userName}</p> <p>Harvard University</p> <div style="margin: 24px 0;"> <a href="{repoLink}"><i class="fa fa-dribbble"></i></a> <a href="#"><i class="fa fa-twitter"></i></a> <a href="#"><i class="fa fa-linkedin"></i></a> <a href="#"><i class="fa fa-facebook"></i></a> </div> <p><button>Contact</button></p> </div> </body> </html>'


htmlTamplet = htmlTamplet.replace('{name}', name).replace('{userName}', userName)

with open('AyonProfile.html', "w") as f:
  f.write(htmlTamplet)



# print(type(data))
# jsonContent = json.dumps(data, indent=4)
# print(jsonContent)