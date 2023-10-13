my_numbers = [1, 2, 3, 5]
my_numbers[3] = 4 #কিভাবে একটা নির্দিষ্ট ইনডেক্সে বা পজিশনে নতুন কোন এলিমেন্ট যুক্ত করা যায়
print(my_numbers)


first_list = [1, 2, 3]
print(first_list + [4, 5, 6])
print(first_list * 3) #string এর মত করে লিস্ট নিয়েও যোগ বা গুনের কাজ করা যায়। যেমন - নিচের উদাহরণটা দেখে নেই



# লিস্টের মধ্যের এলিমেন্ট চেক
# কোন লিস্টের মধ্যে নির্দিষ্ট কোন এলিমেন্ট আছে কিনা সেটা চেক করার জন্য in অপারেটর ব্যবহার করা হয়। যদি এলিমেন্টটি লিস্টের মধ্যে এক বা একাধিকবার থাকে তাহলে এটি True রিটার্ন করে অন্যথায় False রিটার্ন করে
fruits = ["apple", "orange", "pineappe", "grape"]

print("orange" in fruits)
print("rice" in fruits)
print("apple" in fruits)


#একই ভাবে এর সাথে not অপারেটর ব্যবহার করে কোন এলিমেন্টের অনুপস্থিতিও চেক করা যাতে পারে। যেমন
fruits = ["apple", "orange", "pineappe", "grape"]

print("orange" not in fruits)
print(not "rice" in fruits)