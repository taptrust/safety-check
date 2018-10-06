# -*- coding: utf-8 -*-
# from flask import jsonify, request
import logging
# import threading
# import requests
from mythril.mythril import Mythril


# class SecurityAnalyzer(object):

# def __init__(self, *args, **kwargs):
#         pass


def security(bytecode):
    # logging.info('/security')
    # logging.info('Analysis job requested from {}'.format(origin))
    # analyzer = SecurityAnalyzer()
    # if request.args.get('callback_url'):
    #     # Async. Start analysis in new thread.
    #     blob_id = ''
    #     thread = threading.Thread(target=analyzer.analyze_bytecode,
    #                               args=(blob_id, request.args))
    #     thread.start()
    #     return 'success', 200
    # else:
        # Synchronous
        # response = {
        #     'analysis': _mythril(bytecode)
        # }
    return _mythril(bytecode)

# def analyze_bytecode(self, bytecode, args):
#     analysis = {
#         'mythril': self._mythril(bytecode)
#     }
#     if args.get('callback_url'):
#         # return callback via HTTP request
#         # TODO - use some form of auth token etc.
#         logging.info('posting analysis result to callback_url')
#         requests.post(args.get('callback_url'), json=jsonify(analysis))
#     else:
#         logging.info('no callback_url specified. Returning analysis')
#         return analysis


def _mythril(bytecode):
    # import pudb; pudb.set_trace();
    logging.info('starting mythril analysis')
    max_depth = 12
    mythril = Mythril()
    address, contract_object = mythril.load_from_bytecode(bytecode)
    issues = mythril.fire_lasers(strategy="dfs", verbose_report=True,
                                 contracts=[contract_object],
                                 address=address, max_depth=max_depth,
                                 execution_timeout=30, create_timeout=30,
                                 modules=None)
    return issues.as_text()  # issues.as_json() also available
