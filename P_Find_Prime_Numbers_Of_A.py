def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def find_prime_numbers(lst, a):
    return [num for num in lst if is_prime(num)][:a]

def main():
    L = list(map(int, input("Nhập các số nguyên trong list, cách nhau bởi dấu cách: ").split()))
    a = int(input("Nhập số nguyên dương a: "))
    result = find_prime_numbers(L, a)
    print(f"Danh sách mới gồm {a} số nguyên tố đầu tiên trong list là: {result}")

if __name__ == "__main__":
    main()
