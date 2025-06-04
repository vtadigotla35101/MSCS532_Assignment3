1.QUICKSORT_COMPARISIONS:
Instructions:
Save the Code: Copy the provided Python code and save it as a .py file (e.g., quicksort_comparison.py) on your computer.
Open Terminal: Open your computer's terminal or command prompt.
Navigate: Use cd to change your directory to where you saved the file (e.g., cd C:\Users\YourUser\Desktop).
Run: Execute the script using python quicksort_comparison.py (or python3).
View Results: A file named quicksort_results.txt will be created in the same directory, containing all the output.

Summary of Findings:
Randomized Quicksort consistently shows O(NlogN) performance across all input types.
Deterministic Quicksort performs O(NlogN) on random data but degrades to behavior for deterministic Quicksort on sorted/reverse-sorted inputs is significantly slower and may hit recursion limits.
Arrays with repeated elements are handled robustly by Randomized Quicksort, maintaining O(NlogN) average performance.
This empirical comparison confirms the theoretical advantage of randomization in avoiding worst-case scenarios for Quicksort.


2.HASHTABLE CHAINING:
Instructions:
- Ensure hash_table.py and test_hash_table.py are in the same directory.
- Navigate to the folder in your terminal:
- Run the test suite using:
           python -m unittest test_hash_table.py
