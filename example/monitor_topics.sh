#!/bin/bash
KAFKA_ROOT="$HOME/programs/kafka_2.13-2.6.0"
ZK="localhost:2181"  # zookeeper
BB="localhost:9090"  # bootstrap broker

# total list of topics:
#$KAFKA_ROOT/bin/kafka-topics.sh --zookeeper $ZK --list

for TOPIC in "detections" "detections-utm" "fusion-inout-utm" "fusion-inout-objects-utm" "fusion-utm" "objects-utm" "objects" "campus-st" #"systemstatus" "systemcontrol" "dummycontrol"
do
	$KAFKA_ROOT/bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list $BB --topic $TOPIC --time -1 --offsets 1 | awk -v topic="$TOPIC" -F  ":" '{sum += $3} END {print topic, "\ttotal messages:", sum}'
    [[ $1 == "-v" ]] && $KAFKA_ROOT/bin/kafka-topics.sh --zookeeper $ZK --describe --topic $TOPIC
done
