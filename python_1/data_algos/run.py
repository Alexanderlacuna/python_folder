class Solution(object):
	def twoSum(self, nums, target):

		d={}
		for i,n in enumerate(nums):
			m=target-n
			if  m in d:
				return [d[m]-1]

			else:
				d[n]=i
		
  

c=Solution()

ari=[1,6,7,4,3,5,5,3]
print(c.twoSum(ari,12))