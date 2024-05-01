import random 
def generate_string(length):
  random_string = ""
  for _ in range(length):
    random_string += chr(random.randint(ord('a'), ord('z'))) 
  return random_string

class is_palindrome:
    def __init__(self, text):
        self.text = text
        self.processed_text = "#" + "#".join(self.text) + "#"
        self.C = [0] * (2 * len(self.processed_text) + 1)  
        self.P = [0] * (2 * len(self.processed_text) + 1) 
        self.C_center = 0
        self.R = 0
    def calculate(self):
        for i in range(1, len(self.processed_text) - 1):
            i_mirror = 2 * self.C_center - i
            if i <= self.R:
                self.P[i] = min(self.R - i, self.P[i_mirror])  
            else:
                self.P[i] = 0
            
            while (i - self.P[i] - 1 >= 0 and i + self.P[i] + 1 < len(self.processed_text) and
                   self.processed_text[i - self.P[i] - 1] == self.processed_text[i + self.P[i] + 1]):
                self.P[i] += 1

            if i + self.P[i] > self.R:
                self.C_center = i
                self.R = i + self.P[i]

        palindromes = []
        for i in range(1, len(self.processed_text) - 1, 2):
            if self.P[i] > 0:
                start_index = (i - self.P[i]) // 2
                length = self.P[i]
                palindromes.append((start_index, length))

        return palindromes


while True:
  random_string = generate_string(random.randint(5, 20))
  print("Is the string a palindrome?")
  print(random_string)
  user_guess = input("Enter your guess (palindrome/not palindrome): ").lower()
  is_correct = is_palindrome(random_string) == (user_guess == "palindrome")
  if is_correct:
    print("Correct!")
  else:
    print("Incorrect.")
  print("Play another round? (y/n)")
  play_again = input().lower()
  if play_again != "y":
    break

print("Thanks for playing!")