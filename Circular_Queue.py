class CircularQueue:
    def __init__(self, size=100):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        if (self.front == 0 and self.rear == self.size - 1) or (self.rear == (self.front - 1) % (self.size - 1)):
            return True
        return False

    def is_empty(self):
        if self.front == -1:
            return True
        return False

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full.")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            print(f"Enqueued element: {value}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
            return -1
        else:
            element = self.queue[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            print(f"Dequeued element: {element}")
            return element

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Elements in the queue:", end=" ")
            i = self.front
            while i != self.rear:
                print(self.queue[i], end=" ")
                i = (i + 1) % self.size
            print(self.queue[i])

q = CircularQueue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()

q.dequeue()
q.dequeue()
q.display()

q.enqueue(50)
q.enqueue(60)
q.display()
