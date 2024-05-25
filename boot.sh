#! /bin/bash

read -p "Would you like to play a game of Rock, Paper, Scissors? (Y/N): " reply 



if [ ${reply,,} == "y" ]
then 
    python rpc.py 
else
    echo "That's too bad, maybe next time?"
fi
