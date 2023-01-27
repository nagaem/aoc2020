import re
import collections


class DAG:
    nodes = []
    edges = collections.defaultdict(list)

    def parseLine(self, line):
        bag_groups = re.split(r" bags contain | bag, | bags, | bag\.| bags\.", line)
        containing_bag = bag_groups[0]

        # Get index of containing bag
        if containing_bag not in self.nodes:
            self.nodes.append(containing_bag)
        from_ind = self.nodes.index(containing_bag)

        for group in bag_groups[1:]:
            # regex has one empty match at end (w/e), or sometimes there's no other bags contained
            if len(group) == 0 or group == "no other":
                continue

            num_edges = group[0]
            bag = group[2:]

            # get index of contained bag
            if bag not in self.nodes:
                self.nodes.append(bag)
            to_ind = self.nodes.index(bag)

            # add edges to graph
            for edge in range(int(num_edges)):
                self.edges[from_ind].append(to_ind)

    def traverse(self, src, visited, exclusive=True):
        # simple df travel algorithm
        for node in [e for e in self.edges[src]]:
            if exclusive and visited[node]:
                continue
            visited[node] += 1
            self.traverse(node, visited, exclusive)

    def findRoutes(self, dest):
        dest_idx = self.nodes.index(dest)
        paths = 0
        # find routes with length at least 1 to dest node
        for node in [n for n in self.nodes if n != dest]:
            visited = [0] * len(self.nodes)
            self.traverse(self.nodes.index(node), visited)
            if visited[dest_idx]:
                paths += 1

        return paths

    def countBags(self, src):
        bags = 0
        visited = [0] * len(self.nodes)
        self.traverse(self.nodes.index(src), visited, exclusive=False)
        return sum(visited)

    def __str__(self):
        return f"{self.nodes}\n\n{self.edges}"


if __name__ == "__main__":
    g = DAG()
    with open("./day7/input.py") as f:
        for line in f:
            g.parseLine(line.strip())

    print(
        f"{g.findRoutes('shiny gold')} bag colors can eventually contain at least one shiny gold bag"
    )
    print(f"Shiny gold bags must contain {g.countBags('shiny gold')} other bags.")
