# AES

## Overview
### Algorithm Steps

1. Input both (key and plaintext).
2. Key expansion.
3. Initial round.
4. 9 Intermediate rounds (for AES block and key 128bit).
5. Final round.
6. Ciphered text.

## Requirements

1. Software shall encrypt either (128, 192, or 256-bit) data blocks.
2. Software shall encrypt data blocks using (128, 192, or 256-bit) keys.

## Building Blocks Info
### Key Expansion

#### Goal
The aim of this operation is to expand the key block to obtain different sub-key block for each round (here 128 key bits block is expanded to 128*11 bits). The first 4 words in the expanded key are the same as the initial key. The key expansion algorithm is given below.

## Run Tests

```
npm test
```

