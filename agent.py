import time
from main import add, multiply

def run_agent():
    print("Agent started...")

    while True:
        a, b = 2, 3
        print(f"Add({a},{b}) =", add(a, b))
        print(f"Multiply({a},{b}) =", multiply(a, b))
        print("------")
        time.sleep(5)

if __name__ == "__main__":
    run_agent()
