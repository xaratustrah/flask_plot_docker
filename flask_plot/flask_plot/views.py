# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from flask_plot.forms import InputForm
from flask_plot.model import compute
from flask_plot import app

Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.A.data, form.b.data,
                         form.w.data, form.T.data)
    else:
        result = None

    return render_template('view_bootstrap.html', form=form, result=result)
