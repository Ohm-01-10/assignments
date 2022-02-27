class Towers:
    def __init__(self, disks=3):
        self.disks = disks
        self.towers = [[]]*3
        self.towers[0] = [i for i in range(self.disks, 0, -1)]
        self.towers[1] = []
        self.towers[2] = []
    def __str__(self):
        output = ""
        for i in range(self.disks, -1, -1):
            for j in range(3):
                if len(self.towers[j]) > i:
                    output += " " + str(self.towers[j][i])
                else:
                    output += "  "
            output += "\n"
        return output + "-------"
    def move(self, from_tower, dest_tower):
        disk = self.towers[from_tower].pop()
        self.towers[dest_tower].append(disk)

def solve_tower_of_hanoi(towers, n, start_tower, dest_tower, aux_tower):
    # Base case - do nothing
    if n == 0:
        return
    # Move subproblem of n - 1 disks from start_tower to aux_tower.
    solve_tower_of_hanoi(towers, n - 1, start_tower, aux_tower, dest_tower)
    # Move disk n to dest_tower.
    towers.move(start_tower, dest_tower)
    print(towers)
    # Move subproblem of n - 1 disk from aux_tower to dest_tower.
    solve_tower_of_hanoi(towers, n - 1, aux_tower, dest_tower, start_tower)

t = Towers()
print(t)
solve_tower_of_hanoi(t, len(t.towers), 0, 2, 1)