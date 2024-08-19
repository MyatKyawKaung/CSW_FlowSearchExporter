import os

def read_and_format_file(input_filename, prefix):
    with open(input_filename, 'r') as f:
        lines = f.readlines()
    
    # Initialize an empty set to store unique formatted lines
    formatted_lines = set()
    
    for line in lines:
        # Remove the prefix and split the line by comma
        parts = line.strip().replace(prefix, '').split(', ')
        # Add each part to the set to ensure uniqueness
        for part in parts:
            formatted_lines.add(part)
    
    return sorted(formatted_lines)

def generate_output(source_ips, source_hgs, target_ips, target_hgs):
    output = f"Source IP : {', '.join(source_ips)}\n"
    output += f"Source HG : {', '.join(source_hgs)}\n"
    output += f"Target IP : {', '.join(target_ips)}\n"
    output += f"Target HG : {', '.join(target_hgs)}"
    return output

def main():
    # Define your input files and prefixes
    source_ip_filename = "sip.txt"
    source_hg_filename = "s_groups.txt"
    target_ip_filename = "tip.txt"
    target_hg_filename = "t_groups.txt"
    
    # Reading and formatting each file
    source_ips = read_and_format_file(source_ip_filename, "Source IP: ")
    source_hgs = read_and_format_file(source_hg_filename, "Source HG: ")
    target_ips = read_and_format_file(target_ip_filename, "Target IP: ")
    target_hgs = read_and_format_file(target_hg_filename, "Target HG: ")
    
    # Generate the final output
    output = generate_output(source_ips, source_hgs, target_ips, target_hgs)
    
    # Write the output to a file
    output_filename = "output.txt"
    with open(output_filename, 'w') as output_file:
        output_file.write(output)
    
    print(f"Output written to {output_filename}")

if __name__ == "__main__":
    main()
