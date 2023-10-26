import matplotlib.pyplot as plt


class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None

    def add_left_child(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            self.left_child.add_left_child(value)

    def add_right_child(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            self.right_child.add_right_child(value)

    def invert_bfs(self):
        """swap the left and right children of each node at each level"""
        current_level = [self]
        next_level = []

        while current_level:
            for node in current_level:
                if node.left_child:
                    next_level.append(node.left_child)
                if node.right_child:
                    next_level.append(node.right_child)

                node.left_child, node.right_child = node.right_child, node.left_child

            current_level = next_level
            next_level = []

    def invert_dfs(self):
        """Inverting the left and right subtrees of each node"""
        if self is None:
            return None

        if self.left_child:
            self.left_child.invert_dfs()
        if self.right_child:
            self.right_child.invert_dfs()

        self.left_child, self.right_child = self.right_child, self.left_child

    def visualize(self, color="g"):
        _, ax = plt.subplots(figsize=(8, 6))
        self._plot_tree(ax, 0, 0, 100, color)
        ax.set_aspect("equal")
        ax.axis("off")
        plt.show()

    def _plot_tree(self, ax, x, y, dx, color):
        if self is not None:
            circle = plt.Circle((x, y), radius=5, color=color, fill=True)
            ax.add_patch(circle)
            ax.text(
                x, y, str(self.key), va="center", ha="center", color="w", fontsize=12
            )

            if self.left_child:
                dx_new = dx / 2
                x_left = x - dx_new
                y_left = y - 50
                ax.plot([x, x_left], [y, y_left], color="k")
                self.left_child._plot_tree(ax, x_left, y_left, dx_new, color)

            if self.right_child:
                dx_new = dx / 2
                x_right = x + dx_new
                y_right = y - 50
                ax.plot([x, x_right], [y, y_right], color="k")
                self.right_child._plot_tree(ax, x_right, y_right, dx_new, color)
