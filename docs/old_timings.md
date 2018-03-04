Lenovo Z50 
 - Intel Core i7-4510U CPU @ 2.00GHz x2
 - Ubuntu 16.04
 - Python 3.5.2

samples = 10,000,000
 - serial:	3.810s
 - par (2):	2.158s (1.766x)
 - par (4):	2.449s (1.556x)


samples = 100,000,000
 - serial:	36.651s
 - par (2):	21.131s (1.734x)
 - par (4):	23.728s	(1.545x)


samples = 1,000,000,000
 - serial:	380.459s
 - par (2):	226.430s (1.680x)
 - par (4):	257.949s (1.475x)




AWS vCPUs 4 c3.xlarge
  - Python 3.4


samples = 1,000,000
 - serial:	0.721s
 - par (2):	0.472s (1.528x)
 - par (4OS):	0.504 (1.43x)	


samples = 10,000,000
 - serial:	6.92s	
 - par (2):	3.586s (1.93x)
 - par (4OS):	3.461s (1.99x)


samples = 100,000,000
 - serial:	71.099s
 - par (2):	35.261s (2.016x)
 - par (4OS):	35.809s (1.986x)


samples = 1,000,000,000
 - serial:	
 - par (2):
 - par (4OS):
