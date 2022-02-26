class Node(object):
  def __init__(self, data):
    """Initialize this node with the given data."""
    self.data = data
    self.next = None

  def __repr__(self):
    """Return a string representation of this node."""
    return f'Node({self.data})'


class LinkedList:
  def __init__(self, items=None):
    """Initialize this linked list and append the given items, if any."""
    self.head = None  # First node
    self.tail = None  # Last node
    # Append given items
    if items is not None:
      for item in items:
        self.append(item)

  def __repr__(self):
    """Return a string representation of this linked list."""
    ll_str = ""
    for item in self.items():
      ll_str += f'({item}) -> '
    return ll_str

  def items(self):
    """Return a list (dynamic array) of all items in this linked list.
    Best and worst case running time: O(n) for n items in the list (length)
    because we always need to loop through all n nodes to get each item."""
    items = []  # O(1) time to create empty list
    # Start at head node
    node = self.head  # O(1) time to assign new variable
    # Loop until node is None, which is one node too far past tail
    while node is not None:  # Always n iterations because no early return
      items.append(node.data)  # O(1) time (on average) to append to list
      # Skip to next node to advance forward in linked list
      node = node.next  # O(1) time to reassign variable
    # Now list contains items from all nodes
    return items  # O(1) time to return list

  def is_empty(self):
    """Return a boolean indicating whether this linked list is empty."""
    return self.head is None

  def length(self):
    """Return the length of this linked list by traversing its nodes.
    TODO: Running time: O(n) Why and under what conditions?"""
    length = 0
    current = self.head
    while current != None:
      length += 1
      current = current.next
    return length

  def append(self, item):
    """Insert the given item at the tail of this linked list.
    TODO: Running time: O(1) Why and under what conditions?"""
    node = Node(item)
    if self.head == None:
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node

  def prepend(self, item):
    """Insert the given item at the head of this linked list.
    TODO: Running time: O(1) Why and under what conditions?"""
    node = Node(item)
    if self.length() == 0:
      self.head = node
      self.tail = node
    else:
      node.next = self.head
      self.head = node

  def _find_node(self, item):
    """Return an item from this linked list if it is present.
    TODO: Best case running time: O(1) Why and under what conditions?
    TODO: Worst case running time: O(n) Why and under what conditions?"""
    if self.length() > 0:
      current = self.head
      while current != None:
        if current.data == item:
          return current
        elif current.next == None:
          break
        current = current.next
    raise ValueError('item not found: {}'.format(item))

  def find(self, item):
    """Return an item from this linked list if it is present.
    TODO: Best case running time: O(1) Why and under what conditions?
    TODO: Worst case running time: O(n) Why and under what conditions?"""
    if self.length() > 0:
      current = self.head
      while current != None:
        if current.data == item:
          return True
        elif current.next == None:
          return False
        current = current.next

  def find_if_matches(self, matching_function):
    """Return an item from this linked list if it is present."""
    node = self.head
    while node:
        if matching_function(node.data): 
            return node
        node = node.next
    return None

  def _find_previous(self, node):
    if self.length() > 0:
      current = self.head
      while current != None:
        if current.next == node:
          return current
        current = current.next

  def delete(self, item):
    """Delete the given item from this linked list, or raise ValueError.
    TODO: Best case running time: O(1) Why and under what conditions?
    TODO: Worst case running time: O(n) Why and under what conditions?"""
    if self.head and self.head.data == item:
      if self.head.next:
        self.head = self.head.next
      else:
        self.head = None
        self.tail = None
    else:
      node = self._find_node(item)
      previous = self._find_previous(node)
      previous.next = node.next
      if previous.next == None:
        self.tail = previous

if __name__ == "__main__":
  my_ll = LinkedList(["A", "B", "C"])
  my_ll.delete("A")
  my_ll.delete("A")
  print(my_ll)
