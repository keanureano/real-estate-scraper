# Real Estate Region Web Scraper

This program is designed to extract both French and Arabic translations of place names from a specific website. It then merges the data based on unique identifiers. Follow the instructions below to set up and run the program.

## Installation

1. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

2. Run the main program using the following command:

   ```
   python main.py
   ```

3. Wait for the program to load.

4. Select the French language first, then choose the desired region.

5. Run the program and wait for it to complete.

6. Repeat the steps, but this time select the Arabic language.

7. After running the program twice, you will find two output files: `output.csv` and `output (1).csv`.

8. To merge the outputs, run the following command:

   ```
   python merge.py
   ```

9. Delete the `output.csv` and `output (1).csv` files.

10. Rename the `final_output.csv` file to the region you initially selected.

## Example

If you initially selected the Casablanca region, rename `final_output.csv` to `casablanca.csv`.

That's it! You now have the translated place names in the desired region.
