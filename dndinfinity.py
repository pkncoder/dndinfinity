#import all of the libraries that will be used
import json

#func is the func.py, not a real library that would be published to pypi
from dndinfinity.func import create_data_page
from dndinfinity.func import create_input_page
from dndinfinity.func import create_code_for_custom_data_page

#flask is a library that is used as a python framework to create sites with html imbeded
from flask import request
from flask import render_template
from flask import make_response
from flask import redirect
from flask import Blueprint

DnDI = Blueprint(
    'DnDI',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/dndinfinity',
)

#create a variable for the  method list, so it is simplier in the spots below
methodlist = ['GET', 'POST']

#this is the home page, what is loaded first
@DnDI.route('/dndinfinity', methods = methodlist)
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
            return render_template('DnDIhome.html')


#this is the developer's page, testing things out before putting it on the main site. There is a button at the bottom-left corner in the homepage
@DnDI.route('/dndinfinity/dev')
def DevPage():
    return render_template('DnDIdev.html',)


@DnDI.route('/dndinfinity/dice')
def DicePage():
    return render_template('DnDIdice.html')


#this is the monster page that gains input
@DnDI.route('/dndinfinity/monsters')
def MonsNamePage():

    #first, set the vairiables that will be used during computing
    query_name = 'monsters'
    next_page_link = 'monsterdata'
    form_name = 'monsname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


#this is the monster page that shows/gains data
@DnDI.route('/dndinfinity/monsterdata', methods=['GET', 'POST'])
def MonsDataPage():

    #first, set the vairiables that will be used during computing
    form_name = 'monsname'
    query_name = 'monsters'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


#this is the class page that gains input
@DnDI.route('/dndinfinity/classes')
def ClsNamePage():

    #first, set the vairiables that will be used during computing
    query_name = 'classes'
    next_page_link = 'classdata'
    form_name = 'clsname'
    suffix_to_remove = 'es'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


#this is the class page that shows/gains data
@DnDI.route('/dndinfinity/classdata', methods=methodlist)
def ClsDataPage():

    #first, set the vairiables that will be used during computing
    form_name = 'clsname'
    query_name = 'classes'
    suffix_to_remove = 'es'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/abilityscores', methods=methodlist)
def AbSNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'ability-scores'
    next_page_link = 'abilityscoredata'
    form_name = 'absname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@DnDI.route('/dndinfinity/abilityscoredata', methods=methodlist)
def AbsDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'absname'
    query_name = 'ability-scores'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/spells', methods=methodlist)
def SplNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'spells'
    next_page_link = 'spelldata'
    form_name = 'splname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@DnDI.route('/dndinfinity/spelldata', methods=methodlist)
def SplDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'splname'
    query_name = 'spells'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/races', methods=methodlist)
def RcsNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'races'
    next_page_link = 'racedata'
    form_name = 'rcsname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@DnDI.route('/dndinfinity/racedata', methods=methodlist)
def RcsDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'rcsname'
    query_name = 'races'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/magicitems', methods=methodlist)
def MgiNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'magic-items'
    next_page_link = 'magicitemdata'
    form_name = 'mginame'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@DnDI.route('/dndinfinity/magicitemdata', methods=methodlist)
def MgiDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'mginame'
    query_name = 'magic-items'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/skills', methods=methodlist)
def SklNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'skills'
    next_page_link = 'skilldata'
    form_name = 'sklname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@DnDI.route('/dndinfinity/skilldata', methods=methodlist)
def SklDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'sklname'
    query_name = 'skills'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/magicschools', methods=methodlist)
def MgsNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'magic-schools'
    next_page_link = 'magicschooldata'
    form_name = 'mgsname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@DnDI.route('/dndinfinity/magicschooldata', methods=methodlist)
def MgsDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'mgsname'
    query_name = 'magic-schools'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/equipment', methods=methodlist)
def EqiNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'equipment'
    next_page_link = 'equipmentdata'
    form_name = 'eqiname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@DnDI.route('/dndinfinity/equipmentdata', methods=methodlist)
def EqiDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'eqiname'
    query_name = 'equipment'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/features', methods=methodlist)
def FtuNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'features'
    next_page_link = 'featuredata'
    form_name = 'ftuname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@DnDI.route('/dndinfinity/featuredata', methods=methodlist)
def FtuDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'ftuname'
    query_name = 'features'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/subclasses', methods=methodlist)
def SbcNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'subclasses'
    next_page_link = 'subclassdata'
    form_name = 'sbcname'
    suffix_to_remove = 'es'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@DnDI.route('/dndinfinity/subclassdata', methods=methodlist)
def SbcDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'sbcname'
    query_name = 'subclasses'
    suffix_to_remove = 'es'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/alignments', methods=methodlist)
def AlnNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'alignments'
    next_page_link = 'alignmentdata'
    form_name = 'alnname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)


@DnDI.route('/dndinfinity/alignmentdata', methods=methodlist)
def AlnDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'alnname'
    query_name = 'alignments'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/backgrounds', methods=methodlist)
def BgdNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'backgrounds'
    next_page_link = 'backgrounddata'
    form_name = 'bgdname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)



@DnDI.route('/dndinfinity/backgrounddata', methods=methodlist)
def BgdDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'bgdname'
    query_name = 'backgrounds'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/conditions', methods=methodlist)
def ConNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'conditions'
    next_page_link = 'conditiondata'
    form_name = 'conname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)



@DnDI.route('/dndinfinity/conditiondata', methods=methodlist)
def ConDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'conname'
    query_name = 'conditions'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/damage-types', methods=methodlist)
def DmtNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'damage-types'
    next_page_link = 'damage-typedata'
    form_name = 'dmtname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)



@DnDI.route('/dndinfinity/damage-typedata', methods=methodlist)
def DmtDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'dmtname'
    query_name = 'damage-types'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/equipment-categories', methods=methodlist)
def EqcNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'equipment-categories'
    next_page_link = 'equipment-categorydata'
    form_name = 'eqcname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)



@DnDI.route('/dndinfinity/equipment-categorydata', methods=methodlist)
def EqcDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'eqcname'
    query_name = 'equipment-categories'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/feats', methods=methodlist)
def FetNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'feats'
    next_page_link = 'featdata'
    form_name = 'fetname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)



@DnDI.route('/dndinfinity/featdata', methods=methodlist)
def FetDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'fetname'
    query_name = 'feats'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/languages', methods=methodlist)
def LanNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'languages'
    next_page_link = 'languagedata'
    form_name = 'lanname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)



@DnDI.route('/dndinfinity/languagedata', methods=methodlist)
def LanDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'lanname'
    query_name = 'languages'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/proficiencies', methods=methodlist)
def PofNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'proficiencies'
    next_page_link = 'proficienciedata'
    form_name = 'pofname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)



@DnDI.route('/dndinfinity/proficienciedata', methods=methodlist)
def PofDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'pofname'
    query_name = 'proficiencies'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/rule-sections', methods=methodlist)
def RlsNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'rule-sections'
    next_page_link = 'rule-sectiondata'
    form_name = 'rlsname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)



@DnDI.route('/dndinfinity/rule-sectiondata', methods=methodlist)
def RlsDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'rlsname'
    query_name = 'rule-sections'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/rules', methods=methodlist)
def RulNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'rules'
    next_page_link = 'ruledata'
    form_name = 'rulname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)



@DnDI.route('/dndinfinity/ruledata', methods=methodlist)
def RulDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'rulname'
    query_name = 'rules'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/subraces', methods=methodlist)
def SbrNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'subraces'
    next_page_link = 'subracedata'
    form_name = 'sbrname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)



@DnDI.route('/dndinfinity/subracedata', methods=methodlist)
def SbrDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'sbrname'
    query_name = 'subraces'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/traits', methods=methodlist)
def TrtNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'traits'
    next_page_link = 'traitdata'
    form_name = 'trtname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)



@DnDI.route('/dndinfinity/traitdata', methods=methodlist)
def TrtDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'trtname'
    query_name = 'traits'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/weapon-properties', methods=methodlist)
def WppNamePage():
    #first, set the vairiables that will be used during computing
    query_name = 'weapon-properties'
    next_page_link = 'weapon-propertiedata'
    form_name = 'wppname'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_input_page(query_name, suffix_to_remove, next_page_link, form_name)



@DnDI.route('/dndinfinity/weapon-propertiedata', methods=methodlist)
def WppDataPage():
    #first, set the vairiables that will be used during computing
    form_name = 'wppname'
    query_name = 'weapon-properties'
    suffix_to_remove = 's'

    #then we create the data page, all code for the functions are in func.py
    return create_data_page(form_name, query_name, suffix_to_remove)


@DnDI.route('/dndinfinity/custom-urls', methods=methodlist)
def CtuInputPage():
    
    #first set the variables that will be needed during the computing
    form_name = 'ctuname'
    next_page_link = 'custom-urldata'
    
    #at the end, render the html template so it can be seen on screen
    return render_template(
        'DnDIctuinput.html', 
        form_name=form_name,
        next_page_link = next_page_link,
    )


@DnDI.route('/dndinfinity/custom-urldata', methods=methodlist)
def CtuDataPage():

    #first, set the form name that will be needed during the computing
    form_name = 'ctuname'

    #create the code for the custom data page, the code can be overiewed in func.py
    user_input, json_data, image, url, urls = create_code_for_custom_data_page(form_name)

    #at the end, render the html template so it can be seen on screen
    return render_template(

        'DnDIctudata.html',
        user_input = user_input, 
        json_data = json.dumps(
        
            json_data, 
            indent = 4,

        ), 
        image = image,
        url = url,
        urls = urls,

    )