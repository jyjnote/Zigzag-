import streamlit as st

from streamlit_option_menu import option_menu

import keyword_visu, model, DashBoard

st.set_page_config(
    page_title = 'Zig-Zag-Service'
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title,function):
        self.apps.append({
            'title' : title,
            'function' : function
        })

    def run():
        with st.sidebar:
            app = option_menu(
                menu_title= 'Zig-Zag',
                options = ['keyword_visu','model','DashBoard'],
                icons = ['house-fill','person-circle','trophy-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles = {
                    'container':{'padding':'5!important','background-color':'pink'},
                    'icon':{'color':'black', 'font-size':'23px'},
                    'nav-link' : {'color': 'white','font-size':'20px','text-align':'left','margin':'0px'},
                    'nav-link-selected' :{'background-color':'#02ab21'}
                         }
                             )
        if app == 'keyword_visu':
            keyword_visu.app()
        if app == 'model':
            model.app()
        if app == 'DashBoard':
            DashBoard.app()

    run()
