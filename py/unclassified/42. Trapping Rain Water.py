class Solution:
    def trap(self, height: list[int]) -> int:
        l,r = 0,len(height)-1
        # move ptr thats on smaller number
        # remembering greatest left and right number to count water volume
        gl,gr = 0,0
        # empty array for water map
        waterMap = [0]*len(height)
        while l < r:
            # move l or r whichever's smaller
            if height[l] <= height[r]:
                # if terrain lowers, there's water
                if height[l] < gl:
                    waterMap[l] = gl - height[l]
                else:
                    gl = height[l]
                l += 1
            else:
                # if terrain lowers, there's water
                if height[r] < gr:
                    waterMap[r] = gr - height[r]
                else:
                    gr = height[r]
                r -= 1
        print(waterMap)
        return sum(waterMap)

s = Solution()
print(s.trap([4,2,0,3,2,5]))