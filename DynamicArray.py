import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self.n = 0       # count actual elements
        self.capacity = 1   # default array capacity
        self.A = self._make_array(self.capacity)   # low-level array

    def is_empty(self):
        """ Return True if array is empty"""
        return self.n == 0

    def _len_(self):
        """Return numbers of elements stored in the array."""
        return self.n

    def _getitem_(self, i):
        """Return element at index i."""
        if not 0 <= i < self.n:
            # Check it i index is in bounds of array
            raise ValueError('invalid index')
        return self.A[i]

    def append(self, obj):
        """Add object to end of the array."""
        if self.n == self.capacity:
            # Double capacity if not enough room
            self._resize(2 * self.capacity)
        self.A[self.n] = obj  # Set self.n index to obj
        self.n += 1

    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)   # New bigger array
        for k in range(self.n):  # Reference all existing values
            B[k] = self.A[k]
        self.A = B     # Call A the new bigger array
        self.capacity = c  # Reset the capacity

    @staticmethod
    def _make_array(c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()

    def insert(self, k, value):
        """Insert value at position k."""
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        for j in range(self.n, k, -1):
            self.A[j] = self.A[j - 1]
        self.A[k] = value
        self.n += 1

    def pop(self, index):
        """Remove item at index (default first)."""
        if index >= self.n or index < 0:
            raise ValueError('invalid index')
        for i in range(index, self.n - 1):
            self.A[i] = self.A[i + 1]
        self.A[self.n - 1] = None
        self.n -= 1

    def remove(self, value):
        """Remove the first occurrence of a value in the array."""
        for k in range(self.n):
            if self.A[k] == value:
                for j in range(k, self.n - 1):
                    self.A[j] = self.A[j + 1]
                self.A[self.n - 1] = None
                self.n -= 1
                return
        raise ValueError('value not found')

    def _print(self):
        """Print the array."""
        for i in range(self.n):
            print(self.A[i], end=' ')
        print()
