class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer=[]
        for i in range(0, n):
            j=i+1
            if j%3 ==0 and j%5==0:
                answer.append("FizzBuzz")
            elif j%3==0:
                answer.append("Fizz")
            elif j%5==0:
                answer.append("Buzz")
            else:
                answer.append(str(j))
        return answer

# Time complexity = O(n)
# Space complexity = O(n)