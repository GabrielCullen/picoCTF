#!/usr/bin/env python3

import hashlib

u=b"SCHOFIELD"
i=0
a=""
while i < len(u):

	a=(a + (hashlib.sha256(u).hexdigest()[i]))
	i+=1

b=(a[4]+a[5]+a[3]+a[6]+a[2]+a[7]+a[1]+a[8])
print(b)