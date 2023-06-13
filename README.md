# MyHealthMatters by Elon-Musk-Neuralink-Babies

Vansh Saboo: PM  
Daniel Liu: Devo  
Brian Yang: Devo  
Prattay Dey: Devo

# App Description
This is a health-centered app that incentivizes completing daily tasks aimed towards a certain fitness goal. It can also be used to track the nutritional info of one's diet throughout the day, such as calorie and protein intake. Some other cool features are an online forum where users can exchange messages and milestones with each other, interactive maps and charts tracking their fitness data, as well as personalized health tips (like meal planning).

# API Breakdown
US Department of Health API: Return data on health advice for users based off physical attributes
https://health.gov/our-work/national-health-initiatives/health-literacy/consumer-health-content/free-web-content/apis-developers/how-use-api

Nutrition API: alternative api to return nutrition data for food
https://api-ninjas.com/api/nutrition

Be sure to put the nutrition API key in app/keys/key_nutrition.txt for the app to work fully

# Launch Codes

0. Clone repository

 ```bash
 git clone https://github.com/49PES/Elon-Musk-Neuralink-Babies.git
 ```

1. `cd` into the local repository

 ```bash
 cd Elon-Musk-Neuralink-Babies/
 ```

2. Install necessary packages

 ```bash
 pip install -r requirements.txt
 ```

3. `cd` into the app directory

 ```bash
 cd app/
 ```

4. Move nutrition API key into app/keys/key_nutrition.txt

 ```bash
 echo -n your_key > keys/key_nutrition.txt
 ```

5. Start Flask server

 ```bash
 python __init__.py
 ```

6. Visit ` http://127.0.0.1:5000` in browser

7. Vist `https://marshyy.me:5003/` to see the web app on a Digital Ocean Droplet
