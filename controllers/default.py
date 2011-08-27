# -*- coding: utf-8 -*- 

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################  

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html
    """
    response.flash = T('Welcome')
    response.title = T('nicopresto')
    response.subtitle = T('ecology - computing - health')
    return dict()

def cv():
    response.flash = T('PDF updated July 2011')
    response.title = T('nicopresto')
    response.subtitle = T('curriculum vitae - resume')
    goals=db().select(db.goals.ALL)
    current=db().select(db.current.ALL)
    education=db().select(db.education.ALL)
    presentations=db().select(db.presentations.ALL, orderby=~db.presentations.year)
    pubs=db().select(db.publications.ALL, orderby=~db.publications.year)
    work=db().select(db.work.ALL)
    funding=db().select(db.funding.ALL, orderby=~db.funding.year)
    teaching=db().select(db.teaching.ALL)
    societies=db().select(db.societies.ALL)
    referee=db().select(db.referee.ALL)
    volunteer=db().select(db.volunteer.ALL)
    skills=db().select(db.skills.ALL)
    contacts=db().select(db.contacts.ALL)
    return dict(goals=goals, current=current, education=education, presentations=presentations, pubs=pubs, work=work, funding=funding, teaching=teaching, societies=societies, referee=referee, volunteer=volunteer, skills=skills, contacts=contacts)

def about():
    response.flash = T('About Me')
    response.title = T('nicopresto')
    response.subtitle = T('background - current interests')
    return dict()

def projects():
    response.flash = T('Project listings')
    response.title = T('nicopresto')
    response.subtitle = T('projects - projects - projects')
    return dict()

def privacy():
    response.flash = T('Privacy')
    response.title = T('nicopresto')
    response.subtitle = T('privacy - trust')
    return dict()

def terms():
    response.flash = T('Please help yourself')
    response.title = T('nicopresto')
    response.subtitle = T('share - and - share alike')
    return dict()

def index2():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html
    """
    response.flash = T('Welcome to nicopresto.com')
    response.subtitle = T('ecology - computing - health')
    return dict()



def vert():
    return()

def user():
    """
    exposes:
    http://..../[app]/default/user/login 
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    session.forget()
    return service()

