#!/usr/bin/python3

# Just add some liraries that are usually needed. Ignore this
from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

# This creates a section of website
bp = Blueprint('math', __name__, url_prefix='/math')

# Now start adding functions for different parts of the site

@bp.route('/add', methods=('GET', 'POST'))
def math_add():
    operation = "add"
    answer,error,a,b = math_operation(operation, request)
    return render_template('math.html',
            operation = operation,
            a = a,
            b = b,
            answer = str(answer),
        )


@bp.route('/subtract', methods=('GET', 'POST'))
def math_subtract():
    operation = "subtract"
    answer,error,a,b = math_operation(operation, request)
    return render_template('math.html',
            operation = operation,
            a = a,
            b = b,
            answer = str(answer),
        )

@bp.route('/multiply', methods=('GET', 'POST'))
def math_multiply():
    operation = "multiply"
    answer,error,a,b = math_operation(operation, request)
    return render_template('math.html',
            operation = operation,
            a = a,
            b = b,
            answer = str(answer),
        )

def math_operation(operation,request):
    error = None
    answer = ""
    a = 0
    b = 0

    if request.method == 'POST':
        try:
            a = float(request.form['a'])
        except:
            error = "Could not find number in 'a'"

        try:
            b = float(request.form['b'])
        except:
            error = "Could not find number in 'b'"

        if error is None:
            if operation == "add":
                answer = a + b
            if operation == "subtract":
                answer = a - b
            if operation == "multiply":
                answer = a * b
        else:
            flash(error)

    return answer,error,a,b
