docker run -v /tmp/:/host -it localhost:5000/docker-fee:0.1 /bin/sh -c '/root/.local/lib/python3.11/site-packages/fee.py /host/psqlrev'  > psqlrev.py
