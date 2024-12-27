class Graph:
    def __init__(self, initial, goal):
        self.edges = {"Arad": ["Zerind", "Timisoara", "Sibiu"], "Eforie": ["Hirsova"], "Zerind": ["Oradia", "Arad"],
                      "Oradia": ["Sibiu", "Zerind"], "Mehadia": ["Drobeta", "Lugoj"], "Giurgiu": ["Bucharest"],
                      "Timisoara": ["Lugoj", "Arad"], "Lugoj": ["Mehadia", "Timisoara"],
                      "Drobeta": ["Craiova", "Mehadia"],
                      "Sibiu": ["Fagaras", "Rimnicu", "Oradia", "Arad"], "Craiova": ["Rimnicu", "Pitesti", "Drobeta"],
                      "Rimnicu": ["Craiova", "Pitesti", "Sibiu"], "Fagaras": ["Bucharest", "Sibiu"],
                      "Pitesti": ["Bucharest", "Rimnicu", "Craiova"],
                      "Bucharest": ["Giurgiu", "Urziceni", "Pitesti", "Fagaras"],
                      "Urziceni": ["Hirsova", "Vasluni", "Bucharest"], "Hirsova": ["Eforie", "Urziceni"],
                      "Neamt": ["Iasi"],
                      "Vasluni": ["Iasi", "Urziceni"], "Iasi": ["Neamt", "Vasluni"],
                      }

        self.weights = {"AradZerind": 75, "ZerindOradia": 71, "AradTimisoara": 118, "TimisoaraLugoj": 111,
                        "LugojMehadia": 70,
                        "MehadiaDrobeta": 75, "AradSibiu": 140, "OradiaSibiu": 151, "DrobetaCraiova": 120,
                        "CraiovaRimnicu": 146, "CraiovaPitesti": 138, "SibiuFagaras": 99, "SibiuRimnicu": 80,
                        "RimnicuPitesti": 97, "FagarasBucharest": 211, "PitestiBucharest": 101, "BucharestGiurgiu": 90,
                        "BucharestUrziceni": 85, "UrziceniHirsova": 98, "HirsovaEforie": 86, "UrziceniVasluni": 142,
                        "VasluniIasi": 92, "IasiNeamt": 87}

        self.heuristic = {"Arad": 366, "Zerind": 374, "Oradia": 380, "Timisoara": 329, "Lugoj": 244, "Mehadia": 241,
                          "Hirsova": 120,
                          "Drobeta": 242, "Sibiu": 253, "Craiova": 160, "Rimnicu": 193, "Pitesti": 100, "Fagaras": 176,
                          "Bucharest": 0, "Giurgiu": 77, "Urziceni": 80, "Eforie": 161, "Vasluni": 199, "Iasi": 226,
                          "Neamt": 234}
        self.initial_state = initial
        self.goal = goal


    def actions(self, node):
        return self.edges[node]

    def goal_test(self, node):
        if node == self.goal:
            return True

    def get_cost(self, from_node, to_node):
        if from_node == to_node:
            return 0
        else:
            list_weights = list(self.weights.keys())
            if (from_node + to_node) in list_weights:
                return self.weights[(from_node + to_node)]
            else:
                return self.weights[(to_node + from_node)]

    def heuristicc(self, node):
        return self.heuristic[node]


class Child_node:
    def __init__(self, problem, node, child):
        print(f"Yeni Child_node oluşturuluyor: {child}")
        self.state = child
        self.g = problem.get_cost(node.state, child)
        self.h = problem.heuristicc(child)
        self.f = self.g + self.h
        print(f"Child_node: state={self.state}, g={self.g}, h={self.h}, f={self.f}")


class Node:
    def __init__(self, state, g, h):
        self.state = state  # Current state
        self.g = g  # Path cost from the initial state to this state
        self.h = h  # Heuristic estimate of cost from this state to a goal


def recursive_best_first_search(problem):
    print("Recursive Best First Search başlatılıyor")
    initial_node = Node(state=problem.initial_state, g=0, h=problem.heuristicc(problem.initial_state))
    path = []
    result, f_value = rbfs(problem, initial_node, float('inf'), path)
    return result, path

def rbfs(problem, node, f_limit, path):
    print(f"RBFS: Şu anki durum {node.state}, f_limit={f_limit}")
    path.append(node.state)  # Add the current node to the path

    if problem.goal_test(node.state):
        print(f"Hedefe ulaşıldı: {node.state}")
        path.append(node.state)
        return node.state, path  # Hedefe ulaşıldığında node'un durumu ve yol döndürülüyor

    successors = []
    for action in problem.actions(node.state):
        child_node = Child_node(problem, node, action)
        successors.append(child_node)

    if not successors:
        print("Başarısızlık, Successors yok")
        return None, float('inf')

    while True:
        successors.sort(key=lambda x: x.f)
        best = successors[0]
        if best.f > f_limit:
            print("Başarısızlık, en iyi f-limit'i aşıyor")
            return None, best.f  # En iyi değer f_limit'i aşıyorsa başarısızlık döndürülüyor

        alternative = successors[1].f if len(successors) > 1 else float('inf')
        result, best_child_f = rbfs(problem, best, min(f_limit, alternative), path)

        best.f = best_child_f  # Best'in f değeri güncelleniyor
        if result:
            return result, path  # Başarılı sonuç bulunduğunda döndürülüyor

if __name__ == '__main__':
    initial = input("Enter the initial state:")
    problem = Graph(initial, 'Bucharest')
    print("The path from Arad to Bucharest using the Recursive Best first search is :\n")
    result, path = recursive_best_first_search(problem)
    print("Visited places:")
    for ele in path:
        print(ele, end='-->')
    print("\nFinal result:")
    if result:
        print(result)