import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    end_time = time.time()
    return arr, end_time - start_time

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end_time = time.time()
    return arr, end_time - start_time

def print_iteration(iteration, arr):
    print(f"Iterasi ke-{iteration}: {arr}")

def print_analysis(algorithm_name, worst_case, best_case, average_case):
    print(f"Analisis Algoritma {algorithm_name}:")
    print(f"Worst Case: {worst_case} langkah")
    print(f"Best Case: {best_case} langkah")
    print(f"Average Case: {average_case} langkah")

# List awal sebelum pengurutan
numbers = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

# Pilihan pengguna
choice = input("Pilih algoritma pengurutan (1. Bubble Sort, 2. Insertion Sort): ")

if choice == "1":
    sorted_numbers, execution_time = bubble_sort(numbers.copy())
    algorithm_name = "Bubble Sort"
elif choice == "2":
    sorted_numbers, execution_time = insertion_sort(numbers.copy())
    algorithm_name = "Insertion Sort"
else:
    print("Pilihan tidak valid.")
    exit()

# Menampilkan hasil 5 iterasi pertama
print(f"Hasil 5 iterasi pertama {algorithm_name}:")
for i in range(5):
    print_iteration(i + 1, sorted_numbers)
    if i == len(sorted_numbers) - 1:
        break

# Menampilkan hasil 5 iterasi terakhir
print(f"\nHasil 5 iterasi terakhir {algorithm_name}:")
for i in range(len(sorted_numbers) - 5, len(sorted_numbers)):
    print_iteration(i + 1, sorted_numbers)

# Menampilkan waktu komputasi pengurutan
print(f"\nWaktu komputasi pengurutan {algorithm_name}: {execution_time} detik")

# Menampilkan sebelum dan setelah pengurutan
print("\nSebelum pengurutan:")
print(numbers)
print("\nSetelah pengurutan:")
print(sorted_numbers)

# Analisis algoritma
n = len(numbers)
worst_case = n * (n - 1) // 2  # Jumlah maksimum langkah yang diperlukan dalam worst case
best_case = n - 1  # Jumlah langkah yang diperlukan dalam best case
average_case = (worst_case + best_case) // 2  # Jumlah langkah rata-rata
print_analysis(algorithm_name, worst_case, best_case, average_case)
