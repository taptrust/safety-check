#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import render_template
from project import app
import logging


@app.route('/')
def root():
    """Serve the home page of the web app."""
    return render_template('landing_page.html')


if __name__ == '__main__':

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s'
    )
    port = int(os.environ.get("PORT", 5000))
    app.run('0.0.0.0', port=port)
