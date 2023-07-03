#import all of the libraries that will be used
import json

#func is the func.py, not a real library that would be published to pypi
from func import create_code_for_data_page
from func import create_code_for_name_page

#flask is a library that is used as a python framework to create sites with html imbeded
from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from flask import redirect

#create the flask aplication, and asigns 'app' as the main group
app = Flask(__name__)

#create a variable for the  method list, so it is simplier in the spots below
methodlist = ['GET', 'POST']

#this is the home page, what is loaded first
@app.route('/', methods = methodlist)
def homepage():

    #this is for the first time after the user logs in
    if request.method == 'POST':
            name = request.form['username']
            favnum = request.form["favnum"]
            output = f'Welcome {name}, to dndinfinity.'
            output2 = f'{favnum} is your special number <3!'

            resp = make_response(render_template('index.html', namecookie=output, numcookie=output2))
            
            resp.set_cookie('username', name)
            resp.set_cookie('favorite_num', favnum)
            
            return resp

    #this is for when the user comes back to the site    
    elif request.method == 'GET':
        try:
            name = request.cookies.get('username')
            favnum = request.cookies.get('favorite_num')
            output = f'Welcome back {name}, to dndinfinity.'
            output2 = f'{favnum} is still your special number <3!'

            resp = make_response(render_template('index.html', namecookie=output, numcookie=output2))

            resp.set_cookie('username', name)
            resp.set_cookie('favorite_num', favnum)

            return resp

        except:
            return render_template('index.html')


#this is the logout page, so the user can delete the cookies
@app.route('/logout', methods = methodlist)
def logout():
    #this is to delete cookies, and redirect to the homepage
    if request.method == 'POST':
        resp = redirect("/", code=302)
        resp.set_cookie('username', '', expires=0)
    
    elif request.method == "GET":
        resp = make_response(render_template('logout.html')) 

    return resp


#this is the login page, just shows the user's name and favorite number. Will be a database in it at some point
@app.route('/login', methods = methodlist)
def loginpage():
    return render_template('login.html')


#this is the developer's page, testing things out before putting it on the main site. There is a button at the bottom-left corner in the homepage
@app.route('/dev')
def DevPage():
    return render_template('dev.html')


#this is the monster page that gains input
@app.route('/monster')
def MonsNamePage():

    #first, set the vairiables that will be used during computing
    query_name = 'monsters'
    html_page = 'monsinput.html'
    next_page_link = 'monsterdata'
    form_name = 'monsname'
    suffix_to_remove = 's'

    #gain the data that we need, all the code with comments are in func.py
    formated_query_name, namelist = create_code_for_name_page(query_name, suffix_to_remove)

    #finnaly, the temlate is rendered with all of the vairiables needed
    return render_template(
        html_page,
        namelist = namelist,
        query_name = query_name,
        next_page_link = next_page_link,
        form_name = form_name,
        formated_query_name = formated_query_name,
    )


#this is the monster page that shows/gains data
@app.route('/monsterdata', methods=['GET', 'POST'])
def ClsDataPage():

    #first, set the vairiables that will be used during computing
    form_name = 'monsname'
    query_name = 'monsters'
    html_page = 'monsdata.html'
    suffix_to_remove = 's'

    #gain the data that we need, all the code with comments are in func.py
    user_input, json_data, image, formated_query_name = create_code_for_data_page(query_name, suffix_to_remove, form_name)

    #finnaly the template is rendered with all of the needs
    return render_template(

        html_page,
        user_input = user_input,
        json_data = json.dumps(json_data, indent = 4),
        image = image,
        formated_query_name = formated_query_name,
    )


#this is the class page that gains input
@app.route('/class')
def ClsNamePage():

    #first, set the vairiables that will be used during computing
    query_name = 'classes'
    html_page = 'clsinput.html'
    next_page_link = 'classdata'
    form_name = 'clsname'
    suffix_to_remove = 'es'

    #gain the data that we need, all the code with comments are in func.py
    formated_query_name, namelist = create_code_for_name_page(query_name, suffix_to_remove)

    #finnaly, the temlate is rendered with all of the vairiables needed
    return render_template(
        html_page,
        namelist = namelist,
        query_name = query_name,
        next_page_link = next_page_link,
        form_name = form_name,
        formated_query_name = formated_query_name,
    )


#this is the class page that shows/gains data
@app.route('/classdata', methods=['GET', 'POST'])
def MonsDataPage():

    #first, set the vairiables that will be used during computing
    form_name = 'clsname'
    query_name = 'classes'
    html_page = 'clsdata.html'
    suffix_to_remove = 'es'

    #gain the data that we need, all the code with comments are in func.py
    user_input, json_data, image, formated_query_name = create_code_for_data_page(query_name, suffix_to_remove, form_name)
    
    #finnaly the template is rendered with all of the needs
    return render_template(

        html_page,
        user_input = user_input,
        json_data = json.dumps(json_data, indent = 4),
        image = image,
        formated_query_name = formated_query_name,
    )
