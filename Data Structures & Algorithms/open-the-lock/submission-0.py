class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dset = set(deadends)
        visited = set()
        queue = deque() # "1234", moves
        queue.append(('0000', 0))
        visited.add('0000')
        while queue:
            combo, moves = queue.popleft()
            if combo in dset:
                continue
            if combo == target:
                return moves
            parts = [str(c) for c in combo]
            for i in range(4):
                num = (int(parts[i]) + 1) % 10
                new_str = ""
                for j in range(4):
                    if j != i:
                        new_str += parts[j]
                    else:
                        new_str += str(num)
                if new_str not in visited:
                    queue.append((new_str, moves + 1))
                    visited.add(new_str)
                num = (int(parts[i]) - 1) % 10
                new_str = ""
                for j in range(4):
                    if j != i:
                        new_str += parts[j]
                    else:
                        new_str += str(num)
                if new_str not in visited:
                    queue.append((new_str, moves + 1))
                    visited.add(new_str)
        return -1