# -*- coding: utf-8 -*-
from project import app
from flask import jsonify, render_template, request
import logging
import threading
import requests

@app.route('/security', methods=['POST', 'GET'])
def security():
    logging.info('/security')
    origin = request.remote_addr
    logging.info('Analysis job requested from {}'.format(origin))
    analyzer = SecurityAnalyzer()
    if request.args.get('callback_url'):
        # Async. Start analysis in new thread.
        thread = threading.Thread(target=analyzer.analyze_bytecode,
            args=(blob_id, request.args))
        thread.start()
        return 'success', 200
    else:
        # Synchronous
        response = {
            'analysis': analyzer.analyze_bytecode(request.args.get('bytecode'), request.args)
        }
        return jsonify(response), 200


class SecurityAnalyzer(object):

    def __init__(self, *args, **kwargs):
        pass

    def analyze_bytecode(self, bytecode, args):
        analysis = {
            'mythril': self._mythril(bytecode)
        }
        if args.get('callback_url'):
            # return callback via HTTP request
            # TODO - use some form of auth token etc.
            logging.info('posting analysis result to callback_url')
            requests.post(args.get('callback_url'), json=jsonify(analysis))
        else:
            logging.info('no callback_url specified. Returning analysis')
            return analysis

    def _mythril(self, bytecode):
        logging.info('starting mythril analysis')
        max_depth = 12
        """
        TODO:
            - use mythril (https://github.com/ConsenSys/mythril)
            - use CLI argument for bytecode input and JSON output : myth -xo json -d -c "0x6060" --max-depth 12
            -  Alternatively, bypass the CLI and setup via "import mythril" python code
        """
        mythril_analysis = {
            'config': {
                'max-depth': max_depth
            },
            'results': {
                # TODO put JSON results from mythril here
            }
        }
        return mythril_analysis
