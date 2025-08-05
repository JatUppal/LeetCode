from collections import deque, defaultdict
from typing import List

class Excel:

    def __init__(self, height: int, width: str):
        self.h = height
        self.w = ord(width) - ord('A') + 1
        self.mat = [[0] * self.w for _ in range(height)]  # Matrix values
        self.formulas = {}  # (r, c) -> { (ri, ci): count } formula definition
        self.dependents = {}  # (r, c) -> set of (rj, cj) cells that depend on this cell

    def col_to_index(self, col: str) -> int:
        return ord(col) - ord('A')

    def set(self, row: int, column: str, val: int) -> None:
        r = row - 1
        c = self.col_to_index(column)

        # Clear existing formula
        if (r, c) in self.formulas:
            del self.formulas[(r, c)]

        self.mat[r][c] = val
        self.propagate_update(r, c)  # Update all dependent formulas

    def get(self, row: int, column: str) -> int:
        r = row - 1
        c = self.col_to_index(column)
        return self.mat[r][c]  # Always return stored value

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        r = row - 1
        c = self.col_to_index(column)
        formula = {}

        # Parse all input strings into formula dependencies
        for s in numbers:
            if ':' in s:
                start, end = s.split(':')
                r1, c1 = int(start[1:]) - 1, self.col_to_index(start[0])
                r2, c2 = int(end[1:]) - 1, self.col_to_index(end[0])
                for i in range(r1, r2 + 1):
                    for j in range(c1, c2 + 1):
                        formula[(i, j)] = formula.get((i, j), 0) + 1
            else:
                ri = int(s[1:]) - 1
                ci = self.col_to_index(s[0])
                formula[(ri, ci)] = formula.get((ri, ci), 0) + 1

        # Save formula and update reverse dependency map
        self.formulas[(r, c)] = formula

        for key in formula:
            if key not in self.dependents:
                self.dependents[key] = set()
            self.dependents[key].add((r, c))

        total = self.calculate_formula(r, c)
        self.mat[r][c] = total
        self.propagate_update(r, c)  # Propagate to dependents
        return total

    def calculate_formula(self, r: int, c: int) -> int:
        formula = self.formulas[(r, c)]
        total = 0
        for (ri, ci), count in formula.items():
            val = self.mat[ri][ci]
            total += val * count
        return total

    def propagate_update(self, r: int, c: int):
        in_degree = defaultdict(int)
        graph = defaultdict(set)
        queue = deque()

        # Step 1: Build dependency graph of all affected cells
        visited = set()
        queue.append((r, c))
        visited.add((r, c))

        while queue:
            curr_r, curr_c = queue.popleft()
            if (curr_r, curr_c) in self.dependents:
                for dep_r, dep_c in self.dependents[(curr_r, curr_c)]:
                    if (dep_r, dep_c) not in visited:
                        queue.append((dep_r, dep_c))
                        visited.add((dep_r, dep_c))
                    in_degree[(dep_r, dep_c)] += 1
                    graph[(curr_r, curr_c)].add((dep_r, dep_c))

        # Step 2: Topological sort
        queue = deque()
        topo_sorted = []

        for cell in visited:
            if in_degree[cell] == 0:
                queue.append(cell)

        while queue:
            curr = queue.popleft()
            topo_sorted.append(curr)
            for neighbor in graph[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 3: Update all cells in topological order
        for cell in topo_sorted[1:]:  # Skip first cell (already updated)
            if cell in self.formulas:
                val = self.calculate_formula(cell[0], cell[1])
                self.mat[cell[0]][cell[1]] = val
