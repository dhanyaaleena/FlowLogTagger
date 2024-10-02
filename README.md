# FlowLogTagger

Overview
FlowLogTagger is a Python program designed to parse AWS flow logs and map each flow log entry to a corresponding tag based on a predefined lookup table. The lookup table is a CSV file containing a mapping of destination ports and protocols to tags. The program generates a report of tag counts and the number of occurrences for each port/protocol combination.

Assumptions:
The flow logs must be in AWS default log format version 2. Other formats are not supported.
The lookup table CSV file must contain three columns: dstport, protocol, and tag.
The program only supports basic flow logs without additional custom fields.
The protocol numbers are mapped to strings (6 for TCP, 17 for UDP, and 1 for ICMP). Other protocols will be categorized as unknown.
Entries without a matching tag are marked as Untagged.
File Structure
flow_log.txt: Example input file containing flow log data.
lookup_table.csv: CSV file containing the mapping of destination port, protocol, and tag.
output_report.txt: The generated output file containing tag counts and port/protocol combination counts.
Prerequisites
Python 3.x should be installed on your system.
No additional Python packages are required beyond what is included with the standard library.

Usage
1. Clone the repository:
git clone https://github.com/dhanyaaleena/FlowLogTagger.git
cd FlowLogTagger
2. Add your input files:
Place your flow log file (flow_log.txt) and lookup table file (lookup_table.csv) in the project directory.(Currently sample flow_log.txt and lookupTable.csv is added in the repo)
3. Run the Program:
To run the program, execute the following command:
python flowlogtagger.py
4. Check the Output:
After running the program, you will find the generated report in output_report.txt, which contains:

Tag Counts: The number of times each tag was matched.
Port/Protocol Combination Counts: The number of occurrences for each port/protocol combination.
Example:
Tag Counts:
Tag,Count
sv_P1,2
sv_P2,1
email,3
Untagged,9

Port/Protocol Combination Counts:
Port,Protocol,Count
22,tcp,1
25,tcp,1
110,tcp,1
443,tcp,1


The program has been tested with:

Valid AWS flow log entries.
A sample lookup table with different port/protocol combinations.
Cases where no matching tag is found (results in Untagged).