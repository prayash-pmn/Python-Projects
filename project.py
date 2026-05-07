# "Data row parser" — user types a raw string like "Alice,28,50000", 
# script splits it, assigns name/age/salary with correct types, 
# prints a formatted summary with int salary and float calculations.
data = "Alice,28,50000" # raw string 

raw_str = data.split(",") # split raw string into list and store in raw_str variable 

name = raw_str[0] # store name in name variable
age = int(raw_str[1]) # convert age into int and store in age variable
salary = int(raw_str[2]) # convert salary into int and store in salary variable 

print(f"Name: {name} | Age: {age} | Salary: {salary}") # to show clean output

monthly_salary =  salary / 12 # float calculation get montly salary 
print(f"Monthly salary: {monthly_salary:.2f}")


# Build 3 mini scripts: 

# currency converter (str → float → int), 
amount = "10000"
rate = 6.6
converted_amount = float(amount) * rate
print(int(converted_amount))

# age group classifier,
age = int(input("Enter your age: "))
if age < 0 or age > 150:
    print("Invalid age. Should be between (0-150)")
elif age <= 12:
    print("You are a child")
elif age <= 19:
    print("You are a teenage")
elif age <= 39:
    print("You are an adult")
elif age <= 59:
    print("You are a middle age adult")
else:
    print("You are a senior/elderly")

# a "data validator" that checks if age is int and salary is positive — print 
# "valid row" or "invalid row".
age = 25
salary = 50000

if isinstance(age, int) and salary > 0:
    print("Valid row")
else:
    print("Invalid row")


# Grocery bill calculator
# variables · operators · input/output
# ▸
# Problem
# Build a script that takes item names and prices as input and calculates total bill, 
# tax, and final amount.
names = ["rice", "oil", "sugar"]
prices = [100, 200, 150]
tax_rate = 10 / 100
total = sum(prices)
final_amount = total *(1 + tax_rate) # formula to get tax with total bill 

print(f"Final amount: {final_amount:.2f}")

# Input
# item name + price (typed by user, loop until done)
# Output
# itemized list + subtotal + 10% tax + total
# What to build
# Use a while loop to collect items into a list of tuples. Calculate and print formatted bill.
new_ls = []
while True:
    name = input("Enter item name or enter 'done' when finish: ").lower()
    if name == "done":
        break
    else:
        price = int(input("Enter the price: "))
        tup = (name, price)
        new_ls.append(tup)
    
tax_rate = 10 / 100
subtotal = 0
for item in new_ls:
    price = item[1]
    subtotal += price

tax = subtotal * tax_rate
final_bill = subtotal + tax


print("itemized list: ")
for i in new_ls:
    print(f"{i[0]}- {i[1]}")

print(f"subtotal: {subtotal}, 10% tax: {tax}, total_bill: {final_bill}")


# "Row validator" — takes a simulated CSV row as variables, checks: 
# is age between 0–120? Is salary > 0? Is name non-empty? Prints "PASS" or "FAIL" with reason. 
# Then: "Data quality classifier" — given a score 0–100, classify completeness as High/Medium/Low.
row = "Jack,-1,40000"
row_split = row.split(",")

score = 100
name = row_split[0]
age = int(row_split[1])
salary = int(row_split[2])

if 0 <= age <= 120:
    print("PASS: Age is correct")  

else:
    print("FAIL: Age is incorrect")
    score -= 33  

if salary > 0:
    print("PASS: Salary is valid")
  
else:
    print("FAIL: Salary should be greater than 0")
    score -= 33    
     
if name.strip() != "":
    print("PASS: Name is valid")
  
else:
    print("FAIL: Name shouldn't be empty")
    score -= 34
  
print("\nScore:", score)
if 0 <= score <= 20:
    print("Low score")
elif score <= 50:
    print("Medium score")
elif score <= 100:
    print("High score")



# "Multi-column validator" — check 5 columns (id, name, age, salary, email). 
# Each has its own rule. Print a report: how many columns passed, which failed, and why.
row = "1,Bob,20,0,bob@gmail.com"

data = row.split(",")

valid = 0
invalid = 0
if data[0].isdigit():
    print("Id passed") 
    valid += 1
else:
    print("Invalid! id must be number only")
    invalid += 1
   

if data[1].strip() != "":
    print("Name passed")
    valid += 1
else:
    print("Invalid! Name is empty")
    invalid += 1

if data[2].isdigit():
    age = int(data[2])
    if 0 <= age <= 120:
        print("Age passed")
        valid += 1
    else:
        print("Invalid! Age must be between (0-120)")
        invalid += 1
else:
    print("Invalid age format")

if int(data[3]) > 0:
    print("Salary passed")
    valid += 1
else:
    print("Invalid! Salary must be greater than 0")
    invalid += 1
    
if "@" in data[4] and "." in data[4]:
    print("Gmail passed")
    valid +=1 
else:
    print("Invalid! gmail must have '@' and '.'")
    invalid +=1

print(f"Column passed {valid}/5")
print(f"Column failed {invalid}")


# Problem
# Read student names and scores, classify each as Pass/Fail and assign letter grade A/B/C/D/F.
# Input
# List of (name, score) pairs hardcoded in a list
# Output
# Name | Score | Grade | Pass/Fail printed for each
# What to build
# Loop through list, use if/elif chain for grade logic, print formatted table.
data = [("Jack", 80), ("Bob", 90), ("Harry", 75), ("Lacy", 40)]

for item in data:
    name = item[0]
    mark = item[1]
    if mark < 0 or mark > 100:
        print("Invalid! mark must be between (0-100)")
    elif 90 <= mark <= 100:
        grade = "A"
        status = "Pass"

    elif mark >= 75:
        grade = "B"
        status = "Pass"
        
    elif mark >= 60:
        grade = "C"
        status = "Pass"
        
    elif mark >= 45:
        grade = "D"
        status = "Pass"

    else:
        grade = "F"
        status = "Fail"

    print(f"{name} | {mark} | {grade} | {status}")
    

# "Batch row processor" — loop through a list of 10 hardcoded data rows
# (each a string "name,age,salary"), split and validate each one, count valid vs invalid rows.
# Then: loop through a list of file names and print which "exist" (simulate with a set of known names).
data = [
    "Alice,25,50000",
    "Jack,24,40000",
    "Prayash,21,30000",
    "Isha,23,60000",
    "Bob,28,70000",
    "Harry,27,55000",
    "Peter,26,45000",
    "Charlie,30,52000",
    "Emma,22,0",
    "Rita,29,65000"
]
valid_count = 0
invalid_count = 0

for item in data:
    name, age, salary = item.split(",")
    age = int(age)
    salary = int(salary)

    row_valid = True

    if name.strip() == "":
        row_valid = False
   
    if not(18 <= age <= 60):
        row_valid = False
   
    if salary <= 0:
        row_valid = False

    if row_valid:
        valid_count += 1
    else:
        invalid_count += 1

print(f"Valid row: {valid_count}")
print(f"Invalid row: {invalid_count}")

files = [
    "new.py",
    "name.txt",
    "code.py",
    "jin.py"
]

existing = {"new.py", "code.py"}

for file in files:
    if file in existing:
        print(f"{file} exists")
    else:
        print(f"{file} does not exist")


# Add to batch processor: skip invalid rows, collect only valid rows into a new list, 
# print a summary at end (total rows, valid, invalid, average salary of valid rows).
data = [
    "Alice,25,50000",
    "Jack,24,40000",
    "Prayash,21,30000",
    "Isha,23,60000",
    "Bob,28,70000",
    "Harry,27,55000",
    "Peter,26,45000",
    "Charlie,30,52000",
    "Emma,22,0",
    "Rita,29,65000"
]
new_ls = []
valid_rows = 0
invalid_rows = 0

for i in data:
    name, age, salary = i.split(",")

    name = name.strip()
    age = int(age)
    salary = int(salary)

    if name != "" and 18 <= age <= 60 and salary > 0:
        item = name, age, salary
        new_ls.append(item)
        valid_rows += 1
    else:
        invalid_rows += 1   


sum_all = 0

for i in new_ls:
    sum_all += i[2]
count = len(new_ls)
average_salary = sum_all / count if count > 0 else 0

print(f"Average salary: {average_salary:.2f}")

print("\nSummary of all:")
print(f"Total rows: {len(data)}, Valid row: {valid_rows}, Invalid row: {invalid_rows}, Average salary: {average_salary:.2f}")

# Problem
# Given a paragraph of text, count how many times each word appears. Show top 5 most frequent words.
# Input
# A hardcoded string paragraph
# Output
# Word → count, sorted by frequency descending, top 5 shown
# What to build
# Split string into words, loop and build a dict counting each word, sort dict by value.
text = "Nepal is a beautiful country located in South Asia. It is famous for the Himalayas, including Mount Everest, the highest peak in the world."
words = text.split()
seen = {}

for word in words:
    word = word.lower()
    word = word.replace(".", "")
    word = word.replace(",", "")

    if word in seen:
        seen[word] += 1
    else:
        seen[word] = 1

def get_count(item):
    return item[1]

sorted_words = sorted(seen.items(), key=get_count, reverse=True)

top5 = sorted_words[:5]

for word, count in top5:
    print(word, "->", count)


# "In-memory table" — store 5 employee records as a list of tuples: 
# (id, name, dept, salary). Write code to: print all rows, filter by dept, find highest salary,
# print names only using list comprehension.
employee = [
    (1, "Bob", "IT", 650000),
    (2, "Charlie", "Sale", 40000),
    (3, "Harry", "Marketing", 80000),
    (4, "Emma", "HR", 70000),
    (5, "Jack", "Data Engineer", 75000)
]
for row in employee:
    print(row)

max_salary = 0
dept = ["Data Engineer", "Marketing"]
for row in employee:
    if row[2] in dept:
        print(row[2])
        if row[3] > max_salary:
            max_salary = row[3]

print(max_salary)
   
names = [i[1] for i in employee]
print(names)

    

# "Sales data processor" — list of (product, units_sold, unit_price). 
# Calculate revenue per product, total revenue, best-selling product. 
# Use list comprehension to filter products with revenue above average.
sale_data = [
    ("MagBook Pro", 1, 250000),
    ("iphone 15", 2, 1200000),
    ("Dell XPS 13", 1, 180000),
    ("AirPods Pro", 3, 30000),
    ("Xpulse", 2, 2300000)
]
revenues = []
new_lst = []
for data in sale_data:
    product = data[0]
    units_sold = int(data[1])
    unit_price = int(data[2])
    revenue_per_product = units_sold * unit_price
    revenues.append(revenue_per_product)
    new_lst.append((product, revenue_per_product))
   

    print(f"{product} -> {revenue_per_product}")

total = sum(revenues)
print("\nTotal revenue:", total)

best = max(new_lst, key=lambda x:x[1])
print(f"Best selling product: {best[0]} -> {best[1]}")

print("\nProducts with revenue above average")
total = 0
count = 0
for i in new_lst:
    total += i[1]
    count += 1
average = total / count

above_avg = [(product, revenue) for product, revenue in new_lst if revenue > average]
print(above_avg)


# Problem
# You have a list of customer emails with duplicates. Remove duplicates, 
# count how many were removed, return clean list.
# Input
# emails = ['a@x.com','b@x.com','a@x.com','c@x.com','b@x.com']
# Output
# Clean list + 'Removed N duplicates' message
# What to build
# Convert to set, compare lengths, convert back to sorted list.
emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]

clean_list = sorted(set(emails))

removed = len(emails) - len(clean_list)

print(clean_list)
print(f"Removed {removed} duplicates")

# "JSON-style record processor" — store 5 employee records as dicts with keys: id, name, department,
#  salary, active. Write functions to: find by id, filter active employees, 
# compute avg salary per department using a nested dict.
employee = [
    {"id": 1, "name": "Jack", "department": "IT", "salary": 60000, "active": True},
    {"id": 2, "name": "Bob", "department": "Sales", "salary": 40000, "active": False},
    {"id": 3, "name": "Charlie", "department": "HR", "salary": 70000, "active": True},
    {"id": 4, "name": "Harry", "department": "Marketing", "salary": 55000, "active": False},
    {"id": 5, "name": "Emma", "department": "Finance", "salary": 45000, "active": True},
]

def find_by_id(employee, id):
    for emp in employee:
        if emp["id"] == id:
            return emp
    return "ID not found"

result = find_by_id(employee, 2)
print(result)

print("\nFilter active")
def filter_active(employee):
    results = []
    for emp in employee:
        if emp["active"]:
            results.append(emp)
    return results

new_results = filter_active(employee)
print(new_results)

print("\nNested dict")
salary = {}
for emp in employee:
    if emp["department"] in salary:
        salary[emp["department"]].append(emp["salary"])
    else:
        salary[emp["department"]] = [emp["salary"]]
    
avg_salary = {k: sum(v) / len(v) for k, v in salary.items()}
print(avg_salary)


# "Config loader" — store pipeline config as a dict: 
# source_file, output_file, delimiter, encoding, skip_rows.
# Write a function that reads the config and prints a summary.
# Add a second "override" dict and merge it with .update().
config = {
    "source_file": "data.csv",
    "output_file": "output.csv",
    "delimiter": ",",
    "encoding": "utf-8",
    "skip_rows": 1
}

def read_config(config):
    for key, value in config.items():
        print(f"{key}: {value}") 
read_config(config)

override = {
    "encoding": "utf-16"
}

config.update(override)
print(config)


# Problem
# Given a list of sales records (dicts with name, region, amount), group total sales by region.
# Input
# sales = [{'name':'Ali','region':'Asia','amount':500}, ...]
# Output
# Region → total sales, sorted highest to lowest
# What to build
# Loop through list, build nested dict grouping by region, sum amounts, sort and print.

sales = [
    {'name':'Ali','region':'Asia','amount':500},
    {'name':'Bob','region':'Europe','amount':800},
    {'name':'Emma','region':'Asia','amount':200}       
]

# Region → total sales, sorted highest to lowest
total_sales = {}
for item in sales:
    if item['region'] in total_sales:
        total_sales[item['region']].append(item['amount'])
    else:
        total_sales[item['region']] = [item['amount']]

total_sales = {k: sum(v) for k, v in total_sales.items()}
print(total_sales)

sorted_sales = sorted(total_sales.items(), key=lambda x: x[1], reverse=True)

for region, total in sorted_sales:
    print(f"{region} -> {total}")


#  Wrap ALL week 1 scripts in functions. Row validator becomes validate_row(row: dict) → bool.
#  Batch processor becomes process_batch(rows: list) → dict. 
# Each function has a docstring explaining what it does.  
def validate_row(row: dict) -> bool:
    """
    Row validator: check if a single row is valid or not.
    Returns True if valid, Otherwise False.
    """
    name = row["name"]
    age = row["age"]
    salary = row["salary"]
    if name.strip() == "":
        return False
    if age < 18 or age > 60:
        return False
    if salary < 0:
        return False
    return True

def process_batch(rows: list) -> dict:
    """
    Batch processor: validates multiple rows and returns count of valid/invalid rows.
    """
    valid_row = 0
    invalid_row = 0 

    for row in rows:
        if validate_row(row):
            valid_row += 1
        else:
            invalid_row += 1

            
    return {
        "valid_rows" : valid_row,
        "invalid_rows": invalid_row
    }
            
rows =  [
    {"name": "Bob", "age": 25, "salary": 70000},
    {"name": "Harry", "age": 23, "salary": 80000},
    {"name": "Emma", "age": 24, "salary": 60000}
]

print(process_batch(rows))


# "Mini ETL functions library" — write 8 functions: parse_row(), validate_row(), clean_name(), 
# normalize_salary(), filter_active(), compute_stats(), format_output(), generate_summary(). 
# Each does one thing only.
print("\nParse row")   
def parse_row(row):
    data = row.split(",")

    name = data[0].strip()
    salary = data[1].strip()
    status = data[2].strip()
    new_salary = salary.replace("$", "").replace(",", "")
    
    new_data = {"name": name, "salary": int(new_salary), "status": status}

    return new_data

result = parse_row("John Doe, 45000, active")
print(result)

print("\nValidate row")
def validate_row(row):
    if row["name"] == "":
        return False
    if row["salary"] <= 0:
        return False
    if row["status"] not in ["active", "inactive"]:
        return False
    return True

result = validate_row(parse_row("John Doe, 45000, active"))
print(result)

print("\nClean name")
def clean_name(row):
    if row["name"] != "":
        name = row["name"].strip().title()
    
    new_dict = {"name": name, "salary": row["salary"], "status": row["status"]}

    return new_dict

new_result = clean_name(parse_row("John doe, 45000, active"))
print(new_result)

print("\nNormalize salary")
def normalize_salary(row):
    if isinstance(row["salary"], int):
        if row["salary"] >= 0:
            salary = row["salary"]
        else:
            salary = abs(row["salary"])
        new_data = {"name": row["name"], "salary": salary, "status": row["status"]}
    return new_data

result = normalize_salary(parse_row("John Doe, $45000, active"))
print(result)
        
print("\nfilter active")
def filter_active(data):
    new_ls = []
    for item in data:
        if item["status"] == "active":
            new_ls.append(item)
    return new_ls

print(filter_active([
    {"name": "John Doe", "salary": 45000, "status": "active"},
    {"name": "Bob Marley", "salary": 50000, "status": "inactive"},
    {"name": "Jack Reacher", "salary": 30000, "status": "active"}
]))

print("\ncompute stats")
def compute_stats(row):
    ls = []
    for data in row:
        ls.append(data["salary"])
    average = sum(ls) / len(ls)
    total = sum(ls)
    highest = max(ls)
    lowest = min(ls)

    return {"average": average, "highest": highest, "lowest": lowest, "total": total}


print(compute_stats(filter_active([
    {"name": "John Doe", "salary": 45000, "status": "active"},
    {"name": "Bob Marley", "salary": 50000, "status": "inactive"},
    {"name": "Jack Reacher", "salary": 30000, "status": "active"}
])))

print("\nFormat output")
def format_output(row):
    print("Average Salary:", row["average"])
    print("Highest Salary:", row["highest"])
    print("Lowest Salary:", row["lowest"])
    print("Total Salary:", row["total"])

format_output(compute_stats(filter_active([
    {"name": "John Doe", "salary": 45000, "status": "active"},
    {"name": "Bob Marley", "salary": 50000, "status": "inactive"},
    {"name": "Jack Reacher", "salary": 30000, "status": "active"}
])))

print("\ngenerate summary")
def generate_summary(data): 
    count_active = 0
    count_inactive = 0
    for row in data:
        if row["status"] == "active":
            count_active += 1
        else:
            count_inactive += 1

    return f"Active: {count_active}, \nInvactive: {count_inactive}"


print(generate_summary([
    {"name": "John Doe", "salary": 45000, "status": "active"},
    {"name": "Bob Marley", "salary": 50000, "status": "inactive"},
    {"name": "Jack Reacher", "salary": 30000, "status": "active"}
]))



# "In-memory ETL pipeline v1" — hardcoded raw data (10 messy rows as strings). 
# Pipeline: parse_rows() → validate_rows() → clean_rows() → compute_stats() → print_report(). 
# Each step is a separate function. Stats: total rows, valid, invalid, avg salary, top earner.

def parse_rows(data):
    rows = []
    for item in data:
        name, age, salary = item.split(",")
        rows.append({
            "name": name,
            "age": int(age),
            "salary": int(salary)
        })
    return rows

def validate_rows(rows):
    valid = 0
    invalid = 0

    for item in rows:
        if (
            item["name"] == "" or
            item["age"] < 18 or item["age"] > 60 or
            item["salary"] <= 0
        ):
            invalid += 1
        else:
            valid += 1

    return valid, invalid

def clean_rows(rows):
    cleaned = []

    for item in rows:
        name = item["name"].strip().title()
        age = item["age"]
        salary = item["salary"]

        if name == "" or age < 18 or age > 60 or salary <= 0:
            continue
        cleaned.append({
            "name": name,
            "age": age,
            "salary": salary
        })

    return cleaned

def compute_stats(rows):
    salaries = [item["salary"] for item in rows]

    return {
        "average": sum(salaries) / len(salaries),
        "total": sum(salaries),
        "top_earner": max(salaries),
        "low_earner": min(salaries)
    }

def print_report(stats, valid, invalid, rows):
    print("\n==== Report ====")
    print(f"Total rows: {len(rows)}")
    print(f"Valid rows: {valid}")
    print(f"Invalid rows: {invalid}")
    print(f"Average salary: {stats['average']:.2f}")
    print(f"Top Earner: {stats['top_earner']}")
    print(f"Low Earner: {stats['low_earner']}")
    print("=================")

data = [
    "Alice,25,50000",
    "Jack,24,40000",
    "Prayash,21,30000",
    "Isha,23,60000",
    "Bob,28,70000",
    "Harry,27,55000",
    "Peter,26,45000",
    "Charlie,30,52000",
    "Emma,22,0",
    "Rita,29,65000"
]

parsed = parse_rows(data)
valid, invalid = validate_rows(parsed)
cleaned = clean_rows(parsed)
stats = compute_stats(cleaned)

print_report(stats, valid, invalid, cleaned)


# Add a FAILED_ROWS report at the end — list every invalid row and why it failed.
# Add a function to export the clean rows as a printed CSV-formatted string.

def parse_rows(data):
    rows = []
    for item in data:
        name, age, salary = item.split(",")
        rows.append({
            "name": name,
            "age": int(age),
            "salary": int(salary)
        })
    return rows

def validate_rows(rows):
    valid = 0
    invalid = 0

    for item in rows:
        is_valid = True

        if item["name"] == "" :
            is_valid = False

        if item["age"] < 18 or item["age"] > 60:
            is_valid = False
            
        if  item["salary"] <= 0:
            is_valid = False   

        if is_valid:
            valid += 1
        else:
            invalid += 1
        
    return valid, invalid, 

def clean_rows(rows):
    cleaned = []

    for item in rows:
        name = item["name"].strip().title()
        age = item["age"]
        salary = item["salary"]

        if name == "" or age < 18 or age > 60 or salary <= 0:
            continue
        cleaned.append({
            "name": name,
            "age": age,
            "salary": salary
        })

    return cleaned

def compute_stats(rows):
    salaries = [item["salary"] for item in rows]

    return {
        "average": sum(salaries) / len(salaries),
        "total": sum(salaries),
        "top_earner": max(salaries),
        "low_earner": min(salaries)
    }

def print_report(stats, valid, invalid, rows):
    print("\n==== Report ====")
    print(f"Total rows: {len(rows)}")
    print(f"Valid rows: {valid}")
    print(f"Invalid rows: {invalid}")
    print(f"Average salary: {stats['average']:.2f}")
    print(f"Top Earner: {stats['top_earner']}")
    print(f"Low Earner: {stats['low_earner']}")
    print("=================")

def export_csv(rows):
    if not rows:
        return ""
    headers = rows[0].keys()
    csv_output = ",".join(headers)+"\n"

    for row in rows:
        csv_output += ",".join(str(row[h]) for h in headers) + "\n"
    
    return csv_output

def failed_rows(rows):
    fail_rows = []
    for item in rows:
        if item["name"] == "":
            fail_rows.append(item)
            print("Name is empty")

        if item["age"] < 18 or item["age"] > 60:
            fail_rows.append(item)
            print("Age should be between 18-60")

        if item["salary"] <= 0:
            fail_rows.append(item)
            print("Salary is less than or equal 0")

    return fail_rows


data = [
    "Alice,25,50000",
    "Jack,24,40000",
    "Prayash,21,30000",
    "Isha,23,60000",
    "Bob,28,70000",
    "Harry,27,55000",
    ",26,45000",
    "Charlie,17,52000",
    "Emma,22,0",
    "Rita,29,65000"
]

parsed = parse_rows(data)
valid, invalid = validate_rows(parsed)
cleaned = clean_rows(parsed)
stats = compute_stats(cleaned)
csv = export_csv(cleaned)
fail_rows = failed_rows(parsed)
print_report(stats, valid, invalid, cleaned)
print(csv)
print(fail_rows)



# In-memory ETL pipeline — parses, validates, cleans, and reports on data. 
# All logic in clean functions. Pushed to GitHub with README.
def parses(data):
    rows = []
    for item in data:
        name, age, salary = item.split(",")
        rows.append({
            "name": name,
            "age": int(age),
            "salary": int(salary)
        })
    return rows

def validates(rows):
    valid = 0
    invalid = 0
    for item in rows:
        is_valid = True
        if item["name"] == "":
            is_valid = False
        if item["age"] < 18 or item["age"] > 60:
            is_valid = False
        if item["salary"] <= 0:
            is_valid = False
        if is_valid:
            valid += 1
        else:
            invalid += 1
    return valid, invalid

def cleans(rows):
    cleaned = []

    for item in rows:
        name = item["name"].strip().title()
       
        cleaned.append({
            "name": name,
            "age": item["age"],
            "salary": item["salary"]
        })
    return cleaned

def print_report(cleaned, valid, invalid):
    print("==== Report ====")
    print("Valid records:", valid)
    print("Invalid records:", invalid)

    print("\nCleaned data: ")
    for row in cleaned:
        print(row)

data = [
    "Alice,25,50000",
    "Jack,24,40000",
    "Prayash,21,30000",
    "Isha,23,60000",
    "Bob,28,70000",
    "Harry,27,55000",
    ",26,45000",
    "Charlie,17,52000",
    "Emma,22,0",
    "Rita,29,65000"
]

parsed = parses(data)
valid, invalid = validates(parsed)
cleaned = cleans(parsed)
print_report(cleaned, valid, invalid)


        
# Can you write a function that takes a dict and validates it?
def validates_dict(rows): # this is wrong somewhere it is mistake
    valid = 0
    invalid = 0

    for item in rows:
        is_valid = True

        if not isinstance(item["id"], int):
            is_valid = False

        if item["name"] == "":
            is_valid = False

        if item["salary"] <= 0:
            is_valid = False

        if "department" not in item:
            is_valid = False

        if is_valid:
            valid += 1
        else:
            invalid += 1

    return valid, invalid


employee = [
    {"id": 1, "name": "Jack", "department": "IT", "salary": 60000, "active": True},
    {"id": 2, "name": "Bob", "department": "Sales", "salary": 40000, "active": False},
    {"id": 3, "name": "Charlie", "department": "HR", "salary": 70000, "active": True},
    {"id": 4, "name": "Harry", "department": "Marketing", "salary": 55000, "active": False},
    {"id": 5, "name": "Emma", "department": "Finance", "salary": 45000, "active": True},
]

valid, invalid = validates_dict(employee)
print(f"valid: {valid}, invalid: {invalid}")

# Can you process a list of records with loops and comprehensions? 
employee = [
    {"id": 1, "name": "Jack", "department": "IT", "salary": 60000},
    {"id": 2, "name": "", "department": "Sales", "salary": 40000},
    {"id": 3, "name": "Charlie", "department": "HR", "salary": 70000},
    {"id": 4, "name": "Harry", "department": "Marketing", "salary": 55000},
    {"id": 5, "name": "Emma", "department": "Finance", "salary": 0}
]

# using loop 
valid = 0
invalid = 0

for item in employee:
    is_valid = True
    if not isinstance(item["id"], int):
        is_valid = False

    if item.get("name", "").strip() == "":
        is_valid = False

    if item["salary"] <= 0:
        is_valid = False

    if item.get("department", "") == "":
        is_valid = False
    
    if is_valid:
        valid += 1
    else:
        invalid += 1

print(f"Valid: {valid}, Invalid: {invalid}\n")


invalid = [
    item for item in employee
    if not isinstance(item["id"], int) or
    item["name"].strip() == "" or  item["salary"] <= 0 or 
    item.get("department", "") == ""
]

print(f"Invalid: \n{invalid}")

valid = [
    item for item in employee
    if isinstance(item["id"], int) and
    item["name"].strip() != "" and item["salary"] > 0 and
    item.get("department", "") != ""
]
print(f"\nValid: \n{valid}")
















