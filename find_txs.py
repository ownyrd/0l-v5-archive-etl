import os
import json

#### Configure your settings here ... ####
extracted_dir = "./0Lv5/archives/extracted"
address = "<ADDRESS>"
txs_type = "send" # choose between receive and send
##########################################

txs = []

def open_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        for item in data:
            events = item["events"]
            for event in events:
                if "receiver" in event["data"].keys():
                    if txs_type == "receive":
                        if event["data"]["type"] == "receivedpayment" and event["data"]["receiver"] == address:
                            output = "File: {} Sender: {} Receiver: {} Time: {} Amount: {}".format(file_path, event["data"]["sender"],event["data"]["receiver"],event["timestamp_usecs"],event["data"]["amount"]["amount"])
                            # output = "{}".format(event["data"]["amount"]["amount"])
                            txs.append(output)
                            print(output)
                    if txs_type == "send":
                        if event["data"]["type"] == "sentpayment" and event["data"]["sender"] == address:
                            output = "File: {} Sender: {} Receiver: {} Time: {} Amount: {}".format(file_path, event["data"]["sender"],event["data"]["receiver"],event["timestamp_usecs"],event["data"]["amount"]["amount"])
                            # output = "{}".format(event["data"]["amount"]["amount"])
                            txs.append(output)
                            print(output)

for file in os.listdir(extracted_dir):
    data = open_json(os.path.join(extracted_dir, file))

with open(os.path.join("./", "{}-{}-transactions.txt".format(address, txs_type)), 'w') as output:
    for line in txs:
        output.write(f"{line}\n")
