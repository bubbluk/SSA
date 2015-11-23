#####################################################################
# Code is Copyright (C) Bubbl, Inc.
# When editing or/then/and publishing this software full credit and royalties must be given to Bubbl, Inc. through the URL: http://bubbluk.ml/
# You may contain some of the credit for your editing/modifying
# You must email us (jacob@bubbluk.ml) about your release of the software, the URL or place the software is being published must be given to us
# You may not sell or trade with this software, or use it in any illegal or pornographic way
#####################################################################


# -*- coding: utf-8 -*-

# imports necessary modules #
import webrowser

# welcome script #
print("I am SSA, a virtual assistant made in Python")
print("There are several links available")
print("Which one(s) shall I open?\n")
print("1 - http://bubbluk.ml - Makers Site\n2 - http://python.org - Python Programming Language Site")

# runs the code forever #
while True:
  command=input("SSA:/")
    if input in "Hi" or "Hello" or "Yo" or "Sup" or "Hiya":
      print("Hi, I am SSA, your virtual assistant")
    else:
      print("Command not found!")
      print("Opening email app to report issue")
      webbrowser.open_new("mailto:jacob@bubbluk.ml?subject=SSA%20Issue&body=Command", command ,"Not%20Found")
  


