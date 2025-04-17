#!/bin/bash 

for key in {0..31}; do 
  echo "Testing key: $key (0x$(printf "%02x" $key))"
  ./two $key 
  echo # newline
done
