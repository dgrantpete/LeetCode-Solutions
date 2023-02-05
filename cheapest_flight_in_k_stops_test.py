# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cities = [[] for _ in range(n)]
        cost_to_city: List[int | float] = [float('inf')] * n
        
        cost_to_city[src] = 0 # It is free to get to the starting location

        for source, destination, flight_price in flights:
            cities[source].append((destination, flight_price))
        
        queue = [src] # Deque doesn't need to be used since buffer will fill from queue contiguously

        # Buffer below serves two purposes:
        # 1. It allows us to keep track of our current depth. Since we are adding to the buffer instead
        # of directly to the queue, we know that each time the queue is exhausted the current depth
        # has been fully searched.
        # 2. It allows us to defer the price updates until after the current depth has been searched.
        # (We don't want a node in the queue to be able to take advantage of a lower price from an
        # earlier node in the queue that shouldn't be available until the next depth is reached).
        buffer = {}

        for _ in range(k + 1):

            while queue:
                city = queue.pop()
                base_price = cost_to_city[city]

                for destination, flight_price in cities[city]:
                    total_price = flight_price + base_price
                    if cost_to_city[destination] > total_price:
                        # Ensures that buffer only keeps minimum price, and that if the buffer doesn't
                        # have a value that 'total_price' will always be selected.
                        buffer[destination] = min(buffer.get(destination, float('inf')), total_price)

            # If buffer is empty there are no more nodes to search, so we can escape early.
            # (We also don't need to update any prices since there is nothing to update)
            if not buffer:
                break
            
            for updated_city, updated_price in buffer.items():
                queue.append(updated_city)
                cost_to_city[updated_city] = updated_price

            buffer.clear()

        if cost_to_city[dst] == float('inf'):
            return -1
        else:
            return cost_to_city[dst] # type: ignore

# Test cases

def test_findCheapestPrice():
    s = Solution()
    assert s.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1) == 700
    assert s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1) == 200
    assert s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0) == 500

if __name__ == "__main__":
    test_findCheapestPrice()
    