#!/usr/local/bin/python3
import dns.resolver
import argparse

def domain_name_to_fizz_buzz(domain_name):
    answers = resolver.resolve(domain_name)
    unique_sums = set()

    for record in answers:
        record_to_str = str(record)
        splitted_ip = record_to_str.split(".")
        sum = 0
        for value in splitted_ip:
            sum += int(value)
        unique_sums.add(sum)

    converted = list(unique_sums)
    converted.sort()    

    for number in converted:
        if number %15 == 0:
            print("FizzBuzz")
        elif number %3 == 0:
            print("Fizz")
        elif number %5 == 0:
            print("Buzz")
        else:
            print(number)

if __name__ == "__main__":
    resolver = dns.resolver.Resolver()
    parser = argparse.ArgumentParser()
    parser.add_argument("domain_name", type=str, help="Specify domain name")
    args = parser.parse_args()    
    domain_name_to_fizz_buzz(args.domain_name)
