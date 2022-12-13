import os
import json
import random
import secrets
import pandas
import pickle
from serpapi import GoogleSearch
from flask import Flask, request, redirect, render_template, url_for, flash, session

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# API_key = os.getenv('SERP_API_KEY')
API_key = '5074028568879874a7f573b4071fb9c484bf3e91e883b98d94949d6298b85f86'

possible_search_terms = ['TEM','SEM','XRD','XRF','XANES']

def generate_microscope_search_params(microscope, prompt = 'Images from a'):
    params = {
        'q': '{} {}'.format(prompt, microscope),
        'tbm': 'isch',
        'ijn': '0',
        'api_key': API_key
    }
    return params

def generate_numbers(how_many_numbers, total_sum=9):
    numbers = []
    remaining = total_sum
    for i in range(how_many_numbers - 1):
        number = random.randint(1, remaining - (how_many_numbers - i - 1))
        numbers.append(number)
        remaining -= number
    numbers.append(remaining)
    random.shuffle(numbers)
    return numbers

def create_quiz(images):
    # images = tmp
    keys = list(dict.keys(images))
    n_categories = len(images)
    n_pictures = 9

    # Generate a random order for the categories to appear
    quiz_topic_order = list(range(0,n_categories))
    random.shuffle(quiz_topic_order)
    
    # Assign grid slots to categories randomly
    picture_idx_order = [random.randint(0,n_categories-1) for _ in range(0,n_pictures)]
    picture_category_order = [keys[i] for i in picture_idx_order]
    pics_per_category = pandas.value_counts(picture_idx_order)
    
    grab_pics_2dlst = [random.sample(images[keys[i]], pics_per_category[i]) for i in range(0,n_categories)]
    urls_in_order_lst = [grab_pics_2dlst[picture_idx_order[i]].pop() for i in range(0,n_pictures)]
    urls_with_category_2dlst = list(zip(picture_category_order, urls_in_order_lst))
    
    return urls_with_category_2dlst


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        prompt = request.form['prompt']
        options = request.form['options']
        if options == '':
            flash('Error: Options are required.')
        else:        
            return redirect(url_for('quiz', prompt=prompt, options=options))
    return render_template('index.html')

@app.route('/quiz', methods=('GET', 'POST'))
def quiz():
    print("QUIZ")
    if request.args.get("continuation") == "yes":
        session['idx'] = session['idx'] + 1
        return render_template('quiz.html', quiz_images=session['quiz_images'], option=session['options'][session['idx']], cont='yes')
    else:
        session['idx'] = 0
        session['prompt'] = request.args.get("prompt")
        session['options'] = request.args.get("options").split(',')
        # searches = [GoogleSearch(generate_microscope_search_params(option, prompt)).get_dict()['images_results'] for option in options]
        searches_tmp = read_imgs()
        session['all_photos'] = [[res['original'] for res in search[0:10]] for search in searches_tmp]
    session['quiz_images'] = create_quiz(images = dict(zip(session['options'], session['all_photos'])))
    return render_template('quiz.html', quiz_images=session['quiz_images'], option=session['options'][session['idx']])

def read_imgs():
    with open("example_image_data.txt", "rb") as file:
        searches = pickle.load(file)
    return searches

# with open("data.txt", "rb") as file:
#     searches = pickle.load(file)

# import sys
# og_stdout = sys.stdout
# with open('photos_results_all','w') as f:
#     sys.stdout = f
#     print(photos)
#     sys.stdout = og_stdout
