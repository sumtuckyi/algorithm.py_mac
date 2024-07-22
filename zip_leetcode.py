# zip, sort, lambda 연습 - 2418
class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        new_arr = list(zip(names, heights))
        sorted_arr = sorted(new_arr, key=lambda x: x[1], reverse=True)

        return [element[0] for element in sorted_arr]