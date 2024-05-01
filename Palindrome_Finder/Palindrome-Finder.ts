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
  manachers(): string[] {
    const processed_text = `#${this.word.split("").join("#")}#`;
    let n = processed_text.length;
    let P = new Array(2*n+1).fill(0);
    let center = 0,
      r = 0;
    for (let i = 1; i < n-1; i++) {
      let i_mirror = 2 * center - i;
      if (i <= r) {
        P[i] = Math.min(r - i, P[i_mirror]);
      } 
      while (
        processed_text[i + P[i] + 1] &&
        processed_text[i - P[i] - 1] === processed_text[i + P[i] + 1]
    ) {
        P[i]++;
    }
      if (i + P[i] > r) {
        center = i;
        r = i + P[i];
      }
    }
    const palindromes: string[] = [];
    for (let i = 1; i < n - 1; i++) {
        if (P[i] > 0) {
            const startIndex = (i - P[i]) / 2;
            const length = P[i];
            palindromes.push(this.word.substr(startIndex, length));
        }
    }
    return palindromes;
  }
  find_palindromes(): void {
    const palindromes = this.manachers();
    console.log("Palindromic Words:", palindromes);
  }
}
const text = "The quick brown fox level jumps over the lazy dog.";

// Create a PalindromeFinder object with the text
const palindromeFinder = new PalindromeFinder(text);

// Call the PalindromeExtraction function to extract palindromes
palindromeFinder.find_palindromes();

console.log("Original Text:", text);
