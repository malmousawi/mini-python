
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(message,key,direction):
  final = ""
  text2 = [i for i in message]
  if direction == 0:
      key *= -1
  for i in text2:
    if i in alpha:
      pos = alpha.index(i)    
      new_pos = pos + key
      final += alpha[new_pos]
    else:
      final += i
  return final
  
  
def main():
  text = input("Enter your message: ").lower()
  key = int(input("Enter the shift key: "))
  key = key % 26
  option = int(input("Press 1 to encrypt or 0 to decrypt: "))
  print("\n")
  print(f"Your message is {caesar_cipher(text,key,option)}")

main()
