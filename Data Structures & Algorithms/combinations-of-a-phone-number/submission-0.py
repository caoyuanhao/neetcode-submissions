class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        
        res=[]
        d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        def backtrak(index,path):
            if index==len(digits):
                res.append("".join(path))
                return 

            for i in d[digits[index]]:
                
                path.append(i)
                backtrak(index+1,path)
                path.pop()
        backtrak(0,[])
        return res