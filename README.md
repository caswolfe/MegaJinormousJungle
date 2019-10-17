# Jum.py

## Current issues
* How atomic do we want our edits?
  *One-char? <- probably easiest to implement
  * Certain number of bytes/chars?
  * It might be more robust to send smaller, more frequent packets?
* Do we have a "resync" option? 
  * In case packet dropped
* Have to determine if we're using Google Cloud server
  * Might make it easier
  * Can make client code more homeogenous as nobody as to be the server

## TODO's
* Window/GUI
  * Methods to return the edits, and their corresponding position
  * Would like positions to be returned in terms of (row, col)
* Networking
  * Sending data over the network peer-to-peer
  * Using Google Cloud
  * Which is better/easier/less likely to fail?
* Editing
  * Update file dynamically upon recieving a change and a position
  * Ordered by timestamp

## Git
* Remember to git pull before you do anything
