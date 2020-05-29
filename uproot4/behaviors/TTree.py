# BSD 3-Clause License; see https://github.com/scikit-hep/uproot4/blob/master/LICENSE

from __future__ import absolute_import


class TTree(object):
    @property
    def name(self):
        return self.member("fName")

    @property
    def title(self):
        return self.member("fTitle")