# encoding: utf-8

import sys
from workflow import Workflow
from lipsum import lipsum


def main(wf):
    lipsum(wf, "paras")

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
