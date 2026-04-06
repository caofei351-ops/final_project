class CircularBuffer:
    def __init__(self, size):
        # Initialize the buffer with a fixed size
        self.size = size
        # Pre-allocate the list with None to represent empty slots
        self.buffer = [None] * size
        # 'head' points to the first element (for dequeueing)
        self.head = 0
        # 'tail' points to the next available position (for enqueueing)
        self.tail = 0
        # 'count' tracks the current number of elements in the buffer
        self.count = 0

    def is_empty(self):
        # Returns True if the buffer contains no elements
        return self.count == 0

    def is_full(self):
        # Returns True if the buffer has reached its maximum capacity
        return self.count == self.size

    def enqueue(self, item):
        # Add an element to the buffer
        if self.is_full():
            # Scenario: Overwriting old data when the buffer is full
            print("Buffer is full. Overwriting old data.")
            
            # Place the item at the current tail position
            self.buffer[self.tail] = item
            # Use modulo operator (%) to wrap the tail pointer back to the start
            self.tail = (self.tail + 1) % self.size
            # When overwriting, the head must also move to point to the new 'oldest' data
            self.head = (self.head + 1) % self.size
        else:
            # Scenario: Standard addition when space is available
            self.buffer[self.tail] = item
            # Move tail forward and wrap around if necessary
            self.tail = (self.tail + 1) % self.size
            # Increment the total count of elements
            self.count += 1

    def dequeue(self):
        # Remove and return the oldest element from the buffer
        if self.is_empty():
            print("Buffer is empty.")
            return None

        # Retrieve the item from the head position
        item = self.buffer[self.head]
        # Optional: Clear the spot by setting it to None
        self.buffer[self.head] = None
        # Move head forward and wrap around using modulo logic
        self.head = (self.head + 1) % self.size
        # Decrement the total count of elements
        self.count -= 1

        return item

    def display(self):
        # Print the current raw state of the internal buffer list
        print(self.buffer)
