from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node_1: int, node_2: int) -> int:
        visited_1 = [False] * len(edges)
        visited_2 = [False] * len(edges)

        while node_1 != -1 or node_2 != -1:
            next_1, next_2 = edges[node_1], edges[node_2]

            visited_1[node_1] = True
            visited_2[node_2] = True

            if visited_1[node_2]:
                return node_2
            if visited_2[node_1]:
                return node_1

            if next_1 != -1:
                node_1 = next_1
            if next_2 != -1:
                node_2 = next_2

        return -1
