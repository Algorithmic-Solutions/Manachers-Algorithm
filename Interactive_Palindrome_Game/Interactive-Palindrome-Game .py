import random 
def generate_string(length):
  random_string = ""
  for _ in range(length):
    random_string += chr(random.randint(ord('a'), ord('z'))) 
  return random_string

def is_palindrome(text):
  processed_text = text.lower()  # Convert to lowercase for case-insensitive check
  # Iterate through middle characters only
  for i in range(len(processed_text) // 2):
      # Check if characters on either side of the center match
      if processed_text[i] != processed_text[-(i + 1)]:
          return False
  return True

score = 0

while True:
  random_string = generate_string(random.randint(5, 20))
  print("Is the string a palindrome?")
  print(random_string)
  user_guess = input("Enter your guess (palindrome/not palindrome): ").lower()
  is_correct = is_palindrome(random_string) == (user_guess == "palindrome")
  if is_correct:
    print("Correct!")
    score+=1
  else:
    print("Incorrect.")
  print("Your current score:", score)
  print("Play another round? (y/n)")
  play_again = input().lower()
  if play_again != "y":
    break

print("Thanks for playing!")