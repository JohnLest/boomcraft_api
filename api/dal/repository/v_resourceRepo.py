from tools.genericRepository.genericRepo import GenericRepo


class VResourceRepo(GenericRepo):
    def __init__(self, session, table):
        GenericRepo.__init__(self, session, table)
