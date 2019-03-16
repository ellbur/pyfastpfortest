
from pylab import *
import pyfastpfor

c = pyfastpfor.getCodec('fastpfor256')

a = uint32(np.random.binomial(10, 0.5, size=256))
b = zeros((256 * 2,), dtype=uint32)

encoded_len = c.encodeArray(a, len(a), b, len(b))

print(encoded_len)
print(b[:encoded_len])

