class PalindromeFinder {
  private text: string;
  private word: string;
  constructor(text: string) {
    this.text = text.toLowerCase().replace(/[^\w]/, " ");
    this.word = this.Preprocess();
  }
  Preprocess(): string {
    let stopwords: string[] = ["the", "a", "an"];
    let words: string[] = this.text
      .split(/\s+/)
      .filter((word) => !stopwords.includes(word));
    return words.join(" ");
  }
  manachers(): number[] {
    const processed_text = `#${this.text.split("").join("#")}#`;
    let n = processed_text.length;
    let P = new Array(2 * n).fill(0);
    let center = 0,
      r = 0;
    for (let i = 0; i < n - 1; i++) {
      let i_mirror = 2 * center - i;
      if (i < r) {
        P[i] = Math.min(r - i, P[i_mirror]);
      } else {
        P[i] = 0;
      }
      while (processed_text[i - P[i] - 1] === processed_text[i + P[i] + 1]) {
        P[i]++;
      }
      if (i + P[i] > r) {
        center = i;
        r = i + P[i];
      }
    }
    return P;
  }
  find_palindromes() {
    const p = this.manachers();
    console.log("p:", p);

    return palindromes;
  }
}
const text = "The quick brown fox jumps over the lazy dog.";

// Create a PalindromeFinder object with the text
const palindromeFinder = new PalindromeFinder(text);

// Call the manachers function to find palindrome lengths
const P = palindromeFinder.manachers();

// Call the PalindromeExtraction function to extract palindromes
const palindromes = palindromeFinder.find_palindromes();

console.log("Original Text:", text);
console.log("Extracted Palindromes:", palindromes);