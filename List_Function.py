#Append কোন একটি লিস্টের শেষে নতুন এলিমেন্ট যুক্ত করতে এই মেথড ব্যবহার করা যাবে
nums = [1, 2, 3]
nums.append(4)
print(nums)

#insert লিস্টের কোন একটি নির্দিষ্ট পজিশনে বা ইনডেক্সে কোন এলিমেন্ট যুক্ত করতে চাইলে append এ কাজ হবে না (কারন এটা শেষে যুক্ত করে) বরং insert ব্যবহার করতে হবে।
words = ["A", "C"]
index = 1
words.insert(index, "B")

print(words)


#index একটি এলিমেন্ট লিস্টের কোন ইনডেক্সে অবস্থা করছে সেটা চেক করার জন্য index মেথড ব্যবহার করেছি
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
# print(letters.index('z'))


# Count:লিস্টের মধ্যে কোন একটি এলিমেন্ট মোট কতবার আছে তার সংখ্যা জানতে নিচের মত করে count() মেথডের ব্যবহার করা যেতে পারে,
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.count('p'))

#অবজেক্ট মেথড বাদেও লিস্ট এর জন্য কিছু উপকারী ফাংশন আছে। যেমন - max(), min(), len() ইত্যাদি. যেমন একটি লিস্টের মধ্যে থাকা এলিমেন্ট গুলোর মধ্যে থেকে বড়টি দেখে নিতে max() ফাংশনের ব্যবহার করা যেতে পারে
nums = [1, 2, 4, 20, 50, 3, 4]
print(max(nums))
print(min(nums))
print(len(nums))