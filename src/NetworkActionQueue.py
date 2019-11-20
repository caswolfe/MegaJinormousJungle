import heapq
import time


from DataPacket import DataPacket


class ActionQueue():

    queue = []

    def __init__(self):
        self.queue = heapq.heapify(self.queue)

    def addChange(self,packet):
        """
        This function adds a change to the priority queue, given parsed data
        See NetworkActionHandler.parse_packet
        Args:
            packet: tuple, data that is to be added
        Returns:
            None, modifies queue() instance variable
        """
        #TODO verify packet structure/data types from parsePacket()
        #should be in the form of tuple(timestamp,content) 

        #TODO verify that heapq supports timestamp comparisons in Python 3.7
        heapq.heappush(self.queue,packet)

    
    def getNextChange(self):
        """
        This function gets the next change off of the priority queue
        Args:
            None
        Returns:
            difference: string that describes the change that needs to be made.
        """
        return heapq.heappop(self.queue)


