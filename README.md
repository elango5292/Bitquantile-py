

!This project is dedicated to unveiling the formidable prowess of Bitcoin and the intricate artistry of cryptography, demonstrating their resounding impact in the digital realm.

# Bitquantile-p

Bitquantile is a experimental program to bruteforce BITCOIN private keys. 

Modular arithmetic, ECMultiplication, ECaddition and Point doubling are written purely in python. No bitcoin libraries are used in the entire code. Hence, Bitquantile should be the fastest publickey generator in a single instance.

# Usage
Bitquantile has a simple use case which is to find privatekey of a certain publickey provided. So, one must provide "Range" and "Target publickey".

```$ python3 Bitquantile.py START_RANGE:END_RANGE TARGET_PUBLICKEY```

Bitquantile will generate publickey from the START-RANGE and compare the X-PUB of the provided public key. 

If you are extreamly lucky and FOUND a privatekey, it will automatially be written inside CHEST.txt of the same folder.

## Example Usage

I have targeted a publickey from a known privatekey. So, I have the information of range for this particular wallet. In case of a random publickey from blockchain, the possiblity of finding its privatekey is as equivalant as finding an atom from the visible universe.

## Information about the wallet used for testing:

! Do not send funds to this wallet.
### Privatekey
* HEX: ```609a8b20586af2f18ae1a9bf2635a60e675e6a963eccb5ff171de41475a7ce30```

* Decimal:```43695088126741419640577511729699449976371966004604696387592279976530175053360```

### Publickey
* Uncompressed: ```04852870e941a699b61a40d978f63611c33ec7d88d33a2016df19e45ec3434c2b5422b98fdf1780a9bf6c0327fd4ce07cb9b84bec7f39f6ebe584e2ca8ba986946```

* Compressed: ```02852870e941a699b61a40d978f63611c33ec7d88d33a2016df19e45ec3434c2b5```

#### Running Bitquantile in Linux:

![image](https://user-images.githubusercontent.com/91737914/193783146-fcf4889b-bda5-484e-92a6-fe24e658ee55.png)

If a privatekey is found, it will be written in '''CHEST.txt'''

![image](https://user-images.githubusercontent.com/91737914/193783468-8d38292d-4cd1-4bed-bc6a-8af02731d804.png)

# Perfomance

By using efficient generation of publickeys, Bitquantile is faster than other python programs for bruteforce. 
Now, I will set the start range 1 million keys away from the target privatekey and measure the time taken to complete the search.

Start range: ''' 609A8B20586AF2F18AE1A9BF2635A60E675E6A963ECCB5FF171DE41475988BF0 '''

![image](https://user-images.githubusercontent.com/91737914/193785885-a2619cce-a93d-4d47-9f06-2a19f5f4ddb0.png)

![image](https://user-images.githubusercontent.com/91737914/193786241-dfcb26c5-3dd6-4f68-b346-b05c50f86718.png)

Bitquantile took 

* real - ``` 1m31.659s ```
* user - ``` 1m31.029s ```
* sys - ``` 0m0.032s ```

[real time] – time elapsed between invocation and termination of the command.

[user CPU time] – the CPU time used by your process.

[system CPU time] – the CPU time used by the system on behalf of your process.

___
## Donate
BTC - bc1qwxa4mvsyldrw9ep9h9kql26975fr08h4rvvqx3
