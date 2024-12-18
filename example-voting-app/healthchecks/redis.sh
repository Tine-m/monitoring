#!/bin/sh
set -eo pipefail

host="127.0.0.1"  # Directly set the host IP

if ping="$(redis-cli -h "$host" ping)" && [ "$ping" = 'PONG' ]; then
	exit 0
fi

exit 1
