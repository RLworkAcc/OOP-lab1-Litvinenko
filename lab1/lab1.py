class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


# кольцевой список
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            node.next = node
            return
        tail = self.head
        while tail.next != self.head:
            tail = tail.next
        node.next = self.head
        self.head = node
        tail.next = self.head

    def add_last(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            node.next = node
            return
        tail = self.head
        while tail.next != self.head:
            tail = tail.next
        tail.next = node
        node.next = self.head

    def add_after(self, target, value):
        if not self.head: return False
        current = self.head
        while True:
            if current.value == target:
                node = Node(value)
                node.next = current.next
                current.next = node
                return True
            current = current.next
            if current == self.head: break
        return False

    def delete_if(self, condition):
        if not self.head: return
        while self.head and condition(self.head.value):
            tail = self.head
            while tail.next != self.head: tail = tail.next
            self.head = self.head.next
            tail.next = self.head
            if self.head == tail: return
        current = self.head
        while current and current.next != self.head:
            if condition(current.next.value):
                current.next = current.next.next
            else:
                current = current.next

    def delete_first(self):
        if not self.head: return
        self.delete_if(lambda x: x == self.head.value)

    def delete_last(self):
        if not self.head: return
        prev, cur = None, self.head
        while cur.next != self.head:
            prev, cur = cur, cur.next
        if prev: prev.next = self.head
        else: self.head = None

    def delete_middle(self):
        if not self.head: return
        size = self.count()
        mid = size // 2
        i, cur = 0, self.head
        while i < mid - 1:
            cur = cur.next
            i += 1
        cur.next = cur.next.next

    def count(self):
        if not self.head: return 0
        cnt, cur = 0, self.head
        while True:
            cnt += 1
            cur = cur.next
            if cur == self.head: break
        return cnt

    def print_forward(self):
        if not self.head: print("Список пуст"); return
        values, cur = [], self.head
        while True:
            values.append(str(cur.value))
            cur = cur.next
            if cur == self.head: break
        print(" -> ".join(values))

    def print_reverse(self):
        if not self.head: print("Список пуст"); return
        values, cur = [], self.head
        while True:
            values.append(str(cur.value))
            cur = cur.next
            if cur == self.head: break
        print(" -> ".join(values[::-1]))


# 2связный список
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def add_last(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next: cur = cur.next
        cur.next = node
        node.prev = cur

    def add_after(self, target, value):
        cur = self.head
        while cur:
            if cur.value == target:
                node = Node(value)
                node.next, node.prev = cur.next, cur
                if cur.next: cur.next.prev = node
                cur.next = node
                return True
            cur = cur.next
        return False

    def delete_if(self, condition):
        cur = self.head
        while cur:
            if condition(cur.value):
                if cur.prev: cur.prev.next = cur.next
                else: self.head = cur.next
                if cur.next: cur.next.prev = cur.prev
            cur = cur.next

    def delete_first(self):
        if self.head: self.head = self.head.next
        if self.head: self.head.prev = None

    def delete_last(self):
        cur = self.head
        if not cur: return
        while cur.next: cur = cur.next
        if cur.prev: cur.prev.next = None
        else: self.head = None

    def delete_middle(self):
        size = self.count()
        mid = size // 2
        i, cur = 0, self.head
        while i < mid: cur, i = cur.next, i + 1
        if cur.prev: cur.prev.next = cur.next
        if cur.next: cur.next.prev = cur.prev

    def count(self):
        cnt, cur = 0, self.head
        while cur:
            cnt += 1
            cur = cur.next
        return cnt

    def print_forward(self):
        values, cur = [], self.head
        while cur:
            values.append(str(cur.value))
            cur = cur.next
        print(" -> ".join(values) if values else "Список пуст")

    def print_reverse(self):
        values, cur = [], self.head
        if not cur: print("Список пуст"); return
        while cur.next: cur = cur.next
        while cur:
            values.append(str(cur.value))
            cur = cur.prev
        print(" -> ".join(values))


# xor список
class XORNode:
    def __init__(self, value):
        self.value = value
        self.both = []

class XORLinkedList:
    def __init__(self):
        self.nodes = []
        self.head = None

    def add_first(self, value):
        node = XORNode(value)
        if self.head:
            node.both = [None, self.head]
            self.head.both[0] = node
        self.head = node
        self.nodes.append(node)

    def add_last(self, value):
        node = XORNode(value)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.both and cur.both[1]: cur = cur.both[1]
            cur.both = [cur.both[0] if cur.both else None, node]
            node.both = [cur, None]
        self.nodes.append(node)

    def print_forward(self):
        cur, values = self.head, []
        while cur:
            values.append(str(cur.value))
            cur = cur.both[1] if cur.both else None
        print(" -> ".join(values) if values else "Список пуст")

    def print_reverse(self):
        if not self.head: print("Список пуст"); return
        cur = self.head
        while cur.both and cur.both[1]: cur = cur.both[1]
        values = []
        while cur:
            values.append(str(cur.value))
            cur = cur.both[0]
        print(" -> ".join(values))


# main
def main():
    with open("data.txt") as f:
        numbers = list(map(int, f.read().strip().split(",")))

    print("\n=== Кольцевой список ===")
    cl = CircularLinkedList()
    for n in numbers: cl.add_last(n)
    cl.print_forward(); cl.print_reverse()
    print("Count:", cl.count())
    cl.add_first(100); cl.add_after(numbers[1], 200); cl.add_last(300)
    cl.print_forward()
    cl.delete_if(lambda x: x % 2 == 0)
    print("После удаления чётных:"); cl.print_forward()
    cl.delete_first(); print("Удалён первый:"); cl.print_forward()
    cl.delete_middle(); print("Удалён средний:"); cl.print_forward()
    cl.delete_last(); print("Удалён последний:"); cl.print_forward()

    print("\n=== Двунаправленный список ===")
    dl = DoublyLinkedList()
    for n in numbers: dl.add_last(n)
    dl.print_forward(); dl.print_reverse()
    print("Count:", dl.count())
    dl.add_first(100); dl.add_after(numbers[1], 200); dl.add_last(300)
    dl.print_forward()
    dl.delete_if(lambda x: x > 10)
    print("После удаления >10:"); dl.print_forward()
    dl.delete_first(); print("Удалён первый:"); dl.print_forward()
    dl.delete_middle(); print("Удалён средний:"); dl.print_forward()
    dl.delete_last(); print("Удалён последний:"); dl.print_forward()

    print("\n=== XOR-список (имитация) ===")
    xl = XORLinkedList()
    for n in numbers: xl.add_last(n)
    xl.print_forward(); xl.print_reverse()
    xl.add_first(100); xl.add_last(300)
    xl.print_forward()


if __name__ == "__main__":
    main()
