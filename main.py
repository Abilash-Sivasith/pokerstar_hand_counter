import os

"""
main file to read pokerstars data.
Please look at the readme for more infomation on how to use the software
"""

def parse_individual_file(file_path):
    """reads each individual file"""
    with open(file_path, "r") as file:
        content = file.read()
        return (content.strip());
        print(f"Contents of {file}:")
        print(content)

def parse_all_input_file():
    """take the pokerstar data file and puts it in a readable format"""
    all_file_data = []
    for filename in os.listdir('pokerstar_raw_data_files'):
        if filename.endswith(".txt"):
            file_path = os.path.join("pokerstar_raw_data_files", filename)
            ind_file_content = parse_individual_file(file_path)
            all_file_data.append(ind_file_content)

    return all_file_data

def hand_counter():
    """return the number of hands played from all files"""
    pass

def hand_counter_per_file():
    """take an incomming file and return the number of hands played in each individual file"""
    pass

def main():
    """main logic function"""
    pass

print(len(parse_all_input_file())) # index 0 is file 1