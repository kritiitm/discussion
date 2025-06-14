### Post 39
**Post URL**: /t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/39
- **ID**: 579372
- **Author**: Shouvik Roy  (roy2003)
- **Created At**: 2025-01-13T16:24:09.236Z
- **Reply To**: Post 38 (Jivraj Singh Shekhawat, Jivraj)
- **Content**:  
  <pre data-code-wrap="bash"><code class="lang-bash">!pip install chardet==5.1.0  # Install the chardet library
</code></pre>
<pre data-code-wrap="python"><code class="lang-python">import chardet
def read_files():
  """Gets two CSV files and one TXT file from the user and reads them.

  Returns:
    A tuple containing the contents of the three files.
  """
    # Get the file paths from the user.
  csv_file_1_path = input("Enter the path to the first CSV file: ")
  csv_file_2_path = input("Enter the path to the second CSV file: ")
  txt_file_path = input("Enter the path to the TXT file: ")

  # ... (Get file paths from user - same as before)

  # Read the CSV files.
  try:
    with open(csv_file_1_path, 'rb') as f:  # Open in binary mode
      rawdata = f.read()
      encoding = chardet.detect(rawdata)['encoding']  # Detect encoding
    with open(csv_file_1_path, 'r', encoding=encoding) as csv_file_1:  # Use detected encoding
      csv_data_1 = csv_file_1.read()

    # Repeat for csv_file_2_path using the same pattern
    with open(csv_file_2_path, 'rb') as f:
        rawdata = f.read()
        encoding = chardet.detect(rawdata)['encoding']
    with open(csv_file_2_path, 'r', encoding=encoding) as csv_file_2:
        csv_data_2 = csv_file_2.read()

  except FileNotFoundError:
    print("Error: One or both of the CSV files could not be found.")
    return None
  except UnicodeDecodeError:
    print("Error: Could not decode one or both of the CSV files.")
    return None

  # Read the TXT file.
  try:
    with open(txt_file_path, 'rb') as f:  # Open in binary mode to detect encoding
        rawdata = f.read()
        encoding = chardet.detect(rawdata)['encoding']  # Detect encoding
    with open(txt_file_path, 'r', encoding=encoding) as txt_file:  # Open in text mode with detected encoding
        txt_data = txt_file.read() # Read the content of the file
  except FileNotFoundError:
    print("Error: The TXT file could not be found.")
    return None
  except UnicodeDecodeError:
    print("Error: Could not decode the TXT file.")
    return None

  # Return the contents of the files.
  return csv_data_1, csv_data_2, txt_data

# Call the function to read the files.
file_contents = read_files()
if file_contents:
  csv_data_1, csv_data_2, txt_data = file_contents
  #print("Content of the first CSV file:\n", csv_data_1)
  #print("\nContent of the second CSV file:\n", csv_data_2)
  #print("\nContent of the TXT file:\n", txt_data)

  # Combine the content of all files into a single string
  all_content = csv_data_1 + csv_data_2 + txt_data

  # Split the content into lines
  lines = all_content.split('\n')

  # Initialize the total sum
  total_sum = 0

  # Iterate through each line
  for line in lines:
    # Split the line into symbol and value, handling potential extra spaces
    try:
      parts = line.strip().split(',')
      symbol = parts[0].strip()  # Remove leading/trailing spaces from symbol
      value = parts[1].strip()   # Remove leading/trailing spaces from value

      # Check if the symbol matches the criteria (using a more robust check)
      if symbol in ['€', 'ˆ', '’'  # Euro symbol variations
                     # Add any other known variations of the target symbols
                   ]:
        # Convert the value to a number and add it to the total sum
        total_sum += float(value)

    except (IndexError, ValueError):
      # Ignore lines with incorrect formatting or non-numeric values
      pass

  # Print the total sum
  print("The sum of all values associated with the specified symbols is:", total_sum)
</code></pre>
- **Reactions**: None
- **Post Number**: 39

