class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1: 
            return 1
        
        if target == 1:
            return 1
      
        pos_to_hours = {}
        for i, pos in enumerate(position):
            pos_to_hours[pos] = (target-pos)/ speed[i]

        # sort for position 
        sorted_position = sorted(position, reverse=True)

        # If a car has hours to arrive slower than the next position, they should merge into fleet
        #  4,1,0,7        
        #  7,4,1,0
        #  3 3 5 10

        # Meaning we can use a stack, if the next position is faster, we dont accept and merge into the latest position
        stack = []

        for pos in sorted_position:
            hours = pos_to_hours[pos]

            if len(stack) == 0:
                stack.append(hours)
            elif stack and stack[-1] < hours:
                stack.append(hours)


        print(stack)
        return len(stack)