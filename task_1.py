class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        last_node = self.head
        if last_node is None or last_node.next is None:
            return

        while last_node.next:
            last_node = last_node.next

        current = self.head
        while current != last_node:
            self.delete_node(current.data)
            self.insert_after(last_node, current.data)
            current = self.head

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        current = self.head
        while current is not None:
            next_after_current = current.next

            sorted_part = self.head
            while current != sorted_part:
                if current.data < sorted_part.data:
                    self.delete_node(current.data)
                    if self.head == sorted_part:
                        self.insert_at_beginning(current.data)
                    else:
                        prev_for_insert = self.head
                        while prev_for_insert.next != sorted_part:
                            prev_for_insert = prev_for_insert.next

                        self.insert_after(prev_for_insert, current.data)

                    break

                sorted_part = sorted_part.next

            current = next_after_current


def merge_sorted_ll(l1: LinkedList, l2: LinkedList) -> LinkedList:
    merged_ll = LinkedList()
    l1_item, l2_item = l1.head, l2.head
    while l1_item is not None or l2_item is not None:
        if l1_item is not None and l2_item is not None:
            if l1_item.data <= l2_item.data:
                merged_ll.insert_at_end(l1_item.data)
                l1_item = l1_item.next

                continue
            merged_ll.insert_at_end(l2_item.data)
            l2_item = l2_item.next
        elif l1_item is not None:
            merged_ll.insert_at_end(l1_item.data)
            l1_item = l1_item.next
        elif l2_item is not None:
            merged_ll.insert_at_end(l2_item.data)
            l2_item = l2_item.next

    return merged_ll


llist = LinkedList()

llist.insert_at_end(5)
llist.insert_at_end(15)
llist.insert_at_end(10)
llist.insert_at_end(35)
llist.insert_at_end(25)

print("Зв'язний список:")
llist.print_list()

print("Обернений зв'язний список:")
llist.reverse()
llist.print_list()

# Друк зв'язного списку
print("Сортований зв'язний список:")
llist.insertion_sort()
llist.print_list()

llist2 = LinkedList()

llist2.insert_at_end(5)
llist2.insert_at_end(12)
llist2.insert_at_end(13)
llist2.insert_at_end(14)
llist2.insert_at_end(14)
llist2.insert_at_end(23)
llist2.insert_at_end(35)
llist2.insert_at_end(37)
llist2.insert_at_end(39)
llist2.insert_at_end(41)

# Друк зв'язного списку
print("Сортований зв'язний список - 2:")
llist2.print_list()

print("Змержені сортовані списки")
merge_sorted_ll(llist, llist2).print_list()
