from flask import Flask, render_template, request, url_for
import random
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/form', methods=['GET', 'POST'])
#def form():
#    if request.method == 'POST':
#        restrictions = request.form.getlist('restrictions')
#        meal = generate_meal(restrictions)
#        return render_template('meal.html', meal=meal['name'], video_url=meal['video_url'])
#    return render_template('dietary_restrictions.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        restrictions = request.form.getlist('restrictions')
        meal = generate_meal(restrictions)
        return render_template('dietary_restrictions.html')


@app.route('/meal', methods=['GET', 'POST'])
def meal():
    time.sleep(3)
    if request.method == 'POST':
        restrictions = request.form.getlist('restrictions')
        meal = generate_meal(restrictions)
        return render_template('meal.html', meal=meal['name'], video_url=meal['video_url'])
    

@app.route('/new_meal', methods=['GET', 'POST'])
def new_meal():
    if request.method == 'POST':
        restrictions = request.form.getlist('restrictions')
        meal = generate_meal(restrictions)
        return render_template('meal.html', meal=meal['name'], video_url=meal['video_url'])

def generate_meal(restrictions):
    meals = [
        {'name': 'Grilled salmon with asparagus', 'restrictions': ['gluten-free', 'nut-free'], 'video_url': 'https://www.youtube.com/embed/Kdq3khk_8n0'},
        {'name': 'Roasted vegetable stir-fry', 'restrictions': ['vegetarian', 'vegan'], 'video_url': 'https://www.youtube.com/embed/h8IXBipqYgs'},
        {'name': 'Spaghetti with meat sauce', 'restrictions': ['nut-free'], 'video_url': 'https://www.youtube.com/embed/yfA94mLU0oo'},
        {'name': 'Carrot Soup', 'restrictions': ['gluten-free', 'nut-free', 'vegetarian'], 'video_url': 'https://www.youtube.com/embed/4coBVpdCIMQ'},
        {'name': 'Chicken Stroganoff', 'restrictions': ['gluten-free', 'nut-free'], 'video_url': 'https://www.youtube.com/embed/5nGg68FnbM4'},
        {'name': 'Quick Chicken Marsala', 'restrictions': ['nut-free',], 'video_url': 'https://www.youtube.com/embed/_Nw3bDUpb7Q'},
        {'name': 'Chicken & Spinach Skillet Pasta with Lemon & Parmesan', 'restrictions': ['nut-free', 'gluten-free'], 'video_url': 'https://www.youtube.com/embed/So3MmXLYAFA'},
        {'name': 'Spinach & Mushroom Quiche', 'restrictions': ['gluten-free', 'nut-free', 'vegetarian'], 'video_url': 'https://www.youtube.com/embed/Dfsgi5_J2Oc'},
        {'name': 'Chicken Cutlets with Sun-Dried Tomato Cream Sauce', 'restrictions': ['gluten-free', 'nut-free'], 'video_url': 'https://www.youtube.com/embed/C6YPhoqfHsg'},
        {'name': 'One-Pot Garlicky Shrimp & Broccoli', 'restrictions': ['nut-free', 'gluten-free'], 'video_url': 'https://www.youtube.com/embed/exuzvgnyECk?start=10'},
        {'name': 'Vegetable Weight-Loss Soup', 'restrictions': ['gluten-free'], 'video_url': 'https://www.youtube.com/embed/escHMukMphc'},
        {'name': 'Shirataki Noodles with Tofu & Veggies', 'restrictions': ['nut-free', 'vegetarian'], 'video_url': 'https://www.youtube.com/embed/qkv_CxkdWB4'},
        {'name': 'The Ultimate Vegetarian Club Sandwhich', 'restrictions': ['vegetarian', 'nut-free'], 'video_url': 'https://www.youtube.com/embed/j5gg365Ewaw'},
        {'name': 'Crispy Smashed Potatoes', 'restrictions': ['vegetarian', 'nut-free', 'gluten-free'], 'video_url': 'https://www.youtube.com/embed/Ai_kivZXN9o'},
        {'name': 'Creamy Sun-Dried Tomato and Spinach Pasta', 'restrictions': ['nut-free', 'vegetarian'], 'video_url': 'https://www.youtube.com/embed/ll-FAFOVNVk'},
        {'name': 'Spinach & Artichoke Dip Pasta', 'restrictions': ['nut-free', 'vegetarian'], 'video_url': 'https://www.youtube.com/embed/MS1eAjcp2HU?start=10'}
    ]

    available_meals = []
    for meal in meals:
        if all(restriction in meal['restrictions'] for restriction in restrictions):
            available_meals.append(meal)

    if len(available_meals) == 0:
        return 'No meals available with these restrictions'

    return random.choice(available_meals)

if __name__ == '__main__':
    app.run(debug=True)