import random
import time
import sys
import os # Import the os module

# Set a higher recursion limit for deep recursion in Quicksort
sys.setrecursionlimit(20000) 

# --- 1. Randomized Quicksort Implementation ---

def _partition_randomized(arr, low, high):
    """
    Partitions the array around a randomly chosen pivot.
    Uses Lomuto partition scheme.
    """
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    """
    Implements Randomized Quicksort.
    """
    if low < high:
        pi = _partition_randomized(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

def sort_randomized_quicksort(arr):
    """Wrapper function for easier use."""
    temp_arr = list(arr)
    randomized_quicksort(temp_arr, 0, len(temp_arr) - 1)
    return temp_arr

# --- Deterministic Quicksort (First Element Pivot) Implementation ---

def _partition_deterministic(arr, low, high):
    """
    Partitions the array around the first element as pivot.
    Uses Lomuto partition scheme for simplicity.
    """
    pivot = arr[low]
    i = low
    
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[low], arr[i] = arr[i], arr[low]
    return i

def deterministic_quicksort(arr, low, high):
    """
    Implements Deterministic Quicksort with first element as pivot.
    """
    if low < high:
        pi = _partition_deterministic(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)

def sort_deterministic_quicksort(arr):
    """Wrapper function for easier use."""
    temp_arr = list(arr)
    deterministic_quicksort(temp_arr, 0, len(temp_arr) - 1)
    return temp_arr

# --- 3. Empirical Comparison Framework ---

def generate_random_array(n):
    return [random.randint(0, n * 10) for _ in range(n)]

def generate_sorted_array(n):
    return list(range(n))

def generate_reverse_sorted_array(n):
    return list(range(n, 0, -1))

def generate_repeated_elements_array(n, num_unique_elements=5):
    if n == 0:
        return []
    unique_vals = [random.randint(0, 100) for _ in range(num_unique_elements)]
    return [random.choice(unique_vals) for _ in range(n)]

def run_experiment(sorter_func, data_generator, sizes, trials=5):
    results = {}
    # Print to the currently redirected stdout
    print(f"\n--- Running experiments for {sorter_func.__name__.replace('sort_', '')} ---")
    for n in sizes:
        total_time = 0
        for _ in range(trials):
            data = data_generator(n)
            start_time = time.perf_counter()
            sorter_func(data)
            end_time = time.perf_counter()
            total_time += (end_time - start_time)
        avg_time_ms = (total_time / trials) * 1000
        results[n] = avg_time_ms
        print(f"  Size {n}: Average time = {avg_time_ms:.4f} ms")
    return results

if __name__ == "__main__":
    # Define the output file name
    output_filename = "test_quicksort_results.txt"
    
    # Store the original stdout
    original_stdout = sys.stdout

    # Wrap the entire main logic in a try...except...finally block
    try:
        # Open the file in write mode, overwriting if it exists
        # Using 'with' ensures the file is properly closed
        with open(output_filename, 'w') as f:
            # Redirect stdout to the file
            sys.stdout = f

            # Define input sizes to test
            # Start with smaller sizes for quick testing
            sizes = [100, 500, 1000, 5000, 10000] 
            
            print("Starting Empirical Comparison...")

            # --- Run experiments for Randomized Quicksort ---
            print("\n--- Randomized Quicksort ---")
            random_qs_random_data = run_experiment(sort_randomized_quicksort, generate_random_array, sizes)
            random_qs_sorted_data = run_experiment(sort_randomized_quicksort, generate_sorted_array, sizes)
            random_qs_reverse_sorted_data = run_experiment(sort_randomized_quicksort, generate_reverse_sorted_array, sizes)
            random_qs_repeated_data = run_experiment(sort_randomized_quicksort, generate_repeated_elements_array, sizes)

            # --- Run experiments for Deterministic Quicksort ---
            print("\n--- Deterministic Quicksort (First Element Pivot) ---")
            det_qs_random_data = run_experiment(sort_deterministic_quicksort, generate_random_array, sizes)
            det_qs_sorted_data = run_experiment(sort_deterministic_quicksort, generate_sorted_array, sizes)
            det_qs_reverse_sorted_data = run_experiment(sort_deterministic_quicksort, generate_reverse_sorted_array, sizes)
            det_qs_repeated_data = run_experiment(sort_deterministic_quicksort, generate_repeated_elements_array, sizes)

            print("\n--- Summary of Results (Average Time in ms) ---")
            print("{:<10} {:<25} {:<25} {:<25} {:<25}".format("Size", "Randomized (Random)", "Deterministic (Random)", "Randomized (Sorted)", "Deterministic (Sorted)"))
            for n in sizes:
                print("{:<10} {:<25.4f} {:<25.4f} {:<25.4f} {:<25.4f}".format(
                    n,
                    random_qs_random_data.get(n, 0),
                    det_qs_random_data.get(n, 0),
                    random_qs_sorted_data.get(n, 0),
                    det_qs_sorted_data.get(n, 0)
                ))
            
            print("\n{:<10} {:<25} {:<25} {:<25} {:<25}".format("Size", "Randomized (Rev.Sorted)", "Deterministic (Rev.Sorted)", "Randomized (Repeated)", "Deterministic (Repeated)"))
            for n in sizes:
                print("{:<10} {:<25.4f} {:<25.4f} {:<25.4f}".format(
                    n,
                    random_qs_reverse_sorted_data.get(n, 0),
                    det_qs_reverse_sorted_data.get(n, 0),
                    random_qs_repeated_data.get(n, 0),
                    det_qs_repeated_data.get(n, 0)
                ))
            
            print("\n*Note: For larger sizes (e.g., N=100,000), Deterministic Quicksort on sorted/reverse-sorted data will be extremely slow (O(N^2)) and may hit recursion limit or timeout.")

    except Exception as e:
        # Catch any exceptions and print them to the original stdout (console)
        # This ensures you see errors even if redirection is active
        sys.stdout = original_stdout # Restore stdout before printing error
        print(f"An error occurred: {e}", file=sys.stderr)
    finally:
        # Always restore original stdout, even if an error occurs
        sys.stdout = original_stdout
        # This final print will go to the console
        print(f"\n--- Experiment complete. Results saved to {output_filename} ---")