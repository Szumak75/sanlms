# -*- coding: utf-8 -*-
"""
  test01.py
  Author : Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
  Created: 27.02.2024, 09:13:20
  
  Purpose: 
"""

import mt940
import pprint

transactions = mt940.parse("2402221260140001.TXT")

print("Transactions:")
print(transactions)
pprint.pprint(transactions.data)

print()
for transaction in transactions:
    print("Transaction: ", transaction)
    pprint.pprint(transaction.data)

# #[EOF]#######################################################################
