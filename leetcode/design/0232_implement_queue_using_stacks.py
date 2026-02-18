class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []


    def shift_push_to_pop(self) -> None:
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())


    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if not self.pop_stack:
            self.shift_push_to_pop()

        return self.pop_stack.pop()

    def peek(self) -> int:
        return self.pop_stack[-1] if self.pop_stack else self.push_stack[0]

    def empty(self) -> bool:
        return not self.push_stack and not self.pop_stack


if __name__ == "__main__":
    # Basic push and pop (FIFO order)
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == 3

    # Peek returns front without removing
    q2 = MyQueue()
    q2.push(1)
    q2.push(2)
    assert q2.peek() == 1
    assert q2.peek() == 1  # still 1 after peek
    assert q2.pop() == 1
    assert q2.peek() == 2

    # Empty check
    q3 = MyQueue()
    assert q3.empty() == True
    q3.push(1)
    assert q3.empty() == False
    q3.pop()
    assert q3.empty() == True

    # Interleaved push and pop
    q4 = MyQueue()
    q4.push(1)
    q4.push(2)
    assert q4.pop() == 1   # drains into output stack
    q4.push(3)             # push while output stack still has elements
    assert q4.pop() == 2
    assert q4.pop() == 3

    # LeetCode example
    q5 = MyQueue()
    q5.push(1)
    q5.push(2)
    assert q5.peek() == 1
    assert q5.pop() == 1
    assert q5.empty() == False

    print("All tests passed.")