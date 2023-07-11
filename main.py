#rcs=races, mgi=magicitems, skl=skills, mgs=magicschools, eqi=equipment, ftu=fetures


#import all of the libraries that will be used
import json

#func is the func.py, not a real library that would be published to pypi
from func import create_code_for_data_page
from func import create_code_for_name_page
from func import create_data_page
from func import create_input_page

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
@app.route('/monsters')
def MonsNamePage():

    #first, set the vairiables that will be used during computing
    query_name = 'monsters'
    next_page_link = 'monsterdata'
    form_name = 'monsname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


#this is the monster page that shows/gains data
@app.route('/monsterdata', methods=['GET', 'POST'])
def MonsDataPage():

    #first, set the vairiables that will be used during computing
    form_name = 'monsname'
    query_name = 'monsters'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


#this is the class page that gains input
@app.route('/classes')
def ClsNamePage():

    #first, set the vairiables that will be used during computing
    query_name = 'classes'
    next_page_link = 'classdata'
    form_name = 'clsname'
    suffix_to_remove = 'es'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


#this is the class page that shows/gains data
@app.route('/classdata', methods=methodlist)
def ClsDataPage():

    #first, set the vairiables that will be used during computing
    form_name = 'clsname'
    query_name = 'classes'
    suffix_to_remove = 'es'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@app.route('/abilityscores', methods=methodlist)
def AbSNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'ability-scores'
    next_page_link = 'abilityscoredata'
    form_name = 'absname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@app.route('/abilityscoredata', methods=methodlist)
def AbsDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'absname'
    query_name = 'ability-scores'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@app.route('/spells', methods=methodlist)
def SplNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'spells'
    next_page_link = 'spelldata'
    form_name = 'splname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@app.route('/spelldata', methods=methodlist)
def SplDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'splname'
    query_name = 'spells'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@app.route('/races', methods=methodlist)
def RcsNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'races'
    next_page_link = 'racedata'
    form_name = 'rcsname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@app.route('/racedata', methods=methodlist)
def RcsDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'rcsname'
    query_name = 'races'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@app.route('/magicitems', methods=methodlist)
def MgiNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'magic-items'
    next_page_link = 'magicitemdata'
    form_name = 'mginame'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@app.route('/magicitemdata', methods=methodlist)
def MgiDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'mginame'
    query_name = 'magic-items'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@app.route('/skills', methods=methodlist)
def SklNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'skills'
    next_page_link = 'skilldata'
    form_name = 'sklname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@app.route('/skilldata', methods=methodlist)
def SklDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'sklname'
    query_name = 'skills'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@app.route('/magicschools', methods=methodlist)
def MgsNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'magic-schools'
    next_page_link = 'magicschooldata'
    form_name = 'mgsname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@app.route('/magicschooldata', methods=methodlist)
def MgsDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'mgsname'
    query_name = 'magic-schools'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@app.route('/equipment', methods=methodlist)
def EqiNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'equipment'
    next_page_link = 'equipmentdata'
    form_name = 'eqiname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@app.route('/equipmentdata', methods=methodlist)
def EqiDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'eqiname'
    query_name = 'equipment'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@app.route('/features', methods=methodlist)
def FtuNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'features'
    next_page_link = 'featuredata'
    form_name = 'ftuname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@app.route('/featuredata', methods=methodlist)
def FtuDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'ftuname'
    query_name = 'features'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@app.route('/subclasses', methods=methodlist)
def SbcNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'subclasses'
    next_page_link = 'subclassdata'
    form_name = 'sbcname'
    suffix_to_remove = 'es'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@app.route('/subclassdata', methods=methodlist)
def SbcDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'sbcname'
    query_name = 'subclasses'
    suffix_to_remove = 'es'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@app.route('/alignments', methods=methodlist)
def AlnNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'alignments'
    next_page_link = 'alignmentdata'
    form_name = 'alnname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@app.route('/alignmentdata', methods=methodlist)
def AlnDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'alnname'
    query_name = 'alignments'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@app.route('/backgrounds', methods=methodlist)
def BgdNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'backgrounds'
    next_page_link = 'backgrounddata'
    form_name = 'bgdname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)



@app.route('/backgrounddata', methods=methodlist)
def BgdDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'bgdname'
    query_name = 'backgrounds'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


