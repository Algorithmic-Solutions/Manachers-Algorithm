import random 
def generate_string(length):
  random_string = ""
  for _ in range(length):
    random_string += chr(random.randint(ord('a'), ord('z'))) 
  return random_string

def is_palindrome(text):
        processed_text = "#" + "#".join(text) + "#"
        C = [0] * (2 * len(processed_text) + 1)  
        P = [0] * (2 * len(processed_text) + 1) 
        C_center = 0
        R = 0
        for i in range(1, len(processed_text) - 1):
            i_mirror = 2 * C_center - i
            if i <= R:
                P[i] = min(R - i, P[i_mirror])  
            else:
                P[i] = 0
            
            while (i - P[i] - 1 >= 0 and i + P[i] + 1 < len(processed_text) and
                   processed_text[i - P[i] - 1] == processed_text[i + P[i] + 1]):
                P[i] += 1

            if i + P[i] > R:
                C_center = i
                R = i + P[i]

        palindromes = []
        for i in range(1, len(processed_text) - 1, 2):
            if P[i] > 0:
                start_index = (i - P[i]) // 2
                length = P[i]
                palindromes.append((start_index, length))

        return palindromes

random_string = generate_string(random.randint(5, 20))
print(random_string)
debug = is_palindrome(random_string)
print("is palindrome?:", debug)

# score = 0

# while True:
#   random_string = generate_string(random.randint(5, 20))
#   print("Is the string a palindrome?")
#   print(random_string)
#   debug = is_palindrome(random_string)
#   print("debug:",debug)
#   user_guess = input("Enter your guess (palindrome/not palindrome): ").lower()
#   is_correct = is_palindrome(random_string) == (user_guess == "palindrome")
#   if is_correct:
#     print("Correct!")
#     score+=1
#   else:
#     print("Incorrect.")
#   print("Your current score:", score)
#   print("Play another round? (y/n)")
#   play_again = input().lower()
#   if play_again != "y":
#     break

# print("Thanks for playing!")