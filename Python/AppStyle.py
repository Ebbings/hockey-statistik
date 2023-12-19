Style = """
QMainWindow{
background-color: {{prim_bk}};
}


QWidget{
background-color: {{prim_bk}};
border-radius: {{holder_rad}};
}

QStackedWidget{
background-color: {{sec_bk}};
border-radius: {{holder_rad}};
}

QGroupBox{
background-color: {{sec_bk}};
border-radius: {{holder_rad}};
}

QScrollArea{
background-color: {{sec_bk}};
border-radius: {{holder_rad}};
}

QPushButton{
border-radius: {{comp_rad}};
background-color: {{prim_fg}};
border: 2px solid {{sec_fg}};
border-left: none;
border-right: none;
border-top: none;
border-bottom-left-radius: 0px;
border-bottom-right-radius: 0px;
}

QPushButton:hover{
border-radius: {{comp_rad}};
background-color: {{hover_prim_fg}};
border: 2px solid {{sec_fg}};
border-left: none;
border-right: none;
border-top: none;
border-bottom-left-radius: 0px;
border-bottom-right-radius: 0px;
}

QPushButton:pressed{
border-radius: {{comp_rad}};
background-color: {{hover_prim_fg}};
border: 2px solid {{sec_fg}};
border-left: none;
border-right: none;
border-top: none;
border-bottom-left-radius: 0px;
border-bottom-right-radius: 0px;
}

QLineEdit{
border-radius: {{comp_rad}};
background-color: {{prim_fg}};
border: 2px solid {{sec_fg}};
border-left: none;
border-right: none;
border-top: none;
border-bottom-left-radius: 0px;
border-bottom-right-radius: 0px;
}


QLineEdit:focus{
border-radius: {{comp_rad}};
background-color: {{hover_prim_fg}};
border: 2px solid {{sec_fg}};
border-left: none;
border-right: none;
border-top: none;
border-bottom-left-radius: 0px;
border-bottom-right-radius: 0px;
}


QTextEdit{
border-radius: {{comp_rad}};
background-color: {{prim_fg}};
border: 2px solid {{sec_fg}};
border-left: none;
border-right: none;
border-top: none;
border-bottom-left-radius: 0px;
border-bottom-right-radius: 0px;
}

QTextEdit:focus{
border-radius: {{comp_rad}};
background-color: {{hover_prim_fg}};
border: 2px solid {{sec_fg}};
border-left: none;
border-right: none;
border-top: none;
border-bottom-left-radius: 0px;
border-bottom-right-radius: 0px;
}


QLabel{
background-color:none;
}
"""
str_color_mainback = "#e9e9e9"
str_color_maingroup = "#f7f7f7"
str_main = "#e9e9e9"
str_accent = "#818290"
str_hover = "#f0f0f0"
holder_rad = "8px"
comp_rad = "6px"
#str_color_30 = "blue"
Style = Style.replace("{{prim_bk}}", str_color_mainback)
Style = Style.replace("{{sec_bk}}", str_color_maingroup)
Style = Style.replace("{{prim_fg}}", str_main)
Style = Style.replace("{{sec_fg}}", str_accent)
Style = Style.replace("{{hover_prim_fg}}", str_hover)
Style = Style.replace("{{sec_fg}}", str_accent)
Style = Style.replace("{{hover_prim_fg}}", str_hover)
Style = Style.replace("{{holder_rad}}", holder_rad)
Style = Style.replace("{{comp_rad}}", comp_rad)
#style = style.replace("{{hover_color_30}}", str_color_30)
