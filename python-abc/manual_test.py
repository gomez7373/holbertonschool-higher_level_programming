#!/usr/bin/env python3

from task_02_verboselist import VerboseList

# Create a VerboseList object
vl = VerboseList([1, 2, 3])

# Test append method
vl.append(4)

# Test extend method
vl.extend([5, 6])

# Test remove method
vl.remove(2)

# Test pop method without index
vl.pop()

# Test pop method with index
vl.pop(0)

# Expected output:
# Added [4] to the list.
# Extended the list with [2] items.
# Removed [2] from the list.
# Popped [6] from the list.
# Popped [1] from the list.

