import csv
from collections import defaultdict

def load_lookup_table(file_path):
    lookup = {}
    with open(file_path, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            port = row['dstport']
            protocol = row['protocol'].lower()
            tag = row['tag']
            lookup[(port, protocol)] = tag
    return lookup

def parse_flow_logs(flow_log_file, lookup_table):
    tag_count = defaultdict(int)
    port_protocol_count = defaultdict(int)
    
    untagged_tag = 'Untagged'
    
    with open(flow_log_file, mode='r') as file:
        for line in file:
            fields = line.strip().split()
            if len(fields) < 13:
                continue
            
            dstport = fields[6]
            protocol_num = fields[7]
            
            protocol = map_protocol_number(protocol_num)
            
            if (dstport, protocol) in lookup_table:
                tag = lookup_table[(dstport, protocol)]
            else:
                tag = untagged_tag
            
            tag_count[tag] += 1
            
            port_protocol_count[(dstport, protocol)] += 1
    
    return tag_count, port_protocol_count

def map_protocol_number(protocol_num):
    protocol_map = {
        '6': 'tcp',
        '17': 'udp',
        '1': 'icmp'
    }
    return protocol_map.get(protocol_num, 'unknown')

def write_report(tag_count, port_protocol_count, output_file):
    with open(output_file, 'w') as file:
        file.write("Tag Counts:\n")
        file.write("Tag,Count\n")
        for tag, count in tag_count.items():
            file.write(f"{tag},{count}\n")
        
        file.write("\nPort/Protocol Combination Counts:\n")
        file.write("Port,Protocol,Count\n")
        for (port, protocol), count in port_protocol_count.items():
            file.write(f"{port},{protocol},{count}\n")

def main():
    lookup_table_file = 'lookup_table.csv'
    flow_log_file = 'flow_log.txt'
    output_file = 'output_report.txt'
    
    lookup_table = load_lookup_table(lookup_table_file)
    tag_count, port_protocol_count = parse_flow_logs(flow_log_file, lookup_table)
    write_report(tag_count, port_protocol_count, output_file)

if __name__ == "__main__":
    main()
