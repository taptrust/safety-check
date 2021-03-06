#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import render_template, request, jsonify
from project import app
import logging
from importlib import import_module

SUCCESS = 200
BAD_REQUEST = 400
FORBIDDEN = 403
NOT_FOUND = 404


@app.route('/')
def root():
    """Serve the home page of the web app."""
    return render_template('landing_page.html')


@app.route('/ajax', methods=['GET', 'POST'])
def ajaxHandler():
    # import pudb; pudb.set_trace();
    origin = request.remote_addr
    logging.info('Request from {}'.format(origin))
    module = request.args.get('module')
    file = request.args.get('file')
    method = request.args.get('method')
    logging.info('Target method {}'.format(module + '/' + file + '/' + method))
    try:
        kwargs = request.get_json()
    except:
        return jsonify({
            'success': False,
            'message': 'Could not parse request JSON'
        }), BAD_REQUEST

    try:
        function = getattr(import_module('.'.join(['project', module, file])),
                           method)
    except:
        return jsonify({
            'success': False,
            'message': 'Method not found.'
        }), NOT_FOUND

    try:
        data = function(**kwargs)
        return jsonify({'success': True, 'data': data})

    except:
        return jsonify({
            'message': 'Something failed. Please contact TapTrust Support.',
            'success': False
            }), BAD_REQUEST


if __name__ == '__main__':

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s'
    )
    port = int(os.environ.get("PORT", 5000))
    app.run('0.0.0.0', port=port)
