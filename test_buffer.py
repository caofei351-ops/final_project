from circular_buffer import CircularBuffer

buffer = CircularBuffer(5)

buffer.enqueue(10)
buffer.enqueue(20)
buffer.enqueue(30)
buffer.enqueue(40)
buffer.enqueue(50)

buffer.display()

print("Removed:", buffer.dequeue())
print("Removed:", buffer.dequeue())

buffer.display()

buffer.enqueue(60)
buffer.enqueue(70)

buffer.display()
