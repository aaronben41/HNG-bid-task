import csv, hashlib, json
from settings import INPUT_FILE_URL, OUTPUT_FILE_URL


#Create an empty output csv file and open it
csv_output = OUTPUT_FILE_URL
open_csv = open(csv_output, 'w')

write_csv = csv.writer(open_csv)

# Read input csv file and create json for each row
csv_input = INPUT_FILE_URL
with open('csv_input', 'r') as csv_file:
    read_csv_file = csv.reader(csv_file, delimiter=',')
    next(read_csv_file)
    data = [a for a in read_csv_file] 

    for row in data:

        if row[1] and row[2]:
    
            serial_no = row[0]
            file_name = row[1]
            name= row[2]
            description= row[3]
            gender = row[4]
            attributes = row[5]
            uuid = row[6]
           
            created_json = {
                'format' : 'CHIP-0007',
                'name' : file_name.replace('-', ' ').title(),
                'description' : '',
                'minting_tool' : '',
                'series_number' : serial_no,
                'sensitive_content' : False,
                'series_total' : data[-1][0],
                 "attributes": [
                    {
                        "trait_type": "gender",
                        "value": gender
                    }
                ],
                "collection": {
                    "name": "Zuri NFT tickets for free lunch",
                    "id": uuid,
                    "attributes": [
                        {
                            "type": "description",
                            "value": "Rewards for accomplishments during HNGi9"
                        }
                    ]
                },
            }

            # Create json file for every row and convert to string
            json_file = json.dumps(created_json, indent=4) 
            
            with open(f'json/{file_name}.json', 'w') as output:
                output.write(json_file)
            output.close()

           # Calculate and append hash to each file
            hash = hashlib.sha256(json_file.encode()).hexdigest()

           # Appending the file name to the csv file.
            row.append(hash)
            write_csv.writerow(row)

# Close output file
open_csv.close