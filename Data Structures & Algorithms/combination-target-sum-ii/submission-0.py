class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        cand = []

        def dfs(start):
            total = sum(cand)

            # 已经凑够目标：保存答案，结束当前分支
            if total == target:
                result.append(cand.copy())
                return

            for i in range(start, len(candidates)):

                # 同一层中，相同的数字只尝试一次
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                num = candidates[i]

                # 数组已经升序排列，当前数字都太大，后面更不用试
                if total + num > target:
                    break

                cand.append(num)  # 选择当前数字
                dfs(i + 1)        # 从后面的元素中继续选
                cand.pop()        # 撤销当前选择

        dfs(0)
        return result