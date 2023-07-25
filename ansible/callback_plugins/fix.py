from __future__ import (absolute_import, division, print_function)
try:
    from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionRootPkgLoader
    apply_fix = True
except:
    apply_fix = False
__metaclass__ = type


from ansible import constants as C
from ansible import context
from ansible.playbook.task_include import TaskInclude
from ansible.plugins.callback import CallbackBase
from ansible.utils.color import colorize, hostcolor


class CallbackModule(CallbackBase):

    '''
    This is the default callback interface, which simply prints messages
    to stdout when new callback events are received.
    '''

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'fix'
    CALLBACK_NAME = 'fix_collections'

    def __init__(self):

        super(CallbackModule, self).__init__()

    def v2_runner_on_ok(self, result):
        if apply_fix:
            if "cmd" in self._dump_results(result._result, serialize=False):
                if self._dump_results(result._result, serialize=False)['cmd'][0] == "ansible-galaxy":
                    loader = _AnsibleCollectionRootPkgLoader(
                      'ansible_collections', C.COLLECTIONS_PATHS
                    )
                    loader.load_module('ansible_collections')
