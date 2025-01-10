from __future__ import annotations

from docutils import nodes

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective, SphinxRole
# from sphinx.util.typing import ExtensionMetadata

class DocNumRole(SphinxRole):
    # doc_count = 0
    doc_num = [0]

    # def _find_level(self, tree, target, level=0) -> int:
    #     for node in tree.children:
    #         if isinstance(node, nodes.reference) and node['refuri'] == f'{target}.html':
    #             return level
    #     return -1

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:

        text = ''

        # if self.doc_num == 0:
        #     print('DOC TOCS:')
        #     print(self.env.tocs.get(self.env.docname))

        for cmd in self.text.split(' '):
            if cmd == 'step-super':
                if len(self.doc_num) == 1:
                    self.doc_num[0] += 1
                else:
                    self.doc_num.pop()
                    self.doc_num[-1] += 1
            elif cmd == 'step':
                self.doc_num[-1] += 1
            elif cmd == 'step-sub':
                self.doc_num.append(0) #Should I set this to 1?
            elif cmd == 'ref':
                text += ('{}.' * len(self.doc_num))[:-1].format(*self.doc_num)
            elif cmd == 'ref-super':
                text += ('{}.' * (len(self.doc_num) - 1))[:-1].format(*self.doc_num[:-1])

        node = nodes.inline(text=text)
        # self.doc_count += 1
        # node = nodes.inline(text=f'{self.doc_count}')

        return [node], []
    
def setup(app : Sphinx): #-> ExtensionMetadata:
    print('DOCNUM SETUP #######################################################################################')
    app.add_role('docnum', DocNumRole())

    return {
        'version' : '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': False,
    }