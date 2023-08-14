import re

search_patterns = [re.compile(r'7.*eleven'),
                       re.compile(r'target'),
                       re.compile(r'amc'),
                       re.compile(r'build-a-bear'),
                       re.compile(r'party\s+city'),
                       re.compile(r'jimmy\s+johns'),
                       re.compile(r'uchealth'),
                       re.compile(r'netflix'),
                       re.compile(r'adobe'),
                       re.compile(r'zappos'),
                       re.compile(r'panda\s+express'),
                       re.compile(r'prime\s+video'),
                       re.compile(r'king soop'),
                       re.compile(r'nintendo'),
                       re.compile(r'subway'),
                       re.compile(r'apple'),
                       re.compile(r'starbucks'),
                       re.compile(r'mcdonald\'s'),
                       re.compile(r'wendy.?s'),
                       re.compile(r'wal.*mart'),
                       re.compile(r'taco\s+bell'),
                       re.compile(r'doordash')
                   ]

split_patterns = [r'\d{3}-\d{3}.*\d{4}',
                  r'.com',
                  r'\*+',
                  r'\W+\s+co',
                  r'#+'
                  ]

replace_regx_dict = {r'am.?z.?n.*': 'amazon',
                     r'wal.?mart': 'walmart'
                     }
