from collections.abc import Container

class ListNode(Container):
        def __init__(self, prio, data):
            self._prio = prio
            self._data = data
            self.next = None

        @property
        def data(self):
            return self._data

        @data.setter
        def data(self, value):
            self._data = value

        @property
        def prio(self):
            return self._prio

        @prio.setter
        def prio(self, value):
            self._prio = value
        
        def __contains__(self, value):
            if self.data == value:
                return True
            else:
                return False

        def __str__(self):
            #return str(self.prio) + ": " + self.data
            return str(self.prio) + ": " + str(self.data)
