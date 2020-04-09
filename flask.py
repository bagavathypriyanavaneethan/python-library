# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:16:53 2020

@author: Bagavathi Priya
"""

'''from app import db
db.create_all()
'''

from flask import Flask

 
app=Flask(__name__)
print(app)

@app.route('/')
def bpriya():
    return "priya the cool"
    #return 
    
if __name__ =='__main__':
    app.run(debug=False)