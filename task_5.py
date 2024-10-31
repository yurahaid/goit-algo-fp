from collections import deque
from task_4 import Node, draw_tree


def generate_hex_color(value, max_value):
    # Нормалізуємо значення до діапазону [0, 255]
    intensity = int((value / max_value) * 255)
    # Генеруємо HEX-код кольору на основі інтенсивності (R=G=B)
    hex_color = "#{:02x}{:02x}{:02x}".format(intensity, intensity, intensity)
    return hex_color

def dfs(root: Node):
    visited = set()
    stack = deque([root])
    step = 1
    while stack:
        vertex = stack.pop()
        if vertex in visited:
            if vertex.right is not None:
                stack.append(vertex.right)
        else:
            visited.add(vertex)
            vertex.color = generate_hex_color(step, 10)
            step += 1

            if vertex.left is not None:
                stack.append(vertex)
                stack.append(vertex.left)
            elif vertex.right is not None:
                stack.append(vertex)
                stack.append(vertex.right)



def bfs(root: Node):
    visited = set()
    step = 1
    queue = deque([root])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            vertex.color = generate_hex_color(step, 10)
            visited.add(vertex)
            if vertex.left is not None:
                queue.append(vertex.left)
            if vertex.right is not None:
                queue.append(vertex.right)
            step += 1



# Створення дерева
tree = Node(0)
tree.left = Node(4)
tree.left.left = Node(5)
tree.left.right = Node(10)
tree.right = Node(1)
tree.right.left = Node(3)
tree.right.right = Node(1)
tree.right.left.right = Node(3)
tree.right.left.left = Node(6)

# Відображення дерева
dfs(tree)
draw_tree(tree)


bfs(tree)
draw_tree(tree)