# Extract OpenLibra v5 Transactions

1. Install Python3
2. Untar the .tgz archives
   1. Modify the variable `directory` in [untar_tgzs](./untar_tgzs.py); use the directory containing the .tgz archives
   2. Ensure there are ONLY .tgz files in the archive folder
   3. run `python3 untar_tgzs.py`
   4. the results will be stored in a subfolder called `extracted`
3. Extract account specific transactions
   1. Modify the variable `extracted_dir` in [find_txs.py](./find_txs.py) --> use the path of the extracted folder from step 2.3
   2. Modify the variable `address` in [find_txs.py](./find_txs.py) --> your address here
   3. Modify the variable `txs_type` in [find_txs.py](./find_txs.py) --> you can extract all transactions where your account was the sender, or all txs where your account was the receiver
