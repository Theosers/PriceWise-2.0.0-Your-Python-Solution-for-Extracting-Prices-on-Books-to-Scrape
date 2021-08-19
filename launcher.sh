#!/usr/bin/env bash
echo En cours d\'execution...
if [ "$(uname)" == "Darwin" ]; then
    python3 code/main.py       
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    python3 code/main.py 
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
	echo En cours d\'execution...32
    py code/main.py 
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
    py code/main.py 
fi
