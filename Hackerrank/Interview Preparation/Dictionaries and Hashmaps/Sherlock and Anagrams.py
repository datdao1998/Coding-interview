def sherlockAndAnagrams(s):
    # Write your code here
    dict = {}
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            list1 = list(s[i:j].strip())
            list1.sort()
            transf = ''.join(list1)
            if transf in dict:
                count += dict[transf]
                dict[transf] = dict[transf] + 1

            else:
                dict[transf] = 1
    return count


s = 'abba'
print(sherlockAndAnagrams(s))