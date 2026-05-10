import pandas as pd
import numpy as np

def create_rand_orders():
    np.random.seed(61)
    data = {
        'id': range(1, 100001),
        'size': np.random.randint(1, 101, 100000)
    }
    df = pd.DataFrame(data)
    df.to_csv('data.csv', index=False)
    print("OK 200")

def formulas(size, machine):
    match machine:
        case 'A':
            return 0.05 * (size ** 2) + 5
        case 'B':
            return 0.1 * ((size - 50) ** 2) + 15
        case 'C':
            return (2000 / size) + 10

def main():
    machine_list = ["A", "B", "C"]
    machine_workload = {
        "A": 0,
        "B": 0,
        "C": 0,
    }
    results = []
    create_rand_orders()
    
    df = pd.read_csv('data.csv', index_col='id')

    for orders in df.itertuples():
        order = orders.size
        order_id = orders.Index

        completion_times = []
        for machine in machine_list:
            time = formulas(order, machine)
            completion_times.append(machine_workload[machine] + time)
        
        match completion_times.index(min(completion_times)):
            case 0:
                machine_workload["A"] = min(completion_times)
                best_machine = "A"
            case 1:
                machine_workload["B"] = min(completion_times)
                best_machine = "B"
            case 2:
                machine_workload["C"] = min(completion_times)
                best_machine = "C"
        
        results.append({
            "Order_ID": order_id,
            "Size": order,
            "Machine": best_machine,
            "Processing_Time": formulas(order, best_machine),
            "Finish_Time": min(completion_times)
        })


    print(f"Machine A: {machine_workload['A']}\n")
    print(f"Machine B: {machine_workload['B']}\n")
    print(f"Machine C: {machine_workload['C']}\n")

    pd.DataFrame(results).to_csv('results.csv', index=False)


if __name__ == '__main__':
    main()