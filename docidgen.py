# Just a convenience helper - generates a Recogito-compliant document ID
# Note that there is a (theoretical) risk of duplicate IDs. Always cross-check
# whether the generated ID is still available in your target system!
import random
import string

id = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 14))
print(id)