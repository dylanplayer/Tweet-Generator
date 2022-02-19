from linkedlist import LinkedList

class HashTable(object):
  def __init__(self, init_size=8):
    """Initialize this hash table with the given initial size."""
    # Create a new list (used as fixed-size array) of empty linked lists
    self.buckets = []
    for i in range(init_size):
      self.buckets.append(LinkedList())

  def __str__(self):
    """Return a formatted string representation of this hash table."""
    items = []
    for key, val in self.items():
      items.append('{!r}: {!r}'.format(key, val))
    return '{' + ', '.join(items) + '}'

  def __repr__(self):
    """Return a string representation of this hash table."""
    return 'HashTable({!r})'.format(self.items())

  def _bucket_index(self, key):
    """Return the bucket index where the given key would be stored."""
    # Calculate the given key's hash code and transform into bucket index
    return hash(key) % len(self.buckets)

  def keys(self):
    """Return a list of all keys in this hash table.
    TODO: Running time: O(???) Why and under what conditions?"""
    # Collect all keys in each bucket
    all_keys = []
    for bucket in self.buckets:
        for key, value in bucket.items():
            all_keys.append(key)
    return all_keys

  def values(self):
    """Return a list of all values in this hash table.
    TODO: Running time: O(???) Why and under what conditions?"""
    all_values = []
    for bucket in self.buckets:
        for key, value in bucket.items():
            all_values.append(value)
    return all_values

  def items(self):
    """Return a list of all items (key-value pairs) in this hash table.
    TODO: Running time: O(???) Why and under what conditions?"""
    # Collect all pairs of key-value entries in each bucket
    all_items = []
    for bucket in self.buckets:
        all_items.extend(bucket.items())
    return all_items

  def length(self):
    """Return the number of key-value entries by traversing its buckets.
    TODO: Running time: O(???) Why and under what conditions?"""
    return len(self.items())

  def contains(self, key):
    """Return True if this hash table contains the given key, or False.
    TODO: Running time: O(???) Why and under what conditions?"""
    return key in self.keys()

  def get(self, key):
    """Return the value associated with the given key, or raise KeyError.
    TODO: Running time: O(???) Why and under what conditions?"""
    bucket = self._bucket_index(key)
    nodes = self.buckets[bucket].items()
    for node in nodes:
      if node[0] == key:
        return node[1]
    raise KeyError(f'Key not found: {key}')

  def getPair(self, key):
    """Return the key and value associated with the given key, or raise KeyError.
    TODO: Running time: O(???) Why and under what conditions?"""
    bucket = self._bucket_index(key)
    nodes = self.buckets[bucket].items()
    for node in nodes:
      if node[0] == key:
        return node
    raise KeyError(f'Key not found: {key}')

  def set(self, key, value):
    """Insert or update the given key with its associated value.
    TODO: Running time: O(???) Why and under what conditions?"""
    try: 
      node = self.getPair(key)
      node[1] = value
    except KeyError:
       self.buckets[self._bucket_index(key)].append([key, value])

  def delete(self, key):
    """Delete the given key from this hash table, or raise KeyError.
    TODO: Running time: O(???) Why and under what conditions?"""
    bucket = self.buckets[self._bucket_index(key)]
    for node in bucket.items():
      if node[0] == key:
        bucket.delete(node)
        return node
    raise KeyError(f'Key not found: {key}')

if __name__ == '__main__':
  ht = HashTable()
  ht.set("Tiger", 3)
  ht.set("Cat", 5)
  ht.set("Tiger", 4)
  print(ht.get("Tiger"))
  print(ht.contains("Tiger"))
  print(ht.items())
  ht.delete("Cat")
  print('hash table: {}'.format(ht))
