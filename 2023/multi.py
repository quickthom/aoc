import multiprocessing
import time

def worker(x):
    try:
        print(f"Processing {x}")
        # Simulate some work
        time.sleep(1)
        result = x * x
        print(f"Completed {x}")
        return result
    except Exception as e:
        print(f"Error processing {x}: {e}")
        return None

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    try:
        with multiprocessing.Pool(processes=4) as pool:
            results = pool.map(worker, data)
        print("Results:", results)
    except Exception as e:
        print(f"Error: {e}")