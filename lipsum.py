# encoding: utf-8

import sys
from workflow import Workflow, ICON_WEB, web


def main(wf):
    wf.add_item(
        title="lipsum",
        arg="lipsum"
    )
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
