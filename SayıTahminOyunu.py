import random

guesses_taken = 0
max_guesses = 5  # Maksimum tahmin hakkı
number = random.randint(1, 100)

print("Sayı Tahmin Oyununa Hoş Geldiniz!")


def is_prime(num):
    """Verilen sayının asal olup olmadığını kontrol eder."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


while guesses_taken < max_guesses:
    guess = int(input("Bir sayı tahmin edin (1-100 arasında): "))
    guesses_taken += 1

    if guess == number:
        print("Tebrikler! Doğru tahmin ettiniz.")
        break
    elif guess < number:
        print("Daha yüksek bir sayı deneyin.")
    else:
        print("Daha düşük bir sayı deneyin.")

    remaining_guesses = max_guesses - guesses_taken
    if remaining_guesses > 0:
        print("Kalan tahmin hakkınız:", remaining_guesses)

        # İpucu geliştirmeleri
        if abs(guess - number) <= 5:
            print("Çok yaklaştınız!")
        if guess % 2 == 0:
            print("Tahmin ettiğiniz sayı çift.")
        if is_prime(guess):
            print("Tahmin ettiğiniz sayı asal.")
    else:
        print("Tahmin hakkınız bitti. Kaybettiniz.")

if guesses_taken >= max_guesses and guess != number:
    print("Tahmin hakkınız bitti. Kaybettiniz.")

print("Doğru sayı:", number)
