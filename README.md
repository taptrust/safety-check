# safety-check

API to perform security and compliance analysis on smart contracts.

If on Ubuntu, run:
     
     sudo apt-get install python3 python3-pip python-dev python3-dev \
     build-essential libssl-dev libffi-dev \
     libxml2-dev libxslt1-dev zlib1g-dev \
     python-pip

Dependencies :

	git clone https://github.com/taptrust/safety-check.git
	cd safety-check
	sudo pip3 install -r requirements.txt


If on production, set the port to 80:

    export PORT=80
    
    
To run:

    sudo - E python3 runserver.py
    
On production, use `screen` to keep the server running after the SSH session is closed. 
