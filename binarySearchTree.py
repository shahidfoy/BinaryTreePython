class BinarySearchTree:
    class __Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

        def getVal(self):
            return self.val

        def setVal(self, newval):
            self.val = newval

        def getLeft(self):
            return self.left

        def getRight(self):
            return self.right

        def setLeft(self, newleft):
            self.left = newleft

        def setRight(self, newright):
            self.right = newright

        def deleteSelf(self):
            self.val = None

        # gets values in ascending order
        def __iter__(self):
            if self.left is not None:
                for elem in self.left:
                    yield elem

            yield self.val

            if self.right is not None:
                for elem in self.right:
                    yield elem

    # methods for binary search tree
    def __init__(self):
        self.root = None

    def insert(self, val):

            def __insert(root, val):
                if root is None:
                    return BinarySearchTree.__Node(val)

                if val < root.getVal():
                    root.setLeft(__insert(root.getLeft(), val))
                else:
                    root.setRight(__insert(root.getRight(), val))

                return root

            self.root = __insert(self.root, val)

    def search(self, val):

        def __search(root, val):
            try:
                current = root.getVal()
                if current == val:
                    return "Exists in the tree"
                elif val < current:
                    return __search(root.getLeft(), val)
                else:
                    return __search(root.getRight(), val)
            except AttributeError:
                return "Item does not exist"

        checkExistance = __search(self.root, val)
        return checkExistance

    def delete(self, val):

        def __delete(root, value):
            current = root.getVal()
            val = value
            currentLeft = root.getLeft()
            currentRight = root.getRight()

            def findLarge(root, parent, count):
                if count == 0:
                    if root.getRight() is None:
                        parent.setLeft(root.getLeft())
                        return root
                    else:
                        count += 1
                        prev = root
                        return findLarge(root.getRight(), prev, count)
                elif count > 0:
                    if root.getRight() is None:
                        parent.setRight(root.getLeft())
                        return root
                    else:
                        count += 1
                        prev = root
                        return findLarge(root.getRight(), prev, count)

            if current == value:
                count = 0

                if root.getLeft() is None and root.getRight() is not None:
                    root.setVal(root.getRight().getVal())
                    sol = findLarge(root.getRight(), root, count)
                    currentRight.setVal(sol.getVal())

                elif root.getLeft() is not None and root.getRight() is None:
                    root.setVal(root.getLeft().getVal())
                    sol = findLarge(root.getLeft(), root, count)
                    currentLeft.setVal(sol.getVal())

                else:
                    sol = findLarge(root.getLeft(), root, count)
                    root.setVal(sol.getVal())

            else:
                if currentLeft is not None:
                    if currentLeft.getVal() == val:
                        current = currentLeft
                        newLeft = currentLeft.getLeft()
                        newRight = currentLeft.getRight()
                        if currentLeft.getLeft() is None and currentLeft.getRight() is None:
                            root.setLeft(None)

                        elif newLeft is not None and newRight is None:
                            root.setLeft(newLeft)

                        elif newRight is not None and newLeft is None:
                            root.setLeft(newRight)

                        elif newLeft is not None and newRight is not None:
                            # find largest on the left)
                            count = 0

                            sol = findLarge(newLeft, current, count)
                            currentLeft.setVal(sol.getVal())

                    else:
                        __delete(root.getLeft(), val)

                if currentRight is not None:
                    if currentRight.getVal() == val:
                        current = currentRight
                        newLeft = currentRight.getLeft()
                        newRight = currentRight.getRight()
                        if currentRight.getLeft() is None and currentRight.getRight() is None:
                            root.setRight(None)

                        elif newRight is not None and newLeft is None:
                            root.setRight(newRight)

                        elif newLeft is not None and newRight is None:
                            root.setRight(newLeft)

                        elif newRight is not None and newLeft is not None:
                            # find largest on the left
                            count = 0

                            sol = findLarge(newLeft, current, count)
                            currentRight.setVal(sol.getVal())

                    else:
                        __delete(root.getRight(), val)

        __delete(self.root, val)

    def __iter__(self):
        if self.root is not None:
            return self.root.__iter__()
        else:
            return [].__iter__()


def main():
    s = input("Enter a list of numbers: ")
    lst = s.split()

    tree = BinarySearchTree()

    for x in lst:
        tree.insert(float(x))

    tree.delete(8)

    for x in tree:
        print(x)

    # print("item " + str(tree.search(3)))

"""
    for x in tree:
        if x == 3:
            print("Item Exists")
"""


if __name__ == '__main__':
    main()
