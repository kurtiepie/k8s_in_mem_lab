#!/bin/bash

# Remove the contents of /data directory
rm -rf /data/*

# Start the actual application
exec "$@"

