from tools.genericRepository.genericRepo import GenericRepo


class NameResourceRepo(GenericRepo):
    def __init__(self, session, table):
        GenericRepo.__init__(self, session, table)
